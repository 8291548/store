class Laptop:
    size = ""
    cpu= ""
    memsize=""
    price=""
    awaitt=""

    def dazi(self,xuexi):
        print("屏幕大小为",self.size,"价格为",self.price,"cpu型号为",self.cpu,"内存大小为",self.memsize,"待机时常为",self.awaitt,"的笔记本电脑可以",xuexi)

    def youxi(self,game):
        print("屏幕大小为",self.size,"价格为",self.price,"cpu型号为",self.cpu,"内存大小为",self.memsize,"待机时常为",self.awaitt,"的笔记本电脑可以",game)

    def shipin(self,video):
        print("屏幕大小为",self.size,"价格为",self.price,"cpu型号为",self.cpu,"内存大小为",self.memsize,"待机时常为",self.awaitt,"的笔记本电脑可以",video)

p = Laptop()
p.size = "16寸"
p.awaitt="16小时"
p.memsize="16G"
p.cpu="K6-2+"
p.price="8000"

p.dazi("打字")
p.youxi("玩游戏")
p.shipin("看视频")
