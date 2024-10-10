#Acquiring the Min of a List

appliances_cost = [1299, 500, 359, 89, 459, 15]

def minCustom(appliances_cost):
    min_cost = 10000
    for cost in appliances_cost:
        if cost < min_cost:
            min_cost = cost
    return min_cost

#Built in Function
print("The min is: ", min(appliances_cost))

#Custom Function
print("The min is: ", minCustom(appliances_cost))