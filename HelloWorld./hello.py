import PyQt5.QtWidgets as qtw 
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #Add title
        self.setWindowTitle("Hello World !! ")

        #set Vertical layout
        self.setLayout(qtw.QVBoxLayout())
 
        #Create A lable 
        my_label =qtw.QLabel("Hello World! What's your Name ? ");
        #change the font size of lable :
        my_label.setFont(qtg.QFont('Helvetica',18))
        self.layout().addWidget(my_label)

        #Create an Entry box:
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        # Create a Button 
        my_button= qtw.QPushButton("Press Me!",
            clicked = lambda: press_it())
            #A Lambda Function in Python programming is an anonymous function or a function having no name
        self.layout().addWidget(my_button)

        #show the app
        self.show();

        def press_it():
            #add name to lable: 
            my_label.setText(f'Hello {my_entry.text()} !')
            #clear the entry box
            my_entry.setText("")

app = qtw.QApplication([])
mw = MainWindow()


#run the app
app.exec_()

#Self notes:
#to change the size of the lable is a part og Gui : QtGui