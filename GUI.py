import sys
import math
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QLabel, QPushButton, QLineEdit,
                               QGroupBox, QSpinBox, QTextEdit, QSplitter,
                               QComboBox, QMessageBox, QTabWidget, QScrollArea, QSlider, QCheckBox,
                               QDialog)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont, QColor

import numpy as np

import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import networkx as nx

import matplotlib


# --- Tree Node with Depth/Subtree Support ---
class TreeNode:
    """This is a simple tree node class - represents one node in our tree"""

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        # For visualization
        self.x = 0
        self.y = 0
        self.highlighted = False
        self.color = 'skyblue'  # Default color

    def depth(self, root=None, d=0):
        """Return the depth of this node from the root. If root is None, assumes self is root (returns 0)."""
        # Helper for BST: find node's depth from root
        if root is None:
            return 0
        if root == self:
            return d
        if self.key < root.key and root.left:
            return self.depth(root.left, d + 1)
        if self.key > root.key and root.right:
            return self.depth(root.right, d + 1)
        return None  # Not found

    def count_subtree_nodes(self):
        """Return the size of the subtree rooted at this node."""
        left = self.left.count_subtree_nodes() if self.left else 0
        right = self.right.count_subtree_nodes() if self.right else 0
        return 1 + left + right


class BinarySearchTree:
    """Main class that manages the entire binary search tree"""

    def __init__(self, root=None):
        if root is not None:
            self.root = TreeNode(root)
        else:
            self.root = None
        # For visualization and learning
        self.steps = []
        self.current_step = 0

    def insert(self, key):
        """Insert a new key into the binary search tree."""
        self.steps = []  # Reset steps for visualization

        # Log this step
        self.steps.append({
            'action': 'start_insert',
            'value': key,
            'message': f"Starting insertion of value {key}"
        })

        if self.root is None:
            self.root = TreeNode(key)
            # Log this step
            self.steps.append({
                'action': 'insert_root',
                'node': self.root,
                'message': f"Tree was empty. {key} inserted as root node."
            })
        else:
            self._insert_rec(self.root, key)

        # Final step
        self.steps.append({
            'action': 'finish_insert',
            'value': key,
            'message': f"Insertion of {key} completed!"
        })

        return self.steps

    def _insert_rec(self, node, key, path="root"):
        """Helper method to insert a new key recursively."""
        # Log visiting this node
        self.steps.append({
            'action': 'visit',
            'node': node,
            'path': path,
            'message': f"Visiting node with value {node.key}"
        })

        # Log comparison
        if key < node.key:
            self.steps.append({
                'action': 'compare',
                'node': node,
                'value': key,
                'result': 'less',
                'path': path,
                'message': f"{key} < {node.key}, moving to left child"
            })

            if node.left is None:
                node.left = TreeNode(key)
                # Log insertion
                self.steps.append({
                    'action': 'insert',
                    'node': node.left,
                    'parent': node,
                    'direction': 'left',
                    'path': f"{path}.left",
                    'message': f"Left child is empty. Inserting {key} as left child of {node.key}"
                })
            else:
                self._insert_rec(node.left, key, f"{path}.left")

        elif key > node.key:
            self.steps.append({
                'action': 'compare',
                'node': node,
                'value': key,
                'result': 'greater',
                'path': path,
                'message': f"{key} > {node.key}, moving to right child"
            })

            if node.right is None:
                node.right = TreeNode(key)
                # Log insertion
                self.steps.append({
                    'action': 'insert',
                    'node': node.right,
                    'parent': node,
                    'direction': 'right',
                    'path': f"{path}.right",
                    'message': f"Right child is empty. Inserting {key} as right child of {node.key}"
                })
            else:
                self._insert_rec(node.right, key, f"{path}.right")
        else:
            # Duplicate value
            self.steps.append({
                'action': 'duplicate',
                'node': node,
                'value': key,
                'path': path,
                'message': f"Value {key} already exists in the tree. Duplicates are not inserted."
            })

    def search(self, key):
        """Search for a key in the tree and record steps for visualization."""
        self.steps = []  # Reset steps for visualization

        # Log this step
        self.steps.append({
            'action': 'start_search',
            'value': key,
            'message': f"Starting search for value {key}"
        })

        result = self._search_rec(self.root, key)

        # Final step
        if result:
            self.steps.append({
                'action': 'finish_search',
                'value': key,
                'found': True,
                'message': f"Value {key} was found in the tree!"
            })
        else:
            self.steps.append({
                'action': 'finish_search',
                'value': key,
                'found': False,
                'message': f"Value {key} was NOT found in the tree!"
            })

        return result, self.steps

    def _search_rec(self, node, key, path="root"):
        """Helper method to search recursively and record steps."""
        if node is None:
            self.steps.append({
                'action': 'visit_null',
                'path': path,
                'message': f"Reached a null node. Value {key} not found in this path."
            })
            return False

        # Log visiting this node
        self.steps.append({
            'action': 'visit',
            'node': node,
            'path': path,
            'message': f"Visiting node with value {node.key}"
        })

        if key == node.key:
            self.steps.append({
                'action': 'found',
                'node': node,
                'value': key,
                'path': path,
                'message': f"Found! {key} matches current node value."
            })
            return True
        elif key < node.key:
            self.steps.append({
                'action': 'compare',
                'node': node,
                'value': key,
                'result': 'less',
                'path': path,
                'message': f"{key} < {node.key}, moving to left child"
            })
            return self._search_rec(node.left, key, f"{path}.left")
        else:
            self.steps.append({
                'action': 'compare',
                'node': node,
                'value': key,
                'result': 'greater',
                'path': path,
                'message': f"{key} > {node.key}, moving to right child"
            })
            return self._search_rec(node.right, key, f"{path}.right")

    def inorder_traversal(self):
        """Public method to start in-order traversal with visualization steps."""
        self.steps = []  # Reset steps

        self.steps.append({
            'action': 'start_traversal',
            'message': "Starting in-order traversal (Left -> Root -> Right)"
        })

        result = self._inorder_traversal_rec(self.root)

        self.steps.append({
            'action': 'finish_traversal',
            'result': result,
            'message': f"In-order traversal completed: {result}"
        })

        return result, self.steps

    def _inorder_traversal_rec(self, node, path="root"):
        """Private recursive helper for in-order traversal with steps."""
        if node is None:
            return []

        result = []

        # Record step before going left
        if node.left is not None:
            self.steps.append({
                'action': 'traverse_left',
                'node': node,
                'path': path,
                'message': f"At node {node.key}, traversing left subtree first"
            })

        # Traverse left
        result.extend(self._inorder_traversal_rec(node.left, f"{path}.left"))

        # Visit node
        self.steps.append({
            'action': 'visit_inorder',
            'node': node,
            'path': path,
            'message': f"Visiting node {node.key} in in-order traversal"
        })
        result.append(node.key)

        # Record step before going right
        if node.right is not None:
            self.steps.append({
                'action': 'traverse_right',
                'node': node,
                'path': path,
                'message': f"At node {node.key}, traversing right subtree now"
            })

        # Traverse right
        result.extend(self._inorder_traversal_rec(node.right, f"{path}.right"))

        return result

    def get_height(self):
        """Calculate the height of the tree."""
        return self._get_height_rec(self.root)

    def _get_height_rec(self, node):
        """Recursive helper to calculate height."""
        if node is None:
            return 0
        left_height = self._get_height_rec(node.left)
        right_height = self._get_height_rec(node.right)
        return max(left_height, right_height) + 1

    def assign_positions(self):
        """Assign x, y coordinates to nodes for visualization."""
        height = self.get_height()
        max_width = 2 ** (height) - 1
        self._assign_positions_rec(self.root, 0, max_width, 0, height)

    def _assign_positions_rec(self, node, left, right, level, height):
        """Recursive helper to assign positions."""
        if node is None:
            return

        # Calculate node position
        node.x = (left + right) / 2
        node.y = level

        # Calculate spacing based on level
        next_level = level + 1

        # Process children
        if node.left:
            self._assign_positions_rec(node.left, left, node.x, next_level, height)
        if node.right:
            self._assign_positions_rec(node.right, node.x, right, next_level, height)


