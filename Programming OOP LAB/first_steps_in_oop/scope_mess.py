x = "global"

def outer():
    x = "local"

    def inner():
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        x = "global: changed!"
        return x

    print("outer:", x)
    inner()
    print("outer:", "nonlocal")
    print(change_global())

print(x)
outer()