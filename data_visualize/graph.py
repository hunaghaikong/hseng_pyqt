#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/10 0010 15:55
# @Author  : Hadrianl 
# @File    : graph.py
# @License : (C) Copyright 2013-2017, 凯瑞投资
from util import V_logger, MA_COLORS
import pandas as pd
import numpy as np
from PyQt5.Qt import  QBrush, QColor
from data_visualize.baseitems import graph_base, TradeDataScatter, TradeDataLinkLine, CandlestickItem
import pyqtgraph as pg


class Graph_OHLC(graph_base):
    def __init__(self, plt):
        super(Graph_OHLC, self).__init__(plt, 'OHLC')

    def init(self, ohlc):
        V_logger.info(f'G+初始化{self.name}图表')
        self.items_dict = {}
        self.items_dict['ohlc'] = CandlestickItem()
        self.items_dict['tick'] = CandlestickItem()
        self.items_dict['hline'] = self.items_dict['tick'].hline
        self.items_dict['tick'].mark_line()
        self.plt.addItem(self.items_dict['ohlc'])
        self.plt.addItem(self.items_dict['tick'])
        self.plt.addItem(self.items_dict['hline'])

    def update(self, ohlc):
        V_logger.info(f'G↑更新{self.name}图表')
        self.items_dict['ohlc'].setHisData(ohlc)

    def deinit(self):
        V_logger.info(f'G-反初始化{self.name}图表')
        if hasattr(self, 'items_dict'):
            for k, v in self.items_dict.items():
                self.plt.removeItem(v)
            delattr(self, 'items_dict')

class Graph_MA(graph_base):
    def __init__(self, plt):
        super(Graph_MA, self).__init__(plt, 'MA')

    def init(self, ohlc):

        self.items_dict = {}
        i_ma = getattr(ohlc, self.name, None)
        if i_ma:
            V_logger.info(f'G+初始化{self.name}图表')
            for w in i_ma._windows:
                self.items_dict[w] = pg.PlotDataItem(pen=pg.mkPen(color=MA_COLORS.get(w, 'w'), width=1))
                self.plt.addItem(self.items_dict[w])
        else:
            V_logger.error(f'G+初始化{self.name}图表失败，缺失{self.name}数据')

    def update(self, ohlc):
        x = ohlc.x
        i_ma = getattr(ohlc, self.name, None)
        if i_ma:
            V_logger.info(f'G↑更新{self.name}图表')
            for w in self.items_dict:
                self.items_dict[w].setData(x, getattr(i_ma, w).values)
        else:
            V_logger.info(f'数据类缺失{self.name}数据')


    def deinit(self):
        V_logger.info(f'G-反初始化{self.name}图表')
        if hasattr(self, 'items_dict'):
            for k, v in self.items_dict.items():
                self.plt.removeItem(v)
            delattr(self, 'items_dict')

class Graph_MACD(graph_base):
    def __init__(self, plt):
        super(Graph_MACD, self).__init__(plt, 'MACD')


    def init(self, ohlc):

        self.items_dict = {}
        i_macd = getattr(ohlc, self.name, None)
        if i_macd:
            V_logger.info(f'G+初始化{self.name}图表')
            macd_pens = pd.concat([ohlc.close > ohlc.open, i_macd.macd > 0], 1).apply(
                lambda x: (x.iloc[0] << 1) + x.iloc[1], 1).map({3: 'r', 2: 'b', 1: 'y', 0: 'g'})
            macd_brushs = [None if (i_macd.macd > i_macd.macd.shift(1))[i]
                           else v for i, v in macd_pens.iteritems()]
            self.items_dict['MACD'] = pg.BarGraphItem(x=ohlc.x, height=i_macd.macd,
                                                           width=0.5, pens=macd_pens, brushes=macd_brushs)
            self.items_dict['diff'] = pg.PlotDataItem(pen='y')
            self.items_dict['dea'] = pg.PlotDataItem(pen='w')
            self.plt.addItem(self.items_dict['MACD'])
            self.plt.addItem(self.items_dict['diff'])
            self.plt.addItem(self.items_dict['dea'])
        else:
            V_logger.error(f'G+初始化{self.name}图表失败，缺失{self.name}数据')

    def update(self, ohlc):
        i_macd = getattr(ohlc, self.name, None)
        if i_macd:
            V_logger.info(f'G↑更新{self.name}图表')
            x = i_macd.x
            diff = i_macd.diff
            dea = i_macd.dea
            macd = i_macd.macd
            self.items_dict['diff'].setData(x, diff.values)
            self.items_dict['dea'].setData(x, dea.values)
            macd_pens = pd.concat(
                [ohlc.close > ohlc.open, macd > 0], 1).apply(
                lambda x: (x.iloc[0] << 1) + x.iloc[1], 1).map({3: 'r', 2: 'b', 1: 'y', 0: 'g'})
            macd_brushes = [None if (macd > macd.shift(1))[i]
                            else v for i, v in macd_pens.iteritems()]
            self.items_dict['MACD'].setOpts(x=x, height=macd, pens=macd_pens, brushes=macd_brushes)
        else:
            V_logger.info(f'数据类缺失{self.name}数据')

    def deinit(self):
        V_logger.info(f'G-反初始化{self.name}图表')
        if hasattr(self, 'items_dict'):
            for k, v in self.items_dict.items():
                self.plt.removeItem(v)
            delattr(self, 'items_dict')


