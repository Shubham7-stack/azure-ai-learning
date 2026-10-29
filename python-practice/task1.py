print("Welcome to the average calculator of a cricket player!")
Player_name = input("Tell me the name of the player: ")
Total_runs = int(input("Tell me the amount of runs this player has scored: "))
Total_innings = int(input("Tell me the amount of innings this player has played: "))
Total_outs = int(input("Tell me the amount of time he has gone out: "))
Average = float(round(Total_runs / Total_outs, 2))

print(f"{Player_name} has scored {Total_runs} runs with an average of {Average}")