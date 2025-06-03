import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidget, QSizePolicy, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor, QFont

# Simple Binary Tree Example - Educational Version
# Each line explained for learning purposes

class TreeNode:
    """This is a simple tree node class - represents one node in our tree"""

    def __init__(self, key):
        # __init__ is the constructor - runs when we create a new TreeNode
        # 'self' refers to the current instance of the TreeNode we're creating
        # 'key' is the value we want to store in this node
        self.key = key  # Store the value in this node
        self.left = None  # Initialize left child as empty (None)
        self.right = None  # Initialize right child as empty (None)


class BinarySearchTree:
    """Main class that manages the entire binary search tree"""

    def __init__(self, root=None):
        # Constructor for the BST - can optionally start with a root value
        # 'root=None' means if no value is provided, default to None
        if root is not None:  # Check if a starting value was provided
            self.root = TreeNode(root)  # Create the first node with that value
        else:
            self.root = None  # Otherwise, start with an empty tree

    def insert(self, key):
        """Insert a new key into the binary search tree."""
        # Public method that users call to add new values
        if self.root is None:  # Check if tree is completely empty
            self.root = TreeNode(key)  # If empty, make this the root node
        else:
            # Tree has nodes, so use helper method to find correct position
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        """Helper method to insert a new key recursively."""
        # Private method (underscore prefix) - only used internally
        # 'node' is current node we're examining, 'key' is value to insert

        if key < node.key:  # New value is smaller than current node
            if node.left is None:  # No left child exists
                node.left = TreeNode(key)  # Create new node as left child
            else:
                # Left child exists, so recurse down left side
                self._insert_rec(node.left, key)

        elif key > node.key:  # New value is larger than current node
            if node.right is None:  # No right child exists
                node.right = TreeNode(key)  # Create new node as right child
            else:
                # Right child exists, so recurse down right side
                self._insert_rec(node.right, key)
        # If key == node.key, we don't insert duplicates (implicit else case)

    def inorder_traversal(self):
        """Public method to start in-order traversal"""
        return self._inorder_traversal_rec(self.root)

    def _inorder_traversal_rec(self, node):
        """Private recursive helper for in-order traversal"""
        if node is None:
            return []

        result = []
        result.extend(self._inorder_traversal_rec(node.left))
        result.append(node.key)
        result.extend(self._inorder_traversal_rec(node.right))
        return result

    def search(self, key):
        """Search for a key in the tree"""
        # Public method - returns True if key exists, False otherwise
        return self._search_rec(self.root, key)  # Start search from root

    def _search_rec(self, node, key):
        """Helper method to search recursively"""
        # Private recursive method to actually perform the search

        if node is None:  # Reached empty spot - key not found
            return False

        if key == node.key:  # Found exact match
            return True

        elif key < node.key:  # Target is smaller than current node
            # Search left subtree (where smaller values are stored)
            return self._search_rec(node.left, key)
        else:  # key > node.key - target is larger
            # Search right subtree (where larger values are stored)
            return self._search_rec(node.right, key)



