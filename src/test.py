# # # # # # # # # # # from datetime import datetime
# # # # # # # # # # # from rich.console import Console
# # # # # # # # # # # from rich.layout import Layout
# # # # # # # # # # # from rich.panel import Panel
# # # # # # # # # # # from rich.progress import Progress
# # # # # # # # # # # from rich.syntax import Syntax
# # # # # # # # # # # from rich.table import Table
# # # # # # # # # # # from rich.text import Text
# # # # # # # # # # # from rich.tree import Tree

# # # # # # # # # # # console = Console()

# # # # # # # # # # # def make_layout():
# # # # # # # # # # #     """Create the main layout structure."""
# # # # # # # # # # #     layout = Layout()

# # # # # # # # # # #     layout.split(
# # # # # # # # # # #         Layout(name="header", size=3),
# # # # # # # # # # #         Layout(name="body", ratio=1),
# # # # # # # # # # #         Layout(name="footer", size=3),
# # # # # # # # # # #     )
# # # # # # # # # # #     layout["body"].split_row(
# # # # # # # # # # #         Layout(name="tree"),
# # # # # # # # # # #         Layout(name="code"),
# # # # # # # # # # #         Layout(name="jobs"),
# # # # # # # # # # #     )
# # # # # # # # # # #     layout["jobs"].split_column(
# # # # # # # # # # #         Layout(name="Output"),
# # # # # # # # # # #         Layout(name="graph"),
# # # # # # # # # # #     )
# # # # # # # # # # #     return layout

# # # # # # # # # # # def make_header():
# # # # # # # # # # #     """Create the header panel."""
# # # # # # # # # # #     return Panel(
# # # # # # # # # # #         Text("🌟 Design and Analysis of Algorithms 🌟", style="bold cyan"),
# # # # # # # # # # #         style="white on blue"
# # # # # # # # # # #     )
# # # # # # # # # # # def make_tree():
# # # # # # # # # # #     """Create the tree panel with selectable algorithm categories."""
# # # # # # # # # # #     tree = Tree("📂 [bold magenta]Algorithm Categories[/bold magenta]")
# # # # # # # # # # #     sorting = tree.add("📁 [cyan]Sorting Algorithms[/cyan]")
# # # # # # # # # # #     sorting.add("Quick Sort")
# # # # # # # # # # #     sorting.add("Merge Sort")
# # # # # # # # # # #     sorting.add("Bub ble Sort")
# # # # # # # # # # #     sorting.add("Selection Sort")
# # # # # # # # # # #     sorting.add("Radix Sort")
# # # # # # # # # # #     sorting.add("Insertion Sort")
# # # # # # # # # # #     greedy = tree.add("📁 [cyan]Greedy Algorithms[/cyan]")
# # # # # # # # # # #     greedy.add("Activity Selection")
# # # # # # # # # # #     greedy.add("Freactional Knapsack")
# # # # # # # # # # #     greedy.add("Huffman Coding")
# # # # # # # # # # #     greedy.add("Kruskal Algorithm")
# # # # # # # # # # #     greedy.add("Prims Algorithm")
# # # # # # # # # # #     dp = tree.add("📁 [cyan]Dynamic Programming[/cyan]")
# # # # # # # # # # #     dp.add("Knapsack 0/1")
# # # # # # # # # # #     dp.add("Floyd-Warshall")
# # # # # # # # # # #     divide_and_conquer = tree.add("📁 [cyan]Divide and Conquer[/cyan]")
# # # # # # # # # # #     divide_and_conquer.add("Binary Search")
# # # # # # # # # # #     divide_and_conquer.add("Closest Pair Of Points")
# # # # # # # # # # #     graph = tree.add("📁 [cyan]Graph Algortihms[/cyan]")
# # # # # # # # # # #     graph.add("Breadth First Search")
# # # # # # # # # # #     graph.add("Depth First Search")
# # # # # # # # # # #     graph.add("Dijkstra's Algorithm")

# # # # # # # # # # #     return Panel(tree, title="Select Algorithm", border_style="green")


# # # # # # # # # # # def make_code():
# # # # # # # # # # #     """Create the code panel."""
# # # # # # # # # # #     code = ''''''
# # # # # # # # # # #     syntax = Syntax(code, "python", line_numbers=True, theme="monokai", word_wrap=True)
# # # # # # # # # # #     return Panel(syntax, title="Getting Inputs", border_style="magenta")

# # # # # # # # # # # def make_jobs():
# # # # # # # # # # #     """Create the jobs panel with progress bars."""
# # # # # # # # # # #     progress = Progress()
# # # # # # # # # # #     progress.add_task("[cyan]Cooking", total=100, completed=100)
# # # # # # # # # # #     progress.add_task("[green]Baking", total=100, completed=72)
# # # # # # # # # # #     progress.add_task("[red]Mixing", total=100, completed=36)
# # # # # # # # # # #     return Panel(progress, title="Jobs", border_style="red")

# # # # # # # # # # # def make_footer_with_grid():
# # # # # # # # # # #     now = datetime.now().strftime("%a %b %d %H:%M:%S %Y")

# # # # # # # # # # #     grid = Table.grid(expand=True)
# # # # # # # # # # #     grid.add_column(justify="center", ratio=1)
# # # # # # # # # # #     grid.add_column(justify="center", ratio=1)
# # # # # # # # # # #     grid.add_column(justify="center", ratio=1)

# # # # # # # # # # #     grid.add_row(
# # # # # # # # # # #         "[bold green]Status: Active[/bold green]",
# # # # # # # # # # #         f"[bold yellow]Time: {now}[/bold yellow]",
# # # # # # # # # # #         "[bold cyan]User: Mehrnoosh[/bold cyan]",
# # # # # # # # # # #     )

# # # # # # # # # # #     return Panel(grid, style="white on black", title="Footer Grid")

# # # # # # # # # # # def make_output():
# # # # # # # # # # #     """Create the output panel."""
# # # # # # # # # # #     progress = Progress()
# # # # # # # # # # #     progress.add_task("[cyan]test", total=100, completed=100)
# # # # # # # # # # #     progress.add_task("[green]test", total=100, completed=72)
# # # # # # # # # # #     progress.add_task("[red]test", total=100, completed=36)
# # # # # # # # # # #     progress.add_task("[purple]test", total=100, completed=100)
# # # # # # # # # # #     progress.add_task("[yellow]test", total=100, completed=72)
# # # # # # # # # # #     progress.add_task("[red]test", total=100, completed=36)
# # # # # # # # # # #     progress.add_task("[cyan]test", total=100, completed=100)
# # # # # # # # # # #     progress.add_task("[green]test", total=100, completed=72)
# # # # # # # # # # #     progress.add_task("[red]test", total=100, completed=36)
# # # # # # # # # # #     progress.add_task("[yellow]test", total=100, completed=72)
# # # # # # # # # # #     progress.add_task("[red]test", total=100, completed=36)
# # # # # # # # # # #     progress.add_task("[cyan]test", total=100, completed=100)
# # # # # # # # # # #     progress.add_task("[green]test", total=100, completed=72)
# # # # # # # # # # #     progress.add_task("[red]test", total=100, completed=36)
    
# # # # # # # # # # #     return Panel(progress, title="Output", border_style="green")

# # # # # # # # # # # def make_graph():
# # # # # # # # # # #     """Create the graph panel."""
# # # # # # # # # # #     graph_text = Text("This is the graph panel.", style="bold blue")
# # # # # # # # # # #     return Panel(graph_text, title="Graph", border_style="blue")


# # # # # # # # # # # def main():
# # # # # # # # # # #     """Main function to render the layout."""
# # # # # # # # # # #     layout = make_layout()
# # # # # # # # # # #     layout["header"].update(make_header())
# # # # # # # # # # #     layout["footer"].update(make_footer_with_grid())
# # # # # # # # # # #     layout["tree"].update(make_tree())
# # # # # # # # # # #     layout["code"].update(make_code())
# # # # # # # # # # #     layout["jobs"].update(make_jobs())
# # # # # # # # # # #     layout["Output"].update(make_output())  # Update Output panel
# # # # # # # # # # #     layout["graph"].update(make_graph())    # Update Graph panel

# # # # # # # # # # #     console.clear()
# # # # # # # # # # #     console.print(layout)

# # # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # # #     main()

# # # # # # # # # # from textual.app import App, ComposeResult
# # # # # # # # # # from textual.containers import Horizontal, Vertical, Container
# # # # # # # # # # from textual.widgets import Header, Footer, Tree, Static, Button, ProgressBar, Label, Log
# # # # # # # # # # from textual.reactive import reactive
# # # # # # # # # # from textual.message import Message
# # # # # # # # # # from datetime import datetime

