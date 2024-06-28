from controllers.main_menu_controller import MainMenuController


def main():
    print("---------------------------------------------")
    print("Bienvenue sur l'application Club d'échecs ")
    print("---------------------------------------------")

    controller = MainMenuController()
    controller.run()


if __name__ == "__main__":
    main()
