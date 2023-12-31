# Контекст
# Предположим, что мы хотим найти элемент в массиве (получить
# его индекс). Мы можем это сделать просто перебрав все элементы.
# Но что, если массив уже отсортирован? В этом случае можно
# использовать бинарный поиск. Принцип прост: сначала берём
# элемент находящийся посередине и сравниваем с тем, который мы
# хотим найти. Если центральный элемент больше нашего,
# рассматриваем массив слева от центрального, а если больше -
# справа и повторяем так до тех пор, пока не найдем наш элемент.
#
# Задача:
# Написать программу на любом языке в любой парадигме для
# бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого
# элемента нет в массиве.




# императивная парадигма, так как поиск реализован пошагово
# в search используется процедурная (код поиска элемента вынесен в отдельныую фукцию)
# и структурная (испльзуется ветвление, цикл, последовательное выполнение) парадигма
def search(lst, elem):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_val = lst[mid]
        if mid_val == elem:
            return mid
        if mid_val > elem:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# применяется декларативная - используется встроенный метод sorted
def main(lst, elem):
    sorted_lst = sorted(lst)
    print(sorted_lst)
    print(search(sorted_lst, elem))


if __name__ == '__main__':
    main([1, 2, 16, 4, 6, 7, 89, 34, 5], 8)

