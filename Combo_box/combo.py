import PyQt5.QtWidgets as qtw 
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #Add title
        self.setWindowTitle("combo_box ")

        #set Vertical layout
        self.setLayout(qtw.QVBoxLayout())
 
        #Create A lable 
        my_label =qtw.QLabel("Pick something from the list Below");
        #change the font size of lable :
        my_label.setFont(qtg.QFont('Helvetica',24))
        self.layout().addWidget(my_label)

        #Create an combo  box:
        my_combo=qtw.QComboBox(self,
            editable=True,
            insertPolicy= qtw.QComboBox.InsertAtBottom)
        #ADD items to the combo box:
        my_combo.addItem("Pepperoni","something")
        my_combo.addItem("Cheese",2)
        my_combo.addItem("Mushrooms",qtw.QWidget)
        my_combo.addItem("Peppers")
        my_combo.addItems(["one","Two","Three"])
        my_combo.insertItems(2,["one","two","Third thing"])
        #Put combo box on screen :
        self.layout().addWidget(my_combo)

    

        # Create a Button 
        my_button= qtw.QPushButton("Press Me!",
            clicked = lambda: press_it())
            #A Lambda Function in Python programming is an anonymous function or a function having no name
        self.layout().addWidget(my_button)


        #show the app
        self.show();

        def press_it():
            #add name to lable: 
            my_label.setText(f'You Picked {my_combo.currentData()}')
            # my_label.setText(f'You Picked {my_combo.currentText()}')
            # my_label.setText(f'You Picked {my_combo.currentIndex()}')
            

app = qtw.QApplication([])
mw = MainWindow()


#run the app
app.exec_()

#Self notes:
#to change the size of the lable is a part og Gui : QtGui