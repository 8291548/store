class Person:
    username = "战战"
    age= "20"
    sex = "男"
    charge=""
    brand=""
    capacity=""
    size=""
    awaitt=""
    integral=""

    def note(self,messages):
        print(self.username,messages)
    def phone(self, number, hour, charge,):
        if number=="":
            print("电话为空号")
        elif charge<1:
            print("话费不足")
        else:
            if hour<10:
                money=hour*1
                jifen=hour*15
                print("话费为",money,"积分为",jifen)
            elif hour>10 and hour<20:
                money=hour*0.8
                jifen=hour*39
                print("话费为",money,"积分为",jifen)
            else:
                money = hour * 0.65
                jifen = hour * 48
                print("话费为", money, "积分为", jifen)

p=Person()
p.note("发送10086查看话费余额")
p.phone("18932185951",11,3)