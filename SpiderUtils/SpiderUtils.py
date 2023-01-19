#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/11/23 14:01   lbs      1.0         None
"""
import csv
import pathlib
import requests



class SpiderUtils:
    def __init__(self):
        self.urls = self.set_url()
        self.headers = self.set_headers()

    def set_url(self, ):
        """

        :return:
        """
        # ————————————————————————————构造url————————————————————————————
        urls = []
        for page in range(1, 20):
            url = f'https://xueqiu.com/service/v5/stock/screener/quote/list?page={page}&size=30&order=desc&order_by=amount&exchange=CN&market=CN&type=sha&_=1637908787379'
            urls.append(url)
        return urls

    def set_headers(self, headers: dict = None):
        """
        
        :param headers: 
        :return: 
        """
        return headers if headers else {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'}

    def save_to_file(self,file_path: str = './temp', file_type: str = '.csv', encode: str = 'utf-8', file_header: list = None):
        """

        :param file_header:
        :param encode:
        :param file_path:
        :param file_type:
        :return:
        """
        file_path += file_type
        if file_type == '.csv':
            data = self.get_data()
            print(data)
            if data:
                with open(file_path, 'w', encoding=encode, newline='') as f:
                    csv_write = csv.writer(f)
                    if file_header:
                        csv_write.writerow(file_header)
                    csv_write.writerows(data)
                    print(f'file write to {pathlib.Path(file_path).absolute()}')
                    return True
            else:
                return 'data is none'

    def get_data(self, method: str = 'get') -> list:
        """

        :param method:
        :return:
        """
        if method == 'get':
            if isinstance(self.urls, list):
                datas = []
                for url in self.urls:
                    response = requests.get(url, headers=self.headers)
                    data = self.process(response)
                    datas += data
                    # ————————————————————————————这里写入数据处理片段————————————————————————————
                return datas

    def process(self, response):
        """

        :param response:
        :return:
        """
        if response.status_code == 200:
            re_data = []
            # ————————————————————————————这里写入数据处理片段————————————————————————————
            json_data = response.json()
            data_list = json_data['data']['list']
            for data in data_list:
                data1 = data['symbol']
                data2 = data['name']
                data3 = data['current']
                data4 = data['chg']
                data5 = data['percent']
                data6 = data['current_year_percent']
                data7 = data['volume']
                data8 = data['amount']
                data9 = data['turnover_rate']
                data10 = data['pe_ttm']
                data11 = data['dividend_yield']
                data12 = data['market_capital']
                # print(data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12)
                data_row = [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12]
                re_data.append(data_row)
            return re_data
        else:
            return []


if __name__ == '__main__':
    file_header = ['股票代码', '股票名称', '当前价', '涨跌额', '涨跌幅', '年初至今', '成交量','成交额', '换手率', '市盈率(TTM)', '股息率', '市值']
    write = SpiderUtils()
    write.save_to_file(file_path='./files/csv/temp', file_header=file_header)
