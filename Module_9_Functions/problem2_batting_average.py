def batting_average(hits, at_bats):
    if at_bats == 0:
        return 0
    return hits / at_bats


player_count = 0
while True:
    last_name = input("Enter player last name (or stop): ")
    if last_name.lower() == "stop":
        break
    hits = int(input("Enter number of hits: "))
    at_bats = int(input("Enter number of at bats: "))
    average = batting_average(hits, at_bats)
    print(f"Last name: {last_name}, Batting average: {average:.3f}")
    player_count += 1

print(f"Number of players entered: {player_count}")
