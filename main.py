#!/usr/bin/env python3
"""
Unified Main Launcher for PyTree Binary Search Tree Visualizer
Handles both PySide6 and PyQt6 versions with fallback support
"""

import sys
import os


def print_banner():
    """Display the application banner."""
    print("\n" + "=" * 60)
    print("🌳 PyTree - Binary Search Tree Visualizer")
    print("=" * 60)
    print("   Advanced Educational Tool for Learning BST Operations")
    print("   Developed for Southern New Hampshire University")
    print("=" * 60)


def show_version_menu():
    """Display version selection menu."""
    print("\nAvailable versions:")
    print("1. 🚀 PySide6 Version (Feature-Rich & Recommended)")
    print("   • Matplotlib integration for beautiful visualizations")
    print("   • Step-by-step animations with detailed explanations")
    print("   • NetworkX graph views for alternative perspectives")
    print("   • Advanced analysis tools and tree insights")
    print("   • Multiple color schemes and themes")
    print("   • Export capabilities for data analysis")

    print("\n2. ⚡ PyQt6 Version (Lightweight & Fast)")
    print("   • Custom QPainter rendering for performance")
    print("   • Search path highlighting with visual feedback")
    print("   • Real-time operations with immediate response")
    print("   • Minimal dependencies for quick setup")
    print("   • Clean, simple interface")

    print("\n3. 🔍 Auto-detect (Try PySide6, fallback to PyQt6)")
    print("4. 📋 Show System Information")
    print("5. 🚪 Exit")
    print("=" * 60)


def check_dependencies():
    """Check what dependencies are available."""
    deps = {
        'PySide6': False,
        'PyQt6': False,
        'matplotlib': False,
        'networkx': False,
        'numpy': False
    }

    try:
        import PySide6
        deps['PySide6'] = True
    except ImportError:
        pass

    try:
        import PyQt6
        deps['PyQt6'] = True
    except ImportError:
        pass

    try:
        import matplotlib
        deps['matplotlib'] = True
    except ImportError:
        pass

    try:
        import networkx
        deps['networkx'] = True
    except ImportError:
        pass

    try:
        import numpy
        deps['numpy'] = True
    except ImportError:
        pass

    return deps


def show_system_info():
    """Display system and dependency information."""
    print("\n" + "=" * 50)
    print("📋 System Information")
    print("=" * 50)
    print(f"Python Version: {sys.version}")
    print(f"Platform: {sys.platform}")
    print(f"Current Directory: {os.getcwd()}")

    print("\n📦 Dependency Status:")
    deps = check_dependencies()

    for dep, available in deps.items():
        status = "✅ Available" if available else "❌ Missing"
        print(f"   {dep}: {status}")

    print("\n💡 Installation Commands:")
    if not deps['PySide6']:
        print("   PySide6: pip install PySide6")
    if not deps['PyQt6']:
        print("   PyQt6: pip install PyQt6")
    if not deps['matplotlib']:
        print("   Matplotlib: pip install matplotlib")
    if not deps['networkx']:
        print("   NetworkX: pip install networkx")
    if not deps['numpy']:
        print("   NumPy: pip install numpy")

    print("\n🔧 Complete Setup:")
    print("   All dependencies: pip install PySide6 PyQt6 matplotlib networkx numpy")
    print("=" * 50)


def launch_pyside6():
    """Launch PySide6 version with comprehensive error handling."""
    try:
        print("🚀 Initializing PySide6 Version...")

        # Check for PySide6
        try:
            from PySide6.QtWidgets import QApplication
        except ImportError:
            print("❌ PySide6 not found!")
            print("💡 Install with: pip install PySide6")
            return False

        # Check for additional dependencies
        missing_deps = []
        try:
            import matplotlib
        except ImportError:
            missing_deps.append("matplotlib")

        try:
            import networkx
        except ImportError:
            missing_deps.append("networkx")

        try:
            import numpy
        except ImportError:
            missing_deps.append("numpy")

        if missing_deps:
            print(f"⚠️  Warning: Missing optional dependencies: {', '.join(missing_deps)}")
            print("   Some features may not work properly.")
            print(f"💡 Install with: pip install {' '.join(missing_deps)}")

        # Try to import GUI module
        try:
            from GUI import BSTVisualizer
        except ImportError as e:
            print(f"❌ Could not import GUI module: {e}")
            print("💡 Make sure GUI.py is in the current directory")
            return False

        # Launch the application
        print("✨ Starting PySide6 application...")
        app = QApplication(sys.argv)

        # Set application properties
        app.setApplicationName("PyTree BST Visualizer")
        app.setApplicationVersion("2.0")
        app.setOrganizationName("SNHU")

        visualizer = BSTVisualizer()
        visualizer.show()

        print("✅ PySide6 GUI launched successfully!")
        print("🎓 Enjoy learning about Binary Search Trees!")

        sys.exit(app.exec())

    except Exception as e:
        print(f"❌ Unexpected error launching PySide6 version: {e}")
        print("🔧 Try launching PyQt6 version instead")
        return False


