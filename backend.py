import pandas as pd

# Load data
df_player_stats = pd.read_csv('files/t20_player_statistics.csv')
df_batting_stats = pd.read_csv('files/t20_batting_stat.csv')
df_bowling_stats = pd.read_csv('files/t20_bowling_stats .csv')

# Filter for relevant team
team_of_interest = ['Bonn CC Blue', 'Bonn CC Yellow']
player_stat_data = df_player_stats.loc[df_player_stats['Team'].isin(team_of_interest)]
batting_data = df_batting_stats.loc[df_batting_stats['Team'].isin(team_of_interest)]
bowling_data = df_bowling_stats.loc[df_bowling_stats['Team'].isin(team_of_interest)]

# Define columns
player_ranking_columns = ['Player', 'Team', 'Matches', 'Batting', 'Bowling', 'Fielding', 'Other', 'Total']
batting_ranking_columns = ['Player', 'Team', 'Matches', 'Inns', 'NO', 'Runs', '4s', '6s', '50s', '100s'
    , 'HS', 'SR', 'Avg']
bowling_ranking_columns = ['Player', 'Team', 'Matches', 'Inns', 'Overs', 'Runs', 'Wkts', 'BBF', 'Mdns', 'Dots'
    , 'Econ', 'Avg', 'SR', 'Hat-trick', '4w', '5w', 'Wides', 'Nb']

def get_player_statistics(team='All', stat='Player Ranking'):
    if stat == 'Player Ranking':
        df = player_stat_data
        columns = player_ranking_columns
    elif stat == 'Batting Records':
        df = batting_data
        columns = batting_ranking_columns
    elif stat == 'Bowling Records':
        df = bowling_data
        columns = bowling_ranking_columns
    else:
        return None

    if team != 'All':
        df = df[df['Team'] == team]

    return df[columns]


if __name__ == '__main__':
    print(get_player_statistics(stat='Player Ranking'))