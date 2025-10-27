import re
from dataclasses import replace

number_string = '1h 45m,360s,25m,30m 120s,2h 60s'

final_time = 0

for number in re.split('[ ,]', number_string):
    if 'h' in number:
        number = number.replace('h', '')
        final_time += int(number) * 60
    elif 'm' in number:
        number = number.replace('m', '')
        final_time += int(number)
    elif 's' in number:
        number = number.replace('s', '')
        final_time += int(number) // 60
print(f'Общее количество минут: {final_time}')