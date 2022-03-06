import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QFormLayout,
    QLineEdit,
    QDialog,
    QDialogButtonBox,
    QFileDialog
)

from photo import Timestamp


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()

        lbl_location = QLabel("Folder:")
        self.txt_location = QLineEdit()
        btn_location = QPushButton("Location")
        btn_location.clicked.connect(self.show_dialog_location)
        layout1.addWidget(lbl_location)
        layout1.addWidget(self.txt_location)
        layout1.addWidget(btn_location)

        layout.addLayout(layout1)


        lbl_save = QLabel("Folder:")
        self.txt_save = QLineEdit()
        btn_save = QPushButton("Save")
        btn_save.clicked.connect(self.show_dialog_location2)
        layout2.addWidget(lbl_save)
        layout2.addWidget(self.txt_save)
        layout2.addWidget(btn_save)

        layout.addLayout(layout2)

        # Add widgets to the layout
       
        self.button = QPushButton("Proceed")
        self.button.clicked.connect(self.put_timestamp)
        layout.addWidget(self.button)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def show_dialog_location(self, s):
        print("Click", s)

        result = str(QFileDialog.getExistingDirectory())
        print(result)
        self.txt_location.setText(result)

    def show_dialog_location2(self, s):
        print("Click", s)
        
        result = str(QFileDialog.getExistingDirectory())
        print(result)
        self.txt_save.setText(result)

    def put_timestamp(self,s):
        collection_photos = Timestamp(self.txt_location.text(), self.txt_save.text())
        qty_photos = collection_photos.place_timestamp()
        print(f"Timestamp placed in {qty_photos} photos.")
        dlg = CustomDialog(qty_photos)
        if dlg.exec_():
            print("Success!")
        else:
            print("Cancel!")



class CustomDialog(QDialog):
    def __init__(self, number_photos):
        super().__init__()
        self.setWindowTitle("Summary")
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel(f"Timestamp placed in {number_photos} files.")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


      

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())