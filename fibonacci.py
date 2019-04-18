def fibonacci_num(lst):
    index1 = 0
    index2 = 1
    for i in lst:
        index1 += 1
        index2 += 1
        if index1 >= len(lst) or index2 >= len(lst):
            break
        if lst[index2] == lst[index1] + i:
            if index1 == len(lst) - 2:
                print("ფიბონაჩის მიმდევრობაა")
                break
        else:
                print("ფიბონაჩის მიმდევრობა არაა")
                break