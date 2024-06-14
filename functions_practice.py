def hello():
    print("Hello, user!")

def pack(one,two,three):
    return[one,two,three]

def eat_lunch(in_first):
    if len(in_first) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(in_first)):
            if i == 0:
                print(f"First I eat {in_first[0]}")
            else:
                print(f"Next I eat {in_first[i]}")

hello()
print(pack("one", "two", "three"))
eat_lunch([])
eat_lunch(["snails"])
eat_lunch(["apple","banana","sandwich","cookie"])