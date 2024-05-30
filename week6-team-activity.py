# Week 6 Team Activity Hr System
data_set = []
with open("files/hr_system.txt") as raw_data:
    for line in raw_data:
        data_set.append(line.strip())
        info = line.split(" ")
        
        name = info[0]
        id = info[1]
        title = info[2]
        yearly_salary = float(info[3])
        
        paycheck_salary = yearly_salary /12 /2
        
        if title == "Engineer":
            paycheck_salary += 1000
        
        print(f"Name: {name} (ID: {id}) Title: {title} - Salary: ${paycheck_salary:.2f}")
        
