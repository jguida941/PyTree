# PyTree

<div align="center">
  
**A Modern Educational Tool for Visualizing Binary Search Trees**

*Developed by Justin Paul Guida | Southern New Hampshire University*

</div>

## Overview

**PyTree** is an interactive visualization tool that helps students and developers understand Binary Search Tree (BST) operations through visual learning. Built with PyQt6, it provides a clean, professional interface for exploring tree algorithms in real-time.

> **Note:** This is a personal learning project created for educational purposes and portfolio demonstration. While the code is publicly available for reference and learning, this repository is maintained as a solo project and is not accepting external contributions.

## 🌟 Why I Built This

I developed PyTree to help myself and others truly **see the patterns** in binary trees. There's something powerful about watching algorithms unfold visually that reading code alone can't provide. When you can see how a search traverses left and right, how insertions find their perfect spot, and how the tree's structure emerges organically, the abstract concepts become concrete and intuitive.

Binary trees aren't just data structures - they're beautiful patterns of organization that mirror how we naturally categorize and search through information. This visualizer exists because sometimes the best way to understand something is to watch it happen, step by step, until the patterns become second nature.

## 📸 Screenshots

<div align="center">

### Main Interface - Complete Tree
<img width="800" alt="complete_tree" src="https://github.com/user-attachments/assets/8b0e127f-8e37-4fe0-ae14-d9af0c803d97" />

*Fully populated balanced BST showing clear node relationships and complete in-order traversal*

### Insertion Process
<table>
  <tr>
    <td><img width="400" alt="before_insertion" src="https://github.com/user-attachments/assets/2681040b-1bee-4c36-9628-49911e2be155" /></td>
    <td><img width="400" alt="after_insertion" src="https://github.com/user-attachments/assets/96466d5d-2177-418e-be67-64f8e6768f28" /></td>
  </tr>
  <tr>
    <td align="center"><em>Before: Tree ready for new value insertion</em></td>
    <td align="center"><em>After: Tree grows with new node and updated traversal</em></td>
  </tr>
</table>

### Deletion Process
<table>
  <tr>
    <td><img width="400" alt="before_deletion" src="https://github.com/user-attachments/assets/143b9c24-3d79-4617-afc9-a2443b760fd9" /></td>
    <td><img width="400" alt="after_deletion" src="https://github.com/user-attachments/assets/75af97d8-9c38-485c-9609-b83e6dd0f58d" /></td>
  </tr>
  <tr>
    <td align="center"><em>Before: About to delete a node from the tree</em></td>
    <td align="center"><em>After: Tree automatically restructures</em></td>
  </tr>
</table>

### Search Operations with Feedback
<table>
  <tr>
    <td><img width="400" alt="search_result" src="https://github.com/user-attachments/assets/2d6b6a43-d520-4fa8-a6e9-2b8a93dbe048" /></td>
    <td><img width="400" alt="search_result_more_info" src="https://github.com/user-attachments/assets/0c043918-ef4f-449e-861b-e127b687a737" /></td>
  </tr>
  <tr>
    <td align="center"><em>Search confirmation popup</em></td>
    <td align="center"><em>Enhanced search feedback with path details</em></td>
  </tr>
</table>

</div>

## ✨ Features

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

## 🚀 Quick Start

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

<details>
<summary><strong>Click to expand installation options</strong></summary>

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

</details>

### Running PyTree

<details>
<summary><strong>Click to expand running options</strong></summary>

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

</details>

## 💻 Usage Examples

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

## 🧠 The Power of Visual Learning

### Pattern Recognition
- **Tree Shape Patterns** - See how different insertion orders create different tree structures
- **Search Patterns** - Watch how the binary search property guides every search decision
- **Balance Patterns** - Visualize when trees become unbalanced and why it matters

### Algorithmic Intuition
- **Recursive Thinking** - See how tree operations naturally break down into smaller subproblems
- **Comparison Logic** - Watch the simple "less than/greater than" decisions that drive everything
- **Path Visualization** - Understand that every tree operation is really about finding the right path

## 📁 Project Structure

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

## 🔍 Key Classes

<details>
<summary><strong>TreeNode</strong></summary>

Represents individual nodes in the binary search tree with position tracking for visualization.

```python
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
```
</details>

<details>
<summary><strong>BinarySearchTree</strong></summary>

Core BST implementation with educational-focused methods.

```python
class BinarySearchTree:
    def insert(self, key)      # Add new node
    def search(self, key)      # Find node with path tracking
    def delete(self, key)      # Remove node with restructuring
    def inorder_traversal()    # Return sorted sequence
```
</details>

<details>
<summary><strong>TreeVisualizer</strong></summary>

Main GUI application with interactive tree visualization.

```python
class TreeVisualizer(QWidget):
    # Handles all user interactions and visual updates
    # Custom painting with QPainter for tree rendering
    # Real-time updates for all tree operations
```
</details>

## 🎓 Educational Applications

- **Data Structures Courses** - Visual aid for teaching BST concepts and operations
- **Algorithm Analysis** - See the efficiency of different tree operations
- **Self-Study** - Interactive tool for understanding tree algorithms
- **Programming Practice** - Visualize your BST implementations
- **Pattern Recognition** - Develop intuition for tree structures and behaviors

## 💡 Implementation Highlights

<details>
<summary><strong>Visual Design</strong></summary>

- **Custom QPainter Rendering** - Hand-crafted tree visualization
- **Dynamic Layout** - Automatic node positioning based on tree structure
- **Color-coded Feedback** - Visual indicators for search paths and operations
- **Responsive Interface** - Clean, intuitive controls for all operations
</details>

<details>
<summary><strong>Tree Operations</strong></summary>

- **Insertion** - Maintains BST property while updating visualization
- **Deletion** - Handles all cases (leaf, one child, two children) with visual feedback
- **Search** - Shows path traversal with highlighted nodes
- **Traversal** - Real-time in-order sequence display
</details>

<details>
<summary><strong>Educational Focus</strong></summary>

- **Immediate Feedback** - Every operation provides instant visual confirmation
- **Pattern Visualization** - See how different operations affect tree structure
- **Interactive Learning** - Learn by doing rather than just reading
</details>

## 📝 Technical Notes

- Built with PyQt6 for cross-platform compatibility
- Uses custom QPainter rendering for precise tree visualization
- Implements efficient tree layout algorithms for optimal display
- Designed with clean code architecture for educational reference
- Minimal dependencies for easy setup and distribution

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## 👤 Author

<div align="center">
  
**Justin Paul Guida**  
*Southern New Hampshire University*  
*Computer Science, Junior (Class of 2026)*  
*GitHub: [https://github.com/jguida941](https://github.com/jguida941)*

</div>

---

<div align="center">
  
**Educational BST visualization made simple and interactive - because the best way to understand patterns is to see them in action.**

</div>

## 🚧 Project Status

This is a personal educational project developed for learning purposes at Southern New Hampshire University. The code is publicly available for reference and educational use under the MIT License.

**Repository Policy:** This is maintained as a solo educational project. While I appreciate interest in the project, I'm not accepting pull requests, issues, or external contributions at this time.

The project serves as:
- A demonstration of BST visualization techniques  
- An educational resource for other computer science students
- A portfolio piece showcasing GUI development and algorithm visualization

For questions about the implementation, feel free to explore the code and documentation. If you find this useful for your own learning, that's exactly what it was designed for!
