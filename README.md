# PyTree
[![License](https://img.shields.io/badge/License-CC%20BY--NC%204.0-0EE37B?style=for-the-badge&labelColor=0B1020)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.10%2B-66FFDA?style=for-the-badge&labelColor=0B1020)
![GUI](https://img.shields.io/badge/GUI-PyQt6-9BE564?style=for-the-badge&labelColor=0B1020)
![OS](https://img.shields.io/badge/OS-macOS%20%7C%20Linux%20%7C%20Windows-B3B3B3?style=for-the-badge&labelColor=0B1020)
![Status](https://img.shields.io/badge/Status-Educational-0EE37B?style=for-the-badge&labelColor=0B1020)

**A Modern Educational Tool for Visualizing Binary Search Trees**

*Developed by Justin Paul Guida | Southern New Hampshire University*

**Note: Version 2 is coming soon, more educational and better visuals**

## Overview

**PyTree is an interactive visualization tool that helps students and developers understand Binary Search Tree (BST) operations through visual learning. Built with PyQt6 and optionally enhanced with PySide6, it provides a clean, professional interface for exploring tree algorithms in real-time.**

> **Note:** This is a personal learning project created for educational purposes and portfolio demonstration. While the code is publicly available for reference and learning, this repository is maintained as a solo project and is not accepting external contributions.

## Why I Built This

I developed PyTree to help myself and others truly **see the patterns** in binary trees. There's something powerful about watching algorithms unfold visually that reading code alone can't provide. When you can see how a search traverses left and right, how insertions find their perfect spot, and how the tree's structure emerges organically, the abstract concepts become concrete and intuitive.

Binary trees aren't just data structures - they're beautiful patterns of organization that mirror how we naturally categorize and search through information. This visualizer exists because sometimes the best way to understand something is to watch it happen, step by step, until the patterns become second nature.



## Features

### Core Functionality
- **Real-time BST Visualization** - Watch your tree structure update as you insert and delete nodes
- **Interactive Node Operations** - Insert, search, and delete nodes with immediate visual feedback
- **In-Order Traversal Display** - See the sorted sequence automatically update in the sidebar
- **Clean Tree Layout** - Professional node positioning and connection lines
- **Tree Restructuring** - Automatic tree updates when nodes are removed
- **Search Path Highlighting** - Visual feedback showing the path taken during searches
- **Interactive Popup Messages** - Clear confirmation dialogs for search results and operations

### Educational Tools
- **Pattern Recognition** - See how different operations affect tree structure
- **Visual Learning** - Understand algorithms through interactive demonstration
- **Real-time Updates** - Watch traversal sequences change with each operation
- **Intuitive Interface** - Simple input fields for all tree operations

### Technical Features
- **Modern PyQt6 Interface** - Clean, responsive desktop application
- **Custom Tree Rendering** - Hand-crafted visualization using QPainter
- **Efficient Layout Algorithm** - Automatic node positioning for optimal viewing
- **Cross-platform Compatibility** - Runs on Windows, macOS, and Linux

## Quick Start

### Installation & Setup

```bash
# Clone the repository
git clone https://github.com/jguida941/Pytree
cd Pytree

# Install dependencies
pip install -r requirements.txt

# Run the application
python simple_binary_tree_ex.py
```

### macOS Terminal Fix

If you get a Qt platform plugin error on macOS:
```
qt.qpa.plugin: Could not find the Qt platform plugin "cocoa"
```

**Quick Fix (run before your app):**
```bash
export QT_PLUGIN_PATH=$(python -c "import PyQt6.QtCore; import os; print(os.path.join(os.path.dirname(PyQt6.QtCore.__file__), 'plugins'))")
python simple_binary_tree_ex.py
```

**Permanent Fix (add to ~/.zshrc):**
```bash
echo 'export QT_PLUGIN_PATH=$(python -c "import PyQt6.QtCore as qc; import os; print(os.path.join(os.path.dirname(qc.__file__), \"plugins\"))")' >> ~/.zshrc
source ~/.zshrc
```

### Prerequisites

#### Option 1: Install from Requirements File (Recommended)
```bash
pip install -r requirements.txt
```

#### Option 2: Manual Installation
```bash
# Core dependencies
pip install PyQt6==6.9.0 matplotlib==3.10.3 numpy==2.2.6 networkx==3.4.2

# Optional: PySide6 for advanced GUI features
pip install PySide6==6.9.1
```

#### Minimal Installation (Basic Functionality)
```bash
# For simple_binary_tree_ex.py only
pip install PyQt6
```

> **Note:** The application works with PyQt6. PySide6 is included for compatibility with the advanced GUI.py module.

### Running PyTree

#### Option 1: PyCharm (Recommended for Development)
```bash
# Clone the repository
git clone https://github.com/jguida941/Pytree

# Open in PyCharm
# 1. File → Open → Select the Pytree folder
# 2. PyCharm will automatically detect requirements.txt
# 3. Click "Install requirements" when prompted
# 4. Right-click on simple_binary_tree_ex.py → Run
```
*PyCharm automatically handles Qt environment setup - no additional configuration needed!*

#### Option 2: Command Line
```bash
python simple_binary_tree_ex.py
```
*Complete GUI with tree visualization, search path highlighting, and interactive features*

#### Option 3: Alternative Advanced Module (Optional)
```bash
# GUI.py contains additional BSTVisualizer class (requires PySide6)
python -c "from GUI import BSTVisualizer; from PySide6.QtWidgets import QApplication; import sys; app = QApplication(sys.argv); viz = BSTVisualizer(); viz.show(); sys.exit(app.exec())"
```

## Usage Examples

### Building a Tree Programmatically
```python
from simple_binary_tree_ex import BinarySearchTree

# Create a new BST
bst = BinarySearchTree()

# Insert values
values = [50, 30, 70, 20, 40, 60, 80]
for value in values:
    bst.insert(value)

# Perform operations
result = bst.inorder_traversal()
print("In-order traversal:", result)

found = bst.search(60)
print("Search for 60:", "Found" if found else "Not found")
```

### Interactive GUI Features
1. **Insert Operations** - Enter values and watch the tree grow organically
2. **Search Operations** - Find values with visual path highlighting  
3. **Delete Operations** - Remove nodes and see automatic tree restructuring
4. **Real-time Traversal** - In-order sequence updates instantly with each operation
5. **Clear Tree** - Reset to start fresh with new tree structures

## The Power of Visual Learning

### Pattern Recognition
- **Tree Shape Patterns** - See how different insertion orders create different tree structures
- **Search Patterns** - Watch how the binary search property guides every search decision
- **Balance Patterns** - Visualize when trees become unbalanced and why it matters

### Algorithmic Intuition
- **Recursive Thinking** - See how tree operations naturally break down into smaller subproblems
- **Comparison Logic** - Watch the simple "less than/greater than" decisions that drive everything
- **Path Visualization** - Understand that every tree operation is really about finding the right path

## Project Structure

```
PyTree/
├── simple_binary_tree_ex.py   # Main application (run this!)
├── GUI.py                     # Advanced BSTVisualizer class (importable module)
├── main.py                    # NetworkX graph demo
├── requirements.txt           # Python dependencies
├── LICENSE.txt                # Project license
├── README.md                  # This file
├── .gitignore                 # Git ignore rules
└── screenshots/               # Application screenshots
```

## Key Classes

### TreeNode

Represents individual nodes in the binary search tree with position tracking for visualization.

```python
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
```

### BinarySearchTree

Core BST implementation with educational-focused methods.

```python
class BinarySearchTree:
    def insert(self, key)      # Add new node
    def search(self, key)      # Find node with path tracking
    def delete(self, key)      # Remove node with restructuring
    def inorder_traversal()    # Return sorted sequence
```

### TreeVisualizer

Main GUI application with interactive tree visualization.

```python
class TreeVisualizer(QWidget):
    # Handles all user interactions and visual updates
    # Custom painting with QPainter for tree rendering
    # Real-time updates for all tree operations
```

##  Educational Applications

- **Data Structures Courses** - Visual aid for teaching BST concepts and operations
- **Algorithm Analysis** - See the efficiency of different tree operations
- **Self-Study** - Interactive tool for understanding tree algorithms
- **Programming Practice** - Visualize your BST implementations
- **Pattern Recognition** - Develop intuition for tree structures and behaviors

## Implementation Highlights

### Visual Design
- **Custom QPainter Rendering** - Hand-crafted tree visualization
- **Dynamic Layout** - Automatic node positioning based on tree structure
- **Color-coded Feedback** - Visual indicators for search paths and operations
- **Responsive Interface** - Clean, intuitive controls for all operations

### Tree Operations
- **Insertion** - Maintains BST property while updating visualization
- **Deletion** - Handles all cases (leaf, one child, two children) with visual feedback
- **Search** - Shows path traversal with highlighted nodes
- **Traversal** - Real-time in-order sequence display

### Educational Focus
- **Immediate Feedback** - Every operation provides instant visual confirmation
- **Pattern Visualization** - See how different operations affect tree structure
- **Interactive Learning** - Learn by doing rather than just reading

## Technical Notes

- Built with PyQt6 for cross-platform compatibility
- Uses custom QPainter rendering for precise tree visualization
- Implements efficient tree layout algorithms for optimal display
- Designed with clean code architecture for educational reference
- Minimal dependencies for easy setup and distribution

## License

**Evaluation only — all rights reserved.**

You may **clone and run locally** for personal or hiring evaluation.  
You may **not** redistribute, sublicense, or use this work commercially without my written permission.

See the [LICENSE](LICENSE) file for the exact terms.

**Qt note:** This app uses **PyQt6 (GPLv3)**. Do **not** redistribute the app unless you comply with GPLv3 or have a Qt commercial license.


## Author

**Justin Paul Guida**  
*Southern New Hampshire University*  
*Computer Science, Junior (Class of 2026)*  
*GitHub: [https://github.com/jguida941](https://github.com/jguida941)*

---

**Educational BST visualization made simple and interactive, because the best way to understand patterns is to see them in action.**

## Project Status

This is a personal educational project developed for learning purposes. For education or personal, no commericial use. 

**Repository Policy:** This is maintained as a solo educational project. While I appreciate interest in the project, I'm not accepting pull requests, issues, or external contributions at this time.

The project serves as:
- A demonstration of BST visualization techniques  
- An educational resource for other computer science students
- A portfolio piece showcasing GUI development and algorithm visualization

For questions about the implementation, feel free to explore the code and documentation. If you find this useful for your own learning, that's exactly what it was designed for!
