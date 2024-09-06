from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def alert_message(message: str, color: str = "white"):
    """Displays a stylised message in a Rich panel in a custom color.

    Args:
        message (str): message to display.
        color (str, optional): Color display. Defaults to "white".
    """

    text = Text(message)
    text.stylize(color)
    panel = Panel.fit(text)
    console.print(panel)
