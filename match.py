import ISMCTS
import random
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--players', type=int, help='number of players (default:4)', default=4)
    parser.add_argument('--seed', type=int, help='random seed (default:None)', default=None)
    parser.add_argument('--repeat', type=int, help='number of games to play', default=1)
    args = parser.parse_args()
    
    random.seed(args.seed)
    agents = {
        1: lambda s: ISMCTS.ISMCTS(rootstate=s, itermax=1000, verbose=False),
        2: lambda s: ISMCTS.ISMCTS(rootstate=s, itermax=100, verbose=False),
    }
    for i in range(args.repeat):
        ISMCTS.PlayGame(args.players, agents)

if __name__ == "__main__":
    main()