# # # # # # # # # # class AlgorithmApp(App):
# # # # # # # # # #     CSS = """
# # # # # # # # # #     /* Define the CSS directly in the Python file */
# # # # # # # # # #     #left-pane {
# # # # # # # # # #         background: #3b4252;
# # # # # # # # # #         color: white;
# # # # # # # # # #         padding: 10px;
# # # # # # # # # #     }

# # # # # # # # # #     #right-pane {
# # # # # # # # # #         background: #4c566a;
# # # # # # # # # #         color: white;
# # # # # # # # # #         padding: 10px;
# # # # # # # # # #     }
# # # # # # # # # # CSS_PATH = 
# # # # # # # # # #     .panel-title {
# # # # # # # # # #         font-weight: bold;
# # # # # # # # # #         color: #81a1c1;
# # # # # # # # # #     }

# # # # # # # # # #     .code-panel {
# # # # # # # # # #         background: #2e3440;
# # # # # # # # # #         color: #eceff4;
# # # # # # # # # #         padding: 10px;
# # # # # # # # # #         border-radius: 5px;
# # # # # # # # # #     }

# # # # # # # # # #     .graph-box {
# # # # # # # # # #         background: #88c0d0;
# # # # # # # # # #         color: white;
# # # # # # # # # #         padding: 20px;
# # # # # # # # # #         border-radius: 5px;
# # # # # # # # # #     }

# # # # # # # # # #     .progress-bar {
# # # # # # # # # #         height: 20px;
# # # # # # # # # #         margin-bottom: 10px;
# # # # # # # # # #     }
# # # # # # # # # #     """

# # # # # # # # # #     class TreeSelected(Message):
# # # # # # # # # #         def __init__(self, label: str) -> None:
# # # # # # # # # #             self.label = label
# # # # # # # # # #             super().__init__()

# # # # # # # # # #     def compose(self) -> ComposeResult:
# # # # # # # # # #         yield Header(show_clock=True)

# # # # # # # # # #         self.code_panel = Log(highlight=True, markup=True, wrap=True, name="code-panel")

# # # # # # # # # #         yield Horizontal(
# # # # # # # # # #             Vertical(
# # # # # # # # # #                 Static("\U0001F4C2 Algorithm Categories", classes="panel-title"),
# # # # # # # # # #                 self.make_tree(),
# # # # # # # # # #                 id="left-pane",
# # # # # # # # # #             ),
# # # # # # # # # #             Vertical(
# # # # # # # # # #                 Static("Getting Inputs", classes="panel-title"),
# # # # # # # # # #                 self.code_panel,
# # # # # # # # # #                 id="center-pane",
# # # # # # # # # #             ),
# # # # # # # # # #             Vertical(
# # # # # # # # # #                 Static("Jobs", classes="panel-title"),
# # # # # # # # # #                 self.make_jobs_panel(),
# # # # # # # # # #                 Static("Output", classes="panel-title"),
# # # # # # # # # #                 self.make_output_panel(),
# # # # # # # # # #                 Static("Graph", classes="panel-title"),
# # # # # # # # # #                 Static("This is the graph panel.", classes="graph-box"),
# # # # # # # # # #                 id="right-pane",
# # # # # # # # # #             ),
# # # # # # # # # #         )

# # # # # # # # # #         yield Footer()

# # # # # # # # # #     def make_tree(self):
# # # # # # # # # #         tree = Tree("Algorithm Categories", id="alg-tree")
# # # # # # # # # #         sorting = tree.root.add("Sorting Algorithms")
# # # # # # # # # #         for algo in ["Quick Sort", "Merge Sort", "Bubble Sort", "Selection Sort", "Radix Sort", "Insertion Sort"]:
# # # # # # # # # #             sorting.add_leaf(algo)

# # # # # # # # # #         greedy = tree.root.add("Greedy Algorithms")
# # # # # # # # # #         for algo in ["Activity Selection", "Fractional Knapsack", "Huffman Coding", "Kruskal Algorithm", "Prims Algorithm"]:
# # # # # # # # # #             greedy.add_leaf(algo)

# # # # # # # # # #         dp = tree.root.add("Dynamic Programming")
# # # # # # # # # #         for algo in ["Knapsack 0/1", "Floyd-Warshall"]:
# # # # # # # # # #             dp.add_leaf(algo)

# # # # # # # # # #         divide = tree.root.add("Divide and Conquer")
# # # # # # # # # #         for algo in ["Binary Search", "Closest Pair Of Points"]:
# # # # # # # # # #             divide.add_leaf(algo)

# # # # # # # # # #         graph = tree.root.add("Graph Algorithms")
# # # # # # # # # #         for algo in ["Breadth First Search", "Depth First Search", "Dijkstra's Algorithm"]:
# # # # # # # # # #             graph.add_leaf(algo)

# # # # # # # # # #         tree.root.expand()
# # # # # # # # # #         return tree

# # # # # # # # # #     def make_jobs_panel(self):
# # # # # # # # # #         return Vertical(
# # # # # # # # # #             Label("Cooking"), ProgressBar(total=100, value=100),
# # # # # # # # # #             Label("Baking"), ProgressBar(total=100, value=72),
# # # # # # # # # #             Label("Mixing"), ProgressBar(total=100, value=36)
# # # # # # # # # #         )

# # # # # # # # # #     def make_output_panel(self):
# # # # # # # # # #         panel = Vertical()
# # # # # # # # # #         for label, value in zip(["test"] * 14, [100, 72, 36, 100, 72, 36, 100, 72, 36, 72, 36, 100, 72, 36]):
# # # # # # # # # #             panel.mount(Label(label), ProgressBar(total=100, value=value))
# # # # # # # # # #         return panel

# # # # # # # # # #     async def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
# # # # # # # # # #         label = event.node.label
# # # # # # # # # #         if isinstance(label, str):
# # # # # # # # # #             self.code_panel.write(f"[bold yellow]Selected:[/bold yellow] {label}")

# # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # #     AlgorithmApp().run()
# # # # # # # # # from textual.app import App, ComposeResult
# # # # # # # # # from textual.containers import Horizontal, Vertical
# # # # # # # # # from textual.widgets import Header, Footer, Tree, Static
# # # # # # # # # from textual.message import Message


# # # # # # # # # class AlgorithmApp(App):
# # # # # # # # #     """A TUI for selecting and exploring algorithms."""

# # # # # # # # #     CSS = """
# # # # # # # # #         #left-pane {
# # # # # # # # #             background: #3b4252;
# # # # # # # # #             color: white;
# # # # # # # # #             padding: 1 1; /* Simplified padding */
# # # # # # # # #         }

# # # # # # # # #         #center-pane {
# # # # # # # # #             background: #2e3440;
# # # # # # # # #             color: #eceff4;
# # # # # # # # #             padding: 1 1; /* Simplified padding */
# # # # # # # # #         }

# # # # # # # # #         #right-pane {
# # # # # # # # #             background: #4c566a;
# # # # # # # # #             color: white;
# # # # # # # # #             padding: 1 1; /* Simplified padding */
# # # # # # # # #         }

# # # # # # # # #         .panel-title {
# # # # # # # # #             color: #81a1c1; /* Removed unsupported font-weight */
# # # # # # # # #         }
# # # # # # # # #         """

# # # # # # # # #     class TreeSelected(Message):
# # # # # # # # #         """Message sent when a tree node is selected."""
# # # # # # # # #         def __init__(self, label: str) -> None:
# # # # # # # # #             self.label = label
# # # # # # # # #             super().__init__()

# # # # # # # # #     def compose(self) -> ComposeResult:
# # # # # # # # #         """Compose the layout of the TUI."""
# # # # # # # # #         yield Header(show_clock=True)

# # # # # # # # #         self.code_panel = Static(highlight=True, markup=True, name="code-panel")

# # # # # # # # #         yield Horizontal(
# # # # # # # # #             Vertical(
# # # # # # # # #                 Static("\U0001F4C2 Algorithm Categories", classes="panel-title"),
# # # # # # # # #                 self.make_tree(),
# # # # # # # # #                 id="left-pane",
# # # # # # # # #             ),
# # # # # # # # #             Vertical(
# # # # # # # # #                 Static("Algorithm Details", classes="panel-title"),
# # # # # # # # #                 self.code_panel,
# # # # # # # # #                 id="center-pane",
# # # # # # # # #             ),
# # # # # # # # #             Vertical(
# # # # # # # # #                 Static("Output", classes="panel-title"),
# # # # # # # # #                 Static("This is the output panel.", classes="graph-box"),
# # # # # # # # #                 id="right-pane",
# # # # # # # # #             ),
# # # # # # # # #         )

# # # # # # # # #         yield Footer()

