# calculating roots of a quadratic equation

def quadratic_eq(a, b, c):
    delta = (b*b * 4*a*c)**(1/2)
    root1 = (-b + delta)/(2*a)
    root2 = (-b - delta)/(2*a)
    return f"the 2 Roots of quadratic equation are : {root1}, {root2}"


if __name__ == "__main__":
    try:
        print("enter the coefficient of x in quadratic equation:")
        coeff1 = int(input("Enter coefficient of x2 :"))
        coeff2 = int(input("Enter coefficient of x :"))
        coeff3 = int(input("Enter coefficient of constant term :"))
        print(quadratic_eq(coeff1, coeff2, coeff3))
    except ValueError:
        print("enter valid coefficient of x")

