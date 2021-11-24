class OldChef:
    __username = ""
    __age = 0
    def setUsername(self,username):
        if username == "":
            print("姓名不能为空！")
        else:
            self.__username = username

    def getUsername(self):
        return self.__username


    def setAge(self,age):
        if age > 120 or  age < 0:
            print("输入非法！别瞎弄!")
        else:
            self.__age = age

    def getAge(self):
        return self.__age

    def cake(self):
        pass
class NewChef(OldChef):
    def fried(self):
        pass

class BserChef(NewChef):
    def cake(self):
        print("蒸饭",end="")
    def fried(self):
        print("炒菜", end="")

b=BserChef()
b.setUsername("王大厨")
b.setAge(23)
b.cake()
b.fried()