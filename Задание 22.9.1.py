numbers = input('Введите числа через пробел: ').split()
my_number = int(input('Введите любое число: '))
list_of_numbers = [int(item) for item in numbers]

def merge_sort(nums):
    if len(nums) < 2:
        return nums[:]
    else:
        middle = len(nums) // 2
        left = merge_sort(nums[:middle])
        right = merge_sort(nums[middle:])
        return merge(left, right)

def merge(left, right):
    k = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            k.append(left[i])
            i = i + 1
        else:
            k.append(right[j])
            j = j + 1

    while i < len(left):
        k.append(left[i])
        i = i + 1

    while j < len(right):
        k.append(right[j])
        j = j + 1
    return k

def binary_search(list_of_numbers, item, start, stop):
    try:
        if start > stop:
            return False
        middle = (stop + start) // 2
        if list_of_numbers[middle] == item:
            return middle
        elif item < list_of_numbers[middle]:
            return binary_search(list_of_numbers, item, start, middle - 1)
    except IndexError:
        return f'Число выходит за диапазон списка.'
    else:
        return binary_search(list_of_numbers, item, middle + 1, stop)

list_of_numbers = merge_sort(list_of_numbers)
print(f'Список по возрастанию: {list_of_numbers}')

if not binary_search(list_of_numbers, my_number, 0, len(list_of_numbers)):
    low = min(list_of_numbers, key=lambda x: (abs(x - my_number), x))
    id = list_of_numbers.index(low)
    max_index = id + 1
    min_index = id - 1
    if low < my_number:
        print(f'''В списке нет введенного элемента 
Ближайший меньший элемент: {low}, его индекс: {id}
Ближайший больший элемент: {list_of_numbers[max_index]} его индекс: {max_index}''')
    elif min_index < 0:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {low}, его индекс: {list_of_numbers.index(low)}
В списке нет меньшего элемента''')
    elif low > my_number:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {low}, его индекс: {list_of_numbers.index(low)}
Ближайший меньший элемент: {list_of_numbers[min_index]} его индекс: {min_index}''')
    elif list_of_numbers.index(low) == 0:
        print(f'Индекс введенного элемента: {list_of_numbers.index(low)}')
else:
    print(f'Индекс введенного элемента: {binary_search(list_of_numbers, my_number, 0, len(list_of_numbers))}')