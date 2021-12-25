def add(num1, num2):
    res = num1 + num2
    return res

def sub(num1, num2):
    res = num1 - num2
    return res

#main starts from here
alpha = 10
delta = 20
total = add(alpha, delta)
print("sum", total)
diff = sub(alpha, delta)
print("diff", diff)

#new code goes here
eng1 = 250
ind1 = 220
eng2 = 180
eng_total = add(eng1, eng2)
ind2 = sub(eng_total, ind1)
ind_needs = add(ind2, 1)
print(ind_needs)

#new code
veg = 120
fruits = 45
cash = 200
total_cost = add(veg, fruits)
balance = sub(cash, total_cost)
print("amount to return", balance)
