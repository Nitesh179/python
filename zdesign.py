from rich.console import Console
from rich.table import Table

table = Table(title="Star Wars Movies")

table.add_column("Acc.No", justify="right", style="cyan", no_wrap=True)
table.add_column("Customer Name", style="grey0")
table.add_column("Balance", justify="right", style="green")

table.add_row("13210", "Star Wars: The Rise of Skywalker")
table.add_row("13210", "Solo: A Star Wars Story", "$393,151,347")
table.add_row("13210", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
table.add_row("13210", "Rogue One: A Star Wars Story", "$1,332,439,889")

console = Console()
console.print(table)