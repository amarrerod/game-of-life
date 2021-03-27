"""Console script for game_of_life."""
import argparse
import sys


def main():
    """Console script for game_of_life."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "game_of_life.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
