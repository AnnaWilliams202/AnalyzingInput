text = input("Enter series of numbers separated by space:\n ")
list_of_numbers = [int(number) for number in text.split()]


number_friquency = {}
for number in list_of_numbers:
    if not number in number_friquency.keys():
        number_friquency[number] = 1
    else:
        number_friquency[number] += 1


total_numbers = len(list_of_numbers)
sum_of_numbers = sum(list_of_numbers)
range_of_numbers = max(list_of_numbers)-min(list_of_numbers)
most_frequent_number = max(number_friquency,key=number_friquency.get)
average_number = round(sum_of_numbers/total_numbers)

print('Number Analysis results:')
print('-'*25)
print(f'Total numbers: {total_numbers}')
print(f'Sum of numbers: {sum_of_numbers}')
print(f'Range of numbers: {range_of_numbers}')
print(f'Most frequent number: {most_frequent_number}')
print(f'Average number: {average_number}')