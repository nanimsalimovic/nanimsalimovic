

class ItemsAccess:
    def __init__(self):
        self.__item_dict = {}

    def __setitem__(self, item, value):
        self.__item_dict[item] = value

    def __getitem__(self, item):
        try:
            return self.__item_dict[item]
        except KeyError as e:
            print(e)


if __name__ == "__main__":
    ia = ItemsAccess()
    ia["S@lim"] = 46
    ia["@youb"] = 6
    print("S@lim has {} and @youb has {}".format(ia["S@lim"], ia["@youb"]))
    
