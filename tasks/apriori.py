import sys

from algorithms.apriori import AprioriAlgorithm

from PySide6.QtCore import *
from PySide6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Apriori algorithm")
        self.setMinimumSize(400, 300)

        self.root_widget = QWidget()
        self.root_layout = QVBoxLayout()
        self.root_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        #

        self.h1_widget = QWidget()
        self.h1_layout = QHBoxLayout()
        self.h1_widget.setLayout(self.h1_layout)

        self.txt_rows = QLineEdit(self)
        self.txt_rows.setPlaceholderText("Rows")
        self.h1_layout.addWidget(self.txt_rows)

        self.btn_setTable = QPushButton("Set")
        self.btn_setTable.clicked.connect(self.set_table_clicked)
        self.h1_layout.addWidget(self.btn_setTable)

        self.root_layout.addWidget(self.h1_widget)

        #

        self.table = QTableWidget()
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(['Items'])
        self.root_layout.addWidget(self.table)

        #

        self.txt_min_sup = QLineEdit(self)
        self.txt_min_sup.setPlaceholderText("Minimum supply")
        self.root_layout.addWidget(self.txt_min_sup)

        #

        self.btn_calculate = QPushButton("Calculate")
        self.btn_calculate.clicked.connect(self.calculate_clicked)
        self.root_layout.addWidget(self.btn_calculate)

        self.lbl_result = QLabel(self)
        self.root_layout.addWidget(self.lbl_result)

        #

        self.root_widget.setLayout(self.root_layout)
        self.setCentralWidget(self.root_widget)

    def set_table_clicked(self):
        try:
            self.rows = int(self.txt_rows.text())

            self.table.setRowCount(self.rows)

            c_labels = [f"{i}" for i in range(self.rows)]
            self.table.setVerticalHeaderLabels(c_labels)
        except:
            pass

    def calculate_clicked(self):
        l = []
        for r in range(self.rows):
            cell_txt = self.table.item(r, 0).text()
            cell_list = [x.strip() for x in cell_txt.split(',')]
            cell_new_txt = ','.join(cell_list)
            l.append(cell_new_txt)

        alg = AprioriAlgorithm(l, int(self.txt_min_sup.text()))
        answers = alg.solve()

        output = ''
        for index, value in enumerate(answers):
            output += str(value)
            if index < len(answers)-1:
                output += '\n'

        self.lbl_result.setText(output)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
