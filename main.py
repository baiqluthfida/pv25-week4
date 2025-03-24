import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic 

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("pipi.ui", self)  

        self.comboBox.addItems(["Burger (Rp. 15.000)", "Pizza (Rp. 60.000)", "Pasta (Rp. 21.000)", "Salad (Rp. 27.000)", "Sushi (Rp. 32.000)"])
        self.comboBox_2.addItems(["0%", "10%", "15%", "25%", "50%", "75%"])

        self.product_price = {
            "Burger (Rp. 15.000)" : 15000,
            "Pizza (Rp. 60.000)" : 60000,
            "Pasta (Rp. 21.000)" : 21000,
            "Salad (Rp. 27.000)" : 27000,
            "Sushi (Rp. 32.000)" : 32000
        }

        self.discount_values = {
            "0%" : 0,
            "10%" : 10,
            "15%" : 15,
            "25%" : 25,
            "50%" : 50,
            "75%" : 75
        }

        self.total = 0
        

        self.pushButton_2.clicked.connect(self.add_to_cart)
        self.pushButton.clicked.connect(self.cancel_order)  # Hubungkan tombol ke fungsi


    def add_to_cart(self):
        product = self.comboBox.currentText()
        quantity = self.lineEdit.text()
        discount = self.comboBox_2.currentText()

        if not quantity.isdigit():
            QMessageBox.warning(self, "Input Error", "Masukkan jumlah barang dalam angka!")
            return
    
        quantity = int(quantity)
        if quantity <= 0:
            QMessageBox.warning(self, "Input Error", "Jumlah barang harus lebih dari 0!")
            return
        # Hitung harga awal
        price_per_unit = self.product_price.get(product, 0)
        total_price = price_per_unit * quantity

        # Hitung diskon
        discount_percentage = self.discount_values.get(discount, 0)
        discount_amount = (discount_percentage / 100) * total_price
        final_price = total_price - discount_amount

        self.total = self.total + final_price

        # Tambahkan pesanan ke kotak teks
        order_text = f"{product} x{quantity} - Diskon {discount}\nTotal: Rp. {final_price:,.0f}\n"
        self.textEdit_2.append(order_text)

        # Update label total harga
        self.label_9.setText(f"Rp. {self.total:,.0f}")

    def cancel_order(self):
        self.textEdit_2.clear()
        self.total = 0
        self.label_9.setText(f"Rp. {self.total:,.0f}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
