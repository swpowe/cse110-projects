# Week 6 Team Activity Hr System
data_set = []
with open("files/hr_system.txt") as raw_data:
    for line in raw_data:
        data_set.append(line.strip())
        info = line.split(" ")
        print(f"Name: {info[0]} Title: {info[2]}")
        
