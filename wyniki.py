# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wyniki.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Wyniki(object):
    def setupUi(self, Wyniki):
        Wyniki.setObjectName("Wyniki")
        Wyniki.resize(1062, 387)
        self.tabWidget = QtWidgets.QTabWidget(Wyniki)
        self.tabWidget.setGeometry(QtCore.QRect(90, 30, 891, 331))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Tabela_wynikow = QtWidgets.QTableWidget(self.tab)
        self.Tabela_wynikow.setGeometry(QtCore.QRect(340, 10, 211, 261))
        self.Tabela_wynikow.setObjectName("Tabela_wynikow")
        self.Tabela_wynikow.setColumnCount(1)
        self.Tabela_wynikow.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow.setHorizontalHeaderItem(0, item)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.Tabela_wynikow_2 = QtWidgets.QTableWidget(self.tab_2)
        self.Tabela_wynikow_2.setGeometry(QtCore.QRect(20, 10, 841, 261))
        self.Tabela_wynikow_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Tabela_wynikow_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Tabela_wynikow_2.setObjectName("Tabela_wynikow_2")
        self.Tabela_wynikow_2.setColumnCount(6)
        self.Tabela_wynikow_2.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_2.setItem(0, 0, item)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.Tabela_wynikow_3 = QtWidgets.QTableWidget(self.tab_3)
        self.Tabela_wynikow_3.setGeometry(QtCore.QRect(20, 10, 841, 261))
        self.Tabela_wynikow_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Tabela_wynikow_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Tabela_wynikow_3.setObjectName("Tabela_wynikow_3")
        self.Tabela_wynikow_3.setColumnCount(6)
        self.Tabela_wynikow_3.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_3.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_3.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_3.setItem(0, 0, item)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.Tabela_wynikow_4 = QtWidgets.QTableWidget(self.tab_4)
        self.Tabela_wynikow_4.setGeometry(QtCore.QRect(20, 10, 841, 261))
        self.Tabela_wynikow_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Tabela_wynikow_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Tabela_wynikow_4.setObjectName("Tabela_wynikow_4")
        self.Tabela_wynikow_4.setColumnCount(6)
        self.Tabela_wynikow_4.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_4.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_4.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_4.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_4.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_4.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_4.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela_wynikow_4.setItem(0, 0, item)
        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(Wyniki)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Wyniki)

    def retranslateUi(self, Wyniki):
        _translate = QtCore.QCoreApplication.translate
        Wyniki.setWindowTitle(_translate("Wyniki", "Wyniki"))
        item = self.Tabela_wynikow.verticalHeaderItem(0)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow.verticalHeaderItem(1)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow.verticalHeaderItem(2)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow.verticalHeaderItem(3)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow.verticalHeaderItem(4)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow.verticalHeaderItem(5)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow.horizontalHeaderItem(0)
        item.setText(_translate("Wyniki", "Ea (kJ/mol)?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Wyniki", "Tab 1"))
        item = self.Tabela_wynikow_2.verticalHeaderItem(0)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow_2.verticalHeaderItem(1)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow_2.verticalHeaderItem(2)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow_2.verticalHeaderItem(3)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow_2.verticalHeaderItem(4)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow_2.verticalHeaderItem(5)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow_2.horizontalHeaderItem(0)
        item.setText(_translate("Wyniki", "V_NH3 (dm^3/h)"))
        item = self.Tabela_wynikow_2.horizontalHeaderItem(1)
        item.setText(_translate("Wyniki", "Tem (oC)"))
        item = self.Tabela_wynikow_2.horizontalHeaderItem(2)
        item.setText(_translate("Wyniki", "P (atm)"))
        item = self.Tabela_wynikow_2.horizontalHeaderItem(3)
        item.setText(_translate("Wyniki", "m. kat(g)"))
        item = self.Tabela_wynikow_2.horizontalHeaderItem(4)
        item.setText(_translate("Wyniki", "k"))
        item = self.Tabela_wynikow_2.horizontalHeaderItem(5)
        item.setText(_translate("Wyniki", "k/ko"))
        __sortingEnabled = self.Tabela_wynikow_2.isSortingEnabled()
        self.Tabela_wynikow_2.setSortingEnabled(False)
        self.Tabela_wynikow_2.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Wyniki", "Page"))
        item = self.Tabela_wynikow_3.verticalHeaderItem(0)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow_3.verticalHeaderItem(1)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow_3.verticalHeaderItem(2)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow_3.verticalHeaderItem(3)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow_3.verticalHeaderItem(4)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow_3.verticalHeaderItem(5)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow_3.horizontalHeaderItem(0)
        item.setText(_translate("Wyniki", "V_NH3 (dm^3/h)"))
        item = self.Tabela_wynikow_3.horizontalHeaderItem(1)
        item.setText(_translate("Wyniki", "Tem (oC)"))
        item = self.Tabela_wynikow_3.horizontalHeaderItem(2)
        item.setText(_translate("Wyniki", "P (atm)"))
        item = self.Tabela_wynikow_3.horizontalHeaderItem(3)
        item.setText(_translate("Wyniki", "m. kat(g)"))
        item = self.Tabela_wynikow_3.horizontalHeaderItem(4)
        item.setText(_translate("Wyniki", "k"))
        item = self.Tabela_wynikow_3.horizontalHeaderItem(5)
        item.setText(_translate("Wyniki", "k/ko"))
        __sortingEnabled = self.Tabela_wynikow_3.isSortingEnabled()
        self.Tabela_wynikow_3.setSortingEnabled(False)
        self.Tabela_wynikow_3.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Wyniki", "Page"))
        item = self.Tabela_wynikow_4.verticalHeaderItem(0)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow_4.verticalHeaderItem(1)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow_4.verticalHeaderItem(2)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow_4.verticalHeaderItem(3)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow_4.verticalHeaderItem(4)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow_4.verticalHeaderItem(5)
        item.setText(_translate("Wyniki", "New Row"))
        item = self.Tabela_wynikow_4.horizontalHeaderItem(0)
        item.setText(_translate("Wyniki", "V_NH3 (dm^3/h)"))
        item = self.Tabela_wynikow_4.horizontalHeaderItem(1)
        item.setText(_translate("Wyniki", "Tem (oC)"))
        item = self.Tabela_wynikow_4.horizontalHeaderItem(2)
        item.setText(_translate("Wyniki", "P (atm)"))
        item = self.Tabela_wynikow_4.horizontalHeaderItem(3)
        item.setText(_translate("Wyniki", "m. kat(g)"))
        item = self.Tabela_wynikow_4.horizontalHeaderItem(4)
        item.setText(_translate("Wyniki", "k"))
        item = self.Tabela_wynikow_4.horizontalHeaderItem(5)
        item.setText(_translate("Wyniki", "k/ko"))
        __sortingEnabled = self.Tabela_wynikow_4.isSortingEnabled()
        self.Tabela_wynikow_4.setSortingEnabled(False)
        self.Tabela_wynikow_4.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Wyniki", "Page"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Wyniki = QtWidgets.QWidget()
    ui = Ui_Wyniki()
    ui.setupUi(Wyniki)
    Wyniki.show()
    sys.exit(app.exec_())
