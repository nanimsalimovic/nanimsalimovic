

def max_func(x: int, y: int)->int:
    return x if x > y else y


# The code below will execute only when standalone, the above
# function still can be imported.
if __name__ == "__main__":
    x, y = input("Enter two comma-separated integer values: ").split()
    assert(x != y), "The given values can't be equal!."
    try:
        print(f"The biggest number is {max_func(int(x), int(y))}")
    except ValueError as e:
        print(e)