# # # # # # # # #     def make_tree(self):
# # # # # # # # #         """Create the tree panel with algorithm categories."""
# # # # # # # # #         tree = Tree("Algorithm Categories", id="alg-tree")
# # # # # # # # #         sorting = tree.root.add("Sorting Algorithms")
# # # # # # # # #         for algo in ["Quick Sort", "Merge Sort", "Bubble Sort", "Selection Sort", "Radix Sort", "Insertion Sort"]:
# # # # # # # # #             sorting.add_leaf(algo)

# # # # # # # # #         greedy = tree.root.add("Greedy Algorithms")
# # # # # # # # #         for algo in ["Activity Selection", "Fractional Knapsack", "Huffman Coding", "Kruskal Algorithm", "Prims Algorithm"]:
# # # # # # # # #             greedy.add_leaf(algo)

# # # # # # # # #         dp = tree.root.add("Dynamic Programming")
# # # # # # # # #         for algo in ["Knapsack 0/1", "Floyd-Warshall"]:
# # # # # # # # #             dp.add_leaf(algo)

# # # # # # # # #         divide = tree.root.add("Divide and Conquer")
# # # # # # # # #         for algo in ["Binary Search", "Closest Pair Of Points"]:
# # # # # # # # #             divide.add_leaf(algo)

# # # # # # # # #         graph = tree.root.add("Graph Algorithms")
# # # # # # # # #         for algo in ["Breadth First Search", "Depth First Search", "Dijkstra's Algorithm"]:
# # # # # # # # #             graph.add_leaf(algo)

# # # # # # # # #         tree.root.expand()
# # # # # # # # #         return tree

# # # # # # # # #     async def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
# # # # # # # # #         """Handle tree node selection."""
# # # # # # # # #         label = event.node.label
# # # # # # # # #         if isinstance(label, str):
# # # # # # # # #             self.code_panel.update(f"[bold yellow]Selected Algorithm:[/bold yellow] {label}")
# # # # # # # # #             self.display_algorithm_details(label)

# # # # # # # # #     def display_algorithm_details(self, algorithm: str):
# # # # # # # # #         """Display details of the selected algorithm."""
# # # # # # # # #         details = {
# # # # # # # # #             "Quick Sort": "Time Complexity: O(n log n)\nSpace Complexity: O(log n)",
# # # # # # # # #             "Merge Sort": "Time Complexity: O(n log n)\nSpace Complexity: O(n)",
# # # # # # # # #             "Bubble Sort": "Time Complexity: O(n^2)\nSpace Complexity: O(1)",
# # # # # # # # #             "Selection Sort": "Time Complexity: O(n^2)\nSpace Complexity: O(1)",
# # # # # # # # #             "Radix Sort": "Time Complexity: O(nk)\nSpace Complexity: O(n+k)",
# # # # # # # # #             "Insertion Sort": "Time Complexity: O(n^2)\nSpace Complexity: O(1)",
# # # # # # # # #             "Activity Selection": "Greedy algorithm to select maximum non-overlapping activities.",
# # # # # # # # #             "Fractional Knapsack": "Greedy algorithm to maximize value in a knapsack.",
# # # # # # # # #             "Huffman Coding": "Greedy algorithm for data compression.",
# # # # # # # # #             "Kruskal Algorithm": "Greedy algorithm for Minimum Spanning Tree.",
# # # # # # # # #             "Prims Algorithm": "Greedy algorithm for Minimum Spanning Tree.",
# # # # # # # # #             "Knapsack 0/1": "Dynamic Programming algorithm for 0/1 Knapsack problem.",
# # # # # # # # #             "Floyd-Warshall": "Dynamic Programming algorithm for all-pairs shortest paths.",
# # # # # # # # #             "Binary Search": "Divide and Conquer algorithm for searching in sorted arrays.",
# # # # # # # # #             "Closest Pair Of Points": "Divide and Conquer algorithm for closest pair of points.",
# # # # # # # # #             "Breadth First Search": "Graph traversal algorithm using a queue.",
# # # # # # # # #             "Depth First Search": "Graph traversal algorithm using recursion or a stack.",
# # # # # # # # #             "Dijkstra's Algorithm": "Graph algorithm for shortest paths from a source vertex."
# # # # # # # # #         }

# # # # # # # # #         detail_text = details.get(algorithm, "Details not available for this algorithm.")
# # # # # # # # #         self.code_panel.update(f"[bold cyan]{algorithm}[/bold cyan]\n{detail_text}")


# # # # # # # # # if __name__ == "__main__":
# # # # # # # # #     AlgorithmApp().run()


# # # # # # # # from textual.app import App, ComposeResult
# # # # # # # # from textual.containers import Horizontal, Vertical
# # # # # # # # from textual.widgets import Header, Footer, Tree, Static
# # # # # # # # from textual.message import Message


# # # # # # # # class AlgorithmApp(App):
# # # # # # # #     """A TUI for selecting and exploring algorithms."""

# # # # # # # #     CSS = """
# # # # # # # #         #left-pane {
# # # # # # # #             background: #3b4252;
# # # # # # # #             color: white;
# # # # # # # #             padding: 1 1; /* Simplified padding */
# # # # # # # #         }

# # # # # # # #         #center-pane {
# # # # # # # #             background: #2e3440;
# # # # # # # #             color: #eceff4;
# # # # # # # #             padding: 1 1; /* Simplified padding */
# # # # # # # #         }

# # # # # # # #         #right-pane {
# # # # # # # #             background: #4c566a;
# # # # # # # #             color: white;
# # # # # # # #             padding: 1 1; /* Simplified padding */
# # # # # # # #         }

# # # # # # # #         .panel-title {
# # # # # # # #             color: #81a1c1; /* Removed unsupported font-weight */
# # # # # # # #         }
# # # # # # # #         """

# # # # # # # #     class TreeSelected(Message):
# # # # # # # #         """Message sent when a tree node is selected."""
# # # # # # # #         def __init__(self, label: str) -> None:
# # # # # # # #             self.label = label
# # # # # # # #             super().__init__()

# # # # # # # #     def compose(self) -> ComposeResult:
# # # # # # # #         """Compose the layout of the TUI."""
# # # # # # # #         yield Header(show_clock=True)

# # # # # # # #         self.code_panel = Static(highlight=True, markup=True, name="code-panel")

# # # # # # # #         yield Horizontal(
# # # # # # # #             Vertical(
# # # # # # # #                 Static("\U0001F4C2 Algorithm Categories", classes="panel-title"),
# # # # # # # #                 self.make_tree(),
# # # # # # # #                 id="left-pane",
# # # # # # # #             ),
# # # # # # # #             Vertical(
# # # # # # # #                 Static("Algorithm Details", classes="panel-title"),
# # # # # # # #                 self.code_panel,
# # # # # # # #                 id="center-pane",
# # # # # # # #             ),
# # # # # # # #             Vertical(
# # # # # # # #                 Static("Output", classes="panel-title"),
# # # # # # # #                 Static("This is the output panel.", classes="graph-box"),
# # # # # # # #                 id="right-pane",
# # # # # # # #             ),
# # # # # # # #         )

# # # # # # # #         yield Footer()

# # # # # # # #     def make_tree(self):
# # # # # # # #         """Create the tree panel with algorithm categories."""
# # # # # # # #         tree = Tree("Algorithm Categories", id="alg-tree")
# # # # # # # #         sorting = tree.root.add("Sorting Algorithms")
# # # # # # # #         for algo in ["Quick Sort", "Merge Sort", "Bubble Sort", "Selection Sort", "Radix Sort", "Insertion Sort"]:
# # # # # # # #             sorting.add_leaf(algo)

# # # # # # # #         greedy = tree.root.add("Greedy Algorithms")
# # # # # # # #         for algo in ["Activity Selection", "Fractional Knapsack", "Huffman Coding", "Kruskal Algorithm", "Prims Algorithm"]:
# # # # # # # #             greedy.add_leaf(algo)

# # # # # # # #         dp = tree.root.add("Dynamic Programming")
# # # # # # # #         for algo in ["Knapsack 0/1", "Floyd-Warshall"]:
# # # # # # # #             dp.add_leaf(algo)

# # # # # # # #         divide = tree.root.add("Divide and Conquer")
# # # # # # # #         for algo in ["Binary Search", "Closest Pair Of Points"]:
# # # # # # # #             divide.add_leaf(algo)

# # # # # # # #         graph = tree.root.add("Graph Algorithms")
# # # # # # # #         for algo in ["Breadth First Search", "Depth First Search", "Dijkstra's Algorithm"]:
# # # # # # # #             graph.add_leaf(algo)

# # # # # # # #         tree.root.expand()
# # # # # # # #         return tree

# # # # # # # #     async def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
# # # # # # # #         """Handle tree node selection."""
# # # # # # # #         label = event.node.label
# # # # # # # #         if isinstance(label, str):
# # # # # # # #             self.code_panel.update(f"[bold yellow]Selected Algorithm:[/bold yellow] {label}")
# # # # # # # #             self.display_algorithm_details(label)

