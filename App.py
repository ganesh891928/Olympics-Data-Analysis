import streamlit as st
import pandas as pd
import plotly.express as px
import preprocessor,helper
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')


df=preprocessor.preprocess()
st.sidebar.title("Olympics Analysis")
st.sidebar.image("data:image/jpeg;base64,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")
user_menu=st.sidebar.radio(
    'Select an Option',
    ("Medal Tally","Overall Analysis","Country wise Analysis","Athlete wise Analysis")
)


# st.dataframe(df)
st.sidebar.title("Olympics Analysis")
if user_menu=="Medal Tally":
    st.sidebar.header("Medal Tally")
    years,country=helper.Country_year_list(df)
    selected_year=st.sidebar.selectbox("Select Year",years)
    selected_country = st.sidebar.selectbox("Select Country", country)
    medal_tally=helper.fetch_medal(df,selected_year,selected_country)
    if selected_year=="Overall" and selected_country=="Overall":
        st.title("Overall Tally")
    if selected_year!="Overall" and selected_country=="Overall":
        st.title("Medal Tally in " + str(selected_year) + " Olympics")
    if selected_year=="Overall" and selected_country!="Overall":
        st.title(selected_country + " Overall performance in Olympics")
    if selected_year!="Overall" and selected_country!="Overall":
        st.title("Medal Tally for " + selected_country + " in " + str(selected_year))
    st.table(medal_tally)
if user_menu=="Overall Analysis":
    editions=df["Year"].unique().shape[0]-1
    cities=df["City"].unique().shape[0]
    sports=df["Sport"].unique().shape[0]
    events=df["Event"].unique().shape[0]
    athletes=df["Name"].unique().shape[0]
    nations=df["region"].unique().shape[0]
    st.title("Top Statistics")
    col1,col2,col3  = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)

    nations_over_time=helper.data_over_time(df,'region')
    fig = px.line(nations_over_time, x="Year", y="No of Countries")
    st.title("Participating Natios Over the years")
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df,'Event')
    fig = px.line(events_over_time, x="Year", y="No of Countries")
    st.title("Events count Over the years")
    st.plotly_chart(fig)

    athlete_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athlete_over_time, x="Year", y="No of Countries",
                  labels={"No of Countries": "Name", "Year": "Year"})

    st.title("Athletes Over the years")
    st.plotly_chart(fig)

    st.title("No. of events over time (every sport)")
    fig, ax = plt.subplots(figsize=(20, 20))

    x = df.drop_duplicates(subset=['Year', 'Sport', 'Event'])
    ax=sns.heatmap(
    x.pivot_table(index="Sport", columns="Year", values="Event", aggfunc="count").fillna(0).astype(int),annot=True)
    st.pyplot(fig)

    # st.title("Most successful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    # sport_list.insert(0, 'Overall')

    st.title("Most successful Athletes in Olympics history")
    x=helper.get_successful_athletes_overall(df,"")
    st.table(x)

    st.title("successful Athletes on basics sports")
    selected_sport = st.selectbox('Select a Sport', sport_list)
    x = helper.get_successful_athletes(df, selected_sport)
    st.table(x)
