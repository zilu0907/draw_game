from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from canvas import Canvas
from canvas import UP,DOWN,RIGHT,LEFT,BIG,SMALL,BLACK,PINK,PURPLE,OTHER
from functools import partial
import sys

__appname__ = 'draw'

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.width = 800
        self.height = 500
        self.setGeometry(0,0,self.width,self.height)
        self.canvas = Canvas(self)

        self.setCentralWidget(self.canvas)

        self.center()

        self.statusBar().showMessage("ready")

        newGame = QAction(self)
        newGame.setText('New Game')
        newGame.triggered.connect(self.canvas.newGame)

        exit = QAction(self)
        exit.setText('Exit')
        exit.triggered.connect(qApp.quit)

        addUpTri = QAction('up tri',self)
        addUpTri.triggered.connect(self.addUpTriEvent)

        addDownTri = QAction('down tri', self)
        addDownTri.triggered.connect(partial(self.canvas.addTri, DOWN))

        addLeftTri = QAction('left tri', self)
        addLeftTri.triggered.connect(partial(self.canvas.addTri, LEFT))

        addRightTri = QAction('right tri', self)
        addRightTri.triggered.connect(partial(self.canvas.addTri, RIGHT))

        addSmallSquare = QAction('small square',self)
        addSmallSquare.triggered.connect(partial(self.canvas.addSquare,SMALL))

        addBigSquare = QAction('big square',self)
        addBigSquare.triggered.connect(partial(self.canvas.addSquare,BIG))

        toolBar = QAction('tool bar',self,checkable = True)
        toolBar.setChecked(True)
        toolBar.triggered.connect(self.toolBar)

        black = QAction('black',self)
        black.triggered.connect(partial(self.canvas.changeColor,BLACK))

        pink = QAction('pink',self)
        pink.triggered.connect(partial(self.canvas.changeColor,PINK))

        purple = QAction('purple', self)
        purple.triggered.connect(partial(self.canvas.changeColor, PURPLE))

        otherColor = QAction('other',self)
        otherColor.triggered.connect(self.changeColor)

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(newGame)
        fileMenu.addAction(exit)

        addMenu = menubar.addMenu('Add')
        triMenu = QMenu('tri',self)
        triMenu.addAction(addUpTri)
        triMenu.addAction(addDownTri)
        triMenu.addAction(addLeftTri)
        triMenu.addAction(addRightTri)
        addMenu.addMenu(triMenu)
        squareMenu = QMenu('square',self)
        squareMenu.addAction(addSmallSquare)
        squareMenu.addAction(addBigSquare)
        addMenu.addMenu(squareMenu)

        viewMenu = menubar.addMenu('View')
        viewMenu.addAction(toolBar)
        colorMenu = QMenu('color',self)
        colorMenu.addAction(black)
        colorMenu.addAction(pink)
        colorMenu.addAction(purple)
        colorMenu.addAction(otherColor)
        viewMenu.addMenu(colorMenu)



        self.toolbar = self.addToolBar('add')
        self.toolbar.addAction(newGame)
        self.toolbar.addAction(addUpTri)
        self.toolbar.addAction(addDownTri)
        self.toolbar.addAction(addLeftTri)
        self.toolbar.addAction(addRightTri)
        self.toolbar.addAction(addSmallSquare)
        self.toolbar.addAction(addBigSquare)
        self.toolbar.addAction(exit)

        self.setWindowTitle('Draw')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def addUpTriEvent(self):
        self.canvas.addTri(UP)

    def toolBar(self,status):
        if status:
            self.toolbar.show()
        else:
            self.toolbar.hide()

    def changeColor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.canvas.changeColor(OTHER,col)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
