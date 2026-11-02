types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def remove_list_duplicates(tickets_dict):
    list = []
    task_name = ''
    
    for value in tickets_dict.values():
        list.append(value)

    for i in range(0, len(list)):

        for y in range(0, len(list[i])):
            task_name = list[i][y]

            for z in range(i+1, len(list)):
                if task_name in list[z]:
                    list[z].remove(task_name)


def tickets_by_type_combination(types, tickets):
    tickets_by_type = {}

    for key, value in types.items():
        tickets_by_type[value] = tickets[key]
    
    return tickets_by_type