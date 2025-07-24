from cli_game.controller import GameLoop


def main() -> None:
    game = GameLoop()
    game.run()


if __name__ == "__main__":
    main()
