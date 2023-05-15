import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from model import GenderPredictor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gender Detection")
        self.setMinimumSize(400, 450)

        self.gender_predictor = GenderPredictor()

        self.v_box = QVBoxLayout()

        title = QLabel(self)
        title.setText("Gender Detection")
        title.setFont(QFont("Arial", 20))
        title.setFixedHeight(50)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.v_box.addWidget(title)

        placeholders = ["hair length", "forehead width", "forehead height",
                        "nose width", "nose length", "lips thin", "nose to lip length"]
        for i in range(7):
            textBox = QLineEdit(self)
            textBox.setPlaceholderText(f"Enter {placeholders[i]} in cm")
            textBox.setFixedHeight(35)
            self.v_box.addWidget(textBox)

        self.lbl_accuracy = QLabel(self)
        self.lbl_accuracy.setText("Accuracy: ~97%")
        self.lbl_accuracy.setFixedHeight(20)

        self.lbl_gender = QLabel(self)
        self.lbl_gender.setText("Gender:")
        self.lbl_gender.setFixedHeight(20)

        self.h_box = QHBoxLayout()
        self.h_box.addWidget(self.lbl_accuracy)
        self.h_box.addWidget(self.lbl_gender)
        self.h_widget = QWidget()
        self.h_widget.setLayout(self.h_box)
        self.h_widget.setFixedHeight(40)
        self.v_box.addWidget(self.h_widget)

        self.btn_predict = QPushButton("Predict")
        self.btn_predict.setFixedSize(60, 30)
        self.btn_predict.clicked.connect(self.predict_clicked)
        self.v_box.addWidget(
            self.btn_predict, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.widget = QWidget()
        self.widget.setLayout(self.v_box)
        self.setCentralWidget(self.widget)

    def predict_clicked(self):
        try:
            info = [float(self.v_box.itemAt(i).widget().text())
                    for i in range(1, 8)]
            gender = self.gender_predictor.predict(info)
            self.lbl_gender.setText(f"Gender: {gender}")
        except:
            self.lbl_gender.setText(f"Gender: Invalid input")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
