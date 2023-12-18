def home():
    x = 0
    for i in range(4212, 18912513):
        x += i
    return x


if __name__ == "__main__":
    print(home())
