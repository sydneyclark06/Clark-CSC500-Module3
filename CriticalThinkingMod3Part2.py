print("\n\n24 Hour Clock Math Calculator\n")

print("What is the current time? (Hours Only)", end=" ")

current_time = int(input())

print("How many hours do you need to add?", end=" ")

hours = int(input())

time_to_add = hours % 24

final_time = time_to_add + current_time

print("That will take you to ", final_time, ".")
