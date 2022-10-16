from datetime import datetime
import time


if __name__ == "__main__":
    today_day = datetime.now()
    print("Today's Date is : ", today_day)
    start_time = time.time()
    print("Start Time is : ", start_time)
    time.sleep(5)
    end_time = time.time()
    print("End Time is : ", end_time)

    elapse_time = end_time - start_time
    print(f"Time Elapsed(seconds) --> {elapse_time}")



"""
def main():
    while True:
        option = int(input("Enter Value:\n1.Start\t 2.Stop\t 3.Exit\n"))
        if option == 1:
            start_time = time.time()
        if option == 2:
            print(f"Time Elapsed(seconds) --> {time.time() - start_time}")
        if option == 3:
            break


if __name__ == "__main__":
    main()
"""
