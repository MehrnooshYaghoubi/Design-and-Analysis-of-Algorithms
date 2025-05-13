from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, Static, Tree
from textual.widgets.tree import TreeNode
from textual.reactive import reactive
from textual.message import Message
from rich.console import Console
from rich.text import Text
from rich.table import Table
import sys

class AlgorithmApp(App):
    """A TUI for selecting and exploring algorithms using Tree widget."""

    CSS = """
        #left-pane {
            background: black;
            color: #88c0d0;
            border: round #5e81ac;
            padding: 1;
        }

        #center-pane {
            background: black;
            color: #d8dee9;
            border: round #a3be8c;
            padding: 1;
        }

        #right-pane {
            background: black;
            color: #ebcb8b;
            border: round #bf616a;
            padding: 1;
        }

        .panel-title {
            color: #b48ead;
        }

        Tree {
            background: transparent;
            color: #88c0d0;
        }

        Tree:focus {
            border: round #81a1c1;
        }
    """

    algorithms = {
        "Sorting Algorithms": [
            "Quick Sort", "Merge Sort", "Bubble Sort",
            "Selection Sort", "Radix Sort", "Insertion Sort"
        ],
        "Greedy Algorithms": [
            "Activity Selection", "Fractional Knapsack", "Huffman Coding",
            "Kruskal Algorithm", "Prims Algorithm"
        ],
        "Dynamic Programming": ["Knapsack 0_1", "Floyd_Warshall"],
        "Divide and Conquer": ["Binary Search", "Closest Pair Of Points"],
        "Graph Algorithms": ["Breadth First Search", "Depth First Search", "Dijkstra"],
    }

    selected_algorithm: reactive[str | None] = reactive(None)

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        self.code_panel = Static(markup=True, name="code-panel")

        self.alg_tree = Tree("Algorithm Categories", id="alg-tree")
        for category, algos in self.algorithms.items():
            parent = self.alg_tree.root.add(category)
            for algo in algos:
                parent.add_leaf(algo)
        self.alg_tree.root.expand_all()

        yield Horizontal(
            Vertical(
                Static("\U0001F4C2 Algorithm Categories", classes="panel-title"),
                self.alg_tree,
                id="left-pane",
            ),
            Vertical(
                Static("Algorithm Details", classes="panel-title"),
                self.code_panel,
                id="center-pane",
            ),
            Vertical(
                Static("Output", classes="panel-title"),
                Static("This is the output panel.", classes="graph-box"),
                id="right-pane",
            )
        )

        yield Footer()

    def on_mount(self):
        self.set_focus(self.alg_tree)

    def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        node = event.node
        algo_name = node.label.plain if node.is_leaf else None
        if algo_name:
            self.selected_algorithm = algo_name
            self.display_algorithm_details(algo_name)

    def display_algorithm_details(self, algorithm: str):
        details = {
            "Quick Sort": ("O(n log n)", "O(log n)"),
            "Merge Sort": ("O(n log n)", "O(n)"),
            "Bubble Sort": ("O(n^2)", "O(1)"),
            "Selection Sort": ("O(n^2)", "O(1)"),
            "Radix Sort": ("O(nk)", "O(n+k)"),
            "Insertion Sort": ("O(n^2)", "O(1)"),
            "Activity Selection": ("Greedy algorithm to select maximum non-overlapping activities.",),
            "Fractional Knapsack": ("Greedy algorithm to maximize value in a knapsack.",),
            "Huffman Coding": ("Greedy algorithm for data compression.",),
            "Kruskal Algorithm": ("Greedy algorithm for Minimum Spanning Tree.",),
            "Prims Algorithm": ("Greedy algorithm for Minimum Spanning Tree.",),
            "Knapsack 0_1": ("Dynamic Programming algorithm for 0/1 Knapsack problem.",),
            "Floyd_Warshall": ("Dynamic Programming algorithm for all-pairs shortest paths.",),
            "Binary Search": ("Divide and Conquer algorithm for searching in sorted arrays.",),
            "Closest Pair Of Points": ("Divide and Conquer algorithm for closest pair of points.",),
            "Breadth First Search": ("Graph traversal algorithm using a queue.",),
            "Depth First Search": ("Graph traversal algorithm using recursion or a stack.",),
            "Dijkstra": ("Graph algorithm for shortest paths from a source vertex.",),
        }

        if algorithm in details:
            detail = details[algorithm]
            table = Table(title=f"[bold cyan]{algorithm} Details[/bold cyan]")
            table.add_column("Property", style="bold magenta")
            table.add_column("Value", style="bold green")
            if len(detail) == 2:
                table.add_row("Time Complexity", detail[0])
                table.add_row("Space Complexity", detail[1])
            else:
                table.add_row("Description", detail[0])

            console = Console()
            console_text = Text()
            console_text.append("\n")
            console_text.append(table)
            self.code_panel.update(console_text)
        else:
            self.code_panel.update(f"[bold red]Details not available for {algorithm}.[/bold red]")


if __name__ == "__main__":
    if sys.platform.startswith("linux"):
        AlgorithmApp().run()
    else:
        print("This TUI app only runs in a Unix-like terminal environment (Linux/macOS).")