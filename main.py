#coding:utf-8
import itchat
import matplotlib.pyplot as plt

class DataAnalysis:
    '''
    wechat gender analysis
    '''
    itchat = itchat
    friends = None
    def __init__(self):
        self.itchat.login()
        self.friends = self.itchat.get_friends()

    def wechat_user_gender_report(self):

        male_count = 0
        famale_count = 0
        other_count = 0
        for friend in self.friends[1:]:
            gender = friend["Sex"]
            if gender == 1:
                male_count += 1
            elif gender == 2:
                famale_count += 1
            else:
                other_count += 1
        total = len(self.friends[1:])
        print ("-----wechat friends analysis report-----")
        print ("total friends count:{}".format(total))
        print ("male friends count:%d, percent:%.2f%%"%(male_count,float(male_count)/total*100))
        print("famale friends count:%d, percent:%.2f%%" % (famale_count, float(famale_count) / total * 100))
        print("other friends count:%d, percent:%.2f%%" % (other_count, float(other_count) / total * 100))

        datas = [male_count,famale_count,other_count]
        labels = ["Male","Famale","Other"]
        self.get_pie(datas,labels)

    '''
    wechat area analysis
    '''
    def wechat_user_location_report(self):
        friends = self.friends
        province_dict = {}
        for friend in friends[1:]:
            province = friend["Province"]
            if province == "":
                province = "未知"
            else:
                province_dict[province] = province_dict.get(province, 0) + 1

        print(province_dict)
        data_list = []
        for item in province_dict.items():
            data_list.append(item)
        data_list.sort(key=lambda item: item[1], reverse=True)
        top10_datas = data_list[:11]
        print(top10_datas)
        datas_list = []
        labels_list = []
        for data in top10_datas:
            datas_list.append(data[1])
            labels_list.append(data[0])
        self.get_bar(datas_list, labels_list)

    '''
    function : generate pie chart 
    '''

    def get_pie(self, datas, labels):
        # 设置字符集
        plt.rcParams["font.sans-serif"] = ["simhei"]
        plt.figure(figsize=(8, 6), dpi=80)
        plt.axes(aspect=1)
        plt.pie(datas, labels=labels, autopct="%.2f%%", shadow=False)
        plt.title("wechat friends analysis pie chart")
        plt.show()

    def get_bar(self, datas, labels):
        # 设置字符集
        # zhfont = mpl.font_manager.FontProperties(fname = '/usr/share/fonts/opentype/noto/NotoSansCJK-Thin.ttc')
        plt.rcParams[u"font.sans-serif"] = ["simhei"]
        plt.xlabel("province")
        plt.ylabel("count")
        plt.xticks(range(len(datas)), labels)
        plt.bar(range(len(datas)), datas, color="rgb")
        plt.title("wechat friends analysis bar chart")
        plt.show()


if __name__ == "__main__":
    das = DataAnalysis()
    das.wechat_user_gender_report()
    das.wechat_user_location_report()