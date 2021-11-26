from threading import Thread
import time

kep = 0  # 蛋糕篮子（全剧变量）


class chef(Thread):  # 定义一个厨师类
    _name = ''
    kep_sum = 0

    def run(self) -> None:  # 重构run方法
        global kep  # 调用全局变量 kep
        start = time.time()     # 获取开始时间
        while True:
            end = time.time()   # 获取结束时间
            if (end - start) < 60:  # 判断前后时间差是否在一分钟内
                if kep < 500:  # 判断篮子里蛋挞个数：500以内
                    self.kep_sum = self.kep_sum + 1  # 厨师做蛋挞的个数
                    kep = kep + 1  # 篮子内蛋挞个数
                else:  # 500以上停留三秒
                    time.sleep(3)
            else:       # 大于一分钟结束执行
                break
        return self.kep_sum     # 返回做蛋挞的个数


class client(Thread):       # 定义顾客类
    client_name = ''        # 顾客名字
    money = 5000.0          # 顾客余额
    egg = 0                 # 购买个数

    def run(self) -> None:  # 重构run方法
        global kep          # 调用全局变量
        start = time.time()     # 记录开始时间
        while True:
            end = time.time()   # 记录结束时间
            if end - start < 60:    # 判断时间
                if kep > 0:  # 判断篮子里蛋挞个数：不为空
                    if self.money >= 3:     # 判断顾客余额
                        self.money = self.money - 3  # 余额计算
                        kep = kep - 1  # 篮子内蛋挞个数
                        self.egg = self.egg + 1     # 购买蛋挞个数
                    else:       # 余额不足结束
                        break

                else:  # 篮子为空等待2秒
                    time.sleep(2)

            else:       # 大于60秒结束
                break
        print(self.client_name, '一共做了抢了', self.egg, '个蛋挞')
        return self.egg


'''调用厨师类'''
c = chef()
c._name = '厨师1'
c2 = chef()
c2._name = '厨师2'
c3 = chef()
c3._name = '厨师3'

'''调用顾客类'''
l = client()
l.client_name = '顾客1'
l2 = client()
l2.client_name = '顾客2'
l3 = client()
l3.client_name = '顾客3'
l3.money = 5000

'''运行线程'''
c.start()
c2.start()
c3.start()
l.start()
l2.start()
l3.start()

'''闭塞线程'''
c.join()
c2.join()
c3.join()
l.join()
l2.join()
l3.join()

'''会计结算'''
print(c._name, '一共做了', c.kep_sum, '个蛋挞','工资',c.kep_sum*1.5)
print(c2._name, '一共做了', c2.kep_sum, '个蛋挞','工资',c2.kep_sum*1.5)
print(c3._name, '一共做了', c3.kep_sum, '个蛋挞','工资',c3.kep_sum*1.5)