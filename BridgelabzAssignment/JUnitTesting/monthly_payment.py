
def monthly_wage(principal, rate, year):
    n = 12 * year
    _r = rate / (12 * 100)
    payment = (principal * _r) / (1 - (1 + _r)**(-n))
    print("the monthly payments : ", payment)


p = int(input("enter the principal : "))
r = float(input("enter the rate% : "))
y = float(input("enter the year : "))

monthly_wage(p, r, y)
