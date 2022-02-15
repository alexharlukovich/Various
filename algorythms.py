# task 1 Bubble-sort
t = "ВыможетеподуматьчтовхудшемслучаепотребуетсябесконечноевремяТеоретическивсеверноФактическидлялюбогомассивафиксирован" \


# l = list(t)
# print(l)
from datetime import datetime
import random
# while not in_order(deck):
#     shuffle(deck)
start_time = datetime.now()
def bogosort(l):
    while not l == sorted(l):
        random.shuffle(l)
    return l
x = list(t)
print(bogosort(x))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))


# def bubble_sort(l):
#     for run in range (len(l)-1):
#         for i in range (len(l)-1-run):
#             if l[i]>l[i+1]:
#                 l[i], l[i+1] = l[i+1], l[i]
#     return l
# print(bubble_sort(l))