# # # # # # # #     def display_algorithm_details(self, algorithm: str):
# # # # # # # #         """Display details of the selected algorithm."""
# # # # # # # #         details = {
# # # # # # # #             "Quick Sort": "Time Complexity: O(n log n)\nSpace Complexity: O(log n)",
# # # # # # # #             "Merge Sort": "Time Complexity: O(n log n)\nSpace Complexity: O(n)",
# # # # # # # #             "Bubble Sort": "Time Complexity: O(n^2)\nSpace Complexity: O(1)",
# # # # # # # #             "Selection Sort": "Time Complexity: O(n^2)\nSpace Complexity: O(1)",
# # # # # # # #             "Radix Sort": "Time Complexity: O(nk)\nSpace Complexity: O(n+k)",
# # # # # # # #             "Insertion Sort": "Time Complexity: O(n^2)\nSpace Complexity: O(1)",
# # # # # # # #             "Activity Selection": "Greedy algorithm to select maximum non-overlapping activities.",
# # # # # # # #             "Fractional Knapsack": "Greedy algorithm to maximize value in a knapsack.",
# # # # # # # #             "Huffman Coding": "Greedy algorithm for data compression.",
# # # # # # # #             "Kruskal Algorithm": "Greedy algorithm for Minimum Spanning Tree.",
# # # # # # # #             "Prims Algorithm": "Greedy algorithm for Minimum Spanning Tree.",
# # # # # # # #             "Knapsack 0/1": "Dynamic Programming algorithm for 0/1 Knapsack problem.",
# # # # # # # #             "Floyd-Warshall": "Dynamic Programming algorithm for all-pairs shortest paths.",
# # # # # # # #             "Binary Search": "Divide and Conquer algorithm for searching in sorted arrays.",
# # # # # # # #             "Closest Pair Of Points": "Divide and Conquer algorithm for closest pair of points.",
# # # # # # # #             "Breadth First Search": "Graph traversal algorithm using a queue.",
# # # # # # # #             "Depth First Search": "Graph traversal algorithm using recursion or a stack.",
# # # # # # # #             "Dijkstra's Algorithm": "Graph algorithm for shortest paths from a source vertex."
# # # # # # # #         }

# # # # # # # #         detail_text = details.get(algorithm, "Details not available for this algorithm.")
# # # # # # # #         self.code_panel.update(f"[bold cyan]{algorithm}[/bold cyan]\n{detail_text}")


# # # # # # # # if __name__ == "__main__":
# # # # # # # #     AlgorithmApp().run()


# # # # # # # from textual.app import App, ComposeResult
# # # # # # # from textual.containers import Horizontal, Vertical
# # # # # # # from textual.widgets import Header, Footer, Tree, Static
# # # # # # # from textual.message import Message


# # # # # # # class AlgorithmApp(App):
# # # # # # #     """A TUI for selecting and exploring algorithms."""

# # # # # # #     CSS = """
# # # # # # #         #left-pane {
# # # # # # #             background: #3b4252;
# # # # # # #             color: white;
# # # # # # #             padding: 1 1; /* Simplified padding */
# # # # # # #         }

# # # # # # #         #center-pane {
# # # # # # #             background: #2e3440;
# # # # # # #             color: #eceff4;
# # # # # # #             padding: 1 1; /* Simplified padding */
# # # # # # #         }

# # # # # # #         #right-pane {
# # # # # # #             background: #4c566a;
# # # # # # #             color: white;
# # # # # # #             padding: 1 1; /* Simplified padding */
# # # # # # #         }

# # # # # # #         .panel-title {
# # # # # # #             color: #81a1c1; /* Removed unsupported font-weight */
# # # # # # #         }
# # # # # # #         """

# # # # # # #     class TreeSelected(Message):
# # # # # # #         """Message sent when a tree node is selected."""
# # # # # # #         def __init__(self, label: str) -> None:
# # # # # # #             self.label = label
# # # # # # #             super().__init__()

# # # # # # #     def compose(self) -> ComposeResult:
# # # # # # #         """Compose the layout of the TUI."""
# # # # # # #         yield Header(show_clock=True)

# # # # # # #         self.code_panel = Static(markup=True, name="code-panel")  # Removed 'highlight'

# # # # # # #         yield Horizontal(
# # # # # # #             Vertical(
# # # # # # #                 Static("\U0001F4C2 Algorithm Categories", classes="panel-title"),
# # # # # # #                 self.make_tree(),
# # # # # # #                 id="left-pane",
# # # # # # #             ),
# # # # # # #             Vertical(
# # # # # # #                 Static("Algorithm Details", classes="panel-title"),
# # # # # # #                 self.code_panel,
# # # # # # #                 id="center-pane",
# # # # # # #             ),
# # # # # # #             Vertical(
# # # # # # #                 Static("Output", classes="panel-title"),
# # # # # # #                 Static("This is the output panel.", classes="graph-box"),
# # # # # # #                 id="right-pane",
# # # # # # #             ),
# # # # # # #         )

# # # # # # #         yield Footer()

# # # # # # #     def make_tree(self):
# # # # # # #         """Create the tree panel with algorithm categories."""
# # # # # # #         tree = Tree("Algorithm Categories", id="alg-tree")
# # # # # # #         sorting = tree.root.add("Sorting Algorithms")
# # # # # # #         for algo in ["Quick Sort", "Merge Sort", "Bubble Sort", "Selection Sort", "Radix Sort", "Insertion Sort"]:
# # # # # # #             sorting.add_leaf(algo)

# # # # # # #         greedy = tree.root.add("Greedy Algorithms")
# # # # # # #         for algo in ["Activity Selection", "Fractional Knapsack", "Huffman Coding", "Kruskal Algorithm", "Prims Algorithm"]:
# # # # # # #             greedy.add_leaf(algo)

# # # # # # #         dp = tree.root.add("Dynamic Programming")
# # # # # # #         for algo in ["Knapsack 0/1", "Floyd-Warshall"]:
# # # # # # #             dp.add_leaf(algo)

# # # # # # #         divide = tree.root.add("Divide and Conquer")
# # # # # # #         for algo in ["Binary Search", "Closest Pair Of Points"]:
# # # # # # #             divide.add_leaf(algo)

# # # # # # #         graph = tree.root.add("Graph Algorithms")
# # # # # # #         for algo in ["Breadth First Search", "Depth First Search", "Dijkstra's Algorithm"]:
# # # # # # #             graph.add_leaf(algo)

# # # # # # #         tree.root.expand()
# # # # # # #         return tree

# # # # # # #     async def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
# # # # # # #         """Handle tree node selection."""
# # # # # # #         label = event.node.label
# # # # # # #         if isinstance(label, str):
# # # # # # #             self.code_panel.update(f"[bold yellow]Selected Algorithm:[/bold yellow] {label}")
# # # # # # #             self.display_algorithm_details(label)

# # # # # # #     def display_algorithm_details(self, algorithm: str):
# # # # # # #         """Display details of the selected algorithm."""
# # # # # # #         details = {
# # # # # # #             "Quick Sort": "Time Complexity: O(n log n)\nSpace Complexity: O(log n)",
# # # # # # #             "Merge Sort": "Time Complexity: O(n log n)\nSpace Complexity: O(n)",
# # # # # # #             "Bubble Sort": "Time Complexity: O(n^2)\nSpace Complexity: O(1)",
# # # # # # #             "Selection Sort": "Time Complexity: O(n^2)\nSpace Complexity: O(1)",
# # # # # # #             "Radix Sort": "Time Complexity: O(nk)\nSpace Complexity: O(n+k)",
# # # # # # #             "Insertion Sort": "Time Complexity: O(n^2)\nSpace Complexity: O(1)",
# # # # # # #             "Activity Selection": "Greedy algorithm to select maximum non-overlapping activities.",
# # # # # # #             "Fractional Knapsack": "Greedy algorithm to maximize value in a knapsack.",
# # # # # # #             "Huffman Coding": "Greedy algorithm for data compression.",
# # # # # # #             "Kruskal Algorithm": "Greedy algorithm for Minimum Spanning Tree.",
# # # # # # #             "Prims Algorithm": "Greedy algorithm for Minimum Spanning Tree.",
# # # # # # #             "Knapsack 0/1": "Dynamic Programming algorithm for 0/1 Knapsack problem.",
# # # # # # #             "Floyd-Warshall": "Dynamic Programming algorithm for all-pairs shortest paths.",
# # # # # # #             "Binary Search": "Divide and Conquer algorithm for searching in sorted arrays.",
# # # # # # #             "Closest Pair Of Points": "Divide and Conquer algorithm for closest pair of points.",
# # # # # # #             "Breadth First Search": "Graph traversal algorithm using a queue.",
# # # # # # #             "Depth First Search": "Graph traversal algorithm using recursion or a stack.",
# # # # # # #             "Dijkstra's Algorithm": "Graph algorithm for shortest paths from a source vertex."
# # # # # # #         }

