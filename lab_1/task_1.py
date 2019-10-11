def task_1():
    napis = "\n"
    for i in range(1, 10):
        napis = napis + str(i) * i + '\n'
    print(napis)
    return napis




assert task_1() == '''
1
22
333
4444
55555
666666
7777777
88888888
999999999
'''
