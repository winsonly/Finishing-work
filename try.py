import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv
import sys
from pylab import mpl
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import warnings
import os
import shutil
from pygame import mixer, init
import pymysql
import time

warnings.filterwarnings('ignore')

# 背景音乐
mixer.init()
mixer.music.load(r'史岩 - 神话.mp3')
mixer.music.play(-1, 0, 0)


def Sound(S):  # 答题声音

    init()
    soundObj = mixer.Sound(S)
    soundObj.play()


def gethtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("fail")
        sys.exit()


def get(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    trs = soup.find_all('tr')
    for tr in trs:
        list1 = []
        for td in tr:
            ts = td.string
            if ts is None:
                continue
            ts = ts.strip()
            if ts == '\n':
                continue
            list1.append(ts)
        ulist.append(list1)


def save(e, s):
    with open(r'd:\py\gdp' + s + '.csv', 'a', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)  # 此处使用文件
        f_csv.writerows(e)  # 此处使用文件


def gethtml1(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("fail")
        sys.exit()


def get1(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    trs = soup.find_all('tr')
    i = 0
    for tr in trs:
        list1 = []
        if i == 0 or i == 1 or i == 4:
            i += 1
            continue
        for td in tr:
            ts = td.string
            if ts is None:
                i += 1
                continue
            ts = ts.strip()
            list1.append(ts)
        ulist.append(list1)
        i += 1


def save1(e, s):
    with open(r'd:\py\renkou' + s + '.csv', 'a', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(e)

# 以下是对数据的保存，是利用上一部分的函数构建的，数据处理与数据分析也包含在其中

def pa():  # 爬得所有需要的csv文件

    for s in range(2000, 2020):
        s = str(s)
        url = 'https://www.kylc.com/stats/global/yearly/g_gdp/' + s + '.html'
        e = []
        html = gethtml(url)
        get(e, html)
        save(e, s)
    for s in range(2000, 2020):
        s = str(s)
        data = pd.read_csv(r'd:\py\gdp' + s + '.csv', encoding='gbk', index_col=0)  # 此处使用pandas
        a = data.iloc[0:9, [2, 8]]
        a = a.dropna()
        a.to_csv(r'd:\py\gdp.' + s + '.csv', index=False, header=False)  # 此处使用文件
    for s in range(2000, 2020):
        s = str(s)
        url = 'https://www.kylc.com/stats/global/yearly/g_population_total/' + s + '.html'
        e = []
        html = gethtml1(url)
        get1(e, html)
        save1(e, s)
    for s in range(2000, 2020):
        s = str(s)
        data = pd.read_csv(r'd:\py\renkou' + s + '.csv', encoding='gbk', index_col=0)
        a = data.iloc[1:9, [2, 8]]
        a.to_csv(r'd:\py\renkou.' + s + '.csv', index=False, header=False)

    ##rank=pd.read_html('https://www.maigoo.com/news/486551.html')        #此处使用pandas
    ##rank[1].to_csv(r'd:\py\Gdp.csv',encoding='gbk',index=False, header=False)
    ##data = pd.read_csv(r'd:\py\Gdp.csv', encoding='gbk', index_col=0)       #此处使用pandas
    ## for i in range(0,5):
    ##  a = data.iloc[0:9, [i, ]]
    # print(a)
    ## i=str(2022-i)
    ## a.to_csv(r'd:\py\Gdp'+i+'.csv', header=False)

    # 某些国家人口
    rank = pd.read_html(
        'https://www.kylc.com/stats/global/yearly_per_country/g_population_total/chn.html')  # 此处使用pandas
    rank[0].to_csv(r'd:\py\人口chn.csv', encoding='gbk', index=False, header=False)
    data = pd.read_csv(r'd:\py\人口chn.csv', encoding='gbk', index_col=0)  # 此处使用pandas
    # print(data)
    a = data.iloc[0:9, [0, 1]]
    a = a.dropna()
    a.to_csv(r'd:\py\renchn.csv', index=False, header=False)  # 中国      #此处使用文件

    rank = pd.read_html('https://www.kylc.com/stats/global/yearly_per_country/g_population_total/ind.html')
    rank[0].to_csv(r'd:\py\人口ind.csv', encoding='gbk', index=False, header=False)
    data = pd.read_csv(r'd:\py\人口ind.csv', encoding='gbk', index_col=0)
    a = data.iloc[0:9, [0, 1]]
    a.to_csv(r'd:\py\renind.csv', index=False, header=False)  # 印度

    rank = pd.read_html('https://www.kylc.com/stats/global/yearly_per_country/g_population_total/pak.html')
    rank[0].to_csv(r'd:\py\人口pak.csv', encoding='gbk', index=False, header=False)
    data = pd.read_csv(r'd:\py\人口pak.csv', encoding='gbk', index_col=0)
    a = data.iloc[0:9, [0, 1]]
    a.to_csv(r'd:\py\renpak.csv', index=False, header=False)  # 巴基斯坦

    rank = pd.read_html('https://www.kylc.com/stats/global/yearly_per_country/g_population_total/bra.html')
    rank[0].to_csv(r'd:\py\人口bra.csv', encoding='gbk', index=False, header=False)
    data = pd.read_csv(r'd:\py\人口bra.csv', encoding='gbk', index_col=0)
    a = data.iloc[0:9, [0, 1]]
    a.to_csv(r'd:\py\renbra.csv', index=False, header=False)  # 巴西

    rank = pd.read_html('https://www.kylc.com/stats/global/yearly_per_country/g_population_total/usa.html')
    rank[0].to_csv(r'd:\py\人口usa.csv', encoding='gbk', index=False, header=False)
    data = pd.read_csv(r'd:\py\人口usa.csv', encoding='gbk', index_col=0)
    a = data.iloc[0:9, [0, 1]]
    a.to_csv(r'd:\py\renusa.csv', index=False, header=False)  # 美国
    # 相关性检验
    rank = pd.read_html('https://www.kylc.com/stats/global/yearly_per_country/g_gdp/chn.html')
    rank[0].to_csv(r'd:\py\ch.csv', encoding='gbk', index=False, header=False)
    data = pd.read_csv(r'd:\py\ch.csv', encoding='gbk', index_col=0)
    a = data.iloc[0:9, [0, 1]]
    a.to_csv(r'd:\py\ch.csv', index=False, header=False)  # 中国GDP

    rank = pd.read_html('https://www.kylc.com/stats/global/yearly_per_country/g_population_total/chn.html')
    rank[0].to_csv(r'd:\py\人口chn.csv', encoding='gbk', index=False, header=False)
    data = pd.read_csv(r'd:\py\人口chn.csv', encoding='gbk', index_col=0)
    a = data.iloc[0:9, [0, 1]]
    a.to_csv(r'd:\py\renchn.csv', index=False, header=False)  # 中国人口


# 以下是对数据的可视化处理函数


def co2():
    rank = pd.read_html('https://data.chinabaogao.com/nengyuan/2020/0164IN22020.html')
    rank[0].to_csv(r'd:\py\co2.csv', encoding='gbk', index=False, header=False)  # 此处使用文件
    data = pd.read_csv(r'd:\py\co2.csv', encoding='gbk', index_col=0)  # 此处使用pandas
    with open(r'd:\py\co2.csv', 'r', encoding='gbk') as f:
        ff = csv.reader(f)
        a = []
        b = []
        j = 0
        for i in ff:
            if j == 0:
                j += 1
                continue
            a.append(i[0])
            b.append(float(i[1][0:3]))
        mpl.rcParams['font.sans-serif'] = ['KaiTi']
        mpl.rcParams['font.serif'] = ['KaiTi']
        fig, ax = plt.subplots()
        ax.plot(a, b, 'o-')
        ax.set(xlabel='(时间)/(指标)', ylabel='二氧化碳排放量（百万吨二氧化碳）',
               title='2010-2018年世界二氧化碳排放量（百万吨二氧化碳）')
        ax.grid()
        plt.show()


def renkou():
    with open(r'd:\py\renchn.csv', 'r', encoding='utf-8') as f:  # 此处使用文件
        aa = csv.reader(f)
        ch = []
        for i in aa:
            ch.append(float(i[0][0:4]))
        # print(ch)

    with open(r'd:\py\renind.csv', 'r', encoding='utf-8') as f:
        aa = csv.reader(f)
        yd = []
        for i in aa:
            yd.append(float(i[0][0:4]))
        # print(yd)

    with open(r'd:\py\renpak.csv', 'r', encoding='utf-8') as f:
        aa = csv.reader(f)
        bj = []
        for i in aa:
            if i == ['2.2亿 (219,731,479)', '2.8679%']:
                bj.append(2.20)
                continue
            bj.append(float(i[0][0:4]))
        # print(bj)

    with open(r'd:\py\renbra.csv', 'r', encoding='utf-8') as f:
        aa = csv.reader(f)
        bx = []
        for i in aa:
            if i == ['2.1亿 (210,166,592)', '2.7431%']:
                bx.append(2.10)
                continue
            if i == ['2.0亿 (199,977,707)', '2.8005%']:
                bx.append(2.00)
                continue
            bx.append(float(i[0][0:4]))
        # print(bx)

    with open(r'd:\py\renusa.csv', 'r', encoding='utf-8') as f:
        aa = csv.reader(f)
        m = []
        for i in aa:
            m.append(float(i[0][0:4]))
        # print(m)

    mpl.rcParams['font.sans-serif'] = ['KaiTi']
    mpl.rcParams['font.serif'] = ['KaiTi']
    fig, ax = plt.subplots()
    nina = ['2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013']
    plt.subplot(2, 1, 1)
    plt.title('中国，印度,巴基斯坦，巴西，美国 2021--2013人口')
    plt.ylabel('人口数/亿')
    plt.plot(nina, ch, label='中国', color='r')
    plt.plot(nina, yd, '--', label='印度')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.xlabel('年')
    plt.ylabel('人口数/亿')
    plt.plot(nina, bj, 'o-', label='巴基斯坦')
    plt.plot(nina, bx, '*-', label='巴西')
    plt.plot(nina, m, '.-', label='美国')
    plt.legend()
    plt.show()


def bingdong():  # 饼图动图
    fig, ax = plt.subplots()

    for s in range(2000, 2020):
        s = str(s)
        mpl.rcParams['font.sans-serif'] = ['KaiTi']
        mpl.rcParams['font.serif'] = ['KaiTi']
        with open(r'd:\py\gdp.' + s + '.csv', 'r', encoding='utf-8') as f:
            ax.cla()
            aa = csv.reader(f)
            g = []
            m = []
            for i in aa:
                g.append(i[0])
                m.append(float(i[1][0:4]))
            explode = (0, 0.2, 0, 0, 0, 0.2, 0.2)
            ax.pie(m, explode=explode, labels=g, autopct='%1.1f%%', shadow=True, startangle=90)
            ax.axis('equal')
            plt.title(s + '年各国GDP占世界比值')
            fig.canvas.draw()
            plt.pause(0.5)
        if s == 2019:
            break

def zhed():  # 折线动图
    fig, ax = plt.subplots()

    mpl.rcParams['font.sans-serif'] = ['KaiTi']
    mpl.rcParams['font.serif'] = ['KaiTi']
    with open(r'd:\py\renkou.2019.csv', 'r', encoding='utf-8') as f:
        ax.cla()
        ff = csv.reader(f)
        a = []
        b = []
        for i in ff:
            a.append(i[0])
            b.append(float(i[1][0:3]))
        plt.plot(a, b, 'o-')
        plt.xlabel('country')
        plt.ylabel('Population')
        plt.title('Population of each country in 2019')
        plt.show()

        print('人口从少到多：')
        print(a)
        e = np.amax(b)  # 此处使用Numpy
        print('人口最大值')
        print(e)


def zhud():  # 柱状动图
    fig, ax = plt.subplots()

    mpl.rcParams['font.sans-serif'] = ['KaiTi']
    mpl.rcParams['font.serif'] = ['KaiTi']
    with open(r'd:\py\renkou.2019.csv', 'r', encoding='utf-8') as f:
        ax.cla()
        ff = csv.reader(f)
        a = []
        b = []
        for i in ff:
            a.append(i[0])
            b.append(float(i[1][0:3]))

        ax.bar(a, b, width=0.5)
        plt.xlabel('country')
        plt.ylabel('Population')
        plt.title('Population of each country in 2019')

        print('人口从少到多：')
        print(a)

        plt.show()


def xin():
    words = "****"
    print('\n')
    for item in words.split():
        letterlist = []
        for y in range(12, -12, -1):
            list_X = []
            letters = ''
            for x in range(-30, 30):
                expression = ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3
                if expression <= 0:
                    letters += item[(x - y) % len(item)]
                else:
                    letters += ' '
            list_X.append(letters)
            letterlist += list_X
        print('\n'.join(letterlist))


def xiangguan():  # 相关性检验

    with open(r'd:\py\ch.csv', 'r', encoding='utf-8') as f:
        aa = csv.reader(f)  # 此处使用文件
        c = []
        for i in aa:
            c.append(float(i[0][0:4]))
        # print(c)

    with open(r'd:\py\renchn.csv', 'r', encoding='utf-8') as f:
        aa = csv.reader(f)
        ch = []
        for i in aa:
            ch.append(float(i[0][0:4]))
    b = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    c1 = pd.Series(c, index=b)
    c2 = pd.Series(ch, index=b)
    hai = pd.concat([c1, c2], axis=1)
    plt.scatter(c, ch)

    plt.pause(0.5)
    plt.cla
    rDf = hai.corr()
    print(rDf)


def xiang(s):  # 包含新功能-箱状图的绘制
    j = 0
    mpl.rcParams['font.sans-serif'] = ['KaiTi']
    mpl.rcParams['font.serif'] = ['KaiTi']
    with open(r'd:\py\gdp' + s + '.csv', 'r', encoding='gbk') as f:
        aa = csv.reader(f)
        # print(aa)
        a = []
        for i in aa:
            j += 1
            if j == 15:
                break
            # print(i)
            if j == 0 or j == 1 or j == 2:
                continue

            a.append(float(i[7][0:3]))
    # print(a)
    plt.boxplot(a, showmeans=True, meanline=True)
    plt.title('全球')
    plt.ylabel('GDP')
    plt.show()

def renkou_sql():
    # 数据库连接配置
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'lws050122',
        'db': 'xinxi',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor
    }
    # 连接到数据库
    connection = pymysql.connect(**db_config)

    try:
        with connection.cursor() as cursor:
            # 创建表
            create_table_sql = """
            CREATE TABLE IF NOT EXISTS renkou (
                id INT AUTO_INCREMENT PRIMARY KEY,
                美国 FLOAT NOT NULL,
                印尼 FLOAT NOT NULL,
                巴西 FLOAT,
                巴基斯坦 FLOAT,
                俄罗斯 FLOAT,
                孟加拉 FLOAT,
                尼日利亚 FLOAT,
                日本 FLOAT
            );
            """

            cursor.execute(create_table_sql)
            connection.commit()

            # 插入数据

            for file_number in range(2000, 2020):  # 有 20 个 CSV 文件
                file_name = f"d:/py/renkou.{file_number}.csv"
                values = [file_number]
                with open(file_name, 'r', encoding='utf-8') as file:
                    reader = csv.reader(file, delimiter=':')
                    # headers = next(reader)  # 跳过标题行
                    # print(reader)
                    for row in reader:
                        value = row[0].split(",")[1].strip("%")
                        # print(row)
                        # print(value)
                        values.append(float(value))
                    # print(values)

                    insert_data_sql = f"""
                    INSERT INTO renkou VALUES{tuple(values)}
                    """
                    cursor.execute(insert_data_sql)
                    connection.commit()

    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()

    finally:
        # 关闭数据库连接
        connection.close()


def gdp_sql():
    # 数据库连接配置
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'lws050122',
        'db': 'xinxi',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor
    }

    # 连接到数据库
    connection = pymysql.connect(**db_config)

    try:
        with connection.cursor() as cursor:
            # 创建表
            create_table_sql = """
            CREATE TABLE IF NOT EXISTS gdp (
                id INT AUTO_INCREMENT PRIMARY KEY,
                美国 FLOAT NOT NULL,
                中国 FLOAT NOT NULL,
                日本 FLOAT,
                德国 FLOAT,
                法国 FLOAT,
                英国 FLOAT,
                巴西 FLOAT
            );
            """

            cursor.execute(create_table_sql)
            connection.commit()

            # 插入数据

            for file_number in range(2000, 2020):  # 有 20 个 CSV 文件
                file_name = f"d:/py/gdp.{file_number}.csv"
                # print(file_name)
                values = [file_number]
                with open(file_name, 'r', encoding='utf-8') as file:
                    reader = csv.reader(file, delimiter=':')
                    # headers = next(reader)  # 跳过标题行
                    # print(reader)
                    for row in reader:
                        value = row[0].split(",")[1].strip("%")
                        # print(row)
                        # print(value)
                        values.append(float(value))
                    # print(values)

                    insert_data_sql = f"""
                    INSERT INTO gdp VALUES{tuple(values)}
                    """
                    cursor.execute(insert_data_sql)
                    connection.commit()

    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()

    finally:
        # 关闭数据库连接
        connection.close()



def a_system_huatu():

  #  if os.path.exists("d:/py"):
    #  shutil.rmtree("d:/py")
  #  os.mkdir("d:/py")


    for i in range(1, 100):
        print('————欢迎使用小小数据画图系统————')
        print('【0】得到2000年到2019年世界各国GDP占比前六名的国家饼状动画')
        print('【1】得到2019年世界各国人口占比前八名的国家折线图')
        print('【2】得到2019年世界各国人口占比前八名的国家柱状图')
        print('【3】得到中国，印度,巴基斯坦，巴西，美国 2021--2013人口折线图')
        print('【4】得到中国近年来人口与GDP增长的相关性图')
        print('【5】得到2000到2019某年全球GDP箱状图')
        print('【6】得到2010—2018年世界二氧化碳排放量折线图')
        print('【7】退出画图系统')
        a = int(input('请输入操作前的序号:'))

        if a == 1:
            Sound(S21)
            zhed()

        if a == 2:
            Sound(S5)
            zhud()

        if a == 3:
            Sound(S1)
            renkou()
        if a == 4:
            Sound(S11)
            xiangguan()
        if a == 5:
            Sound(S18)
            s = input('请输入年份(2000-2019):')
            xiang(s)
        if a == 6:
            Sound(S16)
            co2()
        if a == 7:
            Sound(S7)
            xin()
            print('欢迎下次使用')
            break
        if a == 0:
            Sound(S9)
            while True:
                bingdong()
                break
        print('输入任意字符返回画图菜单栏：')
        input()
        Sound(S22)

def a_system_guanli():

    def main1():
        conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='lws050122'
        )
        cus = conn.cursor()  # 创建游标
        while True:
            print('*' * 22+"欢迎使用数据管理系统"+'*'*22)
            print('【1】增加数据')
            print('【2】删除数据')
            print('【3】修改数据')
            print('【4】查询数据')
            print('【5】退出系统')
            print('*' * 54)
            n = input('请输入你要执行的命令:\n')
            if n == '1':
                Sound(S2)
                add_data(cus, conn)
                for i in range(3, 0, -1):
                    print(i)
                    time.sleep(1)

            elif n == '2':
                Sound(S11)
                del_data(cus, conn)
                for i in range(3, 0, -1):
                    print(i)
                    time.sleep(1)
            elif n == '3':
                Sound(S5)
                cha_data(cus, conn)
                for i in range(3, 0, -1):
                    print(i)
                    time.sleep(1)
            elif n == '4':
                Sound(S7)
                inq_data(cus, conn)
                for i in range(3, 0, -1):
                    print(i)
                    time.sleep(1)
            elif n == '5':
                Sound(S21)
                cus.close()  # 关闭游标
                conn.close()  # 关闭数据库连接
                print("3秒后退出系统……")
                for i in range(3, 0, -1):
                    print(i)
                    time.sleep(1)
                print("谢谢您的使用，希望您给一个5*好评！！！")
                break
            else:
                print('输入错误请重新输入:\n')

    def add_data(cus, conn):  # 增加数据
        year = input('请输入年份:')
        mg = input('请输入美国人口:')
        yn = input('请输入印尼人口:')
        bx = input('请输入巴西人口:')
        bjst = input('请输入巴基斯坦人口:')
        els = input('请输入俄罗斯人口:')
        mjl = input('请输入孟加拉人口:')
        nrly = input('请输入尼日利亚人口:')
        rb = input('请输入日本人口')
        sql = f"insert into xinxi.renkou values ('{year}','{mg}','{yn}','{bx}','{bjst}','{els}','{mjl}','{nrly}','{rb}')"
        cus.execute(sql)
        conn.commit()
        print('增加成功,'
              '稍等3秒后返回主菜单')
        pass

    def del_data(cus, conn):  # 删除数据
        year = input('请输入需要删除的年份:\n')
        sql = f"select * from xinxi.renkou where id='{year}'"
        n = cus.execute(sql)
        # conn.commit()   # 提交信息
        # print(n)
        if n:
            sql = f"delete from xinxi.renkou where id='{year}'"
            cus.execute(sql)
            conn.commit()
            print('删除成功,'
                  '稍等3秒后返回主菜单')
        else:
            print('查无此年,'
                  '稍等3秒后返回主菜单')

    def cha_data(cus, conn):  # 修改数据
        year = input('请输入需要修改的年份:\n')
        sql = f"select * from xinxi.renkou where id='{year}'"
        n = cus.execute(sql)
        # conn.commit()   # 提交信息
        # print(n) 
        if n:
            print("开始修改…………")
            time.sleep(3)
            year1 = input('请输入修改后年份:')
            mg = input('请输入美国修改后人口:')
            yn = input('请输入印尼修改后人口:')
            bx = input('请输入巴西修改后人口:')
            bjst = input('请输入巴基斯坦修改后人口:')
            els = input('请输入俄罗斯修改后人口:')
            mjl = input('请输入孟加拉修改后人口:')
            nrly = input('请输入尼日利亚修改后人口:')
            rb = input('请输入日本修改后人口：')
            sql = f"update xinxi.renkou set id={year1},美国={mg},印尼={yn},巴西={bx},巴基斯坦={bjst},俄罗斯={els},孟加拉={mjl},尼日利亚={nrly},日本={rb} where id={year}"
            # print(sql)
            cus.execute(sql)
            conn.commit()
            print('修改成功,'
                  '稍等3秒后返回主菜单')
        else:
            print('查无此年,'
                  '稍等3秒后返回主菜单')

    def inq_data(cus, conn):  # 查询数据
        year = input('请输入需要查询的数据年份:\n')
        Sound(S12)
        sql = f"select * from xinxi.renkou where id='{year}'"
        n = cus.execute(sql)
        if n:
            sql = f"select * from xinxi.renkou where id='{year}'"
            cus.execute(sql)  # 接收数据
            u = cus.fetchall()
            # conn.commit()
            # print(u)
            print(f'{year}的美国人口为：', u[0][1])
            print(f'{year}的印尼人口为：', u[0][2])
            print(f'{year}的巴西人口为', u[0][3])
            print(f'{year}的巴基斯坦人口为：', u[0][4])
            print(f'{year}的俄罗斯人口为：', u[0][5])
            print(f'{year}的孟加拉人口为：', u[0][6])
            print(f'{year}的尼日利亚人为：', u[0][7])
            print(f'{year}的日本人口为：', u[0][8])
        else:
            print('查无此年,'
                  '稍等3秒后返回主菜单')

    main1()


def main():

    if os.path.exists("d:/py"):
        shutil.rmtree("d:/py")
    os.mkdir("d:/py")
    pa()
    renkou_sql()
    gdp_sql()


    while True:
        print("--------------------欢迎使用数据画图双系统-------------------")
        print(" 【1】进入数据画图系统")
        print(" 【2】进入数据管理系统")
        print(" 【3】退出系统")
        print("*" * 49)
        res = int(input("请做出你的选择：\n"))
        if res == 1:
            Sound(S9)
            a_system_huatu()
            print("即将返回双系统……")
            time.sleep(2)
        elif res == 2:
            Sound(S21)
            a_system_guanli()
            print("即将返回双系统……")
            time.sleep(2)
        else:
            Sound(S13)
            time.sleep(1)
            print("谢谢您的使用，祝你生活愉快！！！")
            break


if __name__ == "__main__":
    S1 = r'傲娇\01.被偷的是我的…真是的，不说了啦笨蛋!!你让人家怎么说嘛!!.wav'
    S2 = r'傲娇\02.变态 变态 变态 变态 变态 你这个大变态!!我再也不理你了….wav'
    S3 = r'傲娇\03.别把拉面挑这么高，快点吃！ 什么？帮你吹凉一点？去死！.wav'
    S4 = r'傲娇\04.别不理我嘛…我道歉还不行吗….wav'
    S5 = r'傲娇\05.别离我这么近…丢死人了….wav'
    S7 = r'傲娇\07.吵死了吵死了吵死了! 真是吵死了!.wav'
    S8 = r'傲娇\08.给我等一下! 你这个木头人，为什么…为什么你就是注意不到嘛!.wav'
    S9 = r'傲娇\09.尽管放马过来吧! 让我打你个落花流水!.wav'
    S11 = r'傲娇\11.就算你送我琉璃色的发带，我也绝对不会开心的哦!.wav'
    S12 = r'傲娇\12.哭…我的胸部….wav'
    S13 = r'傲娇\13.留在我身边! 一辈子! 没异议吧!.wav'
    S16 = r'傲娇\16.你、你只要看着我一个人就够了!.wav'
    S18 = r'傲娇\18.你可别胡思乱想，我有不是特地为你做的.wav'
    S21 = r"傲娇\21.你这个笨蛋! 根本不知道我的想法….wav"
    S19 = r"傲娇\19.你可不许对我说“No”哦.wav"
    S22 = r'傲娇\22.你这家伙，找块豆腐一头撞死算了!.wav'
    S24 = r'傲娇\24.你至少和我联系一下啊…人家好担心的说….wav'
    S28 = r'傲娇\28.什么利用价值都没有，你这种废柴.wav'
    S29 = r'傲娇\29.是我选的你，你可别以为是你给了我机会哦!.wav'
    S32 = r'傲娇\32.我、我才没有为你担心!.wav'
    S35 = r'傲娇\35.我才没有吃醋!都给你说了没有了嘛!.wav'
    S41 = r'傲娇\41.真是讨厌讨厌讨厌!!你要想做那种事情我不理你了不理你了!.wav'
    main()