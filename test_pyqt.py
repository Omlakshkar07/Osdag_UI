import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt

print("Starting test PyQt5 application...")

app = QApplication(sys.argv)
print("QApplication created")

window = QWidget()
window.setWindowTitle("PyQt5 Test")
window.setGeometry(100, 100, 300, 200)
print("Window created")

label = QLabel("PyQt5 is working!", window)
label.setAlignment(Qt.AlignCenter)
label.move(100, 80)
print("Label added")

print("Showing window...")
window.show()
print("Window shown")

sys.exit(app.exec_())