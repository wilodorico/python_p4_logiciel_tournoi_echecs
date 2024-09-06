from controllers.main_menu_controller import MainMenuController
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def main():
    text = Text("Bienvenue sur l'application Club d'échecs")
    text.stylize("bold dodger_blue1")
    panel = Panel.fit(text)
    print()
    console.print(panel)
    print()

    controller = MainMenuController()
    controller.run()


if __name__ == "__main__":
    main()
