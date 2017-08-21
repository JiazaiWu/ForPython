# -*- coding: utf-8 -*-

def accumulate():    # 子生成器，将传进的非None值累加，传进的值若为None，则返回累加结果
    tally = 0
    while 1:
        print('will call yield')
        next = yield 1
        print(next)
        if next is None:
            return tally
        tally += next
def gather_tallies(tallies):    # 外部生成器，将累加操作任务委托给子生成器
    while 1:
        tally = yield from accumulate()
        print('here')
        tallies.append(tally)

tallies = []
acc = gather_tallies(tallies)
print('before next')
print(next(acc))    # 使累加生成器准备好接收传入值
print('after next')
for i in range(4):
    print(acc.send(i))

acc.send(None)    # 结束第一次累加
for i in range(5):
    acc.send(i)
acc.send(None)    # 结束第二次累加
print(tallies)    # 输出最终结果