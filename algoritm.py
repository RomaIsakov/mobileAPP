def index(P1, P2, P3):
    return (4 * (P1 + P2 + P3) - 200)/10
def minCount(Age):
    formul=21-(Age-7)//2*1.5
    return formul
def result(formul, index):
    print(formul, index)
    if index>formul:
        return "Низкий"
    elif index>formul-4:
        return "Удовлетворительный"
    elif index>formul-9:
        return "Средний"
    elif index>formul-14.5:
        return "Выше среднего"
    else:
        return "Высокий"
def SResult(P1, P2, P3, Age):
    a=index(P1, P2, P3)
    return result(minCount(Age), a)