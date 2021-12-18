

ItemsInCart = 0
#2 items will be added in cart

if ItemsInCart != 2: #raise Exception("products cart count not matched")
    pass

assert(ItemsInCart == 0)


# try , catch -> in python we use (except)

try:
    with open('test.txt', 'r') as reader:
        reader.read()

except:
    print("Failure test")

# to catch exception message

try:
    with open('test.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("it will print no matter what whether it fails or passed")


