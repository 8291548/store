class car:
    model = ""
    num = 0
    color = ""
    weight = 0.0
    size = 0.0

    def run(self,runn):
        print("一辆",self.num,"个轮子","油箱储存大小为",self.size,"升",self.color,self.model, "可以跑")


car1 = car()
car1.model="法拉利"
car1.color="红色"
car1.num=4
car1.weight=10000
car1.size=2.6
car1.run("跑")

car2 = car()
car2.model="宝马"
car2.color="白色"
car2.num=4
car2.weight=10000
car2.size=2.6
car2.run("跑")

car3 = car()
car3.model="铃木"
car3.color="黑色"
car3.num=4
car3.weight=10000
car3.size=3.3
car3.run("跑")

car4 = car()
car4.model="五菱"
car4.color="银色"
car4.num=4
car4.weight=10000
car4.size=4.1
car4.run("跑")

car4 = car()
car4.model="拖拉机"
car4.color="绿色"
car4.num=3
car4.weight=10000
car4.size=4.1
car4.run("跑")