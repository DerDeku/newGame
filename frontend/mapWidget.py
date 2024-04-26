from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys
from backend.map import Map
from backend import room
from frontend.subprocessManager import SubprocessManager

class MapWidget(QWidget):
    def __init__(self, size_x, size_y, backendManager : SubprocessManager):
        super().__init__()
        self.layout = QGridLayout()
        self.layout.setSpacing(0)
        self.setLayout(self.layout)
        self.backendManger = backendManager
        
        # Erstelle ein GridLayout
        
    def clearLayout(self):
        if self.layout is not None:
            while self.layout.count() > 0:
                item = self.layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)  # Entfernen Sie das Widget aus dem Layout, ohne es zu löschen
                else:
                    layout_item = item.layout()
                    if layout_item is not None:
                        self.clearLayout(layout_item)  # Rekursiv das enthaltene Layout leeren
    
    def displayNextStepInMap( self, depth : int):
        self.backendManger.proceedAlgo(depth, 0)
        map = self.backendManger.getMap(depth)
        self.displayMap(map, depth)

    def displayNextMap(self, depth : int):
        map = self.backendManger.getMap(depth)
        self.displayMap(map, depth)

    def displayMap(self, map : Map, depth : int):
        
        self.clearLayout()
        
        for yi, y in enumerate(map.listRooms):
            for xi, x in enumerate(y):
                # Erstelle das Hintergrund-Label (70x70)
                background_label = QLabel(self)
                background_label.setGeometry(50, 50, 70, 70)
                if room.Dir.RIGHT in x.getDoors() and not room.Dir.LEFT in x.getDoors() and not room.Dir.ABOVE in x.getDoors()and not room.Dir.BELOW in x.getDoors():
                    background_pixmap = QPixmap("frontend/map/border/door_right.png")
                elif room.Dir.LEFT in x.getDoors() and not room.Dir.RIGHT in x.getDoors() and not room.Dir.ABOVE in x.getDoors()and not room.Dir.BELOW in x.getDoors():
                    background_pixmap = QPixmap("frontend/map/border/door_left.png")
                elif room.Dir.ABOVE in x.getDoors() and not room.Dir.LEFT in x.getDoors() and not room.Dir.RIGHT in x.getDoors()and not room.Dir.BELOW in x.getDoors():
                    background_pixmap = QPixmap("frontend/map/border/door_above.png")
                elif room.Dir.BELOW in x.getDoors() and not room.Dir.LEFT in x.getDoors() and not room.Dir.ABOVE in x.getDoors()and not room.Dir.RIGHT in x.getDoors():
                    background_pixmap = QPixmap("frontend/map/border/door_below.png")
                elif room.Dir.RIGHT in x.getDoors() and room.Dir.BELOW in x.getDoors() and not room.Dir.ABOVE in x.getDoors()and not room.Dir.LEFT in x.getDoors():
                    background_pixmap = QPixmap("frontend/map/border/door_right_below.png")
                elif room.Dir.RIGHT in x.getDoors() and room.Dir.LEFT in x.getDoors() and not room.Dir.ABOVE in x.getDoors()and not room.Dir.BELOW in x.getDoors():
                    background_pixmap = QPixmap("frontend/map/border/door_right_left.png")
                elif room.Dir.ABOVE in x.getDoors() and room.Dir.BELOW in x.getDoors() and not room.Dir.LEFT in x.getDoors()and not room.Dir.RIGHT in x.getDoors():
                    background_pixmap = QPixmap("frontend/map/border/door_above_below.png")
                elif room.Dir.RIGHT in x.getDoors() and room.Dir.ABOVE in x.getDoors() and not room.Dir.BELOW in x.getDoors()and not room.Dir.LEFT in x.getDoors():
                    background_pixmap = QPixmap("frontend/map/border/door_above_right.png")
                elif room.Dir.LEFT in x.getDoors() and room.Dir.BELOW in x.getDoors() and not room.Dir.ABOVE in x.getDoors()and not room.Dir.RIGHT in x.getDoors():
                    background_pixmap = QPixmap("frontend/map/border/door_below_left.png")
                elif room.Dir.LEFT in x.getDoors() and room.Dir.ABOVE in x.getDoors() and not room.Dir.BELOW in x.getDoors()and not room.Dir.RIGHT in x.getDoors():
                    background_pixmap = QPixmap("frontend/map/border/door_left_above.png")
                elif room.Dir.LEFT in x.getDoors() and room.Dir.BELOW in x.getDoors() and room.Dir.ABOVE in x.getDoors():
                    background_pixmap = QPixmap("frontend/map/border/door_below_left_above.png")
                elif room.Dir.RIGHT in x.getDoors() and room.Dir.BELOW in x.getDoors() and room.Dir.ABOVE in x.getDoors():
                    background_pixmap = QPixmap("frontend/map/border/door_above_right_below.png")
                elif room.Dir.LEFT in x.getDoors() and room.Dir.BELOW in x.getDoors() and room.Dir.RIGHT in x.getDoors():
                    background_pixmap = QPixmap("frontend/map/border/door_right_below_left.png")
                elif room.Dir.LEFT in x.getDoors() and room.Dir.RIGHT in x.getDoors() and room.Dir.ABOVE in x.getDoors():
                    background_pixmap = QPixmap("frontend/map/border/door_left_above_right.png")
                else:
                    background_pixmap = QPixmap("frontend/map/border/no_doors.png")
                background_label.setPixmap(background_pixmap)
                self.layout.addWidget(background_label, yi, xi)
                
                # Erstelle das Vordergrund-Label (50x50)
                foreground_label = QLabel(self)
                foreground_label.setGeometry(0, 0, 50, 50)  # Position auf (0, 0) gesetzt, wird später angepasst
                if x.getType() == room.RoomType.ENTRANCE:
                    foreground_pixmap = QPixmap("frontend/map/rooms/entrance.png")
                elif x.getType() == room.RoomType.EXIT:
                    foreground_pixmap = QPixmap("frontend/map/rooms/exit.png")
                else:
                    foreground_pixmap = QPixmap("frontend/map/rooms/empty.png")
                foreground_label.setPixmap(foreground_pixmap)
                foreground_label.setAlignment(Qt.AlignCenter)  # Zentriere das Bild im Label
                self.layout.addWidget(foreground_label, yi, xi)  # Platzierung des Vordergrund-Labels
                
                # Berechne die Position des Vordergrund-Labels, um es in die Mitte des Hintergrund-Labels zu setzen
                foreground_x = (background_label.width() - foreground_label.width()) / 2
                foreground_y = (background_label.height() - foreground_label.height()) / 2
                foreground_label.move(foreground_x, foreground_y)
        # Setze das GridLayout als Layout für das Widget
        self.setLayout(self.layout)