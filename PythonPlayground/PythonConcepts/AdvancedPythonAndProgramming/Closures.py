def multiplier(x):
    def multiply(y):
        return x * y
    return multiply


multipliers = []
for x in range(1, 4):
    multipliers.append(lambda y: x * y)

m1, m2, m3 = multipliers

# print(m1(10))
# print(m2(10))
# print(m3(10))

def my_close(some_string):
    a = "Name - "
    count = 1
    def inside(say):
        nonlocal count
        print("Person number",count)
        count += 1
        print(a,some_string,say)
    return inside

