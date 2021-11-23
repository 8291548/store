class student:
    no = ""
    name = ""
    age = ""
    sex = ""
    height = ""
    weight = ""
    score = ""
    addr = ""
    phone = ""

    def learn(self, time):
        print(self.name, "已经学习了", time, "小时了")
    def game(self, game):
        print(self.name, "喜欢玩", game)
    def code(self,rows):
        print(self.name, "代码写了", rows, "行")
    def sum(self, num1, num2):
        sum = num1 + num2
        print("求和结果:", sum)

student = student()
student.name="小华"
student.game("蜘蛛纸牌")
student.learn(10)
student.code(25)
student.sum(1,2)