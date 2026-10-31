time_str_data = '1h 45m,360s,25m,30m 120s,2h 60s'

def minutes_calculator(time_string = ''):

    time_list = time_string.split(',')
    minutes_sum = 0
    hours = 0
    minutes = 0
    seconds = 0

    for time in time_list:
        separate_time = time.split(' ')
        for i in separate_time:
            if 'h' in i:
                hours += int(i.replace('h',''))
            elif 'm' in i:
                minutes += int(i.replace('m', ''))
            elif 's' in i:
                seconds += int(i.replace('s', ''))

    minutes_sum = (hours * 60) + minutes + (seconds / 60)

    return int(minutes_sum)

print(minutes_calculator(time_str_data))