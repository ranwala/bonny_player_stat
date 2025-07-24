import pandas as pd

# Load T20 data
df_t20_player_stats = pd.read_csv('files/t20/t20_player_statistics.csv')
df_t20_batting_stats = pd.read_csv('files/t20/t20_batting_stat.csv')
df_t20_bowling_stats = pd.read_csv('files/t20/t20_bowling_stats .csv')

# Load ODI data
df_odi_player_stats = pd.read_csv('files/odi/odi_player_statistics.csv')
df_odi_batting_stats = pd.read_csv('files/odi/odi_batting_stats.csv')
df_odi_bowling_stats = pd.read_csv('files/odi/odi_bowling_stats.csv')

# Filter for relevant team
team_of_interest = ['Bonn CC Blue', 'Bonn CC Yellow', 'Bonn CC']

# Organise data
t20_data_raw = {
    'Player': df_t20_player_stats,
    'Batting': df_t20_batting_stats,
    'Bowling': df_t20_bowling_stats
}

odi_data_raw = {
    'Player': df_odi_player_stats,
    'Batting': df_odi_batting_stats,
    'Bowling': df_odi_bowling_stats
}

# Function for filtering data
def filter_team_data(df_dict, teams):
    return {k: df[df['Team'].isin(teams)] for k, df in df_dict.items()}

# Apply team filter
t20_data = filter_team_data(t20_data_raw, team_of_interest)
odi_data = filter_team_data(odi_data_raw, team_of_interest)

# Columns mapping
column_map = {
    'Player': ['Player', 'Team', 'Matches', 'Batting', 'Bowling', 'Fielding', 'Other', 'Total'],
    'Batting': ['Player', 'Team', 'Matches', 'Inns', 'NO', 'Runs', '4s', '6s', '50s', '100s'
    , 'HS', 'SR', 'Avg'],
    'Bowling': ['Player', 'Team', 'Matches', 'Inns', 'Overs', 'Runs', 'Wkts', 'BBF', 'Mdns', 'Dots'
    , 'Econ', 'Avg', 'SR', 'Hat-trick', '4w', '5w', 'Wides', 'Nb']
}

def get_dataset_by_type(match_type):
    return t20_data if match_type == 'T20' else odi_data

def get_player_statistics(team='All', stat='Player Ranking', match_type='T20'):
    data = get_dataset_by_type(match_type)

    key = stat.split()[0]
    df = data.get(key)
    columns = column_map.get(key)

    if df is None or columns is None:
        return None

    if team != 'All':
        df = df[df['Team'] == team]

    return df[columns]

def get_table_data():
    try:
        df = pd.read_csv('files/odi/odi_point_table.csv')
        return df
    except FileNotFoundError:
        print('File not found')
    except pd.errors.EmptyDataError:
        print('Empty data')
    except pd.errors.ParserError:
        print('Paser error')
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

# Test purpose
if __name__ == '__main__':
    print(get_player_statistics(stat='Player Ranking', match_type='T20'))