# # # # # # #         detail_text = details.get(algorithm, "Details not available for this algorithm.")
# # # # # # #         self.code_panel.update(f"[bold cyan]{algorithm}[/bold cyan]\n{detail_text}")


# # # # # # # if __name__ == "__main__":
# # # # # # #     AlgorithmApp().run()



# # # # # # from textual.app import App, ComposeResult
# # # # # # from textual.widgets import Static, Header, Footer
# # # # # # from textual.containers import Container, Horizontal
# # # # # # from textual.reactive import reactive
# # # # # # import psutil
# # # # # # import asyncio


# # # # # # class CPUMonitor(Static):
# # # # # #     cpu_percent = reactive(0)

# # # # # #     def on_mount(self):
# # # # # #         self.set_interval(1, self.update_cpu)

# # # # # #     def update_cpu(self):
# # # # # #         self.cpu_percent = psutil.cpu_percent()

# # # # # #     def render(self):
# # # # # #         bars = "█" * int(self.cpu_percent // 5)
# # # # # #         return f"[bold green]CPU:[/bold green] {self.cpu_percent:.1f}% {bars}"


# # # # # # class MemMonitor(Static):
# # # # # #     def on_mount(self):
# # # # # #         self.set_interval(1, self.refresh)

# # # # # #     def render(self):
# # # # # #         mem = psutil.virtual_memory()
# # # # # #         return (
# # # # # #             f"[bold cyan]Memory[/bold cyan]\n"
# # # # # #             f"Total: {mem.total / 1e9:.2f} GB\n"
# # # # # #             f"Used: {mem.used / 1e9:.2f} GB ({mem.percent}%)\n"
# # # # # #             f"Free: {mem.available / 1e9:.2f} GB"
# # # # # #         )


# # # # # # class DiskMonitor(Static):
# # # # # #     def on_mount(self):
# # # # # #         self.set_interval(1, self.refresh)

# # # # # #     def render(self):
# # # # # #         disk = psutil.disk_usage('/')
# # # # # #         return (
# # # # # #             f"[bold magenta]Disk[/bold magenta]\n"
# # # # # #             f"Total: {disk.total / 1e9:.2f} GB\n"
# # # # # #             f"Used: {disk.used / 1e9:.2f} GB ({disk.percent}%)\n"
# # # # # #             f"Free: {disk.free / 1e9:.2f} GB"
# # # # # #         )


# # # # # # class NetMonitor(Static):
# # # # # #     last_bytes = psutil.net_io_counters()

# # # # # #     def on_mount(self):
# # # # # #         self.set_interval(1, self.refresh)

# # # # # #     def render(self):
# # # # # #         current = psutil.net_io_counters()
# # # # # #         upload = (current.bytes_sent - self.last_bytes.bytes_sent) / 1024
# # # # # #         download = (current.bytes_recv - self.last_bytes.bytes_recv) / 1024
# # # # # #         self.last_bytes = current

# # # # # #         return (
# # # # # #             f"[bold yellow]Network[/bold yellow]\n"
# # # # # #             f"⬆ Upload: {upload:.1f} KiB/s\n"
# # # # # #             f"⬇ Download: {download:.1f} KiB/s"
# # # # # #         )


# # # # # # class SysMonApp(App):
# # # # # #     CSS_PATH = None
# # # # # #     BINDINGS = [("q", "quit", "Quit")]

# # # # # #     def compose(self) -> ComposeResult:
# # # # # #         yield Header()
# # # # # #         with Container():
# # # # # #             with Horizontal():
# # # # # #                 yield CPUMonitor()
# # # # # #                 yield MemMonitor()
# # # # # #                 yield DiskMonitor()
# # # # # #                 yield NetMonitor()
# # # # # #         yield Footer()


# # # # # # if __name__ == "__main__":
# # # # # #     SysMonApp().run()
# # # # # from textual.app import App, ComposeResult
# # # # # from textual.containers import Grid
# # # # # from textual.widgets import Static, Header, Footer
# # # # # from rich.panel import Panel
# # # # # from rich.text import Text


# # # # # class ColorPanel(Static):
# # # # #     def __init__(self, title: str, color: str, content: str):
# # # # #         super().__init__()
# # # # #         self.title = title
# # # # #         self.color = color
# # # # #         self.content = content

# # # # #     def render(self):
# # # # #         return Panel(Text(self.content, style=self.color), title=self.title, border_style=self.color)


# # # # # class SystemGridApp(App):
# # # # #     CSS = """
# # # # #     Screen {
# # # # #         layout: vertical;
# # # # #         padding: 1;
# # # # #     }

# # # # #     Grid {
# # # # #         grid-size: 3;
# # # # #         grid-gutter: 1 1;
# # # # #         height: 1fr;
# # # # #     }

# # # # #     ColorPanel {
# # # # #         border: solid;
# # # # #         padding: 1;
# # # # #     }
# # # # #     """

# # # # #     def compose(self) -> ComposeResult:
# # # # #         yield Header()
# # # # #         with Grid():
# # # # #             yield ColorPanel("CPU", "green", "Core 0: 12%\nCore 1: 7%\nCore 2: 23%")
# # # # #             yield ColorPanel("Memory", "cyan", "Used: 4.6 GiB\nFree: 3.8 GiB")
# # # # #             yield ColorPanel("Disk", "magenta", "Root: 48%\nSwap: 12.5 GiB")
# # # # #             yield ColorPanel("Network", "yellow", "⬆ 2.0 KiB/s\n⬇ 2.0 KiB/s")
# # # # #             yield ColorPanel("Processes", "blue", "tmux\nfish\nfirefox\nsystemd")
# # # # #             yield ColorPanel("Temp", "red", "C0: 44°C\nC1: 45°C\nC2: 46°C")
# # # # #         yield Footer()


# # # # # if __name__ == "__main__":
# # # # #     SystemGridApp().run()


# # # # from textual.app import App, ComposeResult
# # # # from textual.containers import Horizontal, Vertical
# # # # from textual.widgets import Header, Footer, Button, Static
# # # # from textual.message import Message
# # # # from rich.table import Table
# # # # from rich.console import Console
# # # # from rich.text import Text


# # # # class AlgorithmApp(App):
# # # #     """A TUI for selecting and exploring algorithms using buttons instead of a tree."""

# # # #     CSS = """
# # # #         #left-pane {
# # # #             background: black;
# # # #             color: #88c0d0;
# # # #             border: #5e81ac round;
# # # #             padding: 1 1;
# # # #         }

# # # #         #center-pane {
# # # #             background: black;
# # # #             color: #d8dee9;
# # # #             border: #a3be8c round;
# # # #             padding: 1 1;
# # # #         }

# # # #         #right-pane {
# # # #             background: black;
# # # #             color: #ebcb8b;
# # # #             border: #bf616a round;
# # # #             padding: 1 1;
# # # #         }

# # # #         .panel-title {
# # # #             color: #b48ead;
# # # #         }

# # # #         Button {
# # # #             background: #2e3440;
# # # #             color: #8fbcbb;
# # # #             border: solid #5e81ac;
# # # #             padding: 1 2;
# # # #             margin: 1;
# # # #         }

# # # #         Button:hover {
# # # #             background: #4c566a;
# # # #         }
# # # #     """

# # # #     algorithms = {
# # # #         "Sorting Algorithms": [
# # # #             "Quick Sort", "Merge Sort", "Bubble Sort",
# # # #             "Selection Sort", "Radix Sort", "Insertion Sort"
# # # #         ],
# # # #         "Greedy Algorithms": [
# # # #             "Activity Selection", "Fractional Knapsack", "Huffman Coding",
# # # #             "Kruskal Algorithm", "Prims Algorithm"
# # # #         ],
# # # #         "Dynamic Programming": ["Knapsack 0/1", "Floyd-Warshall"],
# # # #         "Divide and Conquer": ["Binary Search", "Closest Pair Of Points"],
# # # #         "Graph Algorithms": ["Breadth First Search", "Depth First Search", "Dijkstra's Algorithm"]
# # # #     }

# # # #     def compose(self) -> ComposeResult:
# # # #         yield Header(show_clock=True)
# # # #         self.code_panel = Static(markup=True, name="code-panel")

