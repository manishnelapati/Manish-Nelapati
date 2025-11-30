#--generating count numbers in the dictionary--
def  count_multiples(numbers):
    result = {}
    keys = [1,2,3,4,5,6,7,8,9]


    for k in keys:
        count = 0
        for num in numbers:
            if num % k == 0:
                count += 1
        result[k] = count

    return result




#--program--

input_str = input("Enter numbers separated by space: ")
input_list = list(map(int,input_str.split()))

output = count_multiples(input_list)
print("output: ", output)