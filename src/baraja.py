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
    self.llenar_tabla()
    self.cartas={}
    self.cartas={1:"as de espadas",2:'2 de espadas',3:'3 de espadas',
                 4:'4 de espadas',5:'5 de espadas',6:'6 de espadas',
                 7:'7 de espadas',8:'8 de espadas',9:'9 de espadas',
                 12:'q de espadas',11:'j de espadas',10:'10 de espadas',
                 13:'k de espadas',
                 14:'as de diamantes',15:'2 de diamantes',16:'3 de diamantes',
                 17:'4 de diamantes',18:'5 de diamantes',19:'6 de diamantes',
                 20:"7 de diamantes",21:'8 de diamantes',22:'9 de diamantes',
                 23:'10 de diamantes',24:'j de diamantes',25:'q de diamantes',
                 26:'k de diamantes',27:'as de corazones',28:'2 de corazones',
                29:'3 de corazones', 30:'4 de corazones',31:'5 de corazones',
                 32:"6 de corazones",33:'7 de corazones',34:'8 de corazones',
                35:'9 de corazones', 36:'10 de corazones',37:'j de corazones',
                 38:'q de corazones',39:'k de corazones',40:'as de treboles',
                41:'2  de treboles', 42:'3 de treboles',43:'4 de treboles',
                 44:"5 de treboles",45:'6 de treboles',46:'7 de treboles',
               47:'8 de treboles', 48:'9 de treboles', 49:'10 de treboles',
                 50:'j de treboles',51:'q de treboles',52:'k de treboles',
                 53:'joker 1',54:'joker 2'}
    self.pbgenerar.clicked.connect(self.generar_numero)
    
  def intervalos(self):
    for i in range(1,55):
      self.asignacion.append(i)
      #qw=QTableWidgetItem(str(i))
      #self.twclasificacion.setItem((i-1),2,qw)
    for j in self.asignacion:
      self.lsuperior.append((1.0/54)*j)
      #qw=QTableWidgetItem(str((1.0/54)*j))
      #self.twclasificacion.setItem((j-1),1,qw)
    for k in range(1,54):
      self.linferior.append(self.lsuperior[k-1]+.001)
      #qw=QTableWidgetItem(str(self.lsuperior[k-1]+.001))
      #self.twclasificacion.setItem(k,0,qw)
    
  def llenar_tabla(self):
    cont=0
    cao=1/54.
    for i in self.cartas.keys():
      qin=QTableWidgetItem(str(cont*cao))
      self.twclasificacion.setItem(i,0,qin)
    
  def generar_numero(self):
    numero=random.random()
    i=0
    while True:
      if numero>self.linferior[i] and numero<self.lsuperior[i]:
        
        self.ltexto.setText(''+ self.cartas[i+1]+'='+str(numero))
        break
      else:
        i+=1
x=QApplication(sys.argv)
y=ventanaFormi1()
y.show()
x.exec_()
