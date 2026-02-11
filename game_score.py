player_name = input("Enter player's name: ")
games_played = int(input("Enter number of games played: "))
total_score = int(input("Enter total score: "))
average_score = total_score / games_played

print(f"Player: {player_name}")
print(f"Games Played: {games_played}")
print(f"Total score: {total_score}")
print(f"Average Score: {average_score:.2f}")

