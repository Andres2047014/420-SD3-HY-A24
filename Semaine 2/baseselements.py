import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QLabel, QStatusBar, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QAction, QKeySequence, QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.label = QLabel()

        barre_menus = self.menuBar()
        self.creer_menus(barre_menus)

        self.barre_statut = QStatusBar(self)
        self.setStatusBar(self.barre_statut)

        bouton_test = QPushButton("Test")
        bouton_test.pressed.connect(self.action_menu1)

        barre_outils = QToolBar("Barre d'outils")
        barre_outils.setIconSize(QSize(16, 16))
        barre_outils.addWidget(bouton_test)
        self.addToolBar(barre_outils)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        #layout.addWidget(self.bouton_changer)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)



    def creer_menus(self, barre_menus):
        menu1 = barre_menus.addMenu("&Menu1")
        action = QAction(text="Menu1", parent=self)
        action.setStatusTip("Menu1")
        action.triggered.connect(self.action_menu1)
        menu1.addAction(action)

        menu2 = barre_menus.addMenu("&Menu2")
        action2 = QAction(text="Menu2", parent=self)
        action2.setStatusTip("Menu2")
        action2.triggered.connect(self.action_menu2)
        menu2.addAction(action2)




    def action_menu1(self):
        print("test")
        self.barre_statut.setStatusTip("click!!!!!!!")

    def action_menu2(self):
        print("test")
        self.barre_statut.setStatusTip("click!!!!!!!")





app = QApplication(sys.argv)
f = MainWindow()
f.show()
app.exec()


