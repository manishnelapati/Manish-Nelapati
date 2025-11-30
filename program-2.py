def generate_odd_series(a):

    result = []

    for i in range(1, a+1):
        odd_num = 2*i-1
        result.append(odd_num)
    return result



a = int(input("Enter a number: "))
odd_num = generate_odd_series(a)
print(odd_num)