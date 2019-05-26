






def listCount1():
    a = [1, 2, 3, 1, 1, 2]
    dictdata = {}
    for key in a:
        print(key)
        dictdata[key] = dictdata.get(key, 0) + 1
    return dictdata




def listCount2():
    from collections import Counter
    a = [1, 2, 3, 1, 1, 2]
    return Counter(a)


def listCount3():
    import pandas as pd
    a = [1, 2, 3, 1, 1, 2]
    result = pd.value_counts(values=a,sort=True)
    print(result)



def listCount4():
    a = [1, 2, 3, 1, 1, 2]
    b = {i:a.count(i) for i in a}
    return b






import timeit


if __name__ == "__main__":
    # listCount2()
    # listCount3()
    # s = listCount4()
    # print (timeit.timeit(stmt="listCount4", setup='from __main__ import listCount4',number=1))
    print (timeit.timeit(stmt="[i for i in range(100)]" ,number=10000))
    print (timeit.timeit(stmt="{i for i in range(100)}" ,number=10000))
