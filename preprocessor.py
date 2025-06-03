import pandas as pd

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

def preprocess():
    global df, region_df

    # Keep only Summer Olympics data
    df = df[df['Season'] == "Summer"]

    # Drop overlapping columns in region_df (except for 'NOC' which is used to merge)
    region_df = region_df.drop(columns=[col for col in ['region', 'notes'] if col in df.columns], errors='ignore')

    # Merge safely
    df = df.merge(region_df, on="NOC", how="left")

    # Drop duplicate rows if any
    df.drop_duplicates(inplace=True)

    # Create medal indicator columns
    df['Gold'] = (df['Medal'] == 'Gold').astype(int)
    df['Silver'] = (df['Medal'] == 'Silver').astype(int)
    df['Bronze'] = (df['Medal'] == 'Bronze').astype(int)

    return df
