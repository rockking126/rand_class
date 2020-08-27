import datetime
import random
import sys
import time

import xlrd
from PyQt5.QtCore import *
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import ui_main


def get_names(info_list):
    nameslist = []
    for each in info_list:
        nameslist.append(each[1])
    return nameslist


def get_data():
    workbook = xlrd.open_workbook(r'names.xlsx')
    sheet = workbook.sheet_by_index(0)  # sheet索引从0开始
    sheet1 = workbook.sheet_by_index(1)  # sheet索引从0开始

    data_list = sheet._cell_values
    teacher_list = sheet1._cell_values

    return data_list[1:], teacher_list[1:]


def bili_caculate(n_list):
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
        cage = cage + delta.days

    ccage = round(cage / len(n_list), 3)
    ccsex = round(csex / len(n_list), 3)
    sss = '\n男女比例：' + str(round(ccsex * 100, 1)) + "平均年龄：6岁+" + str(round(ccage, 0)) + "天\n"
    # print(sss)
    return ccsex, sss


def caculate_count(name_list):
    a = [[], [], [], [], [], []]
    i = 0
    c = [[], [], [], [], [], []]
    boys, girls = [], []
    tmp_list = name_list.copy()
    for each in tmp_list:
        if each[2] == '男':
            boys.append(each)
        else:
            girls.append(each)
    while True:
        if i < 6:
            if len(boys) > 0:
                t = boys.pop()
                a[i].append(t)
                i = i + 1
            elif len(girls) > 0:
                t = girls.pop()
                a[i].append(t)
                i = i + 1
            else:
                break
        else:
            i = 0
    for j in range(6):
        boy, girl = 0, 0
        for each in a[j]:
            if each[2] == '男':
                boy = boy + 1
            else:
                girl = girl + 1
        c[j] = [len(a[j]), boy, girl]
    return c