def launch_pyqt6():
    """Launch PyQt6 version with comprehensive error handling."""
    try:
        print("⚡ Initializing PyQt6 Version...")

        # Check for PyQt6
        try:
            from PyQt6.QtWidgets import QApplication
        except ImportError:
            print("❌ PyQt6 not found!")
            print("💡 Install with: pip install PyQt6")
            return False

        # Try to import required modules
        try:
            from simple_binary_tree_ex import BinarySearchTree, TreeVisualizer
        except ImportError as e:
            print(f"❌ Could not import simple_binary_tree_ex module: {e}")
            print("💡 Make sure simple_binary_tree_ex.py is in the current directory")
            return False

        # Create sample tree as shown in the original code
        print("🌳 Creating sample Binary Search Tree...")
        bst = BinarySearchTree(50)
        values = [30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
        for val in values:
            bst.insert(val)

        # Launch the application
        print("✨ Starting PyQt6 application...")
        app = QApplication(sys.argv)

        # Set application properties
        app.setApplicationName("PyTree BST Visualizer")
        app.setApplicationVersion("1.0")

        visualizer = TreeVisualizer(bst)
        visualizer.show()

        print("✅ PyQt6 GUI launched successfully!")
        print("🎓 Enjoy learning about Binary Search Trees!")

        sys.exit(app.exec())

    except Exception as e:
        print(f"❌ Unexpected error launching PyQt6 version: {e}")
        return False


def auto_detect_and_launch():
    """Try PySide6 first, fallback to PyQt6."""
    print("🔍 Auto-detecting available frameworks...")

    # Check what's available
    deps = check_dependencies()

    if deps['PySide6']:
        print("✅ PySide6 detected - launching feature-rich version...")
        return launch_pyside6()
    elif deps['PyQt6']:
        print("⚠️  PySide6 not available, using PyQt6...")
        print("✅ PyQt6 detected - launching lightweight version...")
        return launch_pyqt6()
    else:
        print("❌ Neither PySide6 nor PyQt6 is available!")
        print("\n💡 Please install one of the following:")
        print("   For full features: pip install PySide6 matplotlib networkx numpy")
        print("   For basic features: pip install PyQt6")
        print("\n🔧 Or install everything: pip install PySide6 PyQt6 matplotlib networkx numpy")
        return False


def main():
    """Main entry point for the unified launcher."""
    try:
        print_banner()

        while True:
            show_version_menu()

            try:
                choice = input("\n🎯 Select option (1-5): ").strip()

                if choice == "1":
                    if launch_pyside6():
                        break
                    else:
                        input("\nPress Enter to return to menu...")

                elif choice == "2":
                    if launch_pyqt6():
                        break
                    else:
                        input("\nPress Enter to return to menu...")

                elif choice == "3":
                    if auto_detect_and_launch():
                        break
                    else:
                        input("\nPress Enter to return to menu...")

                elif choice == "4":
                    show_system_info()
                    input("\nPress Enter to return to menu...")

                elif choice == "5":
                    print("\n👋 Thanks for using PyTree!")
                    print("🎓 Keep learning and exploring Binary Search Trees!")
                    break

                else:
                    print("❌ Invalid choice. Please enter 1, 2, 3, 4, or 5.")

            except KeyboardInterrupt:
                print("\n\n👋 Thanks for using PyTree!")
                break
            except EOFError:
                print("\n\n👋 Thanks for using PyTree!")
                break

    except Exception as e:
        print(f"\n❌ Unexpected error in main launcher: {e}")
        print("\n🔧 Alternative launch methods:")
        print("   Direct PySide6: python GUI.py")
        print("   Direct PyQt6: python simple_binary_tree_ex.py")


if __name__ == "__main__":
    main()