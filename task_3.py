import random

def print_my_call():
    count = []
    range_ = range(random.randint(1, 23))
    for i in range_:
        start_time = random.randint(0, 23)
        end_time = random.randint(1, 24)
        zayavka = (start_time, end_time)
        if start_time < end_time:
            count.append(zayavka)

    sort_index = sorted(count, key=lambda zayavka :zayavka[0])
    #print(sort_index)
    n = 0
    list_wish = []
    for wish in sort_index:
        #if sort_index[n+1][0] > sort_index[n][1]:

        if sort_index[n+1][0] > sort_index[n][1] and sort_index[n+1][1] > sort_index[n][1] and sort_index[n+1][0] > sort_index[n][0]:
            list_wish.append(wish)
            print(wish)
        #else:
            #print(wish)

        #if sort_index[n+1][0] > sort_index[n][1]:

        #print(set(list_wish))
            #print(wish)

    #print(list_wish[n])


print_my_call()