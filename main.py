from controllers.main_menu_controller import MainMenuController
from utils.rich_component import alert_message


def main():
    alert_message("Bienvenue sur l'application Club d'échecs", "bold dodger_blue1")

    controller = MainMenuController()
    controller.run()


if __name__ == "__main__":
    main()
