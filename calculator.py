import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLineEdit, QPushButton
from PyQt6.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Настройка окна
        self.setWindowTitle("Калькулятор")
        self.setFixedSize(450, 40)  # Фиксированный размер окна (ширина 450, высота 40)
        self.setWindowFlags(Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowCloseButtonHint)  # Убираем кнопки управления окном

        # Создаем горизонтальный layout для поля ввода и кнопки
        layout = QHBoxLayout()

        # Убираем margin (внешние отступы)
        layout.setContentsMargins(0, 0, 0, 0)  # Отступы: слева 0, сверху 0, справа 0, снизу 0

        # Убираем spacing (расстояние между виджетами)
        layout.setSpacing(0)  # Расстояние между кнопкой и полем ввода 0 пикселей

        # Кнопка очистки поля ввода
        clear_button = QPushButton("C", self)
        clear_button.setFixedSize(30, 40)  # Фиксированный размер кнопки (30x40)
        clear_button.clicked.connect(self.clear_input)
        layout.addWidget(clear_button)

        # Поле ввода (растягивается на всё оставшееся пространство)
        self.input_line = QLineEdit(self)
        self.input_line.setPlaceholderText("Введите выражение")
        self.input_line.returnPressed.connect(self.calculate)  # Обработка нажатия Enter
        layout.addWidget(self.input_line, stretch=1)  # Поле ввода растягивается на всё доступное пространство

        # Устанавливаем layout для окна
        self.setLayout(layout)

    def calculate(self):
        # Получаем текст из поля ввода
        expression = self.input_line.text()
        try:
            # Вычисляем результат
            result = eval(expression)
            # Выводим результат в поле ввода
            self.input_line.setText(str(result))
        except Exception as e:
            # В случае ошибки выводим сообщение об ошибке
            self.input_line.setText("Ошибка")

    def clear_input(self):
        # Очищаем поле ввода
        self.input_line.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())