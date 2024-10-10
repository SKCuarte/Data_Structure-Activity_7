#Acquiaring Max of a List

appliances_cost = [1299, 500, 359, 89, 459, 15]

def maxCustom(appliances_cost):
    max_cost = 0
    for cost in appliances_cost:
        if cost > max_cost:
            max_cost = cost
    return max_cost

#Built-in Function
print("The max is: ", max(appliances_cost))

#Custom Function
print("The max is: ", maxCustom(appliances_cost))