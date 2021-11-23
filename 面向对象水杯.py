class Cup:
    color = ""
    height = ""
    volume =""
    texture= ""

    def function(self,gongneng):
        print("一个",self.color,self.height,self.volume,self.texture,"的水杯可以",gongneng)
c = Cup()
c.color="黄色"
c.height="12厘米"
c.volume="12立方米"
c.texture="金属材质"
c.function("存放液体")
