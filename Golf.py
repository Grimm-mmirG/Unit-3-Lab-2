num_players = int(input("Enter number of players: "))
players = []

for i in range(num_players):
    name = input("Enter player name: ")
    score = int(input("Enter player score: "))
    players.append((name, score))

with open('golf.txt', 'w') as f:
    for player in players:
        f.write(f"{player[0]}: {player[1]}\n")
