'''
    方法：
        就是解决某一类问题的模型。
    如何申明一个方法？
    def 方法的名称():
        方法体

   任务1：
        旅游的导航系统 + 商城结合在一起。
    任务2：
        看下工商银行的系统。
'''
shop = [
    ["牙膏",21.5],
    ["泡面",6],
    ["矿泉水",12],
    ["芒果干",56],
    ["草莓干",25],
    ["辣条",3],
    ["洗衣粉",25],
    ["利群",160],
    ["红塔山",130]
]

mycart = []  # 空的购物车

# 初始化余额
salary = input("请输入您的钱包余额：") # "356"  -->  356
sal = salary = int(salary)   # "356" --> 356

city = {
    "北京":{
        "昌平":{
            "八达岭":["八达岭长城"],
            "回龙观":["永旺超市","永辉超市","呷哺呷哺"]
        },
        "朝阳":{
            "景观":["玉渊潭公园"]
        },
        "海淀":{
            "高校":["清华","北大"],
            "公园":["香山","植物园"],
            "博物馆":["军事博物馆","国家地质公园"]
        }
    },
    "上海":{

    }
}

def showCity(data):
    for i in data:
        print(i)

while True:
    print("---------------欢迎来到Jason旅行社-----------------")
    print("有以下城市可以去：")
    showCity(city)
    print("请输入您要去的城市：")
    chose = input("")

    if chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break
    elif chose not in city:
        print("输入非法！请重新输入：")
    else:
        showCity(city[chose])
        chose2 = input("请输入您要去二级城市：")
        if chose2 == "q" or chose2 == "Q":
            print("欢迎下次光临！")
            break
        elif chose2 not in city[chose]:
            print("输入错误，别瞎弄！")

        else:
            showCity(city[chose][chose2])
            print("请输入要去的具体景点：")
            chose3 = input("")
            if chose3 == "q" or chose3 == "Q":
                print("欢迎下次光临！")
                break
            elif chose3 not in city[chose][chose2]:
                print("不好意思，没有这个景点！别瞎弄！")
            else:
                showCity(city[chose][chose2][chose3])
                print("每张票1000元/人！")
                yes=input("是否买点纪念品？是or否")
                while yes=="是":
                    # 展示商品架
                    for key, value in enumerate(shop):
                        print(key, value)

                    chose = input("请输入您要买的商品编号：")  # "9aa" --> 9
                    if chose.isdigit():
                        chose = int(chose)
                        if chose >= len(shop):
                            print("温馨提示：这个商品不存在！别瞎弄！")
                        else:
                            if salary < shop[chose][1]:
                                print("温馨提示：穷鬼，没钱，别瞎买！")
                            else:
                                salary = salary - shop[chose][1]
                                mycart.append(shop[chose])
                                print(shop[chose][0], "添加购物车成功！余额还剩:￥", salary)
                    elif chose == "q" or chose == "Q":
                        # 打印购物小条
                        print("------------欢迎下次光临Jason小商店--------------")
                        print("以下是您的购物小条，请拿好：")
                        print("--------------------------------------------------")
                        for key, value in enumerate(mycart):
                            print(key, value)
                        print("-------------------------------------------------")
                        print("您本次还剩余额为：￥", salary, "，本次消费：￥", (sal - salary))
                        break  # 跳出循环
                    else:
                        print("兄弟，商品不存在！别瞎弄！")


















