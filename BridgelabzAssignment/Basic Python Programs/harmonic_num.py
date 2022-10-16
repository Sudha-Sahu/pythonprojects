# Calculating Harmonic number upto nth term

def calc_harmonic(nth_term, sum_nth_harmonic):
    i = 1
    while i <= nth_term:
        if i != nth_term:
            print("1 /", i, "+", end=" ")
            sum_nth_harmonic += 1 / i
        else:
            print("1 /", i)
            sum_nth_harmonic += 1 / i
        i = i + 1
    return f"Sum of nth Harmonic number : {sum_nth_harmonic}"


if __name__ == "__main__":
    try:
        harmonic = int(input("Enter number for nth Harmonic number : "))
        sum_ = 0
        print(calc_harmonic(harmonic, sum_))
    except:
        print("invalid input from user")
