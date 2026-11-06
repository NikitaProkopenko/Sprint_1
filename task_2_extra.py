def digit_root(num):
    num_calc = num
    len_num_calc_list = len(list(str(num_calc)))
    root = 0

    if len_num_calc_list < 2:
        root = num_calc
    
    while len_num_calc_list >= 2:
        num_lst = (list(str(num_calc)))

        for i in range(0, len(num_lst)):
            root += int(num_lst[i])
        
        num_calc = root
        
        if root >= 1 and root <= 9:
            break
        else:
            len_num_calc_list = len(list(str(root)))
            root = 0

    return root

print(digit_root(4851))
#4851 → 4+8+5+1 = 18
#18 → 1+8 = 9

print(digit_root(889987))
#889987 → 8+8+9+9+8+7= 49
#49 → 4+9 = 13
#13 → 4

print(digit_root(38))
#38 → 3+8 = 11
#11 → 2