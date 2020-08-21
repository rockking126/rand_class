import xlrd
import xlwt, time
import random
import pandas as pd

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import ui_main
from PyQt5.QtCore import QTimer

import qdarkstyle
import random, datetime

import time, sys


#
#
# # a = random.choice(datalist)
# a = random.randrange(0, len(datalist), 1)
#

#
# now = datetime.datetime.now()
# now.strftime('%Y-%m-%d %H:%M:%S')


def write_excel():
    # 2. 创建Excel工作薄
    myWorkbook = xlwt.Workbook()
    # 3. 添加Excel工作表
    mySheet = myWorkbook.add_sheet('A Test Sheet')
    # 4. 写入数据
    myStyle = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')  # 数据格式
    mySheet.write(i, j, 1234.56, myStyle)
    mySheet.write(2, 0, 1)  # 写入A3，数值等于1
    mySheet.write(2, 1, 1)  # 写入B3，数值等于1
    mySheet.write(2, 2, xlwt.Formula("A3+B3"))  # 写入C3，数值等于2（A3+B3）
    # 5. 保存
    myWorkbook.save('excelFile.xls')


class MainWindow(QMainWindow, ui_main.Ui_MainWindow):
    statA = [0, 1, 0]
    statB = [0, 1, 0]
    statC = [0, 1, 0]

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # gets defined in the UI file
        self.setup_ui_style()
        self.all_name.setWordWrap(True)
        self.statues_show.setAlignment(Qt.AlignLeading | Qt.AlignHCenter | Qt.AlignVCenter)
        self.class_group = [[], [], [], [], [], []]
        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.operate)  # 计时结束调用operate()方法
        self.timer.start(500)  # 设置计时间隔并启动
        self.start_flag = False
        self.teacher_round = False
        self.tmp = []
        self.i = 0
        self.a = 0

        self.datalist = []
        self.teacherlist = []
        # self.statues_show.setAlignment(Qt.AlignLeft)
        self.statues_show.setText('分班说明：\n1.系统从上表中随机抽取学生，顺序放入各班;\n2.为方便平衡男女生比例，先处理男生；\n3.该系统使用python编写，源码见https://github.com/rockking126/rand_class')

    def load_data(self):
        namelist = []
        self.datalist, self.teacherlist = self.get_data()

        for each in self.datalist:
            namelist.append(each[1])
        self.all_name.setText('教师：\n' + str(self.teacherlist) + '\n学生名单：\n' + str(namelist))

    def get_data(self):
        workbook = xlrd.open_workbook(r'names.xlsx')

        # 获取所有sheet
        sheet_name = workbook.sheet_names()[0]

        # 根据sheet索引或者名称获取sheet内容
        sheet = workbook.sheet_by_index(0)  # sheet索引从0开始
        sheet1 = workbook.sheet_by_index(1)  # sheet索引从0开始

        datalist = sheet._cell_values
        teacherlist = sheet1._cell_values


        return datalist[1:],teacherlist[1:]

    def setup_ui_style(self):
        style_fonts = "QLabel{color:rgb(255,255,255);" \
                      "font-size:18px;" \
                      "background-color: rgb(105,145,197);}"
        # self.all_name.setStyleSheet(style_fonts)
        self.start.clicked.connect(self.click_start)
        self.getlist.clicked.connect(self.load_data)
        self.pushButton.clicked.connect(self.click_teacher)
        self.quit_bt.clicked.connect(QCoreApplication.quit)

    def click_start(self):
        self.timer.start(10)  # 设置计时间隔并启动
        self.tmp = self.datalist
        self.class_group = [[], [], [], [], [], []]

        self.start_flag = True

    def click_teacher(self):
        self.timer.start(50)  # 设置计时间隔并启动

        if self.teacher_round is True:
            self.teacher_round = False
            self.pushButton.setText('2.教师分班')

        else:
            self.teacher_round = True
            self.pushButton.setText('按下停止')

    def get_names(self, info_list):
        nameslist = []
        for each in info_list:
            nameslist.append(each[1])
        return nameslist

    def sex_fliter(self, wlist, index):

        if wlist[index][2] == '男':
            return False
        for each in wlist:
            if each[2] == '男':
                return True
        return False

    def operate(self):

        # self.statues_show.setAlignment(Qt.AlignCenter)
        if self.teacher_round is True:
            random.shuffle(self.teacherlist)
            self.statues_show.setText('教师顺序:\n' + str(self.teacherlist))
        else:
            pass
        if self.start_flag is True:
            self.update_show()
            num_stu = len(self.tmp)
            if (self.i < 6) and (num_stu > 0):
                self.a = random.randrange(0, num_stu, 1)
                while self.sex_fliter(self.tmp, self.a):  # 先随机男生，完成后随机女生，均衡各班男女比例
                    self.a = random.randrange(0, num_stu, 1)
                show_s = '随机抽取第' + str(self.a) + '位\n学生:' + str(self.tmp[self.a]) + '，\n分班至：' + str(self.i+1) + '班'
                # print('随机抽取第' + str(a) + '位学生，分班至：' + str(self.i + 1) + '班')
                self.statues_show.setText(show_s)
                # print(self.tmp[a])
                self.class_group[self.i].append(self.tmp[self.a])
                self.tmp.pop(self.a)
                self.i = self.i + 1
            else:
                self.i = 0
            self.update_show()

        else:
            pass

    def bili_caculate(self, n_list):
        csex = 0
        cage = 0
        d1 = datetime.datetime.strptime('2012-08-31', '%Y-%m-%d')
        if len(n_list) == 0:
            return 0, ''
        for each in n_list:
            if each[2] == '男':
                csex = csex + 1
            d2 = datetime.datetime.strptime(each[4], '%Y-%m-%d')
            delta = d2 - d1
            # print('年龄：6岁+ ' + str(delta.days) + '天')
            cage = cage + delta.days

        ccage = round(cage / len(n_list), 3)
        ccsex = round(csex / len(n_list), 3)
        sss = '\n男女比例：' + str(round(ccsex * 100, 1)) + "\n平均年龄：6岁+" + str(round(ccage, 0)) + "天"
        # print(sss)
        return csex, sss

    def update_show(self):
        self.label_1.setText(str(self.get_names(self.class_group[0])))
        self.label_2.setText(str(self.get_names(self.class_group[1])))
        self.label_3.setText(str(self.get_names(self.class_group[2])))
        self.label_4.setText(str(self.get_names(self.class_group[3])))
        self.label_5.setText(str(self.get_names(self.class_group[4])))
        self.label_6.setText(str(self.get_names(self.class_group[5])))

        a, ss = self.bili_caculate(self.class_group[0])
        self.label_7.setText('1班：' + str(self.teacherlist[0]) + ss)
        a, ss = self.bili_caculate(self.class_group[1])
        self.label_8.setText('2班：' + str(self.teacherlist[1]) + ss)
        a, ss = self.bili_caculate(self.class_group[2])
        self.label_9.setText('3班：' + str(self.teacherlist[2]) + ss)
        a, ss = self.bili_caculate(self.class_group[3])
        self.label_10.setText('4班：' + str(self.teacherlist[3]) + ss)
        a, ss = self.bili_caculate(self.class_group[4])
        self.label_11.setText('5班：' + str(self.teacherlist[4]) + ss)
        a, ss = self.bili_caculate(self.class_group[5])
        self.label_12.setText('6班：' + str(self.teacherlist[5]) + ss)

        if self.tmp is not []:
            namelist = []
            for each in self.tmp:
                namelist.append(each[1])
            self.all_name.setText(str(namelist))
            # print(namelist)
        else:
            self.all_name.setText(str(''))


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    form = MainWindow()
    form.show()
    # form.detect()
    # form.showFullScreen()

    sys.exit(app.exec_())


# python bit to figure how who started This
if __name__ == "__main__":
    main()
