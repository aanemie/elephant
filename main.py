from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QTextCursor, QTextCharFormat, QTextListFormat

app = QApplication([])
window = QWidget()
window.setWindowTitle("Бро, купи слона...")
# window.resize(800, 850)

main_text = QLabel(f"А вот все говорят OK")
p_text = QLabel("а ты возьми, и купи слона")


ok_button = QPushButton("OK")
main_text.setAlignment(Qt.AlignCenter)
p_text.setAlignment(Qt.AlignCenter)
main_l = QVBoxLayout()
main_l.addWidget(main_text)
main_l.addWidget(p_text)
main_l.addWidget(ok_button)

window.setLayout(main_l)
window.show()
app.exec_()