if user_menu=="Country wise Analysis":
    st.sidebar.title("Country wise Analysis")
    country_list=df['region'].unique().tolist()
    country_list = [str(item) for item in country_list]
    country_list.sort()
    sel_country=st.sidebar.selectbox("Select a Country",country_list)

    country_df=helper.yearwise_medal_tally(df,sel_country)
    fig=px.line(country_df,x="Year",y="Medal")
    st.title( sel_country +" Medal Tally over the years")
    st.plotly_chart(fig)
    #heat map
    st.title(sel_country+" excels in the following sports")
    fig, ax = plt.subplots(figsize=(20, 20))
    temp_df = df.dropna(subset=["Medal"])
    temp_df.drop_duplicates(subset=['Team', "NOC", 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)
    x= temp_df[temp_df["region"] == sel_country]
    ax=sns.heatmap(x.pivot_table(index='Sport',columns='Year',values='Medal',aggfunc='count').fillna(0),annot=True)
    st.pyplot(fig)
    #top 10
    top10_df=helper.most_successful_countrywise(df,sel_country)
    st.title("Top 10 Athletes of " + sel_country)
    st.table(top10_df)

if user_menu=="Athlete wise Analysis":
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()
    fig = ff.create_distplot([x1, x2, x3, x4], ['Age Distribution', 'Gold', 'Silver', 'Bronze'], show_hist=False,
                             show_rug=False)

    fig.update_layout(autosize=False,width=1000,height=600)
    st.title("Distribution of Age")
    st.plotly_chart(fig)


    # Gold medal age dist
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    # Filter only Gold medalists
    gold_athletes = athlete_df[athlete_df['Medal'] == 'Gold']


    top_sports = gold_athletes['Sport'].value_counts().head(30).index.tolist()


    data = []
    labels = []

    for sport in top_sports:
        ages = gold_athletes[gold_athletes['Sport'] == sport]['Age'].dropna()
        if len(ages) > 0:
            data.append(ages)
            labels.append(sport)

    # Create distribution plot
    fig = ff.create_distplot(data, labels, show_hist=False, show_rug=False)

    # Style the plot
    fig.update_layout(
        title='Age Distribution of Gold Medalists by Sport',
        xaxis_title='Age',
        yaxis_title='Density',
        autosize=False,
        width=1000,
        height=600
    )

    # Streamlit output
    st.title("Age Distribution of Gold Medalists by Sport")
    st.plotly_chart(fig)

    # Sliver


    athlete_df = df.drop_duplicates(subset=['Name', 'region'])


    silver_athletes = athlete_df[athlete_df['Medal'] == 'Silver']

    top_sports = silver_athletes['Sport'].value_counts().head(30).index.tolist()

    # Prepare data and labels
    data = []
    labels = []

    for sport in top_sports:
        ages = silver_athletes[silver_athletes['Sport'] == sport]['Age'].dropna()
        if len(ages) > 0:
            data.append(ages)
            labels.append(sport)

    # Create distribution plot
    fig = ff.create_distplot(data, labels, show_hist=False, show_rug=False)

    # Style the plot
    fig.update_layout(
        title='Age Distribution of Silver Medalists by Sport',
        xaxis_title='Age',
        yaxis_title='Density',
        autosize=False,
        width=1000,
        height=600
    )

    # Streamlit output
    st.title("Age Distribution of Silver Medalists by Sport")
    st.plotly_chart(fig)
    #Bronze
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    bronze_athletes = athlete_df[athlete_df['Medal'] == 'Bronze']

    top_sports = bronze_athletes['Sport'].value_counts().head(30).index.tolist()

    # Prepare data and labels
    data = []
    labels = []

    for sport in top_sports:
        ages = bronze_athletes[bronze_athletes['Sport'] == sport]['Age'].dropna()
        if len(ages) > 0:
            data.append(ages)
            labels.append(sport)

    # Create distribution plot
    fig = ff.create_distplot(data, labels, show_hist=False, show_rug=False)

    # Style the plot
    fig.update_layout(
        title='Age Distribution of Bronze Medalists by Sport',
        xaxis_title='Age',
        yaxis_title='Density',
        autosize=False,
        width=1000,
        height=600
    )

    # Streamlit output
    st.title("Age Distribution of Bronze Medalists by Sport")
    st.plotly_chart(fig)

    st.title("Height Vs Weight")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    temp_df=helper.Weight_V_height(df,selected_sport)
    fig,ax=plt.subplots()
    ax=sns.scatterplot(x=temp_df['Weight'], y=temp_df['Height'],hue=temp_df["Medal"],style=temp_df["Sex"],s=60)

    st.pyplot(fig)


    st.title("Men Vs Women participation Over the Years")
    final=helper.Men_v_women(df)
    fig = px.line(final, x='Year', y=['Male', 'Female'])
    st.plotly_chart(fig)



