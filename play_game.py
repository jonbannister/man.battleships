from collections import Counter

import argparse

from config import GAMES_PER_MATCH
from game_types import Game


def play_match(player_1_bot: str, player_2_bot: str, n_games=GAMES_PER_MATCH):
    """
    Plays 'n_games' between 'player_1_bot' and 'player_2_bot' and returns a dictionary of all game info

    :param player_1_bot:
    :param player_2_bot:
    :param n_games:
    :return:
    """

    game_data = []

    for game_id in range(n_games):
        game_data.append(Game([player_1_bot, player_2_bot], game_id).play_game())
        print(f'Finished game {game_id}: winner was {game_data[-1]["winner"]}')

    return game_data


def do_play_match(player_1, player_2, n):
    results = play_match(player_1, player_2, n_games=n)
    return Counter([game["winner"] for game in results])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Play games of battleships between two bots')
    parser.add_argument('-n', type=int, default=10, help='The number of games to play between <bot_1> and <bot_2>')
    parser.add_argument('player_1', type=str, default='ForwardBot', help='First bot to participate in the game')
    parser.add_argument('player_2', type=str, default='BackwardBot', help='Second bot to participate in the game')
    args = parser.parse_args()

    result = do_play_match(args.player_1, args.player_2, args.n)
    print('---------------------------------------')
    print(dict(result))