# # # #         yield Horizontal(
# # # #             Vertical(
# # # #                 Static("\U0001F4C2 Algorithm Categories", classes="panel-title"),
# # # #                 *[Button(alg, id=alg.replace(" ", "_")) for cat in self.algorithms.values() for alg in cat],
# # # #                 id="left-pane",
# # # #             ),
# # # #             Vertical(
# # # #                 Static("Algorithm Details", classes="panel-title"),
# # # #                 self.code_panel,
# # # #                 id="center-pane",
# # # #             ),
# # # #             Vertical(
# # # #                 Static("Output", classes="panel-title"),
# # # #                 Static("This is the output panel.", classes="graph-box"),
# # # #                 id="right-pane",
# # # #             )
# # # #         )

# # # #         yield Footer()

# # # #     def on_button_pressed(self, event: Button.Pressed) -> None:
# # # #         self.display_algorithm_details(event.button.id)

# # # #     def display_algorithm_details(self, algorithm: str):
# # # #         details = {
# # # #             "Quick Sort": ("O(n log n)", "O(log n)"),
# # # #             "Merge Sort": ("O(n log n)", "O(n)"),
# # # #             "Bubble Sort": ("O(n^2)", "O(1)"),
# # # #             "Selection Sort": ("O(n^2)", "O(1)"),
# # # #             "Radix Sort": ("O(nk)", "O(n+k)"),
# # # #             "Insertion Sort": ("O(n^2)", "O(1)"),
# # # #             "Activity Selection": ("Greedy algorithm to select maximum non-overlapping activities.",),
# # # #             "Fractional Knapsack": ("Greedy algorithm to maximize value in a knapsack.",),
# # # #             "Huffman Coding": ("Greedy algorithm for data compression.",),
# # # #             "Kruskal Algorithm": ("Greedy algorithm for Minimum Spanning Tree.",),
# # # #             "Prims Algorithm": ("Greedy algorithm for Minimum Spanning Tree.",),
# # # #             "Knapsack 0/1": ("Dynamic Programming algorithm for 0/1 Knapsack problem.",),
# # # #             "Floyd-Warshall": ("Dynamic Programming algorithm for all-pairs shortest paths.",),
# # # #             "Binary Search": ("Divide and Conquer algorithm for searching in sorted arrays.",),
# # # #             "Closest Pair Of Points": ("Divide and Conquer algorithm for closest pair of points.",),
# # # #             "Breadth First Search": ("Graph traversal algorithm using a queue.",),
# # # #             "Depth First Search": ("Graph traversal algorithm using recursion or a stack.",),
# # # #             "Dijkstra's Algorithm": ("Graph algorithm for shortest paths from a source vertex.",)
# # # #         }

# # # #         if algorithm in details:
# # # #             detail = details[algorithm]
# # # #             table = Table(title=f"[bold cyan]{algorithm} Details[/bold cyan]")
# # # #             table.add_column("Property", style="bold magenta")
# # # #             table.add_column("Value", style="bold green")
# # # #             if len(detail) == 2:
# # # #                 table.add_row("Time Complexity", detail[0])
# # # #                 table.add_row("Space Complexity", detail[1])
# # # #             else:
# # # #                 table.add_row("Description", detail[0])

# # # #             console = Console()
# # # #             console_text = Text()
# # # #             console_text.append("\n")
# # # #             console_text.append(table)
# # # #             self.code_panel.update(console_text)
# # # #         else:
# # # #             self.code_panel.update(f"[bold red]Details not available for {algorithm}.[/bold red]")


# # # # if __name__ == "__main__":
# # # #     AlgorithmApp().run()




# # # from textual.app import App, ComposeResult
# # # from textual.containers import Horizontal, Vertical
# # # from textual.widgets import Header, Footer, Button, Static
# # # from textual.message import Message
# # # from rich.table import Table
# # # from rich.console import Console
# # # from rich.text import Text
# # # import sys


# # # class AlgorithmApp(App):
# # #     """A TUI for selecting and exploring algorithms using buttons instead of a tree."""

# # #     CSS = """
# # #         #left-pane {
# # #             background: black;
# # #             color: #88c0d0;
# # #             border: #5e81ac round;
# # #             padding: 1 1;
# # #         }

# # #         #center-pane {
# # #             background: black;
# # #             color: #d8dee9;
# # #             border: #a3be8c round;
# # #             padding: 1 1;
# # #         }

# # #         #right-pane {
# # #             background: black;
# # #             color: #ebcb8b;
# # #             border: #bf616a round;
# # #             padding: 1 1;
# # #         }

# # #         .panel-title {
# # #             color: #b48ead;
# # #         }

# # #         Button {
# # #             color: #88c0d0;
# # #             padding: 0 1;
# # #             margin: 1;
# # #             height: auto;
# # #             content-align: center middle;
# # #         }

# # #         Button:hover {
# # #             background: blue;
# # #         }
# # #     """

# # #     algorithms = {
# # #         "Sorting Algorithms": [
# # #             "Quick Sort", "Merge Sort", "Bubble Sort",
# # #             "Selection Sort", "Radix Sort", "Insertion Sort"
# # #         ],
# # #         "Greedy Algorithms": [
# # #             "Activity Selection", "Fractional Knapsack", "Huffman Coding",
# # #             "Kruskal Algorithm", "Prims Algorithm"
# # #         ],
# # #         "Dynamic Programming": ["Knapsack 0_1", "Floyd_Warshall"],
# # #         "Divide and Conquer": ["Binary Search", "Closest Pair Of Points"],
# # #         "Graph Algorithms": ["Breadth First Search", "Depth First Search", "Dijkstra"],
# # #     }

# # #     def compose(self) -> ComposeResult:
# # #         yield Header(show_clock=True)
# # #         self.code_panel = Static(markup=True, name="code-panel")

# # #         def sanitize_id(name):
# # #             return name.replace(" ", "_").replace("'", "").replace("/", "_")

# # #         self.button_map = {}
# # #         yield Horizontal(
# # #             Vertical(
# # #                 Static("\U0001F4C2 Algorithm Categories", classes="panel-title"),
# # #                 *[Button(alg, id=sanitize_id(alg)) for cat in self.algorithms.values() for alg in cat],
# # #                 id="left-pane",
# # #             ),
# # #             Vertical(
# # #                 Static("Algorithm Details", classes="panel-title"),
# # #                 self.code_panel,
# # #                 id="center-pane",
# # #             ),
# # #             Vertical(
# # #                 Static("Output", classes="panel-title"),
# # #                 Static("This is the output panel.", classes="graph-box"),
# # #                 id="right-pane",
# # #             )
# # #         )

# # #         yield Footer()

# # #     def on_button_pressed(self, event: Button.Pressed) -> None:
# # #         self.display_algorithm_details(event.button.label)

# # #     def display_algorithm_details(self, algorithm: str):
# # #         details = {
# # #             "Quick Sort": ("O(n log n)", "O(log n)"),
# # #             "Merge Sort": ("O(n log n)", "O(n)"),
# # #             "Bubble Sort": ("O(n^2)", "O(1)"),
# # #             "Selection Sort": ("O(n^2)", "O(1)"),
# # #             "Radix Sort": ("O(nk)", "O(n+k)"),
# # #             "Insertion Sort": ("O(n^2)", "O(1)"),
# # #             "Activity Selection": ("Greedy algorithm to select maximum non-overlapping activities.",),
# # #             "Fractional Knapsack": ("Greedy algorithm to maximize value in a knapsack.",),
# # #             "Huffman Coding": ("Greedy algorithm for data compression.",),
# # #             "Kruskal Algorithm": ("Greedy algorithm for Minimum Spanning Tree.",),
# # #             "Prims Algorithm": ("Greedy algorithm for Minimum Spanning Tree.",),
# # #             "Knapsack 0_1": ("Dynamic Programming algorithm for 0/1 Knapsack problem.",),
# # #             "Floyd_Warshall": ("Dynamic Programming algorithm for all-pairs shortest paths.",),
# # #             "Binary Search": ("Divide and Conquer algorithm for searching in sorted arrays.",),
# # #             "Closest Pair Of Points": ("Divide and Conquer algorithm for closest pair of points.",),
# # #             "Breadth First Search": ("Graph traversal algorithm using a queue.",),
# # #             "Depth First Search": ("Graph traversal algorithm using recursion or a stack.",),
# # #             "Dijkstra": ("Graph algorithm for shortest paths from a source vertex.",),
# # #         }

# # #         if algorithm in details:
# # #             detail = details[algorithm]
# # #             table = Table(title=f"[bold cyan]{algorithm} Details[/bold cyan]")
# # #             table.add_column("Property", style="bold magenta")
# # #             table.add_column("Value", style="bold green")
# # #             if len(detail) == 2:
# # #                 table.add_row("Time Complexity", detail[0])
# # #                 table.add_row("Space Complexity", detail[1])
# # #             else:
# # #                 table.add_row("Description", detail[0])

# # #             console = Console()
# # #             console_text = Text()
# # #             console_text.append("\n")
# # #             console_text.append(table)
# # #             self.code_panel.update(console_text)
# # #         else:
# # #             self.code_panel.update(f"[bold red]Details not available for {algorithm}.[/bold red]")


