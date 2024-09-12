from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def alert_message(message: str, styling: str = "white"):
    """Displays a stylised message in a Rich panel in a custom styling.

    Args:
        message (str): message to display.
        styling (str, optional): styling display. Defaults to "white".
    """

    text = Text(message)
    text.stylize(styling)
    panel = Panel.fit(text)
    console.print(panel)
