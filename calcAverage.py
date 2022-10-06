ages = [10, 20, 30]
incomes = [100,200,300,400]

def calculateAverages(list):
    sum = 0
    for i in list:
        sum += i
    return sum/len(list)

print(calculateAverages(incomes))