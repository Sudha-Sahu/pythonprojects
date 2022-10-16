# Take a range of 0 - 1000 Numbers and find the Prime numbers in that range. Store the prime numbers in a 2D Array,
# the first dimension represents the range 0-100, 100-200, and so on. While the second dimension represents the prime
# numbers in that range.

def prime_list(n1, n2):
    prime_lst = []
    for i in range(n1, n2):
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count += 1
                break
        if count == 0 and i != 1:
            prime_lst.append(i)
    return prime_lst


if __name__ == "__main__":
    try:
        array = []
        limit1 = 1
        limit2 = 100
        while limit2 < 1000:
            result = prime_list(limit1, limit2)
            array.append(result)
            limit1 += 100
            limit2 += 100

        print(array)
    except IndexError:
        print("array got out of index")