# # # if __name__ == "__main__":
# # #     if sys.platform.startswith("linux"):
# # #         AlgorithmApp().run()
# # #     else:
# # #         print("This TUI app only runs in a Unix-like terminal environment (Linux/macOS).")


# # from textual.app import App, ComposeResult
# # from textual.containers import Horizontal, Vertical
# # from textual.widgets import Header, Footer, Button, Static
# # from textual.message import Message
# # from rich.table import Table
# # from rich.console import Console
# # from rich.text import Text
# # import sys


# # class AlgorithmApp(App):
# #     """A TUI for selecting and exploring algorithms with categorized clickable text."""

# #     CSS = """
# #         #left-pane {
# #             background: black;
# #             color: #88c0d0;
# #             border: round #5e81ac;
# #             padding: 1 1;
# #         }

# #         #center-pane {
# #             background: black;
# #             color: #d8dee9;
# #             border: round #a3be8c;
# #             padding: 1 1;
# #         }

# #         #right-pane {
# #             background: black;
# #             color: #ebcb8b;
# #             border: round #bf616a;
# #             padding: 1 1;
# #         }

# #         .panel-title {
# #             color: #b48ead;
# #         }

# #         Button {
# #             background: transparent;
# #             color: #88c0d0;
# #             padding: 0 1;
# #             margin: 1 0;
# #             height: auto;
# #             content-align: left middle;
# #             width: 100%;
# #         }

# #         Button:hover {
# #             background: #5e81ac20;
# #             border: solid #81a1c1;
# #             color: #eceff4;
# #         }
# #     """

# #     algorithms = {
# #         "Sorting Algorithms": [
# #             "Quick Sort", "Merge Sort", "Bubble Sort",
# #             "Selection Sort", "Radix Sort", "Insertion Sort"
# #         ],
# #         "Greedy Algorithms": [
# #             "Activity Selection", "Fractional Knapsack", "Huffman Coding",
# #             "Kruskal Algorithm", "Prims Algorithm"
# #         ],
# #         "Dynamic Programming": ["Knapsack 0_1", "Floyd_Warshall"],
# #         "Divide and Conquer": ["Binary Search", "Closest Pair Of Points"],
# #         "Graph Algorithms": ["Breadth First Search", "Depth First Search", "Dijkstra"],
# #     }

# #     def compose(self) -> ComposeResult:
# #         yield Header(show_clock=True)
# #         self.code_panel = Static(markup=True, name="code-panel")

# #         def sanitize_id(name):
# #             return name.replace(" ", "_").replace("'", "").replace("/", "_")

# #         self.button_map = {}

# #         category_buttons = []
# #         for category, algos in self.algorithms.items():
# #             category_buttons.append(Static(f"[b]{category}[/b]", classes="panel-title"))
# #             for alg in algos:
# #                 btn = Button(alg, id=sanitize_id(alg))
# #                 self.button_map[sanitize_id(alg)] = alg
# #                 category_buttons.append(btn)

# #         yield Horizontal(
# #             Vertical(
# #                 Static("\U0001F4C2 Algorithm Categories", classes="panel-title"),
# #                 *category_buttons,
# #                 id="left-pane",
# #             ),
# #             Vertical(
# #                 Static("Algorithm Details", classes="panel-title"),
# #                 self.code_panel,
# #                 id="center-pane",
# #             ),
# #             Vertical(
# #                 Static("Output", classes="panel-title"),
# #                 Static("This is the output panel.", classes="graph-box"),
# #                 id="right-pane",
# #             )
# #         )

# #         yield Footer()

# #     def on_button_pressed(self, event: Button.Pressed) -> None:
# #         self.display_algorithm_details(event.button.label)

# #     def display_algorithm_details(self, algorithm: str):
# #         details = {
# #             "Quick Sort": ("O(n log n)", "O(log n)"),
# #             "Merge Sort": ("O(n log n)", "O(n)"),
# #             "Bubble Sort": ("O(n^2)", "O(1)"),
# #             "Selection Sort": ("O(n^2)", "O(1)"),
# #             "Radix Sort": ("O(nk)", "O(n+k)"),
# #             "Insertion Sort": ("O(n^2)", "O(1)"),
# #             "Activity Selection": ("Greedy algorithm to select maximum non-overlapping activities.",),
# #             "Fractional Knapsack": ("Greedy algorithm to maximize value in a knapsack.",),
# #             "Huffman Coding": ("Greedy algorithm for data compression.",),
# #             "Kruskal Algorithm": ("Greedy algorithm for Minimum Spanning Tree.",),
# #             "Prims Algorithm": ("Greedy algorithm for Minimum Spanning Tree.",),
# #             "Knapsack 0_1": ("Dynamic Programming algorithm for 0/1 Knapsack problem.",),
# #             "Floyd_Warshall": ("Dynamic Programming algorithm for all-pairs shortest paths.",),
# #             "Binary Search": ("Divide and Conquer algorithm for searching in sorted arrays.",),
# #             "Closest Pair Of Points": ("Divide and Conquer algorithm for closest pair of points.",),
# #             "Breadth First Search": ("Graph traversal algorithm using a queue.",),
# #             "Depth First Search": ("Graph traversal algorithm using recursion or a stack.",),
# #             "Dijkstra": ("Graph algorithm for shortest paths from a source vertex.",),
# #         }

# #         if algorithm in details:
# #             detail = details[algorithm]
# #             table = Table(title=f"[bold cyan]{algorithm} Details[/bold cyan]")
# #             table.add_column("Property", style="bold magenta")
# #             table.add_column("Value", style="bold green")
# #             if len(detail) == 2:
# #                 table.add_row("Time Complexity", detail[0])
# #                 table.add_row("Space Complexity", detail[1])
# #             else:
# #                 table.add_row("Description", detail[0])

# #             console = Console()
# #             console_text = Text()
# #             console_text.append("\n")
# #             console_text.append(table)
# #             self.code_panel.update(console_text)
# #         else:
# #             self.code_panel.update(f"[bold red]Details not available for {algorithm}.[/bold red]")


# # if __name__ == "__main__":
# #     if sys.platform.startswith("linux"):
# #         AlgorithmApp().run()
# #     else:
# #         print("This TUI app only runs in a Unix-like terminal environment (Linux/macOS).")


# from textual.app import App, ComposeResult
# from textual.containers import Horizontal, Vertical
# from textual.widgets import Header, Footer, Static, TreeControl, TreeNode
# from textual.widgets.tree import TreeDataType
# from textual.reactive import reactive
# from textual.message import Message
# from rich.console import Console
# from rich.text import Text
# from rich.table import Table
# import sys

# class AlgorithmApp(App):
#     """A TUI for selecting and exploring algorithms using TreeControl."""

#     CSS = """
#         #left-pane {
#             background: black;
#             color: #88c0d0;
#             border: round #5e81ac;
#             padding: 1;
#         }

#         #center-pane {
#             background: black;
#             color: #d8dee9;
#             border: round #a3be8c;
#             padding: 1;
#         }

#         #right-pane {
#             background: black;
#             color: #ebcb8b;
#             border: round #bf616a;
#             padding: 1;
#         }

#         .panel-title {
#             color: #b48ead;
#         }

#         TreeControl {
#             background: transparent;
#             color: #88c0d0;
#         }

#         TreeControl:focus {
#             border: round #81a1c1;
#         }
#     """

#     algorithms = {
#         "Sorting Algorithms": [
#             "Quick Sort", "Merge Sort", "Bubble Sort",
#             "Selection Sort", "Radix Sort", "Insertion Sort"
#         ],
#         "Greedy Algorithms": [
#             "Activity Selection", "Fractional Knapsack", "Huffman Coding",
#             "Kruskal Algorithm", "Prims Algorithm"
#         ],
#         "Dynamic Programming": ["Knapsack 0_1", "Floyd_Warshall"],
#         "Divide and Conquer": ["Binary Search", "Closest Pair Of Points"],
#         "Graph Algorithms": ["Breadth First Search", "Depth First Search", "Dijkstra"],
#     }

#     selected_algorithm: reactive[str | None] = reactive(None)

#     def compose(self) -> ComposeResult:
#         yield Header(show_clock=True)
#         self.code_panel = Static(markup=True, name="code-panel")

#         self.tree = TreeControl("Algorithm Categories", None)
#         for category, algos in self.algorithms.items():
#             parent = self.tree.root.add(category, category)
#             for algo in algos:
#                 parent.add_leaf(algo, algo)
#         self.tree.root.expand()

