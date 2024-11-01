from PyQt6.QtWidgets import QApplication, QWidget

import sys

from main_windows import MainWindow
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()