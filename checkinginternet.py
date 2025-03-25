import socket
import time

def check_internet_connection():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        return False

check_count = 0
ask_again = True

while True:
    if check_internet_connection():
        print("internet working fine here lad")
    else:
        print("change isp, this shi is gone")

    check_count += 1
    time.sleep(3)

    if ask_again and check_count >= 15:
        while True:
            continue_checking = input("keep goin cunt? (y/n): ").lower()
            if continue_checking in ("y", "n"):
                break
            else:
                print("stupid. 'y' or 'n'.")

        if continue_checking == "n":
            print("damn")
            time.sleep(2)
            exit()
        elif continue_checking == "y":
            ask_again = False
            print("I hate you.")
    elif not ask_again and check_count >= 15:
        check_count = 0