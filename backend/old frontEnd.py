import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QTextEdit, QLineEdit, QPushButton, QLabel
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenstergröße auf Bildschirmgröße setzen
        self.setGeometry(0, 0, QApplication.primaryScreen().size().width(),
                          QApplication.primaryScreen().size().height())

        # Hintergrundbild laden
        self.set_background("background.jpg")  # Pfad zum Bild hier einfügen

        # Spieler-Widget erstellen
        self.player_widget = QWidget(self)
        self.player_label = QLabel("Spieler", self.player_widget)
        self.player_label.setAlignment(Qt.AlignCenter)
        self.player_widget.setGeometry(20, 100, 200, 200)
        self.player_widget.setStyleSheet("background-color: rgba(255, 255, 255, 128);")

        # Gegner-Widget erstellen
        self.enemy_widget = QWidget(self)
        self.enemy_label = QLabel("Gegner", self.enemy_widget)
        self.enemy_label.setAlignment(Qt.AlignCenter)
        self.enemy_widget.setGeometry(self.width() - 220, 100, 200, 200)
        self.enemy_widget.setStyleSheet("background-color: rgba(255, 255, 255, 128);")

        # Textausgabe-Widget erstellen
        self.text_widget = QTextEdit(self)
        self.text_widget.setGeometry(400, 400, 1120, 200)
        self.text_widget.setStyleSheet("background-color: black; color: white;")
        self.text_widget.setFont(QFont("Arial", 12))
        self.text_widget.setReadOnly(True)
        self.text_widget.setPlaceholderText("Hier wird der Spieltext angezeigt")

        # Eingabefeld für Text
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(400, 350, 1120, 30)
        self.input_field.setStyleSheet("background-color: white;")
        self.input_field.setPlaceholderText("Text eingeben")
        self.input_field.returnPressed.connect(self.submit_text)

        # Beenden-Button
        self.btn_exit = QPushButton("Beenden", self)
        self.set_exit_button_position()
        self.btn_exit.clicked.connect(QApplication.instance().quit)

    def submit_text(self):
        text = self.input_field.text()
        if text:
            self.append_text(text)
            self.input_field.clear()

    def append_text(self, text):
        """Text an die Anzeige anhängen."""
        self.text_widget.append(text)

    def set_background(self, path: str):
        # Bild laden
        pixmap = QPixmap(path)

        # Label für das Hintergrundbild erstellen und zum Hauptfenster hinzufügen
        label = QLabel(self)
        label.setPixmap(pixmap)
        label.setGeometry(0, 0, self.width(), self.height())
        label.setAlignment(Qt.AlignCenter)

    def set_exit_button_position(self):
        # Bildschirmgröße abfragen
        screen_size = QApplication.primaryScreen().size()

        # Buttongröße abfragen
        button_size = self.btn_exit.sizeHint()

        # Buttonposition berechnen
        button_x = (screen_size.width() - button_size.width()) / 2
        button_y = (screen_size.height() - button_size.height()) / 2

        # Buttonposition setzen
        self.btn_exit.move(button_x, button_y)

    def keyPressEvent(self, event):
        # ESC-Taste wurde gedrückt
        if event.key() == Qt.Key_Escape:
            self.btn_exit.setVisible(not self.btn_exit.isVisible())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
