from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
import math

cls, wnd = uic.loadUiType('calkulator.ui')

class Nasza (wnd, cls):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.eq=False
        self.ans=''
    #definiowanie sposobów wstawiania po kliknięciu przycisków
    def click_number(self,argument):
        if self.eq==False:
            current=self.lnmain.text()
            self.lnmain.setText(current+argument)
        else:
            self.lnmain.setText(argument)
        self.eq=False
        
    def click_function(self,argument):
        if self.eq==False:
            current=self.lnmain.text()
            if (current[-1]).isdigit():
                self.lnmain.setText(current+'*'+argument)
            else:
                self.lnmain.setText(current+argument)
        else:
            self.lnmain.setText(argument)
        self.eq=False
        
    def click_symbol(self,argument):
        current=self.lnmain.text()
        self.lnmain.setText(current+argument)
        
    #wstawianie numerów       
    def on_pb1_released(self):
        '''current=self.lnmain.text()
        self.lnmain.setText(current+'1')'''
        self.click_number('1')
    def on_pb2_released(self):
        self.click_number('2')
    def on_pb3_released(self):
        self.click_number('3')
    def on_pb4_released(self):
        self.click_number('4')
    def on_pb5_released(self):
        self.click_number('5')
    def on_pb6_released(self):
        self.click_number('6')
    def on_pb7_released(self):
        self.click_number('7')
    def on_pb8_released(self):
        self.click_number('8')
    def on_pb9_released(self):
        self.click_number('9')
    def on_pb0_released(self):
        self.click_number('0')
            
    def on_pbdot_released(self):
        self.click_number('.')
    #wstawianie funkcji    
    def on_pbopenbrac_released(self):
        self.click_function('(')
    def on_pbclosebrac_released(self):
        self.click_number(')')  
    def on_pbsqrt_released(self):
        self.click_function('sqrt(') 
    def on_pbln_released(self):
        self.click_function('ln(')

    def on_pbans_released(self):
        if self.ans!='':
            self.click_function('Ans') 
    #wstawianie symboli       
    def on_pbplus_released(self):
        self.click_symbol('+')
    def on_pbminus_released(self):
        self.click_symbol('-')
    def on_pbmult_released(self):
        self.click_symbol('*')
    def on_pbdiv_released(self):
        self.click_symbol('/')
    def on_pbpower_released(self):
        self.click_symbol('^')
      
    #inne    
    def on_pbdel_released(self):
        current=self.lnmain.text()
        self.lnmain.setText(current[0:-1])       
    def on_pbac_released(self):
        self.lnmain.setText('')
        
        
    #liczenie wyniku
        
    def on_pbeq_released(self):
        change=[['^', '**'],['sqrt(', 'math.sqrt('],['ln(', 'math.log('],['Ans', self.ans] ]
        self.equation=self.lnmain.text()
        for char in change:
            self.equation=(char[1]).join(((self.equation).split(char[0])))
            
        try:
            eval(self.equation)
        except:
            self.lnmain.setText('ERROR')
        else:
            self.ans=str(eval(self.equation))
            self.lnmain.setText(self.ans)
        self.eq=True
        
a = QApplication([])

o = Nasza()
o.show()

a.exec()
