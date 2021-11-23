class monkey:
    type = ""
    sex = ""
    color = ""
    weight =""

    def make_fire(self, tool):
        print(self.color,self.sex,self.type, "可以使用", tool, "来造火")

    def learn(self, what):
        print(self.color,self.sex,self.type, "可以学习", what)


monkey1 = monkey()
monkey1.type="金丝猴"
monkey1.color="棕色"
monkey1.sex="母"
monkey1.weight="80"
monkey1.make_fire("石头")
monkey1.learn('骑车、' + '唱歌')