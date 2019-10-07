def swap(List,i,j):
    tmp = List[i]
    List[i] = List[j]
    List[j] = tmp

    
def mirror(List):
    for i in range( len(List)//2 ):
        swap(List,i,-(i+1))
    return List


def maxList(List):
    i = 1
    x = List[0]
    if len(List) != 0:
        while i < (len(List)):

            if List[i] > x :
                x = List[i]
            i = i+1
        return x
    else:
        return None


def minList(List):
    i = 1
    x = List[0]
    if len(List) != 0:
        while i < (len(List)):

            if List[i] < x :
                x = List[i]
            i = i+1
        return x
    else:
        return None


def TestListCrease(List):
    i = 1

    while i <= (len(List)-1):
        if List[i] < List[i-1]:
            return False
        i = i+1

    return True


def TestListDecrease(List):
    i = 1

    while i <= (len(List)-1):
        if List[i] > List[i-1]:
            return False
        i = i+1

    return True


def TestSortList(List):
	return (TestListCrease() or TestListDecrease()):


def identicalLists(List1,List2):
    if List1 == List2 :
        return True
    else :
        return False


def ShiftLeft(List):
    if len(List) == 0:
	return List
    
    first =List[0]
    for i in range(0,(len(List)-1)):

        List[i] = List[i+1]

    List[-1] = first

    return List


def ShiftRight(List):
    if len(List) == 0:
	return List

    last = List[-1]
    for i in range(len(List)-1, 0, -1):

        List[i] = List[i-1]

    List[0] = last

    return List


def MeanList(List):
    if len(List) == 0:
	return 0

    x = 0
    imax = len(List)

    for i in range(0,imax):
        x = x + int(List[i])

    return (x/len(List))


def Power(val,p):
    res = 1
    for i in range(p)
	res = res*val
    return res


def facto(val):
    res = 1
    if val >=0:
        for i in range(1,val+1):
                res = res*i
        return res
    else :
        return 0
