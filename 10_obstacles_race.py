# Create a function that evaluates if an athlete has successfully completed an
# obstacles race.
# - The function will receive two parameters:
#   - An array that can only contain String with the words "run" or "jump".
#   - A String that represents the track and can only contain "_" (floor)
#   or "|" (fence).
# - The function will print how the race has finished.
#   - If the athlete does "run" on "_" (floor) and "jump" on "|" (fence),
#   will be correct and the symbol of that part of the track will not change.
#   - If you do "jump" on "_" (floor), the track will vary by "x".
#   - If you do "run" on "|" (fence), the track will vary by "/".
# - The function will return a Boolean that indicates whether you have passed the
# race. To do this you have to make the correct option in each section of the
# track.

def obstacles_race(actions, track):
    race_status = True 
    resulting_track = []

    total_actions = len(actions) if (len(actions) >= len(track)) else len(track)

    if set(actions) <= {"run", "jump"} and set(track) <= {"|", "_"}:
            for index in range(0, total_actions):
                if index >= len(actions) or index >= len(track):
                    resulting_track.append("?")
                    race_status = False
                else:    
                    if actions[index] == "run" and track[index] == "|":
                        resulting_track.append("/")
                        race_status = False
                    elif actions[index] == "jump" and track[index] == "_":
                        resulting_track.append("x")
                        race_status = False
                    else: 
                        resulting_track.append(track[index])
            
            resulting_track = ''.join(resulting_track) # Convert the list to a String.
            return race_status, resulting_track
    else:
        print("Invalid action or track.")
        return False, track
    

print(f"{obstacles_race(["run", "jump", "run", "jump", "run"], "_|_|_")}\n")
print(f"{obstacles_race(["run", "run", "run", "jump", "run"], "_|_|_")}\n")
print(f"{obstacles_race(["run", "run", "jump", "jump", "run"], "_|_|_")}\n")
print(f"{obstacles_race(["run", "run", "jump", "jump", "run"], "_|_|_|_")}\n")
print(f"{obstacles_race(["run", "jump", "run", "jump",], "_|_|_")}\n")
print(f"{obstacles_race(["run", "jump", "run", "jump", "run", "jump", "run"], "_|_|_")}\n")
print(f"{obstacles_race(["jump", "jump", "jump", "jump", "jump"], "|||||")}\n")
print(f"{obstacles_race(["jump", "jump", "jump", "jump", "jump"], "||?||")}\n")
