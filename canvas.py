from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from shape import Shape
import random

UP,DOWN,RIGHT,LEFT,BIG,SMALL = list(range(6))
PINK,BLACK,PURPLE,OTHER = list(range(4))

class Canvas(QWidget):
    def __init__(self,*args,**kwargs):
        super(Canvas,self).__init__(*args,**kwargs)
        self._painter = QPainter()
        self.prevPoint = QPointF()
        self.selectedShape = None
        self.shapes = []
        self.targetShapes = []

        self.setMouseTracking(True)
        self.color = QColor(Qt.black)

    def newGame(self):
        print("newGame")
        self.targetShapes = []
        self.shapes = []
        self.generateRandomShapes()
        self.randomMoveShapes()
        self.generateShapesByTargetShapes()
        self.repaint()

    def generateRandomShapes(self):
        num = random.randint(8,12)
        for i in range(0,num):
            shapeType = random.randint(0,5)
            shape = Shape()
            shape.setShape(shapeType)
            self.targetShapes.append(shape)

    def randomMoveShapes(self):
        for shape in self.targetShapes:
            shapeType = shape.getShapeType()
            if shapeType == UP or shapeType == DOWN:
                shape.moveBy(QPointF(random.randint(0,2)*50,random.randint(0,3)*50))
            elif shapeType == LEFT or shapeType == RIGHT:
                shape.moveBy(QPointF(random.randint(0,3)*50,random.randint(0,2)*50))
            elif shapeType == BIG or shapeType == SMALL:
                shape.moveBy(QPointF(random.randint(0,2)*50,random.randint(0,2)*50))

    def generateShapesByTargetShapes(self):
        i=0
        j=0
        for shape in self.targetShapes:
            i = i+1
            newShape = Shape()
            newShape.setShape(shape.getShapeType())
            if i==5 or i==9:
                j=j+1
            newShape.moveBy(QPointF(150+(i-4*j)*110,110*j))
            self.shapes.append(newShape)


    def paintEvent(self,event):
        p = self._painter
        p.begin(self)
        #for shape in self.shapes:
        #    shape.paint(p)
        pen = QPen()
        pen.setWidth(0)
        pen.setColor(Qt.transparent)
        p.setPen(pen)
        p.setBrush(QBrush(self.color))

        line_path = QPainterPath()
        for shape in self.targetShapes:
            shape.paint(line_path)
        line_path.setFillRule(Qt.OddEvenFill)
        p.drawPath(line_path)

        line_path = QPainterPath()
        for shape in self.shapes:
            shape.paint(line_path)
        line_path.setFillRule(Qt.OddEvenFill)
        p.drawPath(line_path)
        p.end()

    def mousePressEvent(self, ev):
        if ev.button() == Qt.LeftButton:
            self.selectShapePoint(ev.pos())
            self.prevPoint = ev.pos()
    def mouseMoveEvent(self, ev):
        pos = ev.pos()
        self.parent().statusBar().showMessage(
            'X: %d; Y: %d' % (pos.x(), pos.y()))
        if Qt.LeftButton & ev.buttons():
            if self.selectedShape:
                self.moveShape(self.selectedShape,pos)
                self.repaint()

    def mouseReleaseEvent(self, ev):
        if ev.button() == Qt.LeftButton:
            if self.selectedShape:
                self.deSelectShape()
    def moveShape(self,shape,pos):
        dp = pos - self.prevPoint
        if dp:
            shape.moveBy(dp)
            self.prevPoint = pos
            return True
    def selectShapePoint(self,pos):
        for shape in self.shapes:
            if shape.containsPoint(pos):
                self.selectShape(shape)

    def selectShape(self, shape):
        self.deSelectShape()
        shape.selected = True
        self.selectedShape = shape

    def deSelectShape(self):
        if self.selectedShape:
            self.selectedShape.selected = False
            self.selectedShape = None

    def addTri(self,direction):
        if direction == UP:
            shape = Shape()
            shape.addPoint(QPointF(50,0))
            shape.addPoint(QPointF(0,50))
            shape.addPoint(QPointF(100,50))
            shape.moveBy(QPointF(0,0))
            shape.close()
            self.shapes.append(shape)

        elif direction == DOWN:
            shape = Shape()
            shape.addPoint(QPointF(0,0))
            shape.addPoint(QPointF(50,50))
            shape.addPoint(QPointF(100,0))
            shape.moveBy(QPointF(0,0))
            shape.close()
            self.shapes.append(shape)

        elif direction == LEFT:
            shape = Shape()
            shape.addPoint(QPointF(50,0))
            shape.addPoint(QPointF(0,50))
            shape.addPoint(QPointF(50,100))
            shape.moveBy(QPointF(0,0))
            shape.close()
            self.shapes.append(shape)

        elif direction == RIGHT:
            shape = Shape()
            shape.addPoint(QPointF(0,0))
            shape.addPoint(QPointF(50,50))
            shape.addPoint(QPointF(0,100))
            shape.moveBy(QPointF(0,0))
            shape.close()
            self.shapes.append(shape)
        self.repaint()
    def addSquare(self,size):
        #square
        shape = Shape()
        if size == SMALL:
            shape.addPoint(QPointF(50, 0))
            shape.addPoint(QPointF(100, 50))
            shape.addPoint(QPointF(50, 100))
            shape.addPoint(QPointF(0, 50))
        elif size == BIG:
            shape.addPoint(QPointF(0, 0))
            shape.addPoint(QPointF(0, 100))
            shape.addPoint(QPointF(100, 100))
            shape.addPoint(QPointF(100, 0))
        shape.close()
        self.shapes.append(shape)
        self.repaint()


    def changeColor(self,color,choosedColor):
        if color == BLACK:
            self.color.setNamedColor("#000000")
        elif color == PINK:
            self.color.setNamedColor("#FFAEB9")
        elif color == PURPLE:
            self.color.setNamedColor("#9F79EE")
        elif color == OTHER:
            self.color = choosedColor
        self.repaint()