# --- TreeCanvas Widget for graphical rendering of the BST ---
class TreeCanvas(QWidget):
    """A QWidget that draws the binary search tree using QPainter."""
    def __init__(self, bst: BinarySearchTree, parent=None):
        super().__init__(parent)
        self.bst = bst
        # Allow the widget to expand
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.node_radius = 22  # Radius of the node ellipses
        self.level_height = 70  # Vertical distance between levels
        self.horiz_spacing = 30  # Minimum horizontal spacing between nodes
        self.highlight_path = []
        self.highlight_color = QColor(0, 200, 0)  # Default green

    def paintEvent(self, event):
        # Glow effect and highlight explanation:
        # Nodes part of search path glow with thick colored border (green if found, red if not)
        # Lines remain static for now, but can be animated with QTimer in future (e.g., traversing step-by-step)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        if self.bst.root is not None:
            # Compute layout
            positions = {}
            # First, compute subtree sizes for layout
            def compute_subtree_size(node):
                if node is None:
                    return 0
                left = compute_subtree_size(node.left)
                right = compute_subtree_size(node.right)
                return left + right + 1
            # Recursive function to assign positions
            def layout(node, depth, x_min, x_max):
                if node is None:
                    return
                # Compute horizontal position: center of allotted space
                x = (x_min + x_max) // 2
                y = self.level_height * depth + self.node_radius + 10
                positions[node] = (x, y)
                # Count left/right nodes for better spacing
                left_count = compute_subtree_size(node.left)
                right_count = compute_subtree_size(node.right)
                total = left_count + right_count
                # Split available horizontal space proportional to subtree sizes
                if node.left:
                    left_x_max = x - self.horiz_spacing // 2
                    left_x_min = x_min
                    if left_count > 0 and total > 0:
                        left_x_max = x - self.horiz_spacing // 2
                    layout(node.left, depth + 1, x_min, x - self.horiz_spacing)
                if node.right:
                    right_x_min = x + self.horiz_spacing // 2
                    right_x_max = x_max
                    if right_count > 0 and total > 0:
                        right_x_min = x + self.horiz_spacing // 2
                    layout(node.right, depth + 1, x + self.horiz_spacing, x_max)
            # Use widget width for layout
            width = self.width()
            layout(self.bst.root, 0, self.node_radius, width - self.node_radius)
            # Draw edges first
            pen = QPen(QColor(80, 80, 80), 2)
            painter.setPen(pen)
            def draw_edges(node):
                if node is None:
                    return
                x1, y1 = positions[node]
                if node.left:
                    x2, y2 = positions[node.left]
                    painter.drawLine(x1, y1, x2, y2)
                    draw_edges(node.left)
                if node.right:
                    x2, y2 = positions[node.right]
                    painter.drawLine(x1, y1, x2, y2)
                    draw_edges(node.right)
            draw_edges(self.bst.root)
            # Draw nodes
            for node, (x, y) in positions.items():
                if node.key in self.highlight_path:
                    painter.setBrush(QBrush(self.highlight_color.lighter(150)))
                else:
                    painter.setBrush(QBrush(QColor(200, 220, 255)))
                glow_color = self.highlight_color if node.key in self.highlight_path else QColor(150, 200, 255)
                glow_pen = QPen(glow_color, 10, Qt.PenStyle.SolidLine)
                painter.setPen(glow_pen)
                painter.drawEllipse(QRectF(x - self.node_radius - 5, y - self.node_radius - 5,
                                           (self.node_radius + 5) * 2, (self.node_radius + 5) * 2))
                painter.setPen(QPen(QColor(50, 80, 180), 2))
                painter.drawEllipse(QRectF(x - self.node_radius, y - self.node_radius,
                                           self.node_radius * 2, self.node_radius * 2))
                painter.setPen(QPen(Qt.GlobalColor.black))
                font = QFont("Arial", 11)
                painter.setFont(font)
                text = str(node.key)
                text_rect = painter.boundingRect(QRectF(x - self.node_radius, y - self.node_radius,
                                                        self.node_radius * 2, self.node_radius * 2),
                                                Qt.AlignmentFlag.AlignCenter, text)
                painter.drawText(text_rect, Qt.AlignmentFlag.AlignCenter, text)
        painter.end()

    def refresh(self):
        """Call this to trigger a repaint of the tree."""
        self.update()

    def highlight_search_path(self, path_keys, success=True):
        self.highlight_path = path_keys
        self.highlight_color = QColor(0, 200, 0) if success else QColor(200, 0, 0)
        self.update()


