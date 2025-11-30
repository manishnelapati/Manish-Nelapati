#-- generating odd numbers--

def generate_series(a):
    # if a is even, reduce by 1

    if a % 2 == 0:
        count = a-1
    else:
        count = a


    # generate first count odd numbers
    result = []

    for i in range(1,count+1):
        odd_num = 2*i-1
        result.append(odd_num)

    return result




# problem

a = int(input("Enter a number: "))
series = generate_series(a)
print("Output:", ",".join(map(str,series)))