class Graph_MACD_HL_MARK(graph_base):
    def __init__(self, plt):
        super(Graph_MACD_HL_MARK, self).__init__(plt, 'MACD_HL_MARK')

    def init(self, ohlc):

        h_macd_hl_mark = getattr(ohlc, self.name, None)
        if h_macd_hl_mark:
            V_logger.info(f'G+初始化{self.name}图表')
            self.items_dict = {}
            self.items_dict['high_pos'] = []
            self.items_dict['low_pos'] = []
        else:
            V_logger.error(f'G+初始化{self.name}图表失败，缺失{self.name}数据')

    def update(self,ohlc):

        h_macd_hl_mark = getattr(ohlc, self.name, None)
        x = ohlc.x
        if h_macd_hl_mark:
            V_logger.info(f'G↑更新{self.name}图表')
            for i in self.items_dict['high_pos']:
                self.plt.removeItem(i)
            for i in self.items_dict['low_pos']:
                self.plt.removeItem(i)
            self.items_dict['high_pos'].clear()
            self.items_dict['low_pos'].clear()
            for k, v in h_macd_hl_mark.high_pos.iteritems():
                textitem = pg.TextItem(html=f'<span style="color:#FF0000;font-size:11px">{v}<span/>',
                                       border=pg.mkPen({'color': "#FF0000", 'width': 1}),
                                       angle=15, anchor=(0, 1))
                textitem.setPos(x[k], v)
                self.plt.addItem(textitem)
                self.items_dict['high_pos'].append(textitem)

            for k, v in h_macd_hl_mark.low_pos.iteritems():
                textitem = pg.TextItem(html=f'<span style="color:#7CFC00;font-size:11px">{v}<span/>',
                                       border=pg.mkPen({'color': "#7CFC00", 'width': 1}),
                                       angle=-15, anchor=(0, 0))
                textitem.setPos(x[k], v)
                self.plt.addItem(textitem)
                self.items_dict['low_pos'].append(textitem)
        else:
            V_logger.info(f'数据类缺失{self.name}数据')


    def deinit(self):
        V_logger.info(f'G-反初始化{self.name}图表')
        if hasattr(self, 'items_dict'):
            for k, v in self.items_dict.items():
                for i in v:
                    self.plt.removeItem(i)
            delattr(self, 'items_dict')

