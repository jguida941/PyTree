# PyTree

**PyTree** is a modern educational tool for visualizing and understanding Binary Search Trees (BSTs) using PySide6/PyQt6.

*Developed by Justin Paul Guida - Southern New Hampshire University*

> **Note:** This is a personal learning project created for educational purposes and portfolio demonstration. While the code is publicly available for reference and learning, this repository is maintained as a solo project and is not accepting external contributions.

## Why I Built This

I developed PyTree to help myself and others truly **see the patterns** in binary trees. There's something powerful about watching algorithms unfold visually that reading code alone can't provide. When you can see how a search traverses left and right, how insertions find their perfect spot, and how the tree's structure emerges organically, the abstract concepts become concrete and intuitive.

Binary trees aren't just data structures - they're beautiful patterns of organization that mirror how we naturally categorize and search through information. This visualizer exists because sometimes the best way to understand something is to watch it happen, step by step, until the patterns become second nature.

## Features

### Core Functionality
- **Real-time BST Visualization** - Watch your tree structure update as you insert nodes
- **Interactive Node Operations** - Insert, search, and delete nodes with immediate visual feedback
- **Step-by-Step Animation** - Visualize algorithms executing with detailed explanations
- **Multiple Traversal Methods** - See in-order, pre-order, and post-order traversals
- **Search Path Highlighting** - Visual feedback showing the path taken during searches

### Educational Tools
- **Code Display** - View the actual implementation code for each operation
- **Detailed Explanations** - Step-by-step breakdown of what's happening during operations
- **Animation Controls** - Play, pause, and step through operations at your own pace
- **Node Insights** - Analyze tree properties like depth, subtree size, and balance
- **Balance Warnings** - Get notified when your tree becomes unbalanced

### Technical Features
- **Modern PySide6 Interface** - Clean, responsive desktop application
- **NetworkX Integration** - Alternative graph-based tree visualization
- **Multiple Color Modes** - Colorize nodes by depth or subtree size
- **Theme Support** - Dark mode, high contrast, and custom themes
- **Export Capabilities** - Save tree data and analysis results

## Quick Start

### Prerequisites
```bash
pip install PySide6 matplotlib networkx numpy
```

### Running PyTree

#### GUI Application (Full Featured)
```bash
python GUI.py
```

#### Simple Visualizer (Basic Interface)
```bash
python simple_binary_tree_ex.py
```

#### Minimal Example (Command Line Demo)
```bash
python main.py
```

## Usage Examples

### Building a Tree Programmatically
```python
from GUI import BinarySearchTree

# Create a new BST
bst = BinarySearchTree()

# Insert values
values = [50, 30, 70, 20, 40, 60, 80]
for value in values:
    bst.insert(value)

# Perform operations
result, steps = bst.inorder_traversal()
print("In-order traversal:", result)

found, search_steps = bst.search(60)
print("Search for 60:", "Found" if found else "Not found")
```

### Interactive GUI Features
1. **Insert Operations** - Use the spin box to add values and watch the tree grow
2. **Search Visualization** - Search for values and see the path highlighted
3. **Animation Controls** - Step through operations to understand the algorithm
4. **Code Learning** - View the implementation code alongside the visualization
5. **Tree Analysis** - Get insights about node properties and tree balance

## The Power of Visual Learning

### Pattern Recognition
- **Tree Shape Patterns** - See how different insertion orders create different tree structures
- **Search Patterns** - Watch how the binary search property guides every search decision
- **Balance Patterns** - Visualize when trees become unbalanced and why it matters

### Algorithmic Intuition
- **Recursive Thinking** - See how tree operations naturally break down into smaller subproblems
- **Comparison Logic** - Watch the simple "less than/greater than" decisions that drive everything
- **Path Visualization** - Understand that every tree operation is really about finding the right path

### Memory and Understanding
Visual patterns stick in memory differently than abstract concepts. When you've seen a search animation dozens of times, you internalize not just what happens, but why it works and how to think about similar problems.

## Project Structure

```
PyTree/
├── GUI.py                     # Main PySide6 application with full features
├── simple_binary_tree_ex.py   # Simplified PyQt6 visualizer
├── main.py                    # Basic tree graph visualization
├── LICENSE.txt                # Project license
└── README.md                  # This file
```

## Key Classes

### TreeNode
Represents individual nodes in the binary search tree with position tracking for visualization.

### BinarySearchTree
Core BST implementation with step-by-step operation tracking for educational purposes.

### BSTVisualizer (GUI.py)
Full-featured PySide6 application with:
- Tabbed interface (Tree View, Insights, Settings)
- Animation controls and speed adjustment
- Code display and explanations
- Theme support and customization

### TreeVisualizer (simple_binary_tree_ex.py)
Simplified interface focusing on basic BST operations with visual feedback.

## Educational Applications

- **Data Structures Courses** - Visual aid for teaching BST concepts and operations
- **Algorithm Analysis** - Compare performance of different tree operations
- **Self-Study** - Interactive tool for understanding tree algorithms
- **Programming Practice** - Visualize your BST implementations
- **Pattern Recognition** - Develop intuition for tree structures and behaviors

## Implementation Features

### Animation System
- Step-by-step operation breakdown
- Configurable animation speed
- Play/pause/step controls
- Visual highlighting of current operations

### Tree Analysis
- Real-time balance checking
- Node depth calculation
- Subtree size analysis
- Path tracking and visualization

### Visualization Modes
- Traditional tree layout
- NetworkX graph representation
- Color-coded nodes (by depth or subtree size)
- Search path highlighting

## Learning Philosophy

This tool embodies the belief that:
- **Visualization accelerates understanding** - Seeing patterns makes them memorable
- **Interactivity deepens learning** - Doing beats reading about doing
- **Step-by-step revelation** - Complex algorithms become simple when broken into steps
- **Multiple perspectives help** - Code + visualization + explanation = deeper understanding

## Contributing

Contributions are welcome! Areas for improvement:
- Additional tree operations (deletion, rotation)
- More traversal algorithms
- Performance metrics and complexity analysis
- Enhanced animation effects
- Additional export formats

The goal is always to make the patterns more visible and the learning more intuitive.

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Author

**Justin Paul Guida**  
*Southern New Hampshire University*  
*Computer Science, Junior (Class of 2026)*  
*GitHub: https://github.com/jguida941*

## Technical Notes

- Built with PySide6/PyQt6 for cross-platform compatibility
- Uses matplotlib for tree rendering and NetworkX for graph layouts
- Implements educational-focused step tracking for all operations
- Designed with extensibility in mind for additional tree algorithms

---

**Educational BST visualization made simple and interactive - because the best way to understand patterns is to see them in action.**

## Project Status

This is a personal educational project developed for learning purposes at Southern New Hampshire University. The code is publicly available for reference and educational use under the MIT License.

**Repository Policy:** This is maintained as a solo educational project. While I appreciate interest in the project, I'm not accepting pull requests, issues, or external contributions at this time.

The project serves as:
- A demonstration of BST visualization techniques  
- An educational resource for other computer science students
- A portfolio piece showcasing GUI development and algorithm visualization

For questions about the implementation, feel free to explore the code and documentation. If you find this useful for your own learning, that's exactly what it was designed for!