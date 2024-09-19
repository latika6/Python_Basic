def compute_hcf(x, y):
    while y:
        x, y = y, x % y
    return x
num1 = 5
num2 = 4
print(f"The HCF of {num1} and {num2} is {compute_hcf(num1, num2)}")
