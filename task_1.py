text = "flfkxkckg lglglglvl glofkg, fkfkfkfrdr."
modify_text = text.replace(" ", "")
modify_text = modify_text.replace(",", "")
modify_text = modify_text.replace(".", "")

print(len(modify_text)//2)
count_slog = len(modify_text) // 2
for slog in range(1, count_slog + 1):
    list = []# список слогов
    list.append(slog)


    count_pleyer = 3
    list_count_player = []
    assert count_pleyer < count_slog
    for player in range(1, count_pleyer+1):
        #list2 = []# список игроков
        list_count_player.append(player)
    for player in list_count_player:

        players = len(list_count_player)
        counter = 0
        pointer = 1
    # while slog > player:
    #     #print(list_count_player)
    #     num = count_slog % count_pleyer
    #     if player == 1:
    #         print("победитель", player)
    #     else:
    #         list_count_player.pop()
    #         pointer -= 1

    while player > 1:
            if player == 1:
                print("победитель", player)
            else:
                num = count_slog % count_pleyer
                for num in range(1, len(list_count_player)+1):
                    list_count_player.pop()
                    pointer -= 1

                    print(num)