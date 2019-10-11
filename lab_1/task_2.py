def task_2():
    napis = '*'
    print(napis)
    for i in range(1, 5):
        napis = napis + " *"
        print(napis)

    napis2 = "\n"
    for i in range(1,5):
        napis2 = (5-i) * "* "
        print(napis2)

    return napis




assert task_2() == '''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