# --- MatplotlibCanvas with Colorization Support ---
class MatplotlibCanvas(FigureCanvas):
    """Matplotlib canvas for drawing the tree."""

    def __init__(self, parent=None, width=8, height=6, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MatplotlibCanvas, self).__init__(self.fig)

        # Remove axis ticks and labels
        self.axes.set_xticks([])
        self.axes.set_yticks([])
        self.axes.set_frame_on(False)

        self.tree = None
        self.node_colors = {}
        self.edge_colors = {}
        self.highlighted_node = None
        self.highlighted_edge = None
        self.color_mode = "None"  # Default: no colorization

    def set_tree(self, tree):
        """Set the tree to visualize."""
        self.tree = tree
        self.reset_colors()
        self.update_figure()

    def set_color_mode(self, mode):
        """Set the node colorization mode."""
        self.color_mode = mode
        self.update_figure()

    def reset_colors(self):
        """Reset all node and edge colors."""
        self.node_colors = {}
        self.edge_colors = {}
        self.highlighted_node = None
        self.highlighted_edge = None

    def update_figure(self):
        """Update the figure with the current tree."""
        self.axes.clear()

        if not self.tree or not self.tree.root:
            self.axes.set_title("Empty Tree")
            self.draw()
            return

        # Assign positions for visualization
        self.tree.assign_positions()

        # Draw the tree
        self._draw_tree(self.tree.root, None)

        # Adjust plot limits based on tree size
        height = self.tree.get_height()
        width = 2 ** height

        self.axes.set_xlim([-1, width])
        self.axes.set_ylim([-height, 1])

        self.fig.tight_layout()
        self.draw()

    def _draw_tree(self, node, parent=None):
        """Recursively draw the tree nodes and edges."""
        if node is None:
            return

        # Node colorization logic
        node_id = id(node)
        color = self.node_colors.get(node_id)
        if not color:
            if self.color_mode == "By Depth":
                # Use depth from root to colorize
                depth = node.depth(self.tree.root)
                # Blue (shallow) to red (deep)
                max_depth = self.tree.get_height() - 1
                if max_depth <= 0:
                    color = 'skyblue'
                else:
                    cmap = plt.get_cmap("coolwarm")
                    color = cmap(depth / max_depth) if max_depth > 0 else 'skyblue'
            elif self.color_mode == "By Subtree Size":
                size = node.count_subtree_nodes()
                max_size = self.tree.root.count_subtree_nodes() if self.tree.root else 1
                cmap = plt.get_cmap("YlGnBu")
                color = cmap((size - 1) / (max_size - 1)) if max_size > 1 else 'skyblue'
            else:
                color = 'skyblue'

        # Draw node
        circle = plt.Circle((node.x, -node.y), 0.3, color=color, alpha=0.8)
        self.axes.add_patch(circle)

        # Add node label
        self.axes.text(node.x, -node.y, str(node.key),
                       horizontalalignment='center',
                       verticalalignment='center',
                       fontsize=10,
                       fontweight='bold')

        # Draw edge from parent if exists
        if parent:
            edge_key = (id(parent), id(node))
            edge_color = self.edge_colors.get(edge_key, 'black')
            self.axes.plot([parent.x, node.x], [-parent.y, -node.y],
                           color=edge_color, linewidth=2)

        # Draw children
        self._draw_tree(node.left, node)
        self._draw_tree(node.right, node)

    def highlight_node(self, node, color='yellow'):
        """Highlight a specific node."""
        if node:
            node_id = id(node)
            self.node_colors[node_id] = color
            self.highlighted_node = node_id
            self.update_figure()

    def highlight_edge(self, parent, child, color='red'):
        """Highlight a specific edge."""
        if parent and child:
            edge = (id(parent), id(child))
            self.edge_colors[edge] = color
            self.highlighted_edge = edge
            self.update_figure()

    def reset_highlights(self):
        """Reset all highlights."""
        self.reset_colors()
        self.update_figure()


