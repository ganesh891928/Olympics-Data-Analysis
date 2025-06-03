import numpy as np
def medal_tally(df):
    medal_tally =df.drop_duplicates(subset=["Team","NOC","Games","Year","City","Sport","Event","Medal"])
    medal_tally = medal_tally.groupby('NOC').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index()
    medal_tally["total"] = medal_tally["Gold"] + medal_tally["Silver"] + medal_tally["Bronze"]
    return  medal_tally



def Country_year_list(df):
    years = df["Year"].unique().tolist()
    years.sort()
    years.insert(0,"Overall")
    country = np.unique(df['region'].dropna().values).tolist()
    country.sort()
    country.insert(0,"Overall")
    return years,country

def fetch_medal(df, year, country):
    medal_df = df.drop_duplicates(subset=["Team", "NOC", "Games", "Year", "City", "Sport", "Event", "Medal"])
    flag = 0
    year = str(year).lower()
    country = str(country).lower()

    df = medal_df.copy()
    if 'Year' in df.columns and df['Year'].dtype != 'int64':
        df['Year'] = df['Year'].astype(int)
    if 'region' in df.columns:
        df['region'] = df['region'].astype(str)

    if year == "overall" and country == "overall":
        temp_df = df
    elif year == "overall" and country != "overall":
        flag = 1
        temp_df = df[df['region'].str.lower() == country]
    elif year != "overall" and country == "overall":
        temp_df = df[df["Year"] == int(year)]
    else:
        temp_df = df[(df["Year"] == int(year)) & (df['region'].str.lower() == country)]

    if temp_df.empty:
        print("No data available for the given year and country.")
        return
    if flag == 1:
        x = temp_df.groupby('Year')[['Gold', 'Silver', 'Bronze']].sum().sort_values('Year', ascending=True)
    else:
        x = temp_df.groupby('region')[['Gold', 'Silver', 'Bronze']].sum().sort_values('Gold', ascending=False)

    x['total'] = x['Gold'] + x['Silver'] + x['Bronze']
    return x
def data_over_time(df,col):
    nations_over_time = df.drop_duplicates(["Year", col])["Year"].value_counts().reset_index().sort_values("Year")
    nations_over_time.rename(columns={'count': "No of Countries"}, inplace=True)
    return nations_over_time

def get_successful_athletes_overall(df, sport=None):
    medal_df = df.dropna(subset=["Medal"])

    # Filter by sport if provided
    if sport:

        medal_df.groupby("Name").size().sort_values(ascending=False)

    # Group by Name, Sport, Region,count medals
    grouped = (
        medal_df.groupby(["Name", "Sport", "region"])
        .size()
        .reset_index(name="Total Medals")
        .sort_values(by="Total Medals", ascending=False)
    )

    return grouped.head(20)

def get_successful_athletes(df, sport=None):
    medal_df = df.dropna(subset=["Medal"])

    # Filter by sport if provided
    if sport:
        medal_df = medal_df[medal_df["Sport"] == sport]

    grouped = (
        medal_df.groupby(["Name", "Sport", "region"])
        .size()
        .reset_index(name="Total Medals")
        .sort_values(by="Total Medals", ascending=False)
    )

    return grouped.head(20)
def yearwise_medal_tally(df,country):
    temp_df = df.dropna(subset=["Medal"])
    temp_df.drop_duplicates(subset=['Team', "NOC", 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)
    new_df = temp_df[temp_df["region"] == country]
    final_df = new_df.groupby("Year").count()['Medal'].reset_index()
    return final_df

def most_successful_countrywise(df,sel_country):
    medal_df = df.dropna(subset=["Medal"])
    medal_df = medal_df[medal_df["region"] == sel_country]
    grouped = (
        medal_df.groupby(["Name", "Sport"])
        .size()
        .reset_index(name="Total Medals")
        .sort_values(by="Total Medals", ascending=False))
    return grouped.head(10)
def Weight_V_height(df,sport):
    athlete_df=df.drop_duplicates(subset=["Name","region"])
    athlete_df["Medal"].fillna("NO Medal",inplace=True)
    if sport!="Overall":
        temp_df=athlete_df[athlete_df["Sport"]==sport]
        return temp_df
    else:
        return athlete_df
def Men_v_women(df):
    athlete_df = df.drop_duplicates(subset=["Name", "region"])
    men = athlete_df[athlete_df['Sex'] == 'M'].groupby('Year').count()['Name'].reset_index()

    # Count number of female athletes per year
    women = athlete_df[athlete_df['Sex'] == 'F'].groupby('Year').count()['Name'].reset_index()

    # Merge male and female counts on 'Year'
    final = men.merge(women, on='Year', how='left')
    final.rename(columns={"Name_x": "Male", "Name_y": "Female"}, inplace=True)
    final.fillna(0, inplace=True)
    return final