"""This code helps us to check the currencies in real time with graphic interface ( 27 currencies available ).
   Ce code nous aide vérifier les devises en temps réel avec une interface graphique ( 27 devises disponibles )."""
"""If one of the conversions doesn't work and you have an error, this means that the currency is not found.
   Si l'une de ces devises ne fonctionne pas, cela veut dire qu'elle n'est pas trouvée."""

from PySide6 import QtWidgets
import requests
dict_with_all_currencies = {'DKK', 'CZK', 'HKD', 'MYR', 'USD', 'KRW', 'PHP', 'RON', 'CAD', 'HUF', 'THB', 'BGN', 'RUB', 'MXN', 'BRL', 'HRK', 'NZD', 'IDR', 'ZAR', 'EUR', 'JPY', 'CNY', 'NOK', 'SEK', 'ILS', 'GBP', 'CHF'}

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.c = dict_with_all_currencies
        self.setWindowTitle("Convertisseur de Devises")
        self.setup_ui()
        self.setup_css()
        self.set_default_values()
        self.connections()

    def setup_ui(self):
        # Ici nous allons créer notre "layout" et les elements qui sont dedans.
        self.layout = QtWidgets.QHBoxLayout(self)
        self.combobox_from = QtWidgets.QComboBox()
        self.spin_box_1 = QtWidgets.QSpinBox()
        self.combobox_to = QtWidgets.QComboBox()
        self.spin_box_2 = QtWidgets.QSpinBox()
        self.button = QtWidgets.QPushButton("Inverser les devises")

        # Nous allons les ajouter dans dans le layout pour qu'on puisse les voir quand meme.
        self.layout.addWidget(self.combobox_from)
        self.layout.addWidget(self.spin_box_1)
        self.layout.addWidget(self.combobox_to)
        self.layout.addWidget(self.spin_box_2)
        self.layout.addWidget(self.button)

    def set_default_values(self):
        self.combobox_from.addItems(sorted(list(self.c)))
        self.combobox_to.addItems(sorted(list(self.c)))
        self.combobox_from.setCurrentText("EUR")
        self.combobox_to.setCurrentText("EUR")

        self.spin_box_1.setRange(1, 1000000000)
        self.spin_box_2.setRange(1, 1000000000)

        self.spin_box_1.setValue(100)
        self.spin_box_2.setValue(100)

    def connections(self):
        self.combobox_from.activated.connect(self.compute)
        self.combobox_to.activated.connect(self.compute)
        self.spin_box_1.valueChanged.connect(self.compute)
        self.button.clicked.connect(self.inverser_devise)

    def compute(self):
        symbol = f'{self.combobox_from.currentText()}/{self.combobox_to.currentText()}'

        key = 'You need to have a key! Go to https://twelvedata.com and get one.'
        url = f"https://api.twelvedata.com/exchange_rate?symbol={symbol}&apikey={key}"
        try:
            request = requests.get(url)
            data = request.json()
            if 'status' in data.keys():
                print("La convertion n'a pas fonctionné")
                exit()

            montant = float(self.spin_box_1.value())
            result = f"{montant * float(data['rate'])}"
            self.spin_box_2.setValue(float(result))
        except requests.exceptions.RequestException as e:
            print("La convertion n'a pas fonctionné"), e

    def setup_css(self):
        self.setStyleSheet("""
        background-color: rgb(30, 30, 30);
        color: rgb(240, 240, 240);
        """)
        self.button.setStyleSheet('color: rgb(106, 90, 205)')

    def inverser_devise(self):
        devise_from = self.combobox_from.currentText()
        devise_to = self.combobox_to.currentText()
        self.combobox_from.setCurrentText(devise_to)
        self.combobox_to.setCurrentText(devise_from)
        self.compute()

app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec()