import matplotlib.pyplot as plt
import networkx as nx
from PySide6.QtWidgets import QMessageBox, QMainWindow

class BSTVisualizer(QMainWindow):

    def show_tree_graph(self):
        if not self.bst or not self.bst.root:
            QMessageBox.warning(self, "Empty Tree", "The tree is empty. Please insert nodes first.")
            return

        graph = nx.DiGraph()

        def add_edges(node):
            if node.left:
                graph.add_edge(node.key, node.left.key)
                add_edges(node.left)
            if node.right:
                graph.add_edge(node.key, node.right.key)
                add_edges(node.right)

        add_edges(self.bst.root)

        try:
            pos = nx.nx_pydot.graphviz_layout(graph, prog="dot")
        except Exception:
            pos = nx.spring_layout(graph)

        plt.figure(figsize=(8, 6))
        nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold')
        plt.title("Binary Search Tree Visualization")
        plt.show()