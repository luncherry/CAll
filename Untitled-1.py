import sys
#  []
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QLabel, QComboBox


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 550, 300)
        self.setWindowTitle('Миникалькулятор')
        dist = 145

        self.first, self.second, self.summa = QLabel(self), QLabel(self), QLabel(self)
        self.raznost, self.proizved, self.chastnost = QLabel(self), QLabel(self), QLabel(self)
        self.a, self.b, self.c = QLabel(self), QLabel(self), QLabel(self)
        self.oneSist, self.twoSist = QLineEdit(self), QLineEdit(self)
        self.perevod = QLabel(self)

        self.a.setText('       Начальная\n система счисления')
        self.b.setText('        Конечная\n система счисления')
        self.c.setText('кол-во чисел:')
        self.a.move(5, 20)
        self.b.move(5, 200)
        self.c.move(0, 110)
        self.perevod.setText('')
        self.perevod.move(5 + dist, 170)
        self.first.move(5 + dist, 30)
        self.second.move(5 + dist, 210)
        self.oneSist.setMaxLength(2)
        self.twoSist.setMaxLength(2)

        self.first.setText("Начальное ЦЕЛОЕ число")
        self.second.setText("второе ЦЕЛОЕ число")
        self.first.resize(self.first.sizeHint())
        self.second.resize(self.second.sizeHint())
        self.summa.setText("сумма = ")
        self.raznost.setText("разность = ")
        self.proizved.setText("произведение = ")
        self.chastnost.setText("частное = ")
        self.summa.setFixedWidth(3000)
        self.proizved.setFixedWidth(3000)
        self.raznost.setFixedWidth(3000)
        self.chastnost.setFixedWidth(3000)
        self.perevod.setFixedWidth(3000)
        self.a.setFixedWidth(3000)
        self.b.setFixedWidth(3000)
        self.perevod.setFixedHeight(60)

        self.summa.move(155 + dist, 50)
        self.raznost.move(155 + dist, 90)
        self.proizved.move(155 + dist, 130)
        self.chastnost.move(155 + dist, 170)

        self.count_number = QComboBox(self)
        self.count_number.addItems(['1', '2'])
        self.count_number.currentTextChanged.connect(self.saaa)
        self.count_number.move(85, 110)
        self.count_number.setFixedWidth(50)

        self.btn = QPushButton('->', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(52 + dist, 110)
        self.one = QLineEdit(self)
        self.two = QLineEdit(self)
        self.one.move(5 + dist, 50)
        self.two.move(5 + dist, 170)
        self.btn.clicked.connect(self.run)

        self.oneSist.move(5, 50)
        self.twoSist.move(5, 170)

        self.saaa('1')
        self.summa.setVisible(False)
        self.raznost.setVisible(False)
        self.chastnost.setVisible(False)
        self.proizved.setVisible(False)

    def saaa(self, text):
        flag = text == '2'
        self.second.setVisible(flag)
        self.two.setVisible(flag)
        self.twoSist.setVisible(not flag)
        self.oneSist.setVisible(not flag)
        self.a.setVisible(not flag)
        self.b.setVisible(not flag)
        self.first.setText("первое ЦЕЛОЕ число" if flag else 'Начальное ЦЕЛОЕ число')
        self.perevod.setVisible(False)
        self.one.setMaxLength(10)
        self.two.setMaxLength(10)
        self.summa.setVisible(flag)
        self.raznost.setVisible(flag)
        self.chastnost.setVisible(flag)
        self.proizved.setVisible(flag)
        self.perevod.setVisible(not flag)

    def run(self):
        flag = self.count_number.currentText() == '2'
        if flag:
            try:
                x, y = int(self.one.text()), int(self.two.text())
                self.raznost.setText(f"разность = {x - y}")
                self.summa.setText(f"сумма = {x + y}")
                self.proizved.setText(f"произведение = {x * y}")
                if y != 0:
                    v = float('{:.3f}'.format(x / y))
                    self.chastnost.setText(f"частное = {v}")
                else:
                    self.chastnost.setText(f"На ноль делить нельзя!")
            except ValueError:
                self.perevod.setText(f"Нельзя перевести!")
        else:
            try:
                x = self.one.text()
                last_sistem = int(self.oneSist.text())
                next_sistem = int(self.twoSist.text())
                res = self.convert_base(x, next_sistem, last_sistem)
                if res == "нет возможности перевести":
                    self.perevod.setText(f"Нельзя перевести!")
                    return
                self.perevod.setText(f"из {last_sistem}-ой системы счисления\n"
                                     f"число {x} переведено в {next_sistem}-ую систему:\n{res}")
            except ValueError:
                self.perevod.setText(f"Нельзя перевести!")

    def convert_base(self, num, to_base=10, from_base=10):
        n = int(num, from_base) if isinstance(num, str) else num
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = ""
        if to_base > len(alphabet) or from_base > len(alphabet):
            return "нет возможности перевести"
        while n > 0:
            n, m = divmod(n, to_base)
            res += alphabet[m]
        return res[::-1]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
    