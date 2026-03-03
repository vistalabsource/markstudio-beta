from PySide6.QtWidgets import QApplication, QMainWindow
from logic import MainWindowLogic

def main():
    app = QApplication([])
    window = MainWindowLogic()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
