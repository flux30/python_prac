cricket_players = {"Sachin", "Virat", "Rohit", "Dhoni", "Bumrah"}
football_players = {"Messi", "Ronaldo", "Neymar", "Mbappe", "Pogba"}

print("Players of Cricket game:", cricket_players)

print("Players of Football game:", football_players)

common_players = cricket_players.intersection(football_players)
print("Players who have participated in both Cricket and Football:", common_players)

all_players = cricket_players.union(football_players)
print("List of all players:", all_players)
print("Total number of players:", len(all_players))

cricket_only_players = cricket_players.difference(football_players)
print("Players who have participated in Cricket but not in Football:", cricket_only_players)

football_only_players = football_players.difference(cricket_players)
print("Players who have participated in Football but not in Cricket:", football_only_players)