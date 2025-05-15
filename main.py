from regression import regress_price
from  PyQt5 import QtWidgets 
from PyQt5.QtGui import  QPixmap
import sys
from pyqttoast import Toast, ToastPreset , ToastPosition
from PyQt5.QtCore import Qt

#===============================================
def notification(title , text , state):
    toast = Toast(window)
    toast.setDuration(5000)  # Hide after 5 seconds
    toast.setTitle(title)
    toast.setText(text)
    toast.applyPreset(state)  # Apply style preset
    Toast.setPosition(ToastPosition.TOP_MIDDLE)
    toast.show()
def getSurface():

    surface = text_input.toPlainText()
    try:
        price = regress_price(surface)
        if float(surface) < 0 :
            notification('ERROR','Surface Not Valid' ,ToastPreset.ERROR ) 
            return  
        notification('SUCCESS',f'PRICE = {price} $' ,ToastPreset.SUCCESS )
    except Exception as e:
        notification('ERROR',f'{e}' ,ToastPreset.ERROR )        
screen = 5200
app = QtWidgets.QApplication(sys.argv) 
window = QtWidgets.QMainWindow()
window.resize(1200, screen)  # Increase the window size to accommodate all elemen
window.setStyleSheet('background : #34495e')
window.setWindowTitle("Price Home Prediction")
title = QtWidgets.QLabel("Price House Prediction ", window)
title.resize(300 , 50)
title.move(670 , 20)
title.setStyleSheet('color : white ; font-size : 30px')
p = QtWidgets.QLabel(window)
photo = QPixmap('house.jpg')
p.setPixmap(photo)
p.resize(9000 , 500)
p.move(670 , 60)
label = QtWidgets.QLabel("Enter Surface : ", window)
label.resize(200 , 50)
label.move(670 , 550)
label.setStyleSheet('color : white ; font-size : 20px')
text_input = QtWidgets.QPlainTextEdit(window)
text_input.setStyleSheet('background : white ; border-radius : 4px  ; padding-top : 8px ; font-size : 20px')
text_input.move(670 , 600)
text_input.resize(340 , 55)
calc = QtWidgets.QPushButton('Calc', window)
calc.move(670 + 350 , 600)
calc.resize(150 , 55)
calc.setStyleSheet('color : white ; background-color : green ; font-size: 20px ; border-radius : 4px ')
calc.clicked.connect(getSurface)
window.show()
app.exec_()