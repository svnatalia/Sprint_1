# Задание 1

line = '1h 45m,360s,25m,30m 120s,2h 60s'
line_list = line.split(',')
total_minutes = 0

for block in line_list:
    time_block = block.split()

    for elem in time_block:
        if 'h' in elem:
            unit = elem.replace('h', '')
            total_minutes += int(unit) * 60
        elif 'm' in elem:
            unit = elem.replace('m', '')
            total_minutes += int(unit)
        elif 's' in elem:
            unit = elem.replace('s', '')
            total_minutes += int(unit) // 60
print(total_minutes)