class Graph_STD(graph_base):
    def __init__(self, plt):
        super(Graph_STD, self).__init__(plt, 'STD')

    def init(self, ohlc):

        self.items_dict = {}
        i_std = getattr(ohlc, self.name, None)
        if i_std:
            V_logger.info(f'G+初始化{self.name}图表')
            self.plt.setMaximumHeight(150)
            std_inc_pens = pd.cut((i_std.inc / i_std.std).fillna(0), [-np.inf, -2, -1, 1, 2, np.inf],  # 设置画笔颜色
                                  labels=['g', 'y', 'l', 'b', 'r'])
            inc_gt_std = (i_std.inc.abs() / i_std.std) > 1
            std_inc_brushes = np.where(inc_gt_std, std_inc_pens, None)  # 设置画刷颜色
            self.items_dict['inc'] = pg.BarGraphItem(x=i_std.x, height=i_std.inc,
                                                     width=0.5, pens=std_inc_pens, brushes=std_inc_brushes)
            self.items_dict['pos_std'] = pg.PlotDataItem(pen='r')
            self.items_dict['neg_std'] = pg.PlotDataItem(pen='g')
            self.plt.addItem(self.items_dict['inc'])
            self.plt.addItem(self.items_dict['pos_std'])
            self.plt.addItem(self.items_dict['neg_std'])
        else:
            V_logger.error(f'G+初始化{self.name}图表失败，缺失{self.name}数据')

    def update(self, ohlc):
        x = ohlc.x
        i_std = getattr(ohlc, self.name, None)
        if i_std:
            V_logger.info(f'G↑更新{self.name}图表')
            inc = i_std.inc
            std = i_std.std
            pos_std = i_std.pos_std
            neg_std = i_std.neg_std
            std_inc_pens = pd.cut((inc / std).fillna(0), [-np.inf, -2, -1, 1, 2, np.inf],
                                  labels=['g', 'y', 'l', 'b', 'r'])
            inc_gt_std = (inc.abs() / std) > 1
            std_inc_brushes = np.where(inc_gt_std, std_inc_pens, None)
            self.items_dict['pos_std'].setData(x, pos_std)
            self.items_dict['neg_std'].setData(x, neg_std)
            self.items_dict['inc'].setOpts(x=x, height=inc, pens=std_inc_pens, brushes=std_inc_brushes)
        else:
            V_logger.info(f'数据类缺失{self.name}数据')

    def deinit(self):
        V_logger.info(f'G-反初始化{self.name}图表')
        if hasattr(self, 'items_dict'):
            for k, v in self.items_dict.items():
                self.plt.removeItem(v)
            delattr(self, 'items_dict')

