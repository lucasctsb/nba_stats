from nba_api.stats.static import players
from nba_api.stats.endpoints import PlayerCareerStats
import pandas as pd

# Get player ID & active stats
def get_player_id(player_name):
    player_dict = players.get_players()
    find_player = next((player for player in player_dict if player['full_name'] == player_name), None)
    if find_player:
        return find_player['id'], find_player['is_active']
    else:
        return None, None

# Get player stats -> add to dataframe
def get_player_stats(player_id):
    career_stats = PlayerCareerStats(player_id)
    career_df = career_stats.get_data_frames()[0]
    return career_df

# Display player stats
def display_season_stats(player_stats):
    current_season = player_stats.loc[player_stats['SEASON_ID'] == '2023-24']
    if not current_season.empty:
        player_stats = current_season[['TEAM_ABBREVIATION', 'GP', 'REB', 'AST', 'PTS']].astype({'REB': float, "AST": float, 'PTS': float})
        player_stats[['REB', 'AST', 'PTS']] = player_stats[['REB', 'AST', 'PTS']].div(player_stats['GP'], axis=0)
        print(player_stats.head())
    else:
        print("No stats available for the current season.")

# Loop and function calls
def main():
    while True:
        player_name = input('Player name: ')
        player_id, is_active = get_player_id(player_name)
        if player_id:
            print(f'The ID of {player_name} is {player_id}')
            if is_active:
                print('The player is active')
            else:
                print('The player is not active')
            player_stats = get_player_stats(player_id)
            display_season_stats(player_stats)
        else:
            print("Player not found. Please enter a valid player name.")

if __name__ == "__main__":
    main()
