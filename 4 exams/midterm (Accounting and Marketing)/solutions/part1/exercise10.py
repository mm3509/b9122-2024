# Note: because this function takes input from the user in the command-line
# and not as an argument, it has no doc-tests.

def sum_positive_numbers():

    res = 0
    while True:
        s = input("Please enter a positive number: ")

        try:
            n = int(s)
        except (TypeError, ValueError):
            return res

        if str(n) != s:
            return res

        if n <= 0:
            return res

        res += n

    return res

if __name__ == "__main__":
    print(sum_positive_numbers())
