






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






if __name__ == "__main__":
    # listCount2()
    listCount3()