#         yield Horizontal(
#             Vertical(
#                 Static("\U0001F4C2 Algorithm Categories", classes="panel-title"),
#                 self.tree,
#                 id="left-pane",
#             ),
#             Vertical(
#                 Static("Algorithm Details", classes="panel-title"),
#                 self.code_panel,
#                 id="center-pane",
#             ),
#             Vertical(
#                 Static("Output", classes="panel-title"),
#                 Static("This is the output panel.", classes="graph-box"),
#                 id="right-pane",
#             )
#         )

#         yield Footer()

#     def on_mount(self):
#         self.set_focus(self.tree)

#     async def on_tree_node_selected(self, message: TreeControl.NodeSelected[TreeDataType]) -> None:
#         node_data = message.node.data
#         if node_data and isinstance(node_data, str):
#             self.selected_algorithm = node_data
#             self.display_algorithm_details(node_data)

#     def display_algorithm_details(self, algorithm: str):
#         details = {
#             "Quick Sort": ("O(n log n)", "O(log n)"),
#             "Merge Sort": ("O(n log n)", "O(n)"),
#             "Bubble Sort": ("O(n^2)", "O(1)"),
#             "Selection Sort": ("O(n^2)", "O(1)"),
#             "Radix Sort": ("O(nk)", "O(n+k)"),
#             "Insertion Sort": ("O(n^2)", "O(1)"),
#             "Activity Selection": ("Greedy algorithm to select maximum non-overlapping activities.",),
#             "Fractional Knapsack": ("Greedy algorithm to maximize value in a knapsack.",),
#             "Huffman Coding": ("Greedy algorithm for data compression.",),
#             "Kruskal Algorithm": ("Greedy algorithm for Minimum Spanning Tree.",),
#             "Prims Algorithm": ("Greedy algorithm for Minimum Spanning Tree.",),
#             "Knapsack 0_1": ("Dynamic Programming algorithm for 0/1 Knapsack problem.",),
#             "Floyd_Warshall": ("Dynamic Programming algorithm for all-pairs shortest paths.",),
#             "Binary Search": ("Divide and Conquer algorithm for searching in sorted arrays.",),
#             "Closest Pair Of Points": ("Divide and Conquer algorithm for closest pair of points.",),
#             "Breadth First Search": ("Graph traversal algorithm using a queue.",),
#             "Depth First Search": ("Graph traversal algorithm using recursion or a stack.",),
#             "Dijkstra": ("Graph algorithm for shortest paths from a source vertex.",),
#         }

#         if algorithm in details:
#             detail = details[algorithm]
#             table = Table(title=f"[bold cyan]{algorithm} Details[/bold cyan]")
#             table.add_column("Property", style="bold magenta")
#             table.add_column("Value", style="bold green")
#             if len(detail) == 2:
#                 table.add_row("Time Complexity", detail[0])
#                 table.add_row("Space Complexity", detail[1])
#             else:
#                 table.add_row("Description", detail[0])

#             console = Console()
#             console_text = Text()
#             console_text.append("\n")
#             console_text.append(table)
#             self.code_panel.update(console_text)
#         else:
#             self.code_panel.update(f"[bold red]Details not available for {algorithm}.[/bold red]")


# if __name__ == "__main__":
#     if sys.platform.startswith("linux"):
#         AlgorithmApp().run()
#     else:
#         print("This TUI app only runs in a Unix-like terminal environment (Linux/macOS).")

# from textual.app import App, ComposeResult
# from textual.containers import Horizontal, Vertical
# from textual.widgets import Header, Footer, Tree, Static
# from textual.widgets.tree import TreeNode
# from textual.reactive import reactive
# from textual.message import Message
# import sys

# class AlgorithmApp(App):
#     """A TUI for selecting and exploring algorithms using Tree widget."""

#     CSS = """
#         #left-pane {
#             background: black;
#             color: #88c0d0;
#             border: round #5e81ac;
#             padding: 1;
#         }

#         #center-pane {
#             background: black;
#             color: #d8dee9;
#             border: round #a3be8c;
#             padding: 1;
#         }

#         #right-pane {
#             background: black;
#             color: #ebcb8b;
#             border: round #bf616a;
#             padding: 1;
#         }

#         .panel-title {
#             color: #b48ead;
#         }

#         Tree {
#             background: transparent;
#             color: #88c0d0;
#         }

#         Tree:focus {
#             border: round #81a1c1;
#         }

#         #code-panel {
#             height: 100%;
#             overflow: auto;
#             padding: 1;
#         }
#     """

#     algorithms = {
#         "Sorting Algorithms": [
#             "Quick Sort", "Merge Sort", "Bubble Sort",
#             "Selection Sort", "Radix Sort", "Insertion Sort"
#         ],
#         "Greedy Algorithms": [
#             "Activity Selection", "Fractional Knapsack", "Huffman Coding",
#             "Kruskal Algorithm", "Prims Algorithm"
#         ],
#         "Dynamic Programming": ["Knapsack 0_1", "Floyd_Warshall"],
#         "Divide and Conquer": ["Binary Search", "Closest Pair Of Points"],
#         "Graph Algorithms": ["Breadth First Search", "Depth First Search", "Dijkstra"],
#     }

#     selected_algorithm: reactive[str | None] = reactive(None)

#     def compose(self) -> ComposeResult:
#         yield Header(show_clock=True)
#         self.code_panel = Static("", id="code-panel", markup=True)

#         self.alg_tree = Tree("Algorithm Categories", id="alg-tree")
#         for category, algos in self.algorithms.items():
#             parent = self.alg_tree.root.add(category)
#             for algo in algos:
#                 parent.add_leaf(algo)
#         self.alg_tree.root.expand_all()

#         yield Horizontal(
#             Vertical(
#                 Static("\U0001F4C2 Algorithm Categories", classes="panel-title"),
#                 self.alg_tree,
#                 id="left-pane",
#             ),
#             Vertical(
#                 Static("Algorithm Details", classes="panel-title"),
#                 self.code_panel,
#                 id="center-pane",
#             ),
#             Vertical(
#                 Static("Output", classes="panel-title"),
#                 Static("This is the output panel.", classes="graph-box"),
#                 id="right-pane",
#             )
#         )

#         yield Footer()

#     def on_mount(self):
#         self.set_focus(self.alg_tree)

#     def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
#         node = event.node
#         algo_name = node.label.plain if node.is_leaf else None
#         if algo_name:
#             self.selected_algorithm = algo_name
#             self.display_algorithm_details(algo_name)

#     def display_algorithm_details(self, algorithm: str):
#         details = {
#             "Quick Sort": ("O(n log n)", "O(log n)"),
#             "Merge Sort": ("O(n log n)", "O(n)"),
#             "Bubble Sort": ("O(n^2)", "O(1)"),
#             "Selection Sort": ("O(n^2)", "O(1)"),
#             "Radix Sort": ("O(nk)", "O(n+k)"),
#             "Insertion Sort": ("O(n^2)", "O(1)"),
#             "Activity Selection": ("Greedy algorithm to select maximum non-overlapping activities.",),
#             "Fractional Knapsack": ("Greedy algorithm to maximize value in a knapsack.",),
#             "Huffman Coding": ("Greedy algorithm for data compression.",),
#             "Kruskal Algorithm": ("Greedy algorithm for Minimum Spanning Tree.",),
#             "Prims Algorithm": ("Greedy algorithm for Minimum Spanning Tree.",),
#             "Knapsack 0_1": ("Dynamic Programming algorithm for 0/1 Knapsack problem.",),
#             "Floyd_Warshall": ("Dynamic Programming algorithm for all-pairs shortest paths.",),
#             "Binary Search": ("Divide and Conquer algorithm for searching in sorted arrays.",),
#             "Closest Pair Of Points": ("Divide and Conquer algorithm for closest pair of points.",),
#             "Breadth First Search": ("Graph traversal algorithm using a queue.",),
#             "Depth First Search": ("Graph traversal algorithm using recursion or a stack.",),
#             "Dijkstra": ("Graph algorithm for shortest paths from a source vertex.",),
#         }

#         if algorithm in details:
#             detail = details[algorithm]
#             if len(detail) == 2:
#                 content = (
#                     f"[bold cyan]{algorithm}[/bold cyan]\n\n"
#                     f"[bold magenta]Time Complexity:[/bold magenta] [green]{detail[0]}[/green]\n"
#                     f"[bold magenta]Space Complexity:[/bold magenta] [green]{detail[1]}[/green]"
#                 )
#             else:
#                 content = f"[bold cyan]{algorithm}[/bold cyan]\n\n[green]{detail[0]}[/green]"
#             self.code_panel.update(content)
#         else:
#             self.code_panel.update(f"[bold red]Details not available for {algorithm}.[/bold red]")


# if __name__ == "__main__":
#     if sys.platform.startswith("linux"):
#         AlgorithmApp().run()
#     else:
#         print("This TUI app only runs in a Unix-like terminal environment (Linux/macOS).")


