
from PySide6.QtWidgets import *
from .mapWidget import MapWidget
from .uiMainWindow import Ui_MainWindow
from . import subprocessManager

def main(): 
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mapDepth = -1
        backendUtility = subprocessManager.SubprocessManager()
        backendUtility.startBackend()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout(self.central_widget)
        
        # Erstellen und Hinzufügen des MapWidgets zum zentralen Widget
        self.mapWidget = MapWidget(5, 5, backendUtility)
        self.central_widget.setLayout(self.grid_layout)
        self.grid_layout.addWidget(self.mapWidget, 1, 1)
        
        # Hinzufügen des Spacers und des Buttons zum zentralen Layout
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.horizontalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.grid_layout.addItem(self.verticalSpacer, 0, 0)
        self.grid_layout.addItem(self.verticalSpacer, 1, 0)
        self.grid_layout.addItem(self.verticalSpacer, 1, 2)
        self.grid_layout.addItem(self.verticalSpacer, 2, 2)
        self.button = QPushButton("next Map")
        self.grid_layout.addWidget(self.button, 2, 1)
        self.button.clicked.connect(self.buttonNextMap)
        self.button = QPushButton("next step")
        self.grid_layout.addWidget(self.button, 2, 3)
        self.button.clicked.connect(self.buttonNextStage)

    def buttonNextMap(self):
        self.mapDepth+= 1
        if self.mapDepth < 30:
            self.mapWidget.displayNextMap(self.mapDepth)
        else:
            self.mapDepth = 0
        

    def buttonNextStage(self):
        if self.mapDepth < 30:
            self.mapWidget.displayNextStepInMap(self.mapDepth)
            
        else: 
            print("ERROR: index mapDepth > depth available")
        

if __name__ == "__main__":
    main()
    