# PyQt6 Tree Visualizer for BST, now using TreeCanvas
class TreeVisualizer(QWidget):
    def __init__(self, bst: BinarySearchTree):
        super().__init__()
        self.bst = bst
        self.setWindowTitle("Binary Search Tree Visualizer")
        self.setGeometry(100, 100, 800, 500)
        layout = QVBoxLayout()

        # Tree graphical canvas at the top
        self.tree_canvas = TreeCanvas(bst)
        self.tree_canvas.setMinimumHeight(250)
        layout.addWidget(self.tree_canvas)

        # Traversal list at the bottom
        self.traversal_label = QLabel("In-Order Traversal (Sorted):")
        layout.addWidget(self.traversal_label)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        self.insert_input = QLineEdit()
        self.insert_input.setPlaceholderText("Enter value to insert")
        self.insert_button = QPushButton("Insert")
        self.insert_button.clicked.connect(self.insert_value)

        insert_layout = QHBoxLayout()
        insert_layout.addWidget(self.insert_input)
        insert_layout.addWidget(self.insert_button)
        layout.addLayout(insert_layout)

        # --- Search input and button ---
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Enter value to search")
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_value)

        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)
        layout.addLayout(search_layout)

        self.delete_input = QLineEdit()
        self.delete_input.setPlaceholderText("Enter value to delete")
        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete_value)

        delete_layout = QHBoxLayout()
        delete_layout.addWidget(self.delete_input)
        delete_layout.addWidget(self.delete_button)
        layout.addLayout(delete_layout)

        self.clear_button = QPushButton("Clear Tree")
        self.clear_button.clicked.connect(self.clear_tree)
        layout.addWidget(self.clear_button)

        self.setLayout(layout)
        self.refresh_display()

    def refresh_display(self):
        """Update both the list and graphical tree."""
        values = self.bst.inorder_traversal()
        self.list_widget.clear()
        for val in values:
            self.list_widget.addItem(str(val))
        self.tree_canvas.refresh()
        self.tree_canvas.highlight_path = []

    def insert_value(self):
        value_text = self.insert_input.text()
        if value_text.isdigit():
            value = int(value_text)
            self.bst.insert(value)
            self.insert_input.clear()
            self.refresh_display()
        else:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid integer.")

    def search_value(self):
        value_text = self.search_input.text()
        if value_text.isdigit():
            value = int(value_text)
            path = []
            found = self._search_with_path(self.bst.root, value, path)
            self.tree_canvas.highlight_search_path(path, success=found)
            if found:
                QMessageBox.information(self, "Search Result", f"Value {value} was found in the tree.")
            else:
                QMessageBox.information(self, "Search Result", f"Value {value} was NOT found in the tree.")
            explanation = f"Searching for {value}:\n\n"
            explanation += "The tree was traversed comparing values top-down.\n"
            explanation += "Green nodes indicate a successful path to the target.\n" if found else "Red nodes show the failed path.\n"
            explanation += f"Final decision: Value {'FOUND' if found else 'NOT FOUND'} in the BST."
            QMessageBox.information(self, "Search Explanation", explanation)
            self.search_input.clear()
            self.refresh_display()
        else:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid integer.")

    def _search_with_path(self, node, key, path):
        if node is None:
            return False
        path.append(node.key)
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_with_path(node.left, key, path)
        else:
            return self._search_with_path(node.right, key, path)

    def delete_value(self):
        value_text = self.delete_input.text()
        if value_text.isdigit():
            value = int(value_text)
            self.bst.root = self._delete_recursive(self.bst.root, value)
            self.delete_input.clear()
            self.refresh_display()
        else:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid integer.")

    def _delete_recursive(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._find_min(node.right)
            node.key = temp.key
            node.right = self._delete_recursive(node.right, temp.key)
        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def clear_tree(self):
        self.bst.root = None
        self.refresh_display()


# Example usage with PyQt6 visual analyzer:
if __name__ == "__main__":
    print("=== Creating Binary Search Tree ===")
    bst = BinarySearchTree(50)
    print(f"Created BST with root value: {bst.root.key}")

    print("\n=== Inserting Values ===")
    # More values for visual interest and complexity
    values = [30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
    for val in values:
        print(f"Inserting: {val}")
        bst.insert(val)

    print("\n=== Launching PyQt6 Visual Analyzer ===")
    app = QApplication(sys.argv)
    visualizer = TreeVisualizer(bst)
    visualizer.show()
    sys.exit(app.exec())