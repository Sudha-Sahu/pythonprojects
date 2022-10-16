# Calculating percentage of number of head and tail

import random


def count_head_tail(no_of_flip):
    total_heads = 0
    total_tails = 0
    cnt = 0
    while cnt < no_of_flip:
        coin = random.randint(0, 1)
        if coin < 0.5:
            total_tails += 1
        else:
            total_heads += 1
        cnt += 1
    return total_tails, total_heads


if __name__ == "__main__":
    try:
        no_of_times = int(input("Enter the number of times to flip the coin : "))
        tail, head = count_head_tail(no_of_times)
        print(f"Heads came up {head} times")
        print(f"Tails came up {tail} times")
        calc_per_head = (head / no_of_times) * 100
        print("Percentage of Head is : ", calc_per_head, "%")
        calc_per_tail = 100 - calc_per_head
        print("Percentage of Tail is : ", calc_per_tail, "%")
    except:
        print("give proper integer value")