class Graph_Trade_Data_Mark(graph_base):
    def __init__(self, plt):
        super(Graph_Trade_Data_Mark, self).__init__(plt, 'Trade_Data')

    def init(self, ohlc):

        trade_data = getattr(ohlc, self.name, None)
        if trade_data:
            V_logger.info(f'G+初始化交易数据标记{self.name}')
            self.items_dict = {}
            self.items_dict['open'] = TradeDataScatter()
            self.items_dict['close'] = TradeDataScatter()
            self.items_dict['link_line'] = TradeDataLinkLine(pen=pg.mkPen('w', width=1))
            self.items_dict['info_text'] = pg.TextItem(anchor=(1, 1))
            self.plt.addItem(self.items_dict['open'])
            self.plt.addItem(self.items_dict['close'])
            self.plt.addItem(self.items_dict['link_line'])
            self.plt.addItem(self.items_dict['info_text'])
        else:
            V_logger.error(f'G+初始化{self.name}图表失败，缺失{self.name}数据')

    # --------------------------------添加交易数据-----------------------------------------------------------------
    def update(self, ohlc):
        x = ohlc.x
        trade_data = getattr(ohlc, self.name, None)
        if trade_data:
            V_logger.info(f'G↑更新{self.name}图表')
            try:
                self.items_dict['open'].setData(x=x.reindex(trade_data.open.index.floor(ohlc.ktype)),
                                                y=trade_data['OpenPrice'],
                                                symbol=['t1' if t == 0 else 't' for t in trade_data['Type']],
                                                brush=trade_data['Status'].map(
                                                         {2: pg.mkBrush(QBrush(QColor(0, 0, 255))),
                                                          1: pg.mkBrush(QBrush(QColor(255, 0, 255))),
                                                          0: pg.mkBrush(QBrush(QColor(255, 255, 255)))}).tolist())
            except Exception as e:
                V_logger.error(f'初始化交易数据标记TradeDataScatter-open失败')
            try:
                self.items_dict['close'].setData(x=x.reindex(trade_data.close.index.floor(ohlc.ktype)),
                                                 y=trade_data['ClosePrice'],
                                                 symbol=['t' if t == 0 else 't1' for t in trade_data['Type']],
                                                 brush=trade_data['Status'].map(
                                                          {2: pg.mkBrush(QBrush(QColor(255, 255, 0))),
                                                           1: pg.mkBrush(QBrush(QColor(255, 0, 255))),
                                                           0: pg.mkBrush(QBrush(QColor(255, 255, 255)))}).tolist())
            except Exception as e:
                V_logger.error(f'初始化交易数据标记TradeDataScatter-open失败')

            # -------------------------------------------------------------------------------------------------------------
            def link_line(a, b):
                trade_data = ohlc.Trade_Data
                if a is self.items_dict['open']:
                    for i, d in enumerate(self.items_dict['open'].data):
                        if b[0].pos().x() == d[0] and b[0].pos().y() == d[1]:
                            index = i
                            break
                elif a is self.items_dict['close']:
                    for i, d in enumerate(self.items_dict['close'].data):
                        if b[0].pos().x() == d[0] and b[0].pos().y() == d[1]:
                            index = i
                            break

                open_x = self.items_dict['open'].data[index][0]
                open_y = self.items_dict['open'].data[index][1]
                open_symbol = self.items_dict['open'].data[index][3]  # open_symbol来区别开仓平仓
                if trade_data["Status"].iloc[index] == 2:
                    close_x = self.items_dict['close'].data[index][0]
                    close_y = self.items_dict['close'].data[index][1]
                else:
                    close_x = self.items_dict['close'].data[index][0]
                    close_y = ohlc._last_tick.Price if ohlc._last_tick else ohlc.data.iloc[-1]['close']
                profit = round(close_y - open_y, 2) if open_symbol == "t1" else round(open_y - close_y, 2)
                pen_color_type = ((open_symbol == 't1') << 1) + (open_y < close_y)
                pen_color_map_dict = {0: 'r', 1: 'g', 2: 'g', 3: 'r'}
                self.items_dict['link_line'].setData([[open_x, open_y],
                                                      [close_x, close_y]],
                                                     pen_color_map_dict[pen_color_type])
                self.items_dict['info_text'].setHtml(
                    f'<span style="color:white">Account:{trade_data["Account_ID"].iloc[index]}<span/><br/>'
                    f'<span style="color:blue">Open :{open_y}<span/><br/>'
                    f'<span style="color:yellow">Close:{close_y}<span/><br/>'
                    f'<span style="color:white">Type  :{"Long" if open_symbol == "t1" else "Short"}<span/><br/>'
                    f'<span style="color:{"red" if profit >=0 else "green"}">Profit:{profit}<span/><br/>'
                    f'<span style="color:"white">trader:{trade_data["trader_name"].iloc[index]}<span/>')
                self.items_dict['info_text'].setPos(self.plt.getViewBox().viewRange()[0][1],
                                                    self.plt.getViewBox().viewRange()[1][0])

            self.items_dict['open'].sigClicked.connect(link_line)
            self.items_dict['close'].sigClicked.connect(link_line)

        else:
            V_logger.info(f'数据类缺失{self.name}数据')

    def deinit(self):
        V_logger.info(f'G-反初始化交易数据标记{self.name}')
        if hasattr(self, 'items_dict'):
            for k, v in self.items_dict.items():
                self.plt.removeItem(v)
            delattr(self, 'items_dict')

class Graph_Slicer(graph_base):
    def __init__(self, plt):
        super(Graph_Slicer, self).__init__(plt, 'Slicer')

    def init(self, ohlc):
        V_logger.info(f'G+初始化{self.name}图表')
        self.items_dict = {}
        self.items_dict['close_curve'] = pg.PlotDataItem()
        self.items_dict['date_region'] = pg.LinearRegionItem([1, 100])
        self.plt.addItem(self.items_dict['close_curve'])
        self.plt.addItem(self.items_dict['date_region'])

    def update(self, ohlc):
        V_logger.info(f'G↑更新{self.name}图表')
        self.items_dict['close_curve'].setData(ohlc.x, ohlc.close)

    def deinit(self):
        V_logger.info(f'G-反初始化交易数据标记{self.name}')
        if hasattr(self, 'items_dict'):
            for k, v in self.items_dict.items():
                self.plt.removeItem(v)
            delattr(self, 'items_dict')

