class laptop:
    model = ""
    time = ""
    color = ""
    weight =""
    cpu = ""
    ram = ""
    disk = ""

    def game(self, game):
        print(self.color,self.model, "可以打游戏", game)

    def office(self):
        print(self.color,self.model,"可以办公")


laptop = laptop()
laptop.model="华硕 U4000"
laptop.color="灰色"
laptop.game("扫雷")
laptop.office()