text = "flfkxkckg lglgllvl glog, fkfkfkfrdr."
modify_text = text.replace(" ", "")
modify_text = modify_text.replace(",", "")
modify_text = modify_text.replace(".", "")

count_slog = len(modify_text) // 2

players = []
n = int(input("enter count players: "))
for i in range(1, n+1):
   players.append(str(i))
print(players)
print(len(players))
k = count_slog
point = 1
index = 0
while len(players) > 1:
   if point == k:
      print(index)
      del players[index]
      point =1
      print(players)
   else:
      point += 1
      index += 1
   if index == len(players):
      index = 0
print("wins player: ", players[0])