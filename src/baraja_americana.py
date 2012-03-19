'''
Created on 07/03/2012

@author: piter
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.baraja import Ui_Fbaraja
import sys
import random

class ventanaFormi1(QWidget,Ui_Fbaraja):
  def __init__(self):
    QWidget.__init__(self)
    self.setupUi(self)
    self.twclasificacion.setRowCount(54)
    self.twclasificacion.setColumnCount(3)
    columnas=('limite inferior','limite superior','carta')
    self.twclasificacion.setHorizontalHeaderLabels(columnas)
    self.linferior=[0]
    self.lsuperior=[]
    self.asignacion=[]
    self.intervalos()
    self.cartas={}
    self.cartas={1:"as de espadas",2:'2 de espadas',3:'3 de espadas',
                 4:'4 de espadas',5:'5 de espadas',6:'6 de espadas',
                 7:'7 de espadas',8:'2 de espadas',9:'2 de espadas',
                 12:'2 de espadas',11:'2 de espadas',10:'2 de espadas',
                 11:'2 de espadas',12:'2 de espadas',13:'2 de espadas',
                 14:'2 de espadas',15:'2 de espadas',16:'2 de espadas',
                 17:'2 de espadas',18:'2 de espadas',19:'2 de espadas',
                 20:"as de espadas",21:'2 de espadas',22:'3 de espadas',
                 25:'4 de espadas',24:'5 de espadas',23:'6 de espadas',
                 26:'7 de espadas',27:'2 de espadas',28:'2 de espadas',
                 31:'2 de espadas',30:'2 de espadas',29:'2 de espadas',
                 32:"as de espadas",33:'2 de espadas',34:'3 de espadas',
                 37:'4 de espadas',36:'5 de espadas',35:'6 de espadas',
                 38:'7 de espadas',39:'2 de espadas',40:'2 de espadas',
                 43:'2 de espadas',42:'2 de espadas',41:'2 de espadas',
                 44:"as de espadas",45:'2 de espadas',46:'3 de espadas',
                 49:'4 de espadas',47:'5 de espadas',47:'6 de espadas',
                 50:'7 de espadas',51:'2 de espadas',52:'2 de espadas',
                 53:'2 de espadas',54:'2 de espadas'}
    self.pbgenerar.clicked.connect(self.generar_numero)
  def intervalos(self):
    for i in range(1,55):
      self.asignacion.append(i)
      qw=QTableWidgetItem(str(i))
      self.twclasificacion.setItem((i-1),2,qw)
      
    for j in self.asignacion:
      self.lsuperior.append((1.0/54)*j)
      qw=QTableWidgetItem(str((1.0/54)*j))
      self.twclasificacion.setItem((j-1),1,qw)
    for k in range(1,54):
      self.linferior.append(self.lsuperior[k-1]+.001)
      qw=QTableWidgetItem(str(self.lsuperior[k-1]+.001))
      self.twclasificacion.setItem(k,0,qw)
  def generar_numero(self):
    numero=random.random()
    i=0
    while numero>self.linferior[i] and numero<self.lsuperior[i]:
      i+=1
          
      self.ltexto.setText(''+ self.cartas[i])
x=QApplication(sys.argv)
y=ventanaFormi1()
y.show()
x.exec_()
