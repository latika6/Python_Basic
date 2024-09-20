# Sample Input:
# ['hello', 'world']
# Sample Output:
# ['HELLO', 'WORLD']
input_list = ['hello world']
output_list = list(map(lambda word: word.upper(), input_list[0].split()))
print(output_list)
