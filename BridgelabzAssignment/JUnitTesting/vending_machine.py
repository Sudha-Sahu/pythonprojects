
def get_change(amount):
    notes = [2000, 500, 200, 100, 50, 20, 10, 5, 1]
    no_of_note = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("the change and number of note are :  ")

    for i, j in zip(notes, no_of_note):
        if amount >= i:
            j = amount // i
            amount = amount - j * i
            print(i, " : ", j)


_amount = int(input("enter the amount you want to get change of it: "))
get_change(_amount)
