

def min(x, y):
    return x if x < y else y


if __name__ == "__main__":
    x, y = input("Enter two space-separated values: ").split()
    assert(x != y), "The given values are supposed to be different!."
    try:
        print("The smaller value is {}".format(min(int(x), int(y))))
    except ValueError as e:
        print(e)
    
