from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
UP,DOWN,RIGHT,LEFT,BIG,SMALL,NULL = list(range(7))
class Shape(object):
    def __init__(self):
        self.points = []
        self._closed = False
        self.selected = False
        self.shapeType = NULL

    def isClosed(self):
        return self._closed

    def addPoint(self,point):
        self.points.append(point)

    def popPoint(self):
        if self.points:
            return self.points.pop()
        return None

    def paint(self,line_path):
        if self.points:

            line_path.moveTo(self.points[0])

            for i, p in enumerate(self.points):
                line_path.lineTo(p)

            if self.isClosed():
                line_path.lineTo(self.points[0])

    def containsPoint(self,point):
        return self.makePath().contains(point)

    def makePath(self):
        path = QPainterPath(self.points[0])
        for p in self.points[1:]:
            path.lineTo(p)
        return path

    def moveBy(self,offset):
            self.points = [p + offset for p in self.points]

    def isClosed(self):
        return self._closed

    def close(self):
        self._closed = True

    def open(self):
        self._closed = False

    def setShape(self,shapeType):
        self.shapeType = shapeType
        if shapeType == UP:
            self.addPoint(QPointF(50, 0))
            self.addPoint(QPointF(0, 50))
            self.addPoint(QPointF(100, 50))
            self.close()
        elif shapeType == DOWN:
            self.addPoint(QPointF(0, 50))
            self.addPoint(QPointF(100, 50))
            self.addPoint(QPointF(50, 100))
            self.close()
        elif shapeType == LEFT:
            self.addPoint(QPointF(0, 50))
            self.addPoint(QPointF(50, 0))
            self.addPoint(QPointF(50, 100))
            self.close()
        elif shapeType == RIGHT:
            self.addPoint(QPointF(0, 0))
            self.addPoint(QPointF(50, 50))
            self.addPoint(QPointF(0, 100))
            self.close()
        elif shapeType == SMALL:
            self.addPoint(QPointF(50, 0))
            self.addPoint(QPointF(100, 50))
            self.addPoint(QPointF(50, 100))
            self.addPoint(QPointF(0, 50))
            self.close()
        elif shapeType == BIG:
            self.addPoint(QPointF(0, 0))
            self.addPoint(QPointF(100, 0))
            self.addPoint(QPointF(100, 100))
            self.addPoint(QPointF(0, 100))
            self.close()

    def getShapeType(self):
        return self.shapeType

        
    def __len__(self):
        return len(self.points)