class BSTVisualizer(QMainWindow):
    """Main application window for the BST visualizer."""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Binary Search Tree Visualizer")
        self.setGeometry(100, 100, 1200, 800)
        self.setMinimumSize(800, 600)

        # Create the binary search tree
        self.bst = BinarySearchTree()

        # Predefine all UI attributes to None
        self.canvas = None
        self.insert_input = None
        self.insert_button = None
        self.search_input = None
        self.search_button = None
        self.traversal_combo = None
        self.traversal_button = None
        self.speed_slider = None
        self.prev_button = None
        self.play_button = None
        self.next_button = None
        self.code_text = None
        self.explanation_text = None
        self.log_text = None
        self.sample_button = None
        self.reset_button = None
        self.color_mode_combo = None
        self.insights_groupbox = None
        self.insight_toggle_checkbox = None
        self.view_graph_button = None
        self.insights_layout = None
        self.insight_text = None
        self.export_button = None
        self.balance_warning_group = None
        self.balance_warning_layout = None
        self.balance_warning_label = None
        self.theme_combo = None
        self.anim_speed_spin = None

        # Set up the UI
        self.setup_ui()

        # Animation settings
        self.animation_speed = 1000  # ms
        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self.animation_step)
        self.current_step_index = 0
        self.current_steps = []
        self.is_animating = False

    def setup_ui(self):
        """Set up the user interface."""
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)

        # Create splitter for resizable panels
        splitter = QSplitter(Qt.Horizontal)

        # --- LEFT: Tabbed panel for Tree View, Insights, Settings ---
        tab_widget = QTabWidget()
        tab_widget.setTabPosition(QTabWidget.North)
        tab_widget.setDocumentMode(True)

        # --- Tree View Tab ---
        tree_view_tab = QWidget()
        tree_view_layout = QVBoxLayout(tree_view_tab)
        tree_view_layout.setSpacing(10)
        tree_view_layout.setContentsMargins(12, 12, 12, 12)

        self.canvas = MatplotlibCanvas(width=8, height=6)
        self.canvas.set_tree(self.bst)
        tree_view_layout.addWidget(self.canvas)

        # Add "View Graph" button
        self.view_graph_button = QPushButton("View Graph")
        self.view_graph_button.clicked.connect(self.show_tree_graph)
        tree_view_layout.addWidget(self.view_graph_button, alignment=Qt.AlignLeft)

        # --- Search Animation Speed Slider ---
        speed_box = QGroupBox("Search Animation Speed")
        speed_box_layout = QVBoxLayout(speed_box)
        self.speed_slider = QSlider(Qt.Orientation.Horizontal)
        self.speed_slider.setMinimum(1)
        self.speed_slider.setMaximum(10)
        self.speed_slider.setValue(5)
        self.speed_slider.setTickInterval(1)
        self.speed_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        speed_box_layout.addWidget(self.speed_slider)
        tree_view_layout.addWidget(speed_box)

        # Add stretch to push widgets up
        tree_view_layout.addStretch()

        # Place tree_view_tab in a scroll area
        tree_scroll = QScrollArea()
        tree_scroll.setWidgetResizable(True)
        tree_scroll.setWidget(tree_view_tab)
        tab_widget.addTab(tree_scroll, "Tree View")

        # --- Insights Tab ---
        insights_tab = QWidget()
        insights_layout = QVBoxLayout(insights_tab)
        insights_layout.setSpacing(10)
        insights_layout.setContentsMargins(12, 12, 12, 12)

        self.insights_groupbox = QGroupBox("Node Insights")
        self.insights_layout = QVBoxLayout(self.insights_groupbox)
        self.insight_text = QTextEdit()
        self.insight_text.setReadOnly(True)
        self.export_button = QPushButton("Export Node Data")
        self.export_button.clicked.connect(self.export_node_data)
        self.insights_layout.addWidget(self.insight_text)
        self.insights_layout.addWidget(self.export_button)
        insights_layout.addWidget(self.insights_groupbox)

        # Toggle checkbox
        self.insight_toggle_checkbox = QCheckBox("Show Node Insights")
        self.insight_toggle_checkbox.setChecked(True)
        self.insight_toggle_checkbox.toggled.connect(self.insights_groupbox.setVisible)
        insights_layout.addWidget(self.insight_toggle_checkbox, alignment=Qt.AlignLeft)

        # --- Balance Warning label ---
        self.balance_warning_group = QGroupBox("Balance Warning:")
        self.balance_warning_layout = QVBoxLayout(self.balance_warning_group)
        self.balance_warning_label = QLabel("⚠️ The tree is unbalanced!")
        self.balance_warning_label.setStyleSheet("color: red; font-weight: bold;")
        self.balance_warning_group.setVisible(False)
        self.balance_warning_layout.addWidget(self.balance_warning_label)
        insights_layout.addWidget(self.balance_warning_group)

        # Add stretch to push widgets up
        insights_layout.addStretch()

        # Place insights_tab in a scroll area
        insights_scroll = QScrollArea()
        insights_scroll.setWidgetResizable(True)
        insights_scroll.setWidget(insights_tab)
        tab_widget.addTab(insights_scroll, "Insights")

        # --- Settings Tab ---
        settings_tab = QWidget()
        settings_layout = QVBoxLayout(settings_tab)
        settings_layout.setSpacing(12)
        settings_layout.setContentsMargins(20, 20, 20, 20)

        theme_label = QLabel("Select Theme:")
        theme_label.setMinimumWidth(120)
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Default", "Dark", "Solarized", "High Contrast"])
        self.theme_combo.setMinimumWidth(160)
        self.theme_combo.currentTextChanged.connect(self.change_theme)
        theme_layout = QHBoxLayout()
        theme_layout.addWidget(theme_label)
        theme_layout.addWidget(self.theme_combo)
        theme_layout.addStretch()
        settings_layout.addLayout(theme_layout)
        settings_layout.addStretch()

        # Place settings_tab in a scroll area
        settings_scroll = QScrollArea()
        settings_scroll.setWidgetResizable(True)
        settings_scroll.setWidget(settings_tab)
        tab_widget.addTab(settings_scroll, "Settings")

        # Add tab_widget to splitter (left panel)
        splitter.addWidget(tab_widget)

        # --- RIGHT: Control panel in scroll area ---
        right_panel_widget = QWidget()
        right_panel_layout = QVBoxLayout(right_panel_widget)
        right_panel_layout.setSpacing(12)
        right_panel_layout.setContentsMargins(12, 12, 12, 12)

        # --- Color mode selection ---
        color_mode_layout = QHBoxLayout()
        color_mode_label = QLabel("Node Colorization:")
        self.color_mode_combo = QComboBox()
        self.color_mode_combo.addItems(["None", "By Depth", "By Subtree Size"])
        self.color_mode_combo.setMinimumWidth(140)
        self.color_mode_combo.currentTextChanged.connect(self.on_color_mode_changed)
        color_mode_layout.addWidget(color_mode_label)
        color_mode_layout.addWidget(self.color_mode_combo)
        color_mode_layout.addStretch()
        right_panel_layout.addLayout(color_mode_layout)

        # --- Operations Group ---
        operations_group = QGroupBox("Tree Operations")
        operations_layout = QVBoxLayout()
        # Insert controls
        insert_layout = QHBoxLayout()
        lbl_insert = QLabel("Insert Value:")
        lbl_insert.setMinimumWidth(90)
        insert_layout.addWidget(lbl_insert)
        self.insert_input = QSpinBox()
        self.insert_input.setRange(1, 999)
        self.insert_input.setMinimumWidth(80)
        insert_layout.addWidget(self.insert_input)
        self.insert_button = QPushButton("Insert")
        self.insert_button.setMinimumWidth(80)
        self.insert_button.clicked.connect(self.on_insert)
        insert_layout.addWidget(self.insert_button)
        operations_layout.addLayout(insert_layout)
        # Search controls
        search_layout = QHBoxLayout()
        lbl_search = QLabel("Search Value:")
        lbl_search.setMinimumWidth(90)
        search_layout.addWidget(lbl_search)
        self.search_input = QSpinBox()
        self.search_input.setRange(1, 999)
        self.search_input.setMinimumWidth(80)
        search_layout.addWidget(self.search_input)
        self.search_button = QPushButton("Search")
        self.search_button.setMinimumWidth(80)
        self.search_button.clicked.connect(self.on_search)
        search_layout.addWidget(self.search_button)
        operations_layout.addLayout(search_layout)
        # Traversal controls
        traversal_layout = QHBoxLayout()
        lbl_traversal = QLabel("Traversal:")
        lbl_traversal.setMinimumWidth(90)
        traversal_layout.addWidget(lbl_traversal)
        self.traversal_combo = QComboBox()
        self.traversal_combo.addItems(["In-Order"])
        self.traversal_combo.setMinimumWidth(120)
        traversal_layout.addWidget(self.traversal_combo)
        self.traversal_button = QPushButton("Traverse")
        self.traversal_button.setMinimumWidth(80)
        self.traversal_button.clicked.connect(self.on_traverse)
        traversal_layout.addWidget(self.traversal_button)
        operations_layout.addLayout(traversal_layout)
        operations_group.setLayout(operations_layout)
        right_panel_layout.addWidget(operations_group)

        # --- Animation controls ---
        animation_group = QGroupBox("Animation Controls")
        animation_layout = QVBoxLayout()
        speed_layout = QHBoxLayout()
        speed_layout.addWidget(QLabel("Animation Speed:"))
        self.anim_speed_spin = QSpinBox()
        self.anim_speed_spin.setRange(1, 10)
        self.anim_speed_spin.setValue(5)
        self.anim_speed_spin.setMinimumWidth(60)
        self.anim_speed_spin.valueChanged.connect(self.update_animation_speed)
        speed_layout.addWidget(self.anim_speed_spin)
        animation_layout.addLayout(speed_layout)
        buttons_layout = QHBoxLayout()
        self.prev_button = QPushButton("Previous Step")
        self.prev_button.setMinimumWidth(100)
        self.prev_button.clicked.connect(self.prev_step)
        self.prev_button.setEnabled(False)
        buttons_layout.addWidget(self.prev_button)
        self.play_button = QPushButton("Play")
        self.play_button.setMinimumWidth(80)
        self.play_button.clicked.connect(self.toggle_animation)
        self.play_button.setEnabled(False)
        buttons_layout.addWidget(self.play_button)
        self.next_button = QPushButton("Next Step")
        self.next_button.setMinimumWidth(100)
        self.next_button.clicked.connect(self.next_step)
        self.next_button.setEnabled(False)
        buttons_layout.addWidget(self.next_button)
        animation_layout.addLayout(buttons_layout)
        animation_group.setLayout(animation_layout)
        right_panel_layout.addWidget(animation_group)

        # --- Code and explanation panel ---
        explanation_group = QGroupBox("Learning Panel")
        explanation_layout = QVBoxLayout()
        self.code_text = QTextEdit()
        self.code_text.setReadOnly(True)
        self.code_text.setFont(QFont("Courier New", 10))
        explanation_layout.addWidget(QLabel("Code:"))
        explanation_layout.addWidget(self.code_text)
        self.explanation_text = QTextEdit()
        self.explanation_text.setReadOnly(True)
        explanation_layout.addWidget(QLabel("Explanation:"))
        explanation_layout.addWidget(self.explanation_text)
        explanation_group.setLayout(explanation_layout)
        right_panel_layout.addWidget(explanation_group)

        # --- Log box ---
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setMaximumHeight(100)
        right_panel_layout.addWidget(QLabel("Log:"))
        right_panel_layout.addWidget(self.log_text)

        # --- Sample tree and reset buttons ---
        self.sample_button = QPushButton("Load Sample Tree")
        self.sample_button.clicked.connect(self.load_sample_tree)
        self.sample_button.setMinimumWidth(120)
        right_panel_layout.addWidget(self.sample_button)
        self.reset_button = QPushButton("Reset Tree")
        self.reset_button.clicked.connect(self.reset_tree)
        self.reset_button.setMinimumWidth(120)
        right_panel_layout.addWidget(self.reset_button)

        # --- Right panel in QScrollArea for overflow ---
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(right_panel_widget)
        splitter.addWidget(scroll_area)
        splitter.setSizes([700, 500])
        main_layout.addWidget(splitter)
        self.setCentralWidget(central_widget)

        # Initialize with some welcome text
        self.update_code_view("insert")
        self.log("Welcome to the Binary Search Tree Visualizer!")
        self.explanation_text.setHtml("""
        <h3>Binary Search Tree Basics</h3>
        <p>A Binary Search Tree (BST) is a node-based binary tree data structure that has the following properties:</p>
        <ul>
            <li>The left subtree of a node contains only nodes with keys less than the node's key.</li>
            <li>The right subtree of a node contains only nodes with keys greater than the node's key.</li>
            <li>Both the left and right subtrees are also binary search trees.</li>
        </ul>
        <p>This visualizer will help you understand how BSTs work through interactive visualization and step-by-step animations.</p>
        <p>Get started by:</p>
        <ol>
            <li>Inserting values into the tree</li>
            <li>Searching for values</li>
            <li>Traversing the tree</li>
        </ol>
        <p>You can use the animation controls to step through operations and see exactly how they work!</p>
        """)

    def show_tree_graph(self):
        """Show NetworkX graph visualization of the tree."""
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
        nx.draw(
            graph,
            pos,
            with_labels=True,
            node_color='skyblue',
            node_size=2000,
            font_size=12,
            font_weight='bold',
            arrows=True
        )
        plt.title("Binary Search Tree Visualization")
        plt.show()

    def change_theme(self, theme_name: str):
        """Switch between color themes for the UI."""
        if theme_name == "Default":
            self.setStyleSheet("")
        elif theme_name == "Dark":
            self.setStyleSheet("""
                QWidget { background: #222; color: #EEE; }
                QGroupBox { border: 1px solid #444; margin-top: 8px; }
                QLineEdit, QTextEdit, QSpinBox, QComboBox, QSlider { background: #333; color: #EEE; }
                QPushButton { background: #444; color: #EEE; }
                QLabel { color: #EEE; }
                QTabWidget::pane { border: 1px solid #444; }
            """)
        elif theme_name == "Solarized":
            self.setStyleSheet("""
                QWidget { background: #002b36; color: #839496; }
                QGroupBox { border: 1px solid #586e75; margin-top: 8px; }
                QLineEdit, QTextEdit, QSpinBox, QComboBox, QSlider { background: #073642; color: #93a1a1; }
                QPushButton { background: #586e75; color: #fdf6e3; }
                QLabel { color: #93a1a1; }
                QTabWidget::pane { border: 1px solid #586e75; }
            """)
        elif theme_name == "High Contrast":
            self.setStyleSheet("""
                QWidget { background: #000; color: #FFF; }
                QGroupBox { border: 2px solid #FFF; margin-top: 8px; }
                QLineEdit, QTextEdit, QSpinBox, QComboBox, QSlider { background: #000; color: #FFF; border: 1px solid #FFF; }
                QPushButton { background: #FFF; color: #000; border: 2px solid #FFF; }
                QLabel { color: #FFF; }
                QTabWidget::pane { border: 2px solid #FFF; }
            """)
        self.canvas.update_figure()

    def on_color_mode_changed(self, mode):
        """Handle color mode change."""
        self.canvas.set_color_mode(mode)

    def update_animation_speed(self):
        """Update the animation speed based on slider value."""
        speed_value = self.anim_speed_spin.value()
        self.animation_speed = 2000 // speed_value
        if self.is_animating:
            self.animation_timer.stop()
            self.animation_timer.start(self.animation_speed)

    def log(self, message):
        """Add a message to the log."""
        self.log_text.append(message)
        scrollbar = self.log_text.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def update_code_view(self, operation):
        """Update the code view with the relevant operation's code."""
        if operation == "insert":
            self.code_text.setPlainText("""def insert(self, key):
    \"\"\"Insert a new key into the binary search tree.\"\"\"
    if self.root is None:  # Check if tree is empty
        self.root = TreeNode(key)  # Make this the root node
    else:
        # Tree has nodes, find correct position
        self._insert_rec(self.root, key)

def _insert_rec(self, node, key):
    \"\"\"Helper method to insert recursively.\"\"\"
    if key < node.key:  # New value is smaller
        if node.left is None:  # No left child
            node.left = TreeNode(key)  # Create as left child
        else:
            # Left child exists, recurse down left
            self._insert_rec(node.left, key)
    elif key > node.key:  # New value is larger
        if node.right is None:  # No right child
            node.right = TreeNode(key)  # Create as right child
        else:
            # Right child exists, recurse down right
            self._insert_rec(node.right, key)
    # Duplicates are not inserted (implicit)""")
        elif operation == "search":
            self.code_text.setPlainText("""def search(self, key):
    \"\"\"Search for a key in the tree\"\"\"
    return self._search_rec(self.root, key)

def _search_rec(self, node, key):
    \"\"\"Helper method to search recursively\"\"\"
    if node is None:  # Reached empty spot - not found
        return False

    if key == node.key:  # Found exact match
        return True

    elif key < node.key:  # Target is smaller
        # Search left subtree
        return self._search_rec(node.left, key)
    else:  # key > node.key - target is larger
        # Search right subtree
        return self._search_rec(node.right, key)""")
        elif operation == "traversal":
            self.code_text.setPlainText("""def inorder_traversal(self):
    \"\"\"Public method for in-order traversal\"\"\"
    return self._inorder_traversal_rec(self.root)

def _inorder_traversal_rec(self, node):
    \"\"\"Private recursive helper for traversal\"\"\"
    if node is None:
        return []

    result = []
    # Left subtree first
    result.extend(self._inorder_traversal_rec(node.left))
    # Then current node
    result.append(node.key)
    # Then right subtree
    result.extend(self._inorder_traversal_rec(node.right))
    return result""")

    def on_insert(self):
        """Handle insert button click."""
        value = self.insert_input.value()
        self.log(f"Inserting value: {value}")
        self.current_steps = self.bst.insert(value)
        self.update_code_view("insert")
        self.current_step_index = 0
        self.prev_button.setEnabled(False)
        self.next_button.setEnabled(len(self.current_steps) > 0)
        self.play_button.setEnabled(len(self.current_steps) > 0)
        self.canvas.set_tree(self.bst)
        if self.current_steps:
            self.show_step(0)
        self.update_insights()
        self.check_balance_and_warn()

    def on_search(self):
        """Handle search button click."""
        value = self.search_input.value()
        self.log(f"Searching for value: {value}")
        found, steps = self.bst.search(value)
        self.current_steps = steps
        self.update_code_view("search")
        self.current_step_index = 0
        self.prev_button.setEnabled(False)
        self.next_button.setEnabled(len(self.current_steps) > 0)
        self.play_button.setEnabled(len(self.current_steps) > 0)
        if self.current_steps:
            self.show_step(0)
        self.update_insights()
        self.check_balance_and_warn()

    def on_traverse(self):
        """Handle traverse button click."""
        self.log("Starting in-order traversal")
        result, steps = self.bst.inorder_traversal()
        self.current_steps = steps
        self.update_code_view("traversal")
        self.current_step_index = 0
        self.prev_button.setEnabled(False)
        self.next_button.setEnabled(len(self.current_steps) > 0)
        self.play_button.setEnabled(len(self.current_steps) > 0)
        if self.current_steps:
            self.show_step(0)
        self.update_insights()
        self.check_balance_and_warn()

    def show_step(self, step_index):
        """Show a specific step in the animation sequence."""
        if not self.current_steps or step_index < 0 or step_index >= len(self.current_steps):
            return

        step = self.current_steps[step_index]
        self.canvas.reset_highlights()
        self.explanation_text.setHtml(self.get_explanation_for_step(step))
        self.highlight_for_step(step)
        self.prev_button.setEnabled(step_index > 0)
        self.next_button.setEnabled(step_index < len(self.current_steps) - 1)
        if 'message' in step:
            self.log(step['message'])

    def prev_step(self):
        """Step backward through the animation."""
        if self.current_step_index > 0:
            self.current_step_index -= 1
            self.show_step(self.current_step_index)

    def next_step(self):
        """Step forward through the animation."""
        if self.current_step_index < len(self.current_steps) - 1:
            self.current_step_index += 1
            self.show_step(self.current_step_index)

    def toggle_animation(self):
        """Toggle play/pause for animation."""
        if self.is_animating:
            self.animation_timer.stop()
            self.is_animating = False
            self.play_button.setText("Play")
        else:
            if self.current_steps and self.current_step_index < len(self.current_steps) - 1:
                self.animation_timer.start(self.animation_speed)
                self.is_animating = True
                self.play_button.setText("Pause")

    def animation_step(self):
        """Handle automatic animation stepping."""
        if self.current_step_index < len(self.current_steps) - 1:
            self.current_step_index += 1
            self.show_step(self.current_step_index)
        else:
            self.animation_timer.stop()
            self.is_animating = False
            self.play_button.setText("Play")

    def highlight_for_step(self, step):
        """Highlight nodes/edges based on the current step."""
        action = step.get('action', '')

        if action in ['visit', 'visit_inorder']:
            node = step.get('node')
            if node:
                self.canvas.highlight_node(node, 'yellow')
        elif action == 'found':
            node = step.get('node')
            if node:
                self.canvas.highlight_node(node, 'lightgreen')
        elif action == 'insert':
            node = step.get('node')
            if node:
                self.canvas.highlight_node(node, 'lightblue')

    def load_sample_tree(self):
        """Load a sample tree for demonstration."""
        self.bst = BinarySearchTree()
        sample_values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]

        for value in sample_values:
            self.bst.insert(value)

        self.canvas.set_tree(self.bst)
        self.log("Sample tree loaded with values: " + ", ".join(map(str, sample_values)))
        self.update_insights()
        self.check_balance_and_warn()

    def reset_tree(self):
        """Reset the tree to empty state."""
        self.bst = BinarySearchTree()
        self.canvas.set_tree(self.bst)
        self.current_steps = []
        self.current_step_index = 0

        self.prev_button.setEnabled(False)
        self.next_button.setEnabled(False)
        self.play_button.setEnabled(False)

        if self.is_animating:
            self.animation_timer.stop()
            self.is_animating = False
            self.play_button.setText("Play")

        self.explanation_text.setHtml("""
        <h3>Tree Reset</h3>
        <p>The tree has been cleared. You can now:</p>
        <ul>
            <li>Insert new values</li>
            <li>Load a sample tree</li>
            <li>Explore different tree structures</li>
        </ul>
        """)

        self.log("Tree has been reset to empty state")
        self.update_insights()
        self.check_balance_and_warn()

    def update_insights(self):
        """Update the insights panel with tree statistics."""
        if not self.bst or not self.bst.root:
            self.insight_text.setPlainText("Tree is empty - no insights available.")
            return

        def count_nodes(node):
            if not node:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)

        def count_leaves(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            return count_leaves(node.left) + count_leaves(node.right)

        def find_min_max(node):
            if not node:
                return None, None

            min_node = node
            while min_node.left:
                min_node = min_node.left

            max_node = node
            while max_node.right:
                max_node = max_node.right

            return min_node.key, max_node.key

        total_nodes = count_nodes(self.bst.root)
        total_leaves = count_leaves(self.bst.root)
        height = self.bst.get_height()
        min_val, max_val = find_min_max(self.bst.root)
        traversal_result = self.bst.inorder_traversal()[0] if self.bst.root else []

        insights = f"""Tree Statistics:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Basic Information:
   • Total Nodes: {total_nodes}
   • Leaf Nodes: {total_leaves}
   • Internal Nodes: {total_nodes - total_leaves}
   • Tree Height: {height}
   • Root Value: {self.bst.root.key}

📈 Value Range:
   • Minimum Value: {min_val}
   • Maximum Value: {max_val}
   • Value Range: {max_val - min_val if min_val and max_val else 0}

🔄 Traversal:
   • In-order: {traversal_result}
   • Is Sorted: {traversal_result == sorted(traversal_result)}

⚖️ Balance Analysis:
   • Perfect Binary Tree: {total_nodes == (2 ** height - 1)}
   • Max Possible Height: {height}
   • Min Possible Height: {max(1, int(math.log2(total_nodes)) + 1) if total_nodes > 0 else 0}

🎯 Tree Quality:
   • Fill Ratio: {(total_nodes / (2 ** height - 1) * 100):.1f}% of perfect tree
   • Leaf Ratio: {(total_leaves / total_nodes * 100):.1f}% are leaves
   • Depth Efficiency: {'Good' if height <= math.log2(total_nodes) + 1 else 'Could be improved'}
"""

        self.insight_text.setPlainText(insights)

    def check_balance_and_warn(self):
        """Check if tree is unbalanced and show warning."""
        if not self.bst or not self.bst.root:
            self.balance_warning_group.setVisible(False)
            return

        def calculate_balance_factor(node):
            if not node:
                return 0

            left_height = self.bst._get_height_rec(node.left)
            right_height = self.bst._get_height_rec(node.right)

            return abs(left_height - right_height)

        def is_unbalanced(node):
            if not node:
                return False

            if calculate_balance_factor(node) > 1:
                return True

            return is_unbalanced(node.left) or is_unbalanced(node.right)

        total_nodes = self.bst.root.count_subtree_nodes() if self.bst.root else 0
        height = self.bst.get_height()
        optimal_height = max(1, int(math.log2(total_nodes)) + 1) if total_nodes > 0 else 0

        if height > optimal_height + 2 or is_unbalanced(self.bst.root):
            self.balance_warning_group.setVisible(True)
            self.balance_warning_label.setText(
                f"⚠️ Tree is unbalanced!\n"
                f"Current height: {height}, Optimal: ~{optimal_height}\n"
                f"Consider rebalancing for better performance."
            )
        else:
            self.balance_warning_group.setVisible(False)

    def export_node_data(self):
        """Export tree data for analysis."""
        if not self.bst or not self.bst.root:
            QMessageBox.information(self, "Export", "Tree is empty - nothing to export.")
            return

        def collect_node_data(node, depth=0, path="root"):
            if not node:
                return []

            data = []
            node_info = {
                'value': node.key,
                'depth': depth,
                'path': path,
                'is_leaf': not node.left and not node.right,
                'has_left_child': node.left is not None,
                'has_right_child': node.right is not None,
                'subtree_size': node.count_subtree_nodes()
            }
            data.append(node_info)

            if node.left:
                data.extend(collect_node_data(node.left, depth + 1, f"{path}.left"))
            if node.right:
                data.extend(collect_node_data(node.right, depth + 1, f"{path}.right"))

            return data

        node_data = collect_node_data(self.bst.root)

        export_text = "Value,Depth,Path,IsLeaf,HasLeft,HasRight,SubtreeSize\n"
        for node in node_data:
            export_text += f"{node['value']},{node['depth']},{node['path']},{node['is_leaf']},{node['has_left_child']},{node['has_right_child']},{node['subtree_size']}\n"

        dialog = QDialog(self)
        dialog.setWindowTitle("Export Tree Data")
        dialog.setGeometry(200, 200, 600, 400)

        layout = QVBoxLayout(dialog)

        label = QLabel("Tree data in CSV format (copy to clipboard or save to file):")
        layout.addWidget(label)

        text_edit = QTextEdit()
        text_edit.setPlainText(export_text)
        text_edit.selectAll()
        layout.addWidget(text_edit)

        close_button = QPushButton("Close")
        close_button.clicked.connect(dialog.accept)
        layout.addWidget(close_button)

        dialog.exec()

    def get_explanation_for_step(self, step):
        """Generate HTML explanation for a step."""
        action = step.get('action', '')

        if action == 'start_insert':
            return f"""
            <h3>Insert Operation: Step 1</h3>
            <p>Starting to insert value <b>{step.get('value')}</b> into the tree.</p>
            <p>The insertion algorithm will:</p>
            <ol>
                <li>First check if the tree is empty</li>
                <li>If empty, create a new root node with this value</li>
                <li>Otherwise, traverse the tree to find the correct position</li>
            </ol>
            """
        elif action == 'insert_root':
            return f"""
            <h3>Insert Operation: Creating Root</h3>
            <p>The tree was empty, so we're creating a new root node with value <b>{step.get('node').key}</b>.</p>
            <p>This is the simplest case for insertion - when there's no existing tree structure.</p>
            """
        elif action == 'visit':
            node = step.get('node')
            if node:
                return self._format_visit_node_explanation(node, step.get('path', ''))
        elif action == 'compare':
            node = step.get('node')
            value = step.get('value')
            result = step.get('result', '')
            return self._format_comparison_explanation(node, value, result, step.get('path', ''))
        elif action == 'insert':
            node = step.get('node')
            parent = step.get('parent')
            direction = step.get('direction')
            return f"""
            <h3>Inserting Node</h3>
            <p>Inserting value <b>{node.key}</b> as the <b>{direction}</b> child of node <b>{parent.key}</b>.</p>
            <p>This node is now part of the tree and will be visualized accordingly.</p>
            <p><b>Traversal Path:</b> {step.get('path', '')}</p>
            """
        elif action == 'duplicate':
            return f"""
            <h3>Duplicate Value</h3>
            <p>The value <b>{step.get('value')}</b> already exists in the tree and will not be inserted again.</p>
            <p>Binary search trees do not allow duplicate values.</p>
            <p><b>Traversal Path:</b> {step.get('path', '')}</p>
            """
        elif action == 'start_search':
            return f"""
            <h3>Start Search</h3>
            <p>We are starting a search for the value <b>{step.get('value')}</b> in the tree.</p>
            """
        elif action == 'found':
            node = step.get('node')
            return f"""
            <h3>Value Found</h3>
            <p>We have found the value <b>{step.get('value')}</b> at node <b>{node.key}</b>.</p>
            <p>Search successful!</p>
            <p><b>Traversal Path:</b> {step.get('path', '')}</p>
            """
        elif action == 'visit_null':
            return f"""
            <h3>Reached Null Node</h3>
            <p>We reached a null node — the value <b>{step.get('value', '')}</b> was not found on this path.</p>
            <p><b>Traversal Path:</b> {step.get('path', '')}</p>
            """
        elif action == 'finish_search':
            if step.get('found'):
                return f"""
                <h3>Search Complete</h3>
                <p>The value <b>{step.get('value')}</b> was found in the tree.</p>
                """
            else:
                return f"""
                <h3>Search Complete</h3>
                <p>The value <b>{step.get('value')}</b> was not found in the tree.</p>
                """
        elif action == 'start_traversal':
            return f"""
            <h3>Traversal Start</h3>
            <p>Beginning in-order traversal (Left → Root → Right).</p>
            """
        elif action == 'traverse_left':
            node = step.get('node')
            return f"""
            <h3>Traversing Left</h3>
            <p>At node <b>{node.key}</b>. Moving to the left subtree.</p>
            <p><b>Traversal Path:</b> {step.get('path', '')}</p>
            """
        elif action == 'visit_inorder':
            node = step.get('node')
            return self._format_visit_node_explanation(node, step.get('path', ''))
        elif action == 'traverse_right':
            node = step.get('node')
            return f"""
            <h3>Traversing Right</h3>
            <p>At node <b>{node.key}</b>. Moving to the right subtree.</p>
            <p><b>Traversal Path:</b> {step.get('path', '')}</p>
            """
        elif action == 'finish_traversal':
            result = step.get('result', [])
            return f"""
            <h3>Traversal Complete</h3>
            <p>The in-order traversal is complete.</p>
            <p><b>Traversal Result:</b> {result}</p>
            """
        elif action == 'finish_insert':
            return f"""
            <h3>Insert Complete</h3>
            <p>The insertion operation for value <b>{step.get('value')}</b> is complete.</p>
            """

    @staticmethod
    def _format_visit_node_explanation(node, path):
        """Format explanation for visiting a node."""
        if node is None:
            return ""
        return f"""
        <h3>Visiting Node</h3>
        <p>Currently at node with value <b>{node.key}</b> (highlighted in yellow).</p>
        <p>Next, we'll compare our target value with this node's value to decide which way to go.</p>
        <p><b>Path:</b> {path}</p>
        """

    @staticmethod
    def _format_comparison_explanation(node, value, result, path):
        """Format explanation for comparison steps."""
        if node is None:
            return ""
        comparison_text = "less than" if result == "less" else "greater than"
        return f"""
        <h3>Comparing Values</h3>
        <p>Comparing the value <b>{value}</b> with current node <b>{node.key}</b>.</p>
        <p>Since <b>{value}</b> is <b>{comparison_text}</b> <b>{node.key}</b>, we'll move to the <b>{'left' if result == 'less' else 'right'}</b> child.</p>
        <p><b>Traversal Path:</b> {path}</p>
        """


# --- NetworkX BST Visualization Utilities ---
def visualize_bst_with_networkx(tree: BinarySearchTree):
    """Uses NetworkX and Matplotlib to render the BST as a graph."""

    def add_edges(graph, node):
        if node.left:
            graph.add_edge(node.key, node.left.key)
            add_edges(graph, node.left)
        if node.right:
            graph.add_edge(node.key, node.right.key)
            add_edges(graph, node.right)

    if tree.root is None:
        print("Empty Tree")
        return

    graph = nx.DiGraph()
    add_edges(graph, tree.root)

    positions = hierarchy_pos(graph, tree.root.key)
    plt.figure(figsize=(8, 6))
    nx.draw(graph, positions, with_labels=True, node_color='skyblue', node_size=1200, font_weight='bold', arrows=True)
    plt.title("Binary Search Tree (NetworkX View)")
    plt.show()


def hierarchy_pos(graph, root=None, width=1.0, vert_gap=0.2, _vert_loc=0, _xcenter=0.5):
    """Recursively positions a tree graph in a hierarchical layout."""
    pos = {}

    def _hierarchy_pos(g, node, left, right, level=0):
        x = (left + right) / 2
        pos[node] = (x, -level * vert_gap)
        neighbors = list(g.neighbors(node))
        if neighbors:
            width_per_child = (right - left) / len(neighbors)
            for i, child in enumerate(neighbors):
                _hierarchy_pos(g, child, left + i * width_per_child, left + (i + 1) * width_per_child, level + 1)

    _hierarchy_pos(graph, root, 0, width)
    return pos


# Entry point for running the PySide6 version directly
def main():
    """Main entry point for the PySide6 version."""
    app = QApplication(sys.argv)

    # Set application properties
    app.setApplicationName("PyTree")
    app.setApplicationVersion("1.0")
    app.setOrganizationName("Southern New Hampshire University")
    app.setOrganizationDomain("snhu.edu")

    visualizer = BSTVisualizer()
    visualizer.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()