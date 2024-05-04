# Project 06: Data Analysis
## I skipped the first header row rather then deleting it to make the CSV work
## I added some dynamic line formatting

overall_min_life = 999.0
overall_min_year = ""
overall_min_country = ""

Overall_max_life = 0.0
overall_max_year = ""
overall_max_country = ""

interest_min_life = 999.0
interest_min_year = ""
interest_min_country = ""

interest_max_life = 0.0
interest_max_year = ""
interest_max_country = ""

interest_average = 0.0
interest_life_values = []

year_of_interest = input("Enter the year of interest: ")
print_line = f"Enter the year of interest: {year_of_interest}"

for letter in print_line:
    print("-", end="")

print()

with open("files/life-expectancy.csv") as raw_data:
    for line in raw_data:
        line_data = line.split(",")
        
        if "Entity" in line_data: # skip first row headers
            continue
        
        country = line_data[0].strip()
        country_code = line_data[1].strip()
        year = line_data[2].strip()
        life_expectancy = float(line_data[3].strip())
        
        if life_expectancy < overall_min_life:
            overall_min_life = life_expectancy
            overall_min_year = year
            overall_min_country = country
            
        if life_expectancy > Overall_max_life:
            Overall_max_life = life_expectancy
            overall_max_year = year
            overall_max_country = country
            
        # if year == year_of_interest
        if year == year_of_interest:
            # get average values
            interest_life_values.append(life_expectancy)
            
            # get values and min / max them
            if life_expectancy < interest_min_life:
                interest_min_life = life_expectancy
                interest_min_year = year
                interest_min_country = country
            
            if life_expectancy > interest_max_life:
                interest_max_life = life_expectancy
                interest_max_year = year
                interest_max_country = country
                
# calculate average
for value in interest_life_values:
    interest_average += value

interest_average = interest_average / len(interest_life_values)
            
print(f"The overall min life expectancy is: {overall_min_life} from {overall_min_country} in {overall_min_year}")
print(f"The overall max life expectancy is: {Overall_max_life} from {overall_max_country} in {overall_max_year}")
print()
print(f"For the year {year_of_interest}:")
print(f"The average life expectancy across all countries was {interest_average :.2f}")
print(f"The min life expectancy was in {interest_min_country} with {interest_min_life}")
print(f"The min life expectancy was in {interest_max_country} with {interest_max_life}")