class MainWindow(QMainWindow, ui_main.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.class_group_show = [[], [], [], [], [], []]
        self.class_group = [[], [], [], [], [], []]

        self.setupUi(self)  # gets defined in the UI file
        self.setup_ui_style()

        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.new)  # 计时结束调用operate()方法
        self.timer.start(500)  # 设置计时间隔并启动

        self.start_flag = False
        self.teacher_round = False
        self.step = 0

        self.tmp = []

        self.palette0 = QPalette()
        self.palette0.setColor(self.backgroundRole(), QColor(96, 96, 96))  # 设置背景颜色
        self.palette0.setBrush(self.backgroundRole(), QBrush(QPixmap('bg1.jpg')))  # 设置背景图片
        self.setPalette(self.palette0)

        self.datalist = []
        self.teacherlist = []

    def load_data(self):
        self.step = 1
        self.datalist, self.teacherlist = get_data()
        self.all_name.setText('教师：\n' + str(self.teacherlist) + '\n学生名单：\n' + str(get_names(self.datalist)))

    def setup_ui_style(self):
        style_fonts = "QLabel{color:rgb(255,255,255);" \
                      "}"
        self.all_name.setStyleSheet(style_fonts)
        self.statues_show.setStyleSheet(style_fonts)
        self.label_1.setStyleSheet(style_fonts)
        self.label_2.setStyleSheet(style_fonts)
        self.label_3.setStyleSheet(style_fonts)
        self.label_4.setStyleSheet(style_fonts)
        self.label_5.setStyleSheet(style_fonts)
        self.label_6.setStyleSheet(style_fonts)
        self.start.clicked.connect(self.click_start)
        self.getlist.clicked.connect(self.click_load)
        self.pushButton.clicked.connect(self.click_teacher)
        self.exportdata.clicked.connect(self.export_xls)
        self.quit_bt.clicked.connect(QCoreApplication.quit)
        self.all_name.setWordWrap(True)
        self.statues_show.setAlignment(Qt.AlignLeading | Qt.AlignHCenter | Qt.AlignVCenter)
        self.statues_show.setText('测试分班')

    def click_load(self):
        self.class_group = [[], [], [], [], [], []]
        self.load_data()
        class_count_data = caculate_count(self.datalist)
        print(str('每班人数分配\n' + str(class_count_data)))

    def click_teacher(self):
        if self.step == 1:
            self.step = 2
            self.timer.start(50)  # 设置计时间隔并启动

        if self.step == 2:
            if self.teacher_round is True:
                self.teacher_round = False
                self.pushButton.setText('2.教师分班')
            else:
                self.teacher_round = True
                self.pushButton.setText('2.按下停止')
        else:
            QMessageBox.information(self, '信息提示对话框', '请按步骤操作！')

    def click_start(self):
        if self.step == 2:
            self.step = 3

            self.timer.start(100)  # 设置计时间隔并启动

            self.tmp = self.datalist.copy()
            self.class_group = [[], [], [], [], [], []]

            self.form_data()

            self.start_flag = True
        else:
            QMessageBox.information(self, '信息提示对话框', '请按步骤操作！')

    def form_data(self):
        class_count_data = caculate_count(self.tmp)
        print(str('每班人数分配' + str(class_count_data)))
        class_count_data_for_cousume = class_count_data

        gg = self.tmp.copy()

        while gg:
            st = gg.pop()
            for i in range(6):
                if st[2] == '男':
                    if class_count_data_for_cousume[i][1] > 0:
                        class_count_data_for_cousume[i][1] = class_count_data_for_cousume[i][1] - 1
                        self.class_group[i].append(st)
                        break
                else:
                    if class_count_data_for_cousume[i][2] > 0:
                        class_count_data_for_cousume[i][2] = class_count_data_for_cousume[i][2] - 1
                        self.class_group[i].append(st)
                        break

    def new(self):
        if self.teacher_round is True:
            random.shuffle(self.teacherlist)
            self.statues_show.setText('教师顺序:\n' + str(self.teacherlist))
        else:
            pass
        if self.start_flag and (self.teacher_round is False):
            for i in range(6):
                if self.class_group[i]:
                    t = self.class_group[i].pop()
                    self.class_group_show[i].append(t)
                    show_s = '随机抽取第' + str(self.datalist.index(t)) + '位\n' + str(t) + '，\n分班至：' + str(i + 1) + '班'
                    self.statues_show.setText(show_s)
                    self.datalist.remove(t)
                self.update_show()

    def update_show(self):
        a, ss = bili_caculate(self.class_group_show[0])
        self.label_1.setText('1班：' + str(self.teacherlist[0]) + ss + str(get_names(self.class_group_show[0])))
        a, ss = bili_caculate(self.class_group_show[1])
        self.label_2.setText('2班：' + str(self.teacherlist[1]) + ss + str(get_names(self.class_group_show[1])))
        a, ss = bili_caculate(self.class_group_show[2])
        self.label_3.setText('3班：' + str(self.teacherlist[2]) + ss + str(get_names(self.class_group_show[2])))
        a, ss = bili_caculate(self.class_group_show[3])
        self.label_4.setText('4班：' + str(self.teacherlist[3]) + ss + str(get_names(self.class_group_show[3])))
        a, ss = bili_caculate(self.class_group_show[4])
        self.label_5.setText('5班：' + str(self.teacherlist[4]) + ss + str(get_names(self.class_group_show[4])))
        a, ss = bili_caculate(self.class_group_show[5])
        self.label_6.setText('6班：' + str(self.teacherlist[5]) + ss + str(get_names(self.class_group_show[5])))

        if self.datalist:
            style_fonts = "QLabel{color:rgb(255,255,255);" \
                          "font-size:15px;}"
            self.all_name.setStyleSheet(style_fonts)
            self.all_name.setText(str(get_names(self.datalist)))
            # print(self.datalist)
        else:
            style_fonts = "QLabel{color:rgb(255,255,255);" \
                          "font-size:25px;}"
            self.all_name.setStyleSheet(style_fonts)
            self.all_name.setText(str('分班说明：\n'
                                      '1.系统从上表中随机抽取学生，顺序放入各班;\n'
                                      '2.过程中会自动平衡男女生比例，先处理男生；\n'
                                      '3.双胞胎如果需要分配到同一个班，只由一人参与摇号；\n'
                                      '4.该系统使用python编写，开放源码，欢迎fork;\n'
                                      '5.程序源代码见 https://github.com/rockking126/rand_class '))

    def export_xls(self):
        ticks = time.time()

        output = open(str(ticks) + '分班结果.xls', 'w', encoding='gbk')
        output.write('name\tgender\tstatus\tage\n')
        list1 = self.class_group_show
        for i in range(len(list1)):
            output.write(str(self.teacherlist[i]) + '\n')
            for j in range(len(list1[i])):
                output.write(str(list1[i][j]))  # write函数不能写int类型的参数，所以使用str()转化
                output.write('\n')  # 相当于Tab一下，换一个单元格
        output.close()
        QMessageBox.information(self, '信息提示对话框', '导出成功！')


def main():
    app = QApplication(sys.argv)

    form = MainWindow()
    form.show()
    # form.showFullScreen()

    sys.exit(app.exec_())

# python bit to figure how who started This


if __name__ == "__main__":
    main()
