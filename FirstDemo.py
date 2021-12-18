print("hello")
# here are the comments i have defined

a = 3
print(a)

Str = "hello world"
print(str)

b, c, d = 5, 6.4, "hello"

# print("value is"+b)

print("{} {} {}".format(b, c, d))

print(type(b))
print(type(c))
print(type(d))

# here i learn about values

values = [1, 2, "souvik", 4, 5]

#list allows multiple values and can be wth diff data type

print(values[-1])

print(values[1:3])

values.insert(3,"ghosh")
print(values)

values.append("end")
print(values)

values[2] = "SOUVIK"
print(values)

del values[0]
print(values)


val = [1 ,2, 3, "souvik", "ghosh"]
print(val)
print(val[1])

val[2]= "SOUVIK"
print(val[2])

print(val)


# Dictionary

dic = {"a": 10, 4: "bcd"}
print(dic["a"])


dict = {}
dict["First name"] = "Souvik"
dict["last name"] = "Ghosh"
print(dict["last name"])



# Loops

greeting = "Good Morning"

a = 4
if a > 2:
#if greeting == "Good Morning":
    print("Condition Matches")
else:
    print("Condition do not match")
print(" if else code is completed")

# For Loops

obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i*2)

print("End of Line")
# sum of first natural number 1+2+3+4+5 = 15

summation = 0
for j in range(1, 6):
    summation = summation + j
print(summation)

print("***************************************")


for k in range(1, 10, 2):
    print(k)

print("***************************************")

# Skipping indexes in loops

for m in range(10):
    print(m)

print("***************************************")

# Why loops

it = 10
while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break
    print(it)
    it = it - 1

print("while loop execution is done")


print("***************************************")


# Functions


def GreetMe(name):
    print("Good Morning "+name)


def addintergers(a,b):
    print(a+b)

GreetMe("Souvik Ghosh")

addintergers(2,3) #passing parameters






