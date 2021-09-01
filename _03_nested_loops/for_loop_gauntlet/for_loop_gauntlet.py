"""
Create algorithms and use to solve
https://central.jointheleague.org/levels/Level0/Recipes/ForLoopGauntlet.html
"""


if __name__ == '__main__':
    #for i in range(100):
    #    print(i)
    #for i in reversed(range(100)):
    #  print(i)
    #for i in range(102):
    #    if i%2==0:
    #       print(i)
    #for i in range(100):
    #   if i % 2 !=0:
    #       print(i)
    #for i in range(500):
    #    if i % 2 !=0:
    #       print(str(i) +" is odd")
    #   else:
    #       print(str(i) + " is even")
    #for i in range(78):
    #    if i % 7 ==0:
    #        print(i)
    #num = -1
    #for i in range(2007,2022):
    #        num+=1
    #       print("In "+ str(i) + " I was "+ str(num))
    #for i in range(3):
    #    for x in range(3):
    #        print(i, x)
    num = 0
    startnum = 1
    endnum = 4
    for i in range(1,4):
        if num == 1:
            startnum = 4
            endnum = 7
        if num == 2:
            startnum = 7
            endnum = 10
        for x in range(startnum,endnum):
            print(x, end=" ")
        print('\n')
        num+=1
    pass
