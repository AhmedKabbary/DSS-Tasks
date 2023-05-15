import sys

from algorithms.methods import maximax, maximin, minimax_regret, equally_likely

from PySide6.QtCore import *
from PySide6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Decision making methods")
        self.setMinimumSize(400, 300)

        self.root_widget = QWidget()
        self.root_layout = QVBoxLayout()
        self.root_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        #

        self.h1_widget = QWidget()
        self.h1_layout = QHBoxLayout()
        self.h1_widget.setLayout(self.h1_layout)

        self.txt_projects = QLineEdit(self)
        self.txt_projects.setPlaceholderText("Projects")
        self.h1_layout.addWidget(self.txt_projects)

        self.txt_conditions = QLineEdit(self)
        self.txt_conditions.setPlaceholderText("Conditions")
        self.h1_layout.addWidget(self.txt_conditions)

        self.root_layout.addWidget(self.h1_widget)

        #

        self.btn_setTable = QPushButton("Set table")
        self.btn_setTable.clicked.connect(self.set_table_clicked)
        self.root_layout.addWidget(self.btn_setTable)

        #

        self.table = QTableWidget()
        self.root_layout.addWidget(self.table)

        #

        self.h2_widget = QWidget()
        self.h2_layout = QHBoxLayout()
        self.h2_widget.setLayout(self.h2_layout)

        self.comboBox = QComboBox(self)
        self.comboBox.addItems(
            ["maximax", "maximin", "minimax regret", "equally likely"])
        self.h2_layout.addWidget(self.comboBox)

        self.btn_calculate = QPushButton("Calculate")
        self.btn_calculate.clicked.connect(self.calculate_clicked)
        self.h2_layout.addWidget(self.btn_calculate)

        self.lbl_result = QLabel(self)
        self.h2_layout.addWidget(self.lbl_result)

        self.root_layout.addWidget(self.h2_widget)

        #

        self.root_widget.setLayout(self.root_layout)
        self.setCentralWidget(self.root_widget)

    def set_table_clicked(self):
        try:
            self.rows = int(self.txt_projects.text())
            self.columns = int(self.txt_conditions.text())

            self.table.setRowCount(self.rows)
            self.table.setColumnCount(self.columns)

            c_labels = [f"Condition {i+1}" for i in range(self.columns)]
            self.table.setHorizontalHeaderLabels(c_labels)
            r_labels = [f"Project {i+1}" for i in range(self.rows)]
            self.table.setVerticalHeaderLabels(r_labels)
        except:
            pass

    def calculate_clicked(self):
        method = self.comboBox.currentText()

        matrix = []
        for r in range(self.rows):
            values = []
            for c in range(self.columns):
                num = int(self.table.item(r, c).text())
                values.append(num)
            matrix.append(values)

        if method == "maximax":
            value = maximax(self.rows, self.columns, matrix)
            self.lbl_result.setText(value)

        elif method == "maximin":
            value = maximin(self.rows, self.columns, matrix)
            self.lbl_result.setText(value)

        elif method == "minimax regret":
            value = minimax_regret(self.rows, self.columns, matrix)
            self.lbl_result.setText(value)

        elif method == "equally likely":
            value = equally_likely(self.rows, self.columns, matrix)
            self.lbl_result.setText(value)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
