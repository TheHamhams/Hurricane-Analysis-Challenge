# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East Coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
def damage_float(damage_list):
  i = 0
  while i < len(damage_list):
    if damage_list[i] != "Damages not recorded":
      if damage_list[i][-1] == "M":
        array = damage_list[i].split("M")
        new_amount = float(array[0]) * conversion["M"]
        damage_list[i] = new_amount
      elif damage_list[i][-1] == "B":
        array = damage_list[i].split("B")
        new_amount = float(array[0]) * conversion["B"]
        damage_list[i] = new_amount
    i += 1
# test function by updating damages
damage_float(damages)

# 2 
# Create a Table
def hurricane_dict(name_array, month_array, year_array, wind_array, area_array, damage_array, death_array):
  i = 0
  new_dict = {}
  while i < len(name_array):
    new_dict[name_array[i]] = {"Name": name_array[i], "Month": month_array[i], "Year": year_array[i], "Max Sustained Wind": wind_array[i], "Areas Affected": area_array[i], "Damage": damage_array[i], "Deaths": death_array[i]}
    i += 1
  return new_dict
# Create and view the hurricanes dictionary
hurricane_dictionary = hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
#print(hurricane_dictionary)
# 3
# Organizing by Year
def by_year(dictionary):
  new_dict = {}
  for key in dictionary:
    new_key = dictionary[key]["Year"]
    if dictionary[key]["Year"] not in new_dict:
      new_dict[dictionary[key]["Year"]] = [dictionary[key]]
    else:
      new_dict[dictionary[key]["Year"]].append(dictionary[key])
  return new_dict
  
  

# create a new dictionary of hurricanes with year and key
hurricane_year = by_year(hurricane_dictionary)


# 4
# Counting Damaged Areas
def damaged_areas_count(dictionary):
  new_dict = {}
  for key in dictionary:
    for area in dictionary[key]["Areas Affected"]:
      if area not in new_dict:
        new_dict[area] = 1
      else:
        new_dict[area] += 1
  return new_dict
# create dictionary of areas to store the number of hurricanes involved in
area_count = damaged_areas_count(hurricane_dictionary)
#print(area_count)

# 5 
# Calculating Maximum Hurricane Count
def max_count(dictionary):
  max_count = 0
  result = {}
  for key in dictionary:
    count = dictionary[key]
    if count > max_count:
      max_count = count
      result.clear()
      result.update({key: count})
  return result

# find most frequently affected area and the number of hurricanes involved in
max_area = max_count(area_count)
print(max_area)
# 6
# Calculating the Deadliest Hurricane
def max_deaths(dictionary):
  name = ""
  max_count = 0
  for key in dictionary:
    count = dictionary[key]["Deaths"]
    if count > max_count:
      max_count = count
      name = key
  return {name: max_count}


# find highest mortality hurricane and the number of deaths
deadliest = max_deaths(hurricane_dictionary)
print(deadliest)
# 7
# Rating Hurricanes by Mortality
def by_mortality(dictionary):
  new_dict = {}
  for key in dictionary:
    deaths = dictionary[key]["Deaths"]
    if deaths <= 100:
      death_key = 0
    elif deaths > 100 and deaths <= 500:
      death_key = 1
    elif deaths > 500 and deaths <= 1000:
      death_key = 2
    elif deaths > 1000 and deaths <= 10000:
      death_key = 3
    else:
      death_key = 4
    if death_key not in new_dict:
      new_dict[death_key] = [dictionary[key]]
    else:
      new_dict[death_key].append(dictionary[key])
  return new_dict

# categorize hurricanes in new dictionary with mortality severity as key
sorted_mortality = by_mortality(hurricane_dictionary)
#print(sorted_mortality)

# 8 Calculating Hurricane Maximum Damage
def max_damage(dictionary):
  damage_max = 0
  name = ""
  for key in dictionary:
    if dictionary[key]["Damage"] == "Damages not recorded":
      continue
    damage = dictionary[key]["Damage"]
    if damage > damage_max:
      damage_max = damage
      name = dictionary[key]["Name"]
  return {name: damage_max}


# find highest damage inducing hurricane and its total cost
max_hurricane_damage = max_damage(hurricane_dictionary)
print(max_hurricane_damage)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
def by_damage(dictionary):
  new_dict = {}
  for key in dictionary:
    if dictionary[key]["Damage"] == "Damages not recorded":
      continue
    damage = dictionary[key]["Damage"]
    if damage <= damage_scale[1]:
      damage_key = 0
    elif damage > damage_scale[1] and damage <= damage_scale[2]:
      damage_key = 1
    elif damage > damage_scale[2] and damage <= damage_scale[3]:
      damage_key = 2
    elif damage > damage_scale[3] and damage <= damage_scale[4]:
      damage_key = 3
    else:
      damage_key = 4
    if damage_key not in new_dict:
      new_dict[damage_key] = [dictionary[key]]
    else:
      new_dict[damage_key].append(dictionary[key])
  return new_dict
 
# categorize hurricanes in new dictionary with damage severity as key
sorted_damage = by_damage(hurricane_dictionary)
print(sorted_damage)