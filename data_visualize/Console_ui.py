#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/31 0031 15:12
# @Author  : Hadrianl 
# @File    : Console_ui.py
# @License : (C) Copyright 2013-2017, 凯瑞投资


import pyqtgraph.console
from util import F_logger, ZMQ_SOCKET_HOST, ZMQ_INFO_PORT
import zmq
from console import *
from PyQt5.Qt import QWidget, QTableWidgetItem, QColor
from PyQt5.QtCore import Qt
import datetime as dt
from threading import Thread
from logging import Handler, Formatter
from sp_func.order import *

class AnalysisConsole(QWidget, Ui_Console):
    def __init__(self, namespace):
        QWidget.__init__(self)
        Ui_Console.__init__(self)
        help_text = f'''实盘分析Console测试（help_doc()调用帮助文档）'''
        self.setupUi(self)
        self.logging_handler = self.console_logging_handler(self.ConsoleWidget_con)
        self.ConsoleWidget_con.localNamespace = namespace
        self.ConsoleWidget_con.output.setPlainText(help_text)
        self.__receiver_alive = False
        self.init_server_info_receiver()

    def init_server_info_receiver(self):
        self._server_info_socket = zmq.Context().socket(zmq.SUB)
        self._server_info_socket.connect(f'tcp://{ZMQ_SOCKET_HOST}:{ZMQ_INFO_PORT}')
        self._server_info_socket.set_string(zmq.SUBSCRIBE, '')
        self._server_info_socket.setsockopt(zmq.RCVTIMEO, 5000)
        self._receiver_start()

    def __receiver_run(self):
        print('testing1')
        while self.__receiver_alive:
            try:
                _type, _info = self._server_info_socket.recv_multipart()
                print(_type, _info)
                F_logger.info(_type.decode() + _info.decode())
            except zmq.ZMQError as e:
                print(e)

    def _receiver_start(self):
        if not self.__receiver_alive:
            self.__receiver_alive = True
            self.__receiver_thread = Thread(target=self.__receiver_run)
            self.__receiver_thread.start()


    def _receiver_stop(self):
        if self.__receiver_alive:
            self.__receiver_thread.join()
            self._server_info_socket.disconnect(f'tcp://{ZMQ_SOCKET_HOST}:{ZMQ_INFO_PORT}')
            self.__receiver_alive = False

    def focus(self):
        if self.isHidden():
            self.show()
        else:
            self.setWindowFlags(Qt.WindowStaysOnTopHint)
            self.focusWidget()

    def update_daterange(self, start, end):
        self.DateTimeEdit_start.setDateTime(start)
        self.DateTimeEdit_end.setDateTime(end)

    def add_ticker_to_table(self, ticker):
        self.TableWidget_tickers.insertRow(0)
        self.TableWidget_tickers.setItem(0, 0, QTableWidgetItem(dt.datetime.fromtimestamp(ticker.TickerTime).strftime('%H:%M:%S')))
        self.TableWidget_tickers.setItem(0, 1, QTableWidgetItem(str(ticker.Price)))
        qty = QTableWidgetItem(str(ticker.Qty))
        self.TableWidget_tickers.setItem(0, 2, qty)
        if self.TableWidget_tickers.rowCount() > 100:
            self.TableWidget_tickers.removeRow(100)


    def add_price_to_table(self, price):
        max_depth = 5
        for i, bid, bid_qty, ask, ask_qty in zip(range(20), price.Bid, price.BidQty, price.Ask, price.AskQty):
            self.TableWidget_prices.setItem(5+i, 0, QTableWidgetItem(str(bid)))
            self.TableWidget_prices.setItem(5+i, 1, QTableWidgetItem(str(bid_qty)))
            self.TableWidget_prices.setItem(4-i, 0, QTableWidgetItem(str(ask)))
            self.TableWidget_prices.setItem(4-i, 1, QTableWidgetItem(str(ask_qty)))
            if max_depth == i + 1:
                break

    def init_sp_func_signal(self):
        self.Button_market_long.released.connect(lambda : add_market_order())
        self.Button_market_short.released.connect(lambda : add_market_order())
        self.Button_limit_long.released.connect(lambda : add_limit_order())
        self.Button_limit_short.released.connect(lambda : add_limit_order())

    class console_logging_handler(Handler):
        def __init__(self, consolewidget):
            Handler.__init__(self)
            self.consolewidget = consolewidget
            formatter = Formatter('%(asctime)s - %(levelname)s - %(message)s')
            self.setLevel('INFO')
            self.setFormatter(formatter)

        def emit(self, record):
            msg = self.format(record)
            try:
                self.consolewidget.output.appendPlainText(msg)
            except Exception as e:
                print(e)



