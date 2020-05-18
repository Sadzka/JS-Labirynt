def main():
    from game import Game

    from GUI.errorshower import ErrorshowerException
    from GUI.errorshower import Errorshower as ES

    game = Game()

    while game.is_running():
        try:
            game.update()
            game.render()
        except ErrorshowerException as exc:
            ES.show(exc.get_value())

if __name__ == '__main__':
    main()
    