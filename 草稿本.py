#cs130
#Lab1
#Q1
'''
import math
radius = float(input("Enter a radius: "))
height = float(input("Enter a height: "))

volume = math.floor(math.pi * radius ** 2 * height)

print(f"Volume of cylinder is {volume} cubic cm.")
'''
#Q2
'''
yards = int(input("Enter the years: "))
feet = int(input("Enter the feet: "))
feet_yards = yards * 3
metres = round((feet_yards + feet) * 0.3048)
print(f"{yards} yards {feet} feet is apporximately {metres} metres.")
'''
#Q3
'''
def get_letter(letter, steps):
    alpha = "abcdefghijklmaopqrstuvwxyz"
    index = (alpha.find(letter) + steps)%26
    return alpha[index]

print(get_letter('h', 2))
print(get_letter('a', 2))
print(get_letter('z', 2))
print(get_letter('x', 5))
'''
#Q4
'''
def get_letters(words):
    string = ""
    for i in range(len(words)):
        string += words[i][:i+1]
    return string

print(get_letters(['hello', 'world']))
print(get_letters(["January", "February", "March", "April"]))
print(get_letters(['banana', 'apple', 'grapes']))
'''
#Q5
'''
def get_first_term_difference(numbers):
    numbers = sorted(numbers)
    return (numbers[0], numbers[1] - numbers[0])

number = [1, 3, 5]
data = get_first_term_difference(number)
print(data)
print(get_first_term_difference([5, 2, -1, 8]))
'''
#Q6
'''
def arithmetic_running_sum(numbers):
    for i in range(1, len(numbers)):
        numbers[i] = numbers[i] + numbers[i-1]
    return numbers

numbers = [4, 7, 10, 13, 16]
arithmetic_running_sum(numbers)
print(numbers)
numbers = [2, 5, 8, 11, 14, 17, 20]
arithmetic_running_sum(numbers)
print(numbers)
'''
#Q7
'''
def create_arithmetic(first_term, difference, number_of_values):
    list1 = []
    while len(list1) != number_of_values:
        list1.append(first_term)
        first_term += difference
    return list1

numbers = create_arithmetic(4, 3, 5)
print(numbers)
print(create_arithmetic(-2, -3, 5))
numbers = create_arithmetic(2, 3, 7)
print(numbers)
print(create_arithmetic(-2, 3, 7))
'''
#Q8
'''
def create_zodiac(zodiac_list, start_year):
    a_dict = {}
    index = start_year % 2000

    for i in range(len(zodiac_list)):
        a_dict[zodiac_list[(i + index ) % 12]] = start_year + i
    return a_dict

zodiac_list = ['Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Rabbit']
a_dict = create_zodiac(zodiac_list, 2003)
print(a_dict)
print(create_zodiac(zodiac_list, 2024))
'''
#Q9
'''
def read_rainfall_total(locations, filename):
    a_dict = {}
    f = open(filename, 'r')
    data = file.read().strip()
    for i in range(len(locations)):
        a_dict[locations[i]] = data[i]
    f.close()
    return a_dict
'''
#Q10
'''
def read_numbers(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    sum1 = []

    for line in lines:
        number = line.split()
        sum1.append(sum(number))

    return sum1
'''
#Q11
'''
def get_first_term_difference(numbers):
    numbers = sorted(numbers)
    return (numbers[0], numbers[1] - numbers[0])

def get_arithmetic_data(number_lists):
    return [get_first_term_difference(number) for number in number_lists]

data = [[1, 3, 5], [5, 2, -1, 8]]
result = get_arithmetic_data(data)
print(result)
print(type(result))
print(type(result[0]))
'''
#Q1
'''
integer = int(input("Enter an integer: "))
series = 0
for i in range(1, integer + 1):
    series += 1/i
print(f"The sum is {round(series, 1)}")
'''
#Q2
'''
import math
def get_hypotenuse(side1, side2):
    side3 = math.sqrt(side1 ** 2 + side2 ** 2)
    return side3

print(get_hypotenuse(3, 4))
print(get_hypotenuse(8, 15))
'''
#Q3
'''
def get_string(words):
    return '.'.join(words)

a_list = ['coderunner', 'auckland', 'ac', 'nz']
print(get_string(a_list))
'''
#Q4
'''
def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False

print(is_palindrome('radar'))
print(is_palindrome('python'))
print(is_palindrome('madam'))
print(is_palindrome('computer'))
'''
#Q5
'''
def print_names_and_weights(names, weights):
    print(f"{'Name':<10}{'Weight':<6}")
    print(f"----------------")
    for name, weight in zip(names, weights):
        print(f"{name:<10}{weight:.2f}")
    
print_names_and_weights(['Bill', 'Helen', 'Michael'], [76.27, 54.61, 67.92])
'''
#Q6
'''
def get_appended_list(numbers, value):
    a_list = numbers.copy()
    a_list.append(value)
    return a_list

source_list2 = [1,2,3]
print("before", source_list2)
print("after")
target_list = get_appended_list(source_list2, 4)
print("source", source_list2)
print("target", target_list)
'''
#Q7
'''
def modify_list(numbers, value):
    numbers.append(value)

source_list1 = [1,2,3]
print("before", source_list1)
modify_list(source_list1, 4)
print("after", source_list1)
'''
#Q8
'''
def remove_10(numbers):
    for number in numbers.copy():
        if number > 10:
            numbers.remove(number)

numbers = [12, 122, 3, 32, 14, 2, 400, 1, 42]
print("before", numbers )
remove_10(numbers )
print(numbers)
'''
#Q9
'''
def create_string_lengths_dictionary(fruits):
    a_dict = {}
    for fruit in fruits:
        a_dict[fruit] = len(fruit)
    return a_dict

fruits = ['avocado', 'apple', 'blackcurrant', 'banana']
print(create_string_lengths_dictionary(fruits))
'''
#Q10
'''
def create_dictionary(values):
    a_dict = {'words':[], 'numbers':[]}
    for value in values:
        if str(value).isdigit():
            a_dict['numbers'].append(value)
        else:
            a_dict['words'].append(value)
    return a_dict

fruits = ['avocado', 24, 'blackcurrant', 'banana', 'two', 2, 23, 'one']
print(create_dictionary(fruits))
'''






#--------------------------------------------------------------

#Lab2
#Q1













'''
def read_file(filename):
    list1 = []
    f = open(filename, 'r')
    values = f.read().split('\n')
    for value in values:
        list1.append(str(value))
    f.close()
    return list1

data = read_file("years.txt")
print(data)
print(type(data))
print(type(data[0]))
print(type(data[0][0]), type(data[0][1]), type(data[0][1][0]))
'''
#Q2
'''
def create_dictionary(locations):
    a_dict = {}
    for location in locations:
        a_dict[location] = []
    return a_dict

data = ['Auckland (Auckland)', 'Blenheim (Marlborough)']
a_dict = create_dictionary(data)
for key in sorted(a_dict):
    print(key, a_dict[key])
'''
#Q3
'''
def process_rainfall_data(contents, number_of_locations):
    a_dict = {}
    f = open(contents, 'r')
    content = f.read().split('\n')
    for line in content:
        location, rainfall = line.split(",")
        if not location in a_dict:
            a_dict[location] = float(rainfall)
        else:
            a_dict[location] += float(rainfall)
    return a_dict.values()

contents = 'rainfall_2018_small.txt'
result = process_rainfall_data(contents, 5)
for value in result:
    print('{:.2f}'.format(value))
'''
#Q4
'''
def read_file(filename):
    list1 = []
    f = open(filename, 'r')
    values = f.read().split('\n')
    for value in values:
        list1.append(str(value))
    f.close()
    return list1

def create_dictionary(locations):
    a_dict = {}
    for location in locations:
        a_dict[location] = []
    return a_dict

def process_rainfall_data(rainfall_data, locations, rainfall_dict):
    a_list = [0] * len(locations)
    for i in range(len(contents)):
        a_list[i%len(locations)] += float(contents[i].split(',')[1])
    for location in locations:
        rainfall_dict[location].append(a_list[locations.index(location)])
    return rainfall_dict


locations = ['Auckland (Auckland)', 'Blenheim (Marlborough)', 'Christchurch (Canterbury)', 'Dannevirke (Manawatu-Whanganui)', 'Dunedin (Otago)']
contents = read_file('rainfall_2020_small.txt')
rainfall_dict = create_dictionary(locations)
process_rainfall_data(contents, locations, rainfall_dict)
for key in rainfall_dict:
    print(key, end=" ")
    values = rainfall_dict[key]
    for num in values:
        print("{:.2f}".format(num))
'''
#Q5
'''
def print_heading(years):
    len_of_years = len(years)
    print(f"{'Rainfall Data|' :>41}")
    print(f"{'locations| ' :>42}", end='')
    for year in years:
        print(f"{year}| ", end="")
    print(f"\n{'-' * (41 + len_of_years * 6)}")


years = ['2018']
locations = ['Auckland (Auckland)', 'Blenheim (Marlborough)', 'Christchurch (Canterbury)', 'Dannevirke (Manawatu-Whanganui)', 'Dunedin (Otago)']
print_heading(years)
'''
#Q6
'''
def print_table(number_of_columns, rainfall_dict):
    for location in rainfall_dict:
        print(f"{location:>40}|", end='')
        for data in rainfall_dict[location]:
            print(f"{round(data):>5}|", end='')
        print()
    
years = ['2018', '2019']
rainfall_dict =  {'Auckland (Auckland)': [258.2, 73.2], 'Blenheim (Marlborough)': [81.8, 120.39], 'Christchurch (Canterbury)': [118.19, 61.0], 'Dannevirke (Manawatu-Whanganui)': [174.8, 95.4], 'Dunedin (Otago)': [159.79, 259.4]}
print_table(len(years), rainfall_dict)
'''
#Q7
'''
def main():
    filename_years = input("Enter a filename for reading years: ")
    years = read_file(filename_years)
    
    filename_locations = input("Enter a filename for reading locations: ")
    locations = read_file(filename_locations)
    
    filename_rainfall = input("Enter a filename for reading rainfall data: ")
    rainfall_filenames = read_file(filename_rainfall)
    
    rainfall_dict = create_dictionary(locations)
    
    for rainfall_file in rainfall_filenames:
        rainfall_data = read_file(rainfall_file)
        
        process_rainfall_data(rainfall_data, locations, rainfall_dict)
    
    print_heading(years)
    
    print_table(len(years), rainfall_dict)


def read_file(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()
    

def create_dictionary(locations):
    return {location: [] for location in locations}
    

def process_rainfall_data(contents, locations, rainfall_dict):
    for line in contents:
        location, *rainfall_values = line.split(",")
        if location in locations:
            rainfall_values = [float(value) for value in rainfall_values]
            rainfall_dict[location].extend(rainfall_values)
        else:
            print(f"Location '{location}' not found in the list of locations.")


def print_heading(years):
    print(f"{'Rainfall Data|':>41}")
    print(f"{'locations| ':>42}", end='')
    for year in years:
        print(f"{year}| ", end="")
    print(f"\n{'-' * (41 + len(years) * 6)}")


def print_table(number_of_columns, rainfall_dict):
    for location, values in rainfall_dict.items():
        print(f"{location:>40}|", end='')
        for data in values:
            print(f"{round(data):>5}|", end='')
        print()

main()



def main():
    filename_years = input("Enter a filename for reading years: ")
    years = read_file(filename_years)
    
    filename_locations = input("Enter a filename for reading locations: ")
    locations = read_file(filename_locations)
    
    filename_rainfall = input("Enter a filename for reading rainfall data: ")
    rainfall = read_file(filename_rainfall)
    
    a_dict = create_dictionary(locations)
    
    for file in rainfall:
        data = read_file(file)
        value = process_rainfall_data(data, locations, a_dict)
        
    print_heading(years)
    
    print_table(len(years), a_dict)
    
def read_file(filename):
    list1 = []
    f = open(filename, 'r')
    values = f.read().split('\n')
    for value in values:
        list1.append(str(value))
    f.close()
    return list1
    
def create_dictionary(locations):
    a_dict = {}
    for location in locations:
        a_dict[location] = []
    return a_dict
    
def process_rainfall_data(contents, number_of_locations):
    a_dict = {}

    for line in contents:
        location, rainfall = line.split(",")
        if not location in a_dict:
            a_dict[location] = float(rainfall)
        else:
            a_dict[location] += float(rainfall)
    return a_dict.values()
    
def process_rainfall_data(rainfall_data, locations, rainfall_dict):
    a_list = [0] * len(locations)
    for i in range(len(locations)):
        a_list[i%len(locations)] += float(locations[i].split(',')[1])
    for location in locations:
        rainfall_dict[location].append(a_list[locations.index(location)])
    return rainfall_dict
    
def print_heading(years):
    len_of_years = len(years)
    print(f"{'Rainfall Data|' :>41}")
    print(f"{'locations| ' :>42}", end='')
    for year in years:
        print(f"{year}| ", end="")
    print(f"\n{'-' * (41 + len_of_years * 6)}")
    
def print_table(number_of_columns, rainfall_dict):
    for location in rainfall_dict:
        print(f"{location:>40}|", end='')
        for data in rainfall_dict[location]:
            print(f"{round(data):>5}|", end='')
        print()
main()
'''

#--------------------------------------------------------------

#Lab3
#Q2
'''
import math
def get_semi_circle_area(radius):
    area = math.pi * radius ** 2 / 2
    return area

print(get_semi_circle_area(10.5))
'''
#Q6
'''
def apply_gst(prices_list):
    for i in range(len(prices_list)):
        prices_list[i] = prices_list[i] * 1.15
    return prices_list

numbers = [1.59, 45.67, 3.56, 7.29, 8.36, 1034.99]
apply_gst(numbers)
print(', '.join(["{:.2f}".format(price) for price in numbers]))
'''
#Q7
'''
def no_consonants(text):
    if text == '':
        return True
    else:
        for letter in text:
            if letter not in 'aeiouAEIOU':
                return False
            
    return True    

print(no_consonants('dry'))
print(no_consonants('show'))
print(no_consonants('order'))
print(no_consonants('adoulie'))
print(no_consonants('oo'))
'''
#Q8
'''
my_tuple = get_tuple_at(['May', 'Amy', 'Alan'], 1)
print(my_tuple)
print(type(my_tuple))
print(get_tuple_at(['May', 'Amy', 'Alan'], 0))

my_tuple = get_tuple_at(['Caleb', 'Bastian', 'John', 'David', 'Alan'], 0)
print(my_tuple)
'''
#Q9
'''
def remove_out_of_range(numbers):
    for number in numbers.copy():
        if number < 0 or number > 10:
            numbers.remove(number)
    
numbers = [15, -2, 35, 135, 7]
remove_out_of_range(numbers)
print(numbers)
'''
#Q10
'''
def create_baby_names_dictionary(names_list):
    a_dict = {}
    for name in names_list:
        letter = name[0]
        babby = name[1]
        if letter not in a_dict:
            a_dict[letter] = [babby]
        else:
            a_dict[letter].append(babby)

    for letter, name in a_dict.items():
        a_dict[letter] = sorted(name)

    return a_dict


data = [('A', 'Anthony'), ('C', 'Connor'), ('A', 'Alex')]
a_dict = create_baby_names_dictionary(data)
for key in sorted(a_dict.keys()):
    print(key, a_dict[key])
'''
#Q11
'''
def append_double_to(element, values = None):
    if values is None:
        values = []
        values.append(element*2)
        return values
    else:
        values.append(element*2)
        return values

my_list = append_double_to(12)
print(my_list)
my_list = append_double_to(12, my_list)
print(my_list)
my_list = append_double_to(24)
print(my_list)
'''

#--------------------------------------------------------------

#Lab4
#Q1
'''
def is_old_enough(age_value):
    try:
        age_value = int(age_value)
        if age_value >= 18:
            return (True, age_value)
        else:
            return (False, age_value)
    except TypeError:
        return (False, "ERROR: The type is incorrect!")
    except ValueError:
        return (False, "ERROR: The value is invalid!")


print(is_old_enough([18, 12]))    
'''
#Q2
'''
import math
def get_semicircle_area(radius):
    try:
        radius = float(radius)
        if radius == 0:
            return (0, 'ERROR: Not a semicircle!')
        elif radius < 0:
            return (0, 'ERROR: radius must be positive!')
        else:
            area = round(math.pi * radius ** 2 / 2)
            return (area, '')
        
    except ValueError:
        return (0, 'ERROR: The value is invalid!')
    
    except TypeError:
        return (0, 'ERROR: The type is incorrect!')

print(get_semicircle_area('ten'))
print(get_semicircle_area([1,2,3]))
'''
#Q3
'''
def sum_of_multiples_of_3(numbers, start_index, end_index):
    try:
        sum1 = 0
        for i in range(start_index, end_index + 1):
            number = int(numbers[i])
            if number % 3 == 0:
                sum1 += number
        return sum1
    except IndexError:
        return ("ERROR: Out of range!\n0")
    except ValueError:
        return ("ERROR: Invalid number!\n0")

list1 = [1, 5, 9, 2, 8, 3, 9, 6]
print(sum_of_multiples_of_3(list1, 5, 6))
list1 = [1, 2, 3]
print(sum_of_multiples_of_3(list1, 2, 6))
list2 = [1, 'A', 2]
print(sum_of_multiples_of_3(list2, 1, 2))
'''
#Q4
'''
def get_french_word(word_dictionary, english_word):
    try:
        return word_dictionary[english_word]

    except KeyError:
        return f"ERROR: {english_word} is not available.\nNone"

    except:
        return "ERROR: Invalid dictionary!\nNone"

dictionary = {'yes':'oui','no':'non','hello':'bonjour','thank you':'merci','and':'et','or':'ou','but':'mais'}
print(get_french_word(dictionary, 'hello'))
print(get_french_word(dictionary, 'orange'))
print(get_french_word([1, 2, 3], 'yes'))
print(get_french_word(dictionary, 'yes'))         
'''
#Q5
'''
def sum_of_scores(numbers):
    sum1 = 0
    for number in numbers:
        try:
            number = int(number)
            if number > 0 and number < 10:
                sum1 += number
            
        except(TypeError, ValueError):
            sum1 += 0
            return sum1

    return sum1

my_list = [0, 5, -5, 15, 50, 10, 2]
print(sum_of_scores(my_list))
my_list = [1, 2, 13, 4, "two", 2, 9]
print(sum_of_scores(my_list))
print(sum_of_scores([]))
print(sum_of_scores(['NA']))
'''
#Q6
'''
def sum_of_scores_continue(numbers):
    sum1 = 0
    for number in numbers:
        try:
            number = int(number)
            if number > 0 and number < 10:
                sum1 += number
            
        except(TypeError, ValueError):
            sum1 += 0
            

    return sum1

my_list = [-1, 0, 5, 2, 'ten', 35, 45, 9, 20]
print(sum_of_scores_continue(my_list))
print(sum_of_scores_continue([-1, 0, 10, 20, 'ten', 35, 45, 105, 20]))
my_list = [1, 2, 3, 4, "two", 2]
print(sum_of_scores_continue(my_list))
'''
#Q7
'''
def get_valid_twenty_sided_dice():
    dice = -1
    while dice < 1 or dice > 20:
        try:
            dice = int(input("Enter a valid dice: "))
        except:
            pass
    return dice


value = get_valid_twenty_sided_dice()
print('Valid input:', value)
'''
#Q8
'''
def read_multiples_of_3(filename):
    try:
        a_list = []
        f = open(filename, 'r')
        data = f.read().split()
        for number in data:
            try:
                number = float(number)
                if number % 3 == 0:
                    a_list.append(int(number))
            except (ValueError, TypeError):
                pass
        f.close()
        return a_list
    except FileNotFoundError:
        return f"ERROR: The file '{filename}' does not exist.\n[]"

print(read_multiples_of_3("eight_numbers.txt"))
print(read_multiples_of_3('input_unknown.txt'))
print(read_multiples_of_3('input_unknown.txt'))
'''
#Q9
'''
def read_countries(filename):
    try:
        with open(filename, 'r') as f:
            a_dict = {}
            for line in f:
                line = line.strip()
                if line:
                    part = line.split(',')
                    if len(part) == 2:
                        a_dict[part[0]] = part[1]
                    else:
                        print(f"ERROR: Invalid '{line}'!")
            return a_dict
    except FileNotFoundError:
        return f"ERROR: The file '{filename}' does not exist.\n{{}}"
'''
#Q10
'''
def validate_username(username):
    if 4 > len(username) or len(username) > 8 or (username[-4]).isdigit() or not (username[-3].isdigit()):
        raise ValueError(f"ERROR: '{username}' - Invalid Format!")
    if (int(username[-3]) + (int(username[-2]) * 2)) % 9 != int(username[-1]):
        raise ValueError(f"ERROR: '{username}' - Invalid check digit!")
    return username[-1]

        
print(validate_username('acha455'))
print(validate_username('acha568'))
print(validate_username('kng327'))  

try:
    print(validate_username('cbur974'))
    print(validate_username('k1235'))
except ValueError as e:
    print(e)
else:
    print("Well done!")

try:
    print(validate_username('12345'))
except ValueError as e:
    print(e)
else:
    print("Well done!")

try:
    print(validate_username('username'))
except ValueError as e:
    print(e)
else:
    print("Well done!")
'''

#--------------------------------------------------------------

#Lab5
#Q5
'''
def rate(n):
    big_o = 4
    total = 0
    i = 1
    while i < n:
        total += i
        i *= 2
        big_o += 3
    print(f"Number of operations: {big_o}")
    
rate(2)
rate(8)
'''
#Q6
'''
def rate(n):
    big_o = 4
    total = 0
    i = 1
    while i < n:
        j = n
        while j > 0:
            total += j 
            j -= 1
            big_o += 3
        i *= 2
        big_o += 4
    print(f"Number of operations: {big_o}")

rate(2)
rate(4)
'''
#Q7
'''
def rate(n):
    big_o = 3
    i = 0
    total = 0
    while i < n:
        total += i
        i += 2
        big_o += 3
    return big_o

print(rate(2))
print(rate(3))
print(rate(4))
print(rate(5))
print(rate(6))
print(rate(7))
print(rate(8))
print(rate(9))
'''

#--------------------------------------------------------------

#Lab6
#Q2
'''
def get_position_of_largest(data, index):
    max_num = data[0]
    for i in range(index + 1):
        if data[i] > max_num:
            max_num = data[i]
    return data.index(max_num)

numbers = [53, 48, 24, 76, 28]
print(get_position_of_largest(numbers, 3))
'''
#Q3
'''
def selection_single_pass(data, index):
    max_num = max(data[:index + 1])
    data[data.index(max_num)], data[index] = data[index], data[data.index(max_num)]
    
numbers = [76, 53, 48, 24, 12]
selection_single_pass(numbers, 4)
print(numbers)
'''
#Q4
'''
def selection_single_pass(data, index):
    max_num = max(data[:index + 1])
    data[data.index(max_num)], data[index] = data[index], data[data.index(max_num)]
    
def my_selection_sort(data):	
    for index in range(len(data) - 1, 0, -1 ):
        selection_single_pass(data, index)
    return data

numbers = [76, 53, 48, 24, 12]
my_selection_sort(numbers)
print(numbers)
'''
#Q6
'''
def bubble_single_pass(data, index):
    for i in range(index):
        if data[i] > data[i + 1]:
            data[i], data[i + 1] = data[i + 1], data[i]
    return data

numbers = [76, 53, 48, 24, 12]
bubble_single_pass(numbers, 4)
print(numbers)
numbers = [76, 53, 48, 24, 12]
bubble_single_pass(numbers, 1)
print(numbers)
'''
#Q7
'''
def bubble_single_pass(data, index):
    for i in range(index):
        if data[i] > data[i + 1]:
            data[i], data[i + 1] = data[i + 1], data[i]
    return data

def my_bubble_sort(data): 
    for index in range(len(data) - 1, 0, -1):
        bubble_single_pass(data, index)
    return data
        
numbers = [76, 53, 48, 24, 12]
my_bubble_sort(numbers)
print(numbers)
'''
#Q9





#--------------------------------------------------------------
#2023 S0 Test
#Q1
'''
def print_table(words_list, width):
    for word in words_list:
        print(f"|{word:<{width}}|")

print_table(['Summer', 'is', 'over', 'and', 'the', 'hot', 'days', 'are', 'gone'], 6)
'''
#Q2
'''
def get_check_digit(code):
    what_is_your_name = 0
    my_name_is_jack = 0
    for i in range(len(code)):
        my_name_is_jack += int(code[i]) * what_is_your_name
        what_is_your_name += 1
    nice_to_meet_you_jack = my_name_is_jack % 5
    return nice_to_meet_you_jack


print(get_check_digit('013'))
print(get_check_digit('364'))
'''
#Q3
'''
import math
def get_middle_letter(word):
    index = math.floor(len(word) / 2)
    return word[index]
        
print(get_middle_letter(''))
'''
#Q4
'''
def is_multiple_of_3(username):
    return int(username[4:]) % 3 == 0

print(is_multiple_of_3('rliu061'))
print(is_multiple_of_3('mgra734'))
print(is_multiple_of_3('dng134'))
print(is_multiple_of_3('bcar735'))
'''
#Q5


'''
print(get_pair_sum([1.5, 2, 3, 4]))
print(get_pair_sum([10.5, 2]))
print(get_pair_sum(['input', 'test', 'answer']))
'''
#Q6
'''
def get_word_score(word):
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    total = 0
    string = ''
    
    for i in word:
        if i.isalpha():
            string += i.lower()
            total += valid_letters.find(i.lower())
    return (string, total)


print(get_word_score('Summer,'))
print(get_word_score('Abd,'))
print(get_word_score('At,'))
print(get_word_score('beat'))
result = get_word_score('beta')
print(type(result))
print(result)
print(get_word_score('AT SCHOOL'))

print(get_word_score('arcs'))
print(get_word_score('cars'))
print(get_word_score('OUT!'))

print(get_word_score('angel?'))
print(get_word_score('angle'))

print(get_word_score('down '))
print(get_word_score('down'))

print(get_word_score('STANDARD'))
print(get_word_score('TEST CASE'))
'''
#Q7
'''

def convert_dictionary(scores_dictionary):
    result_dict = {}
    
    for key, words in scores_dictionary.items():
        for word in words:
            score_sum = sum(ord(char.lower()) - ord('a') for char in word)
            
            word_length = len(word)
            
            if word_length not in result_dict:
                result_dict[word_length] = [(word, score_sum)]
            else:
                result_dict[word_length].append((word, score_sum))
    
    for key in result_dict:
        result_dict[key] = sorted(result_dict[key])
    
    return result_dict




data = {24: ['beta', 'beat'], 38: ['fish'], 19: ['of']}
a_dict = convert_dictionary(data)
print(type(a_dict))
for key in sorted(a_dict):
    print(key, a_dict[key])

data = {37: ['arcs', 'cars'], 24: ['beat', 'beta'], 53: ['out'], 15: ['can']}
a_dict = convert_dictionary(data)
for key in sorted(a_dict):
    print(key, a_dict[key])
'''
#Q8
'''
def get_word_score(word):
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    word = ''.join(char for char in word if char.isalpha()).lower()
    score = sum(valid_letters.index(letter) + 1 for letter in word)
    return (word, score)

def read_word_get_sum_score(filename):
    try:
        with open(filename, 'r') as file:
            words = []
            total_score = 0
            for line in file:
                for word in line.split():
                    word, score = get_word_score(word)
                    words.append(word)
                    total_score += score
            return (words, total_score)
    except FileNotFoundError:
        print(f"ERROR: The file '{filename}' does not exist.")
        return None

# Test cases
read_word_get_sum_score('errors.txt')
print(read_word_get_sum_score('text6.txt'))
'''
#Q9
'''
def get_word_score(word):
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    total = 0
    string = ''
    
    for i in word:
        if i.isalpha():
            string += i.lower()
            total += valid_letters.find(i.lower())
    return (string, total)


class WordScore:
    def __init__(self, word):
        self.word = get_word_score(word)[0]
        self.score = get_word_score(word)[1]

    def get_word(self):
        return self.word
    
    def get_score(self):
        return self.score

    def __str__(self):
        return f"{self.word}({self.score})"

    def __eq__(self, other):
        if isinstance(other, WordScore):
            return self.word == other.word and self.score == other.score
        return False

    def __lt__(self, other):
        return self.score < other.score
            

word_score1 = WordScore("Electricity!")
print(word_score1)
print(word_score1.get_word(), word_score1.get_score())
word_score2 = WordScore("Water?")
print(word_score2)
'''
#Q10
'''
def get_word_score(word):
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    total = 0
    string = ''
    
    for i in word:
        if i.isalpha():
            string += i.lower()
            total += valid_letters.find(i.lower())
    return (string, total)


class WordScore:
    def __init__(self, word):
        self.word = get_word_score(word)[0]
        self.score = get_word_score(word)[1]

    def get_word(self):
        return self.word
    
    def get_score(self):
        return self.score

    def __str__(self):
        return f"{self.word}({self.score})"

    def __eq__(self, other):
        if isinstance(other, WordScore):
            return self.word == other.word and self.score == other.score
        return False

    def __lt__(self, other):
        return self.score < other.score

word_score1 = WordScore("beat")
word_score2 = WordScore("beat")
word_score3 = WordScore("beta")
word_score4 = WordScore('standand')
print(word_score1 == word_score2)
print(word_score2 == word_score3)
print(word_score2 < word_score3)
print(word_score3 < word_score4)
'''
#Q11
'''
def get_word_score(word):
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    total = 0
    string = ''
    
    for i in word:
        if i.isalpha():
            string += i.lower()
            total += valid_letters.find(i.lower())
    return (string, total)

class WordScore:
    def __init__(self, word):
        self.word = get_word_score(word)[0]
        self.score = get_word_score(word)[1]

    def get_word(self):
        return self.word
    
    def get_score(self):
        return self.score

    def __str__(self):
        return f"{self.word}({self.score})"

    def __eq__(self, other):
        if isinstance(other, WordScore):
            return self.word == other.word and self.score == other.score
        return False

    def __lt__(self, other):
        return self.score < other.score

class FileScore:
    def __init__(self, filename = ''):
        self.name = name
        try:
            contents = open(filename, 'r')
            self.word_scores_list = contents.read().split()
        except FileNotFoundError:
            self.word_scores_list = []

    def get_filename(self):
        return self.filename

    def get_word_score(self, index):
        return WordScore(self.word_scores_list[index])
        

file_score1 = FileScore("text.txt")
print(type(file_score1))
print(type(file_score1.get_word_score(0)))
print(file_score1.get_word_score(0))
'''
#q7
'''
def get_word_score(word):
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    total = 0
    string = ''
    
    for i in word:
        if i.isalpha():
            string += i.lower()
            total += valid_letters.find(i.lower())
    return (string, total)



def convert_dictionary(scores_dictionary):
    a_dict = {}
    for key, values in scores_dictionary.items():
        for word in values:
            if len(word) not in a_dict:
                a_dict[len(word)] = [(word, key)]
            else:
                a_dict[len(word)].append((word, key))

    for key in a_dict:
        a_dict[key] = sorted(a_dict[key])
        
    return a_dict

data = {24: ['beta', 'beat'], 38: ['fish'], 19: ['of']}
a_dict = convert_dictionary(data)
print(type(a_dict))
for key in sorted(a_dict):
    print(key, a_dict[key])
'''   
























#--------------------------------------------------------------
#Lab7
#Q2
'''
def selection_sort(data):
    compare = []
    swap = []
    number = len(data)
    for pass_num in range(len(data) - 1, 0, -1):
        position_largest = 0
        for i in range(1, pass_num + 1):
            if data[i] > data[position_largest]:
                position_largest = i
        number -= 1
        compare.append(number)
        swap.append(1)
        data[position_largest], data[i] = data[i], data[position_largest]
    return (compare, swap)

numbers = [70, 48, 54, 79, 33]
result = selection_sort(numbers)
print(result)
'''
#Q4
'''
def bubble_sort(data):
    number = len(data)
    compare = []
    swap = []
    for pass_num in range(len(data) - 1, 0, -1):
        count = 0
        for i in range(0, pass_num):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                count += 1

        number -= 1
        compare.append(number)
        swap.append(count)

    return (compare,swap)

numbers = [12, 78, 81, 99, 91]
result = bubble_sort(numbers)
print(result)

numbers = [92, 33, 63, 6, 66, 77, 74, 51, 30, 86]
result = bubble_sort(numbers)
print(result)
'''
#Q6
#垃圾代码，屎山代码
'''
def compare(value, item_to_insert, counts_list):
    counts_list[0] += 1 #Add 1 to number of comparisons
    return value > item_to_insert

def insertion_sort(a_list):
    compare = []
    swap = []
    
    for index in range(1, len(a_list)):
        item_to_insert = a_list[index]
        i = index - 1
        
        compare_count = 0
        swap_count = 0

        if a_list[i] < item_to_insert:
            compare_count += 1
            
        while i >= 0 and a_list[i] > item_to_insert:
            a_list[i + 1] = a_list[i]
            swap_count += 1
            i -= 1
            compare_count += 1

        compare.append(compare_count)
        swap.append(swap_count)
        
        a_list[i + 1] = item_to_insert
    return (compare, swap)
'''
#正确的代码
'''

def compare(value, item_to_insert, counts_list):
    counts_list[0] += 1 #Add 1 to number of comparisons
    return value > item_to_insert

def insertion_sort(a_list):
    compare_list = []
    swap_list = []
    
    for index in range(1, len(a_list)):
        item_to_insert = a_list[index]
        i = index - 1
        counts_list = [0, 0]
        while i >= 0 and compare(a_list[i], item_to_insert, counts_list):
            a_list[i + 1] = a_list[i]
            i -= 1
            counts_list[1] += 1
        compare_list.append(counts_list[0])
        swap_list.append(counts_list[1])
        a_list[i + 1] = item_to_insert
    return compare_list, swap_list
        
numbers = [92, 86, 77, 66, 51, 42, 33, 23]
result = insertion_sort(numbers)
print(result)

numbers = [50, 63, 11, 79, 22, 70, 65, 39, 97, 48]
result = insertion_sort(numbers)
print(result)

numbers = [69, 93, 3, 73, 68, 82, 28, 50, 76, 64, 95, 37, 19, 0, 17, 20, 86, 0, 53, 62]
result = insertion_sort(numbers)
print(result)
'''

#Q7
'''
def bubble_sort(data):
    number = len(data)
    compare = []
    swap = []
    for pass_num in range(len(data) - 1, 0, -1):
        count = 0
        for i in range(0, pass_num):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                count += 1

        number -= 1
        compare.append(number)
        swap.append(count)

    return (len(data),sum(compare),sum(swap))

def bubble_sort_fast(data):
    number = len(data)
    compare = []
    swap = []

    for pass_num in range(len(data)-1, 0, -1):
        count = 0
        for i in range(0, pass_num):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                count += 1

        number -= 1
        compare.append(number)
        swap.append(count)
        if count == 0:
            return (len(data), sum(compare), sum(swap))
        
    return (len(data),sum(compare), sum(swap))


d1 = [12, 15, 19, 37, 39]
result1 = bubble_sort(d1)
print('Normal Bubble Sort: Length: {} Comparisons: {} Swaps: {}'.format(result1[0], result1[1], result1[2]))
d2 = [12, 15, 19, 37, 39]
result2 = bubble_sort_fast(d2)
print('Fast Bubble Sort: Length: {} Comparisons: {} Swaps: {}'.format(result2[0], result2[1], result2[2]))
'''
#Q8
'''
def linear_search(numbers, target_number):
    count = 0
    for number in numbers:
        count += 1
        if number == target_number:
            return (True, count)
            
    return (False,count)

result = linear_search([54, 26, 93, 17, 77, 20], 32)
print('Found: {} Comparisons: {}'.format(result[0], result[1]))
print(type(result))

result = linear_search([93, 54, 78, 18, 61, 13, 36, 42, 16, 60, 58, 92], 61)
print('Found: {} Comparisons: {}'.format(result[0], result[1]))
'''
#Q9
#我的方法更牛逼
'''
def linear_search_sorted(numbers, target_number):
    count = 0
    if target_number > numbers[len(numbers)//2]:
    
        for number in numbers[len(numbers)//2:len(numbers)]:
            count += 1
            if number == target_number:
                return (True, count)
            
    elif target_number == numbers[len(numbers)//2]:
        return (True, len(numbers)//2 + 1)


    
    else:
        for number in numbers[:len(numbers)//2]:
            count += 1
            if number == target_number:
                return (True, count)
        
            
    return (False,count)
'''
#题目要求做法
'''
def linear_search_sorted(numbers, target_number):
    count = 0
    for number in numbers:
        count += 1
        if number == target_number:
            return (True, count)
        if number > target_number:
            return (False, count)
            
    return (False,count)



result = linear_search_sorted([2, 3, 5, 6, 7, 8, 9], 4)
print(type(result))
print('Found: {} Equality Comparisons: {}'.format(result[0], result[1]))

result = linear_search_sorted([2, 3, 5, 6, 7, 8, 9], 6)
print('Found: {} Equality Comparisons: {}'.format(result[0], result[1]))

result = linear_search_sorted([2, 3, 5, 6, 7, 8, 9], 9)
print('Found: {} Equality Comparisons: {}'.format(result[0], result[1]))
'''
#Q11
'''
def binary_search(names_list, target_name):
    left_index = 0
    right_index = len(names_list) - 1

    while left_index <= right_index:

        mid_index = (left_index + right_index) // 2
        mid_name = names_list[mid_index]
        print(f"left: {left_index}, mid: {mid_index}, right: {right_index}")

        if mid_name == target_name:
            return True
        elif mid_name < target_name:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return False



my_list = ['Alexandra', 'Auckland', 'Blenheim', 'Chatham Islands', 'Christchurch', 'Dunedin', 'Gisborne', 'Hamilton', 'Hokitika', 'Invercargill', 'Kaikoura', 'Kaitaia', 'Lake Tekapo', 'Manapouri', 'Masterton', 'Milford Sound', 'Mt Cook', 'Napier', 'Nelson', 'New Plymouth', 'Palmerston North', 'Queenstown', 'Rotorua', 'Taupo', 'Tauranga', 'Timaru', 'Wanganui', 'Wellington', 'Westport', 'Whangarei']
print(binary_search(my_list, "Milford Sound"))
'''
#--------------------------------------------------------------
#Lab8 Exercise
#Q2
'''
class Square:
    def __init__(self, side_length = 1):
        self.side_length = side_length

    def get_perimeter(self):
        return 4 * self.side_length

s = Square(10)
print(s.get_perimeter())
s2 = Square()
print(s2.get_perimeter())
'''
#Q3
'''
class Fraction:
    def __init__(self, numerator=10, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

f1 = Fraction(20, 2)
f2 = Fraction()
print(f1)
print(f2)
'''
#Q4
'''
class Square:
    def __init__(self, side_length = 10):
        self.side_length = side_length

    def get_perimeter(self):
        return 4 * self.side_length

    def __repr__(self):
        return f"Square({self.side_length})"

    def __str__(self):
        return f"{self.side_length} x {self.side_length} Square"

s = Square()
print(s.get_perimeter())
print(repr(s))
print(s)

a_list = [Square(), Square(5)]
for item in a_list:
    print(item)
    print(repr(item))

'''
#Q5
'''
class Circle:
    def __init__(self, radius = 1):
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.radius})"

    def __str__(self):
        return f"A circle with a radius of {self.radius:.2f}cm."

    def set_radius(self, radius):
        if radius > 0:
            self.radius = radius

    def get_diameter(self):
        return 2 * self.radius

c1 = Circle(10)
print(str(c1))
print(repr(c1))
'''
#Q6
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"({self.x}, {self.y})"

    def get_halfway_point(self, target):
        halfway_x = (self.x + target.x) / 2
        halfway_y = (self.y + target.y) / 2
        return Point(halfway_x, halfway_y)
    
p = Point(3, 4)
q = Point(5, 12)
r = p.get_halfway_point(q)
print(type(r))
print(r) 
'''
#Q7
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"({self.x}, {self.y})"

    def get_halfway_point(self, target):
        halfway_x = (self.x + target.x) / 2
        halfway_y = (self.y + target.y) / 2
        return Point(halfway_x, halfway_y)

    def __eq__(self, other):
        if isinstance(other, Point):
            if self.x == other.x and self.y == other.y:
                return True
            return False
        return False

    def __ne__(self, other):
        if not __eq__():
            return True
        return False


p = Point(3, 4)
q = Point(5, 12)
r = Point(3, 4)
print(p == q)
print(p == r)
'''
#Q8
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"({self.x}, {self.y})"

    def get_halfway_point(self, target):
        halfway_x = (self.x + target.x) / 2
        halfway_y = (self.y + target.y) / 2
        return Point(halfway_x, halfway_y)

    def __eq__(self, other):
        if isinstance(other, Point):
            if self.x == other.x and self.y == other.y:
                return True
            return False
        return False

    def __ne__(self, other):
        if not __eq__():
            return True
        return False

    def __add__(self, other):
        dataa = self.x + other.x
        datab = self.y + other.y
        return Point(dataa, datab)

        
p1 = Point(10, 20)
p2 = Point(30, 40)
p3 = p1 + p2
print("p1 =", p1)
print("p2 =", p2)
print("p3 =", p3)
      
p = Point(2, 4)
q = Point(10, 20)
r = p + q
print(p)
print(q)
print(r)
print(type(r))
'''
#Q9
'''
class Circle:
    def __init__(self, radius = 1):
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.radius})"

    def __str__(self):
        return f"A circle with a radius of {self.radius:.2f}cm."

    def set_radius(self, radius):
        if radius > 0:
            self.radius = radius

    def get_diameter(self):
        return 2 * self.radius


    def __lt__(self, other):
        if self.get_diameter() < other.get_diameter():
            return True
        return False
    

c1 = Circle(1)
c2 = Circle(4)
print(c1<c2)
'''

#--------------------------------------------------------------
#Lab8
#Q1
'''
class Pyramid:
    def __init__(self, base_length = 1, base_width = 1, height = 1):
        self.base_length = base_length
        self.base_width = base_width
        self.height = height

    def get_base_length(self):
        return self.base_length

    def set_base_length(self, base_length):
        if base_length > 0:
            self.base_length = base_length

pyramid1 = Pyramid()
print(pyramid1.get_base_length())
pyramid2 = Pyramid(4, 6, 12)
print(pyramid2.get_base_length())
pyramid1.set_base_length(-1)
print(pyramid1.get_base_length())
pyramid1.set_base_length(12)
print(pyramid1.get_base_length())
pyramid3 = Pyramid(1, 1, 1)
print(pyramid1 == pyramid3)
'''
#Q2
'''
class Pyramid:
    def __init__(self, base_length = 1, base_width = 1, height = 1):
        self.base_length = base_length
        self.base_width = base_width
        self.height = height

    def get_base_length(self):
        return self.base_length

    def set_base_length(self, base_length):
        if base_length > 0:
            self.base_length = base_length

    def get_base_width(self):
        return self.base_width

    def set_base_width(self, base_width):
        if base_width > 0:
            self.base_width = base_width

    def get_height(self):
        return self.height

    def set_height(self, height):
        if height > 0:
            return self.height

pyramid1 = Pyramid()
print(pyramid1.get_base_width())
pyramid2 = Pyramid(4, 6, 12)
print(pyramid2.get_base_width())
pyramid1.set_base_length(-1)
print(pyramid1.get_base_width())
pyramid1.set_base_length(12)
print(pyramid1.get_base_width())
pyramid3 = Pyramid(1, 2, 5)
print(pyramid1 == pyramid3)
'''
#Q3
'''
class Pyramid:
    def __init__(self, base_length = 1, base_width = 1, height = 1):
        self.base_length = base_length
        self.base_width = base_width
        self.height = height

    def get_base_length(self):
        return self.base_length

    def set_base_length(self, base_length):
        if base_length > 0:
            self.base_length = base_length

    def get_base_width(self):
        return self.base_width

    def set_base_width(self, base_width):
        if base_width > 0:
            self.base_width = base_width

    def get_height(self):
        return self.height

    def set_height(self, height):
        if height > 0:
            return self.height

    def get_base_area(self):
        return self.base_length * self.base_width


    def get_volume(self):
        return (self.base_length * self.base_width * self.height) / 3

pyramid1 = Pyramid()
print(pyramid1.get_base_area())
print("{:.2f}".format(pyramid1.get_volume()))
pyramid2 = Pyramid(4, 6, 12)
print(pyramid2.get_base_area())
print("{:.2f}".format(pyramid2.get_volume()))
'''
#Q4
'''
class Pyramid:
    def __init__(self, base_length = 1, base_width = 1, height = 1):
        self.base_length = base_length
        self.base_width = base_width
        self.height = height

    def get_base_length(self):
        return self.base_length

    def set_base_length(self, base_length):
        if base_length > 0:
            self.base_length = base_length

    def get_base_width(self):
        return self.base_width

    def set_base_width(self, base_width):
        if base_width > 0:
            self.base_width = base_width

    def get_height(self):
        return self.height

    def set_height(self, height):
        if height > 0:
            return self.height

    def get_base_area(self):
        return self.base_length * self.base_width


    def get_volume(self):
        return (self.base_length * self.base_width * self.height) / 3

    def __repr__(self):
        return f"Pyramid({self.base_length}, {self.base_width}, {self.height})"

    def __str__(self):
        return f"A pyramid with a base area of {self.get_base_area()} and a volume of {self.get_volume():.2f}."

pyramid1 = Pyramid(2, 4, 6)
print(pyramid1)
print(type(pyramid1))
print(repr(pyramid1))
pyramid2 = Pyramid()
print(pyramid2)
print(repr(pyramid2))
'''
#Q5
'''
class Pyramid:
    def __init__(self, base_length = 1, base_width = 1, height = 1):
        self.base_length = base_length
        self.base_width = base_width
        self.height = height

    def get_base_length(self):
        return self.base_length

    def set_base_length(self, base_length):
        if base_length > 0:
            self.base_length = base_length

    def get_base_width(self):
        return self.base_width

    def set_base_width(self, base_width):
        if base_width > 0:
            self.base_width = base_width

    def get_height(self):
        return self.height

    def set_height(self, height):
        if height > 0:
            return self.height

    def get_base_area(self):
        return self.base_length * self.base_width


    def get_volume(self):
        return (self.base_length * self.base_width * self.height) / 3

    def __repr__(self):
        return f"Pyramid({self.base_length}, {self.base_width}, {self.height})"

    def __str__(self):
        return f"A pyramid with a base area of {self.get_base_area()} and a volume of {self.get_volume():.2f}."

    def __eq__(self, other):
        if isinstance(other, Pyramid):
            if self.base_length == other.base_length and self.base_width == other.base_width and self.height == other.height:
                return True
            return False
        return False

pyramid1 = Pyramid()
pyramid2 = Pyramid(2, 4, 6)
print(pyramid1 == pyramid2)
print(pyramid2 == (2, 4, 6))
print(pyramid1 == 1)
print(pyramid1 == (1, 1, 1))
pyramid3 = Pyramid(2, 4, 6)
print(pyramid2 == pyramid3)
print(repr(pyramid2))
print(repr(pyramid3))
'''
#Q6
'''
class Pyramid:
    def __init__(self, base_length = 1, base_width = 1, height = 1):
        self.base_length = base_length
        self.base_width = base_width
        self.height = height

    def get_base_length(self):
        return self.base_length

    def set_base_length(self, base_length):
        if base_length > 0:
            self.base_length = base_length

    def get_base_width(self):
        return self.base_width

    def set_base_width(self, base_width):
        if base_width > 0:
            self.base_width = base_width

    def get_height(self):
        return self.height

    def set_height(self, height):
        if height > 0:
            return self.height

    def get_base_area(self):
        return self.base_length * self.base_width


    def get_volume(self):
        return (self.base_length * self.base_width * self.height) / 3

    def __repr__(self):
        return f"Pyramid({self.base_length}, {self.base_width}, {self.height})"

    def __str__(self):
        return f"A pyramid with a base area of {self.get_base_area()} and a volume of {self.get_volume():.2f}."

    def __eq__(self, other):
        if isinstance(other, Pyramid):
            if self.base_length == other.base_length and self.base_width == other.base_width and self.height == other.height:
                return True
            return False
        return False

    def __lt__(self, other):
        if self.get_volume() < other.get_volume():
            return True
        return False

    def __le__(self, other):
        if self.get_volume() <= other.get_volume():
            return True
        return False

    def __gt__(self, other):
        if self.get_volume() > other.get_volume():
            return True
        return False

    def __ge__(self, other):
        if self.get_volume() >= other.get_volume():
            return True
        return False

pyramid1 = Pyramid()
pyramid2 = Pyramid(2, 4, 6)
print(pyramid1)
print(pyramid2)
print(pyramid1 == pyramid2)
print(pyramid1 < pyramid2)
print(pyramid1 <= pyramid2)
print(pyramid1 > pyramid2)
print(pyramid1 >= pyramid2)
'''
#Q7
'''
class PolygonalNumber:
    def __init__(self, numbers = [1]):
        self.numbers = numbers
        

sequence2 = PolygonalNumber()
print(sequence2.numbers)

sequence1 = PolygonalNumber()
print(type(sequence1))
print(sequence1.numbers)
sequence2 = PolygonalNumber()
print(sequence2.numbers)
print(sequence1 == sequence2)

'''
#Q8
'''
class PolygonalNumber:
    def __init__(self, sides = 1, terms = 1):
        self.sides = sides
        self.terms = terms

        if self.terms == 0:
            self.numbers = [1]

        else:
            self.numbers = []
            for i in range(1, self.terms + 1):
                number = round((((self.sides - 2)*(i**2)) - ((self.sides - 4) * i))/2)
                self.numbers.append(number)

    def __str__(self):
        return f"The polygon numbers are {self.numbers}."

sequence1 = PolygonalNumber()
print(type(sequence1))
print(sequence1.numbers)
sequence2 = PolygonalNumber(3, 4)
print(sequence2.numbers)
print(sequence1 == sequence2)
'''
#--------------------------------------------------------------
#Lab9 Exercise
#Q1
'''
class Engine:
    def start(self):
        print("Engine started")
    def stop(self):
        print("Engine stopped")
class Car:
    def __init__(self):
        self.engine = Engine()
    def start(self):
        self.engine.start()
    def stop(self):
        self.engine.stop()

my_car = Car()
my_car.start()
my_car.stop()
'''
#Q2
'''
class Author:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.name}"
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Title={self.title}, author={self.author}"
author_john = Author("John Doe")
print(author_john)
book = Book("Python Basics", author_john)
print(book)
'''
#Q3
'''
class Point:
    def __init__(self, x = 1, y = 1):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

p1 = Point()
p2 = Point(3, 4)
print(p1)
print(p2)
print(type(p1))
p1.translate(100, -100)
print(p1)
'''
#Q4
'''
class Point:
    def __init__(self, x = 1, y = 1):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
        
class Line:
    def __init__(self, x1 = 1, y1 = 1, x2 = 1, y2 = 1):
        self.start_point = Point(x1, y1)
        self.end_point = Point(x2, y2)

    def __str__(self):
        return f"Line: {self.start_point} to {self.end_point}"


line1 = Line()
print(line1)
line2 = Line(1, 2, 3, 4)
print(line2)
print(type(line1))
print(type(line1.start_point))
'''
#Q5
'''
class Point:
    def __init__(self, x = 1, y = 1):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
        
class Line:
    def __init__(self, x1 = 1, y1 = 1, x2 = 1, y2 = 1):
        self.start_point = Point(x1, y1)
        self.end_point = Point(x2, y2)

    def __str__(self):
        return f"Line: {self.start_point} to {self.end_point}"

    def translate(self, dx, dy):
        self.start_point.translate(dx, dy)
        self.end_point.translate(dx, dy)

        
line1 = Line()
line2 = Line(1, 2, 3, 4)
line1.translate(10, 20)
line2.translate(50, 100)
print(line1)
print(line2)
'''
#Q6
'''
import math
class Circle:
    def __init__(self, radius = 1):
        self.radius = radius

    def __str__(self):
        return f"A circle with a radius of {self.radius:.2f}cm."

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

c1 = Circle(4)
print(c1)
print("Area = {:.2f}".format(c1.get_area()))
print("Perimeter= {:.2f}".format(c1.get_perimeter()))
circle2 = Circle()
print(circle2)
'''
#Q7
'''
import math
class Circle:
    def __init__(self, radius = 1):
        self.radius = radius

    def __str__(self):
        return f"A circle with a radius of {self.radius:.2f}cm."

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

class Cylinder:
    def __init__(self, circle = 1, height = 1):
        self.circle = circle
        self.height = height
        
    def get_total_surface_area(self):
        return 2 * self.circle.get_area() + self.circle.get_perimeter() * self.height
    
c1 = Circle(4)
cy1 = Cylinder(c1, 5)
print("Surface area={:.2f}".format(cy1.get_total_surface_area()))
'''
#Q8
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("Anna", 21)
print(p1)
p2 = Person("Emma", 17)
print(p2)
print(type(p1))
'''
#Q9
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

class Party:
    def __init__(self, holder_name, guests = None):
        self.holder_name = holder_name
        if guests is None:
            self.guest = []
        else:
            self.guest = guests

    def add_guest(self, guest):
        self.guest.append(str(guest))

    def __str__(self):
        return "\n".join(self.guest)
        

g1 = Person("Anna", 6)
g2 = Person("Emma", 7)
g3 = Person("Mary", 6)
party1 = Party("Michael")
party1.add_guest(g1)
party1.add_guest(g2)
party1.add_guest(g3)
print(party1)
print()
party2 = Party("John")
g4 = Person("David", 6)
party2.add_guest(g4)
print(party2)

g1 = Person("David", 6)
g2 = Person("Peter", 7)
party1 = Party("Michael")
party1.add_guest(g1)
party1.add_guest(g2)
print(party1)

'''      
#--------------------------------------------------------------
#Lab9
#Q1
'''
import math
class Circle:
    def __init__(self, radius = 1):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"A circle with a radius of {self.radius:.2f}cm."

    def grow(self, value):
        self.radius += value

        
r = Circle(2)
print("{:.2f}".format(r.get_area()))
print(r)
'''
#Q2
'''
import math
class Circle:
    def __init__(self, radius = 1):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"A circle with a radius of {self.radius:.2f}cm."

    def grow(self, value):
        self.radius += value
        
class Cone:
    def __init__(self, base_circle, slant_height = 1):
        self.slant_height = slant_height
        self.base_circle = base_circle

c1 = Circle(4)
cone1 = Cone(c1, 7)
print(cone1.base_circle, cone1.slant_height)
print(c1)
'''
#Q3
'''
import math
class Circle:
    def __init__(self, radius = 1):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"A circle with a radius of {self.radius:.2f}cm."

    def grow(self, value):
        self.radius += value
        
class Cone:
    def __init__(self, base_circle, slant_height = 1):
        self.slant_height = slant_height
        self.base_circle = base_circle

    def get_total_surface_area(self):
        base_area = self.base_circle.get_area()
        lateral_area = math.pi * self.base_circle.radius * self.slant_height
        return base_area + lateral_area

    def grow(self, value):
        self.base_circle.grow(value)
        self.slant_height += value

    def __str__(self):
        return f"A cone with a base circle area of {self.base_circle.get_area():.2f}cm2 and a slant height of {self.slant_height:.2f}cm."




c1 = Circle(4)
cone1 = Cone(c1, 7)
print("{:.2f}".format(cone1.get_total_surface_area()))
print(cone1)
cone1.grow(10)
print(cone1)
print(c1)
'''
#Q4
'''
class Box:
    def __init__(self, id_number, weight = 10):
        self.id_number = id_number
        self.weight = weight

    def __str__(self):
        return f"Box {self.id_number}: Weight {self.weight}"

b1 = Box(1, 20)
print(b1)
b2 = Box(2)
print(b2)
print(type(b1))
'''
#Q5
'''
class Box:
    def __init__(self, id_number, weight = 10):
        self.id_number = id_number
        self.weight = weight

    def __str__(self):
        return f"Box {self.id_number}: Weight {self.weight}"

class Container:
    def __init__(self, boxes=[]):
        self.boxes = []

    def add_box(self, box):
        self.boxes.append(box)

b1 = Box(1, 20)
b2 = Box(2)
c1 = Container()
print(len(c1.boxes))
c1.add_box(b1)
c1.add_box(b2)
print(len(c1.boxes))

items = [Box(1), Box(2, 10), Box(3, 20), Box(4, 40)]
c1 = Container()
for i in items:
    c1.add_box(i)
    print(i)
print(len(c1.boxes))
'''
#Q6
'''
class Box:
    def __init__(self, id_number, weight = 10):
        self.id_number = id_number
        self.weight = weight

    def __str__(self):
        return f"Box {self.id_number}: Weight {self.weight}"

class Container:
    def __init__(self, boxes=[]):
        self.boxes = []

    def add_box(self, box):
        self.boxes.append(box)

    
    def __str__(self):
        
        a_box = [str(box) for box in self.boxes]
        return "\n".join(a_box)

    def get_weight(self):
        total = 0
        for boxs in self.boxes:
            total += boxs.weight
        return total

b1 = Box(1, 20)
b2 = Box(2)
c1 = Container()
print(len(c1.boxes))
c1.add_box(b1)
c1.add_box(b2)
print(c1)
print(c1.get_weight())
'''
#Q7
'''
class ParkingSpace:
    def __init__(self, space_id = 1, available = True):
        self.space_id = space_id
        self.available = available

    def is_available(self):
        return self.available

space1 = ParkingSpace()
print(type(space1))
print(space1.available)
space2 = ParkingSpace(2)
print(type(space2))
print(space2.available)
print(space1.is_available())
'''
#Q8
'''
class ParkingSpace:
    def __init__(self, space_id = 1, available = True):
        self.space_id = space_id
        self.available = available

    def is_available(self):
        return self.available

    def mark_as_occupied(self):
        self.available = False

    def __str__(self):
        if self.available:
            return f"Parking Space {self.space_id}: available"
        else:
            return f"Parking Space {self.space_id}: occupied"


space1 = ParkingSpace()
print(space1)
space2 = ParkingSpace(2)
space2.mark_as_occupied()
print(space2)

space1 = ParkingSpace()
space1.mark_as_occupied()
print(space1)
space2 = ParkingSpace(5)
print(space2)
'''
#Q9
'''
class ParkingSpace:
    def __init__(self, space_id = 1, available = True):
        self.space_id = space_id
        self.available = available

    def is_available(self):
        return self.available

    def mark_as_occupied(self):
        self.available = False

    def __str__(self):
        if self.available:
            return f"Parking Space {self.space_id}: available"
        else:
            return f"Parking Space {self.space_id}: occupied"

class ParkingSlot:
    def __init__(self, parking_spaces = 1):
        self.parking_spaces = []
        for i in range(0,parking_spaces):
            
            self.parking_spaces.append(ParkingSpace(i))

slot1 = ParkingSlot()
print(', '.join(str(item) for item in slot1.parking_spaces))
slot2 = ParkingSlot(3)
print(', '.join(str(item) for item in slot2.parking_spaces))
'''
#Q10
'''
class ParkingSpace:
    def __init__(self, space_id = 1, available = True):
        self.space_id = space_id
        self.available = available

    def is_available(self):
        return self.available

    def mark_as_occupied(self):
        self.available = False

    def __str__(self):
        if self.available:
            return f"Parking Space {self.space_id}: available"
        else:
            return f"Parking Space {self.space_id}: occupied"

class ParkingSlot:
    def __init__(self, parking_spaces = 1):
        self.parking_spaces = []
        for i in range(0,parking_spaces):
            
            self.parking_spaces.append(ParkingSpace(i))

    def get_available(self):
        for i in self.parking_spaces:
            if ParkingSpace(i).is_available():
                return i
        return None
        
    def check_availability(self):
        count = 0
        for i in self.parking_spaces:
            if i.available == True:
                count += 1
        return count

    def mark_as_occupied(self):
        for i in self.parking_spaces:
            if i.available:
                i.available = False
                break
            else:
                print(f"Sorry, this parking slot is full")
        


parking1= ParkingSlot(3)
print(parking1.check_availability())
space1 = parking1.get_available()
print(space1)
parking1.mark_as_occupied()
print(parking1.check_availability())
space2 = parking1.get_available()
print(space2)

parking1 = ParkingSlot(2)
parking1.mark_as_occupied()
print(parking1.check_availability())
parking1.mark_as_occupied()
print(parking1.check_availability())
'''
#Q11
'''
class ParkingSpace:
    def __init__(self, space_id = 1, available = True):
        self.space_id = space_id
        self.available = available

    def is_available(self):
        return self.available

    def mark_as_occupied(self):
        self.available = False

    def __str__(self):
        if self.available:
            return f"Parking Space {self.space_id}: available"
        else:
            return f"Parking Space {self.space_id}: occupied"

class ParkingSlot:
    def __init__(self, parking_spaces = 1):
        self.parking_spaces = []
        for i in range(0,parking_spaces):
            
            self.parking_spaces.append(ParkingSpace(i))

    def get_available(self):
        for i in self.parking_spaces:
            if ParkingSpace(i).is_available():
                return i
        return None
        
    def check_availability(self):
        count = 0
        for i in self.parking_spaces:
            if i.available == True:
                count += 1
        return count

    def mark_as_occupied(self):
        for i in self.parking_spaces:
            if i.available:
                i.available = False
                break
           

    def __str__(self):
        print(f"Parking Slot: ")
        data = [str(i) for i in self.parking_spaces]
        return "\n".join(data)


parking1= ParkingSlot(3)
print(parking1)
parking1.mark_as_occupied()
print(parking1)
'''
#--------------------------------------------------------------
#Lab10 Exercise
'''
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("ERROR: The stack is empty!")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("ERROR: The stack is empty!")
        
    def size(self):
        return len(self.items)
    
s = Stack()
print(s.is_empty(), end = " ")
s.push(4)
print(s.peek(), end = " ")
s.pop()
s.push(8.4)
print(s.size(), end = " ")
s.push('dog')
print(s.peek(), end = " ")
s.pop()
print(s.size())

m = Stack()
m.push(2)
m.push(3)
m.push(6)
m.peek()
m.push(m.pop() + m.pop())
m.peek()
'''
#Q9
'''
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]
        
    def size(self):
        return len(self.items)

    def double_push(self, element):
        self.items.append(element)
        self.items.append(element)

my_stack = Stack()
my_stack.push('a')
my_stack.push('b')
my_stack.push('c')
my_stack.double_push('d')
print(my_stack.size())
for i in range(my_stack.size()):
    print(my_stack.pop(), end = ' ')

'''
#Q10
'''
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]
        
    def size(self):
        return len(self.items)

def join(a_stack):
    string = ''
    while not a_stack.is_empty():

        string += str(a_stack.pop())
    return string

my_stack = Stack()
my_stack.push('a')
my_stack.push('b')
my_stack.push('c')
result = join(my_stack)
print(type(result))
print(result)
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(join(my_stack))
'''
#--------------------------------------------------------------
#Lab10
#Q7
'''
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("ERROR: The stack is empty!")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("ERROR: The stack is empty!")
        
    def size(self):
        return len(self.items)

try:
    s = Stack()
    print (s.pop())
    print("OK")
except IndexError as err:
    print("ERROR:")
    print (err)

try:
    s = Stack()
    print (s.peek())
except IndexError as err:
    print (err)
'''
#Q8
'''
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("ERROR: The stack is empty!")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("ERROR: The stack is empty!")
        
    def size(self):
        return len(self.items)

    def __str__(self):

        string = f"{self.items}"
        return f"{string[:-1]} <-"


    def clear(self):
        self.items = []


my_stack = Stack()
my_stack.push('a')
my_stack.push('b')
my_stack.push('c')
print(my_stack)
print(my_stack.size())
my_stack.clear()
print(my_stack.size())

s = Stack()
print(s.size())
print(s)
s.push(1)
s.push(2)
print(s)

'''
#Q9
'''
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("ERROR: The stack is empty!")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("ERROR: The stack is empty!")
        
    def size(self):
        return len(self.items)

    def __str__(self):

        string = f"{self.items}"
        return f"{string[:-1]} <-"

    def clear(self):
        self.items = []

def create_stack(first_term, difference, number_of_values):
    a_stack = Stack()
    for i in range(number_of_values):
        a_stack.push(first_term)
        first_term += difference
    return a_stack

print(create_stack(1, 3, 5))
'''
#Q10
'''
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("ERROR: The stack is empty!")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("ERROR: The stack is empty!")
        
    def size(self):
        return len(self.items)

    def __str__(self):

        string = f"{self.items}"
        return f"{string[:-1]} <-"

    def clear(self):
        self.items = []

def create_stack(first_term, difference, number_of_values):
    a_stack = Stack()
    for i in range(number_of_values):
        a_stack.push(first_term)
        first_term += difference
    return a_stack



def reverse_sentence_words(filename):
    a_stack = Stack()
    f = open(filename, 'r')
    contents = f.read().split('\n')
    f.close()
    a_list = []
    
    for sentence in contents:
        words = sentence.split()
        a_list.append(words[0])
        a_list.append(words[-1])
    
    return f"{' '.join(reversed(a_list))}"


data = reverse_sentence_words("sentences.txt")
print(data)
'''
'''
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("ERROR: The stack is empty!")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("ERROR: The stack is empty!")
        
    def size(self):
        return len(self.items)

    def __str__(self):

        string = f"{self.items}"
        return f"{string[:-1]} <-"

    def clear(self):
        self.items = []

def create_stack(first_term, difference, number_of_values):
    a_stack = Stack()
    for i in range(number_of_values):
        a_stack.push(first_term)
        first_term += difference
    return a_stack



def reverse_sentence_words(filename):
    a_stack = Stack()
    f = open(filename, 'r')
    contents = f.read().split('\n')
    f.close()
    a_list = []
    string = ''
    
    for sentence in contents:
        words = sentence.split()
        a_stack.push(words[0])
        a_stack.push(words[-1])
        
    while not a_stack.is_empty():
        string += a_stack.pop() + " "
    
        
    return f"{string.strip()}"


data = reverse_sentence_words("sentences.txt")
print(data)
'''
#Q11
'''
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("ERROR: The stack is empty!")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("ERROR: The stack is empty!")
        
    def size(self):
        return len(self.items)

    def __str__(self):

        string = f"{self.items}"
        return f"{string[:-1]} <-"

    def clear(self):
        self.items = []

def simple_balanced_brackets(text):
    try:
        a_stack = Stack()
        for i in text:
            if i == "(":
                a_stack.push(i)
            elif i == ")":
                a_stack.pop()
            else:
                pass
        return a_stack.is_empty()
    except IndexError:
        return False
        

    
    

print(simple_balanced_brackets('(x)(())()'))
print(simple_balanced_brackets('x(y)z('))
print(simple_balanced_brackets('xy)(z'))

'''
#--------------------------------------------------------------
#Lab11
#Q4
'''
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError(f"ERROR: The queue is empty!")
        return self.items.pop()


    def peek(self):
        if self.is_empty():
            raise IndexError(f"ERROR: The queue is empty!")
        return self.items[len(self.items)-1]  

try:
    q = Queue()
    q.enqueue(2)
    q.enqueue(1)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
except IndexError as err:
    print(err)

try:
    q = Queue()
    print(q.peek())
except IndexError as err:
    print(err)
'''
#Q5
'''
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError(f"ERROR: The queue is empty!")
        return self.items.pop()


    def peek(self):
        if self.is_empty():
            raise IndexError(f"ERROR: The queue is empty!")
        return self.items[len(self.items)-1]

    def clear(self):
        self.items = []

    def __str__(self):
        data = str(self.items)
        data = data[1:-1]
        return f"-> |{data}| ->"

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)
q.clear()
print(q)

import random
random.seed(30)
numbers = [random.randint(1, 50) for index in range(10)]
q = Queue()
for num in numbers:
   q.enqueue(num)
print(q)
'''
#Q6
'''
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError(f"ERROR: The queue is empty!")
        return self.items.pop()


    def peek(self):
        if self.is_empty():
            raise IndexError(f"ERROR: The queue is empty!")
        return self.items[len(self.items)-1]

    def clear(self):
        self.items = []

    def __str__(self):
        data = str(self.items)
        data = data[1:-1]
        return f"-> |{data}| ->"

    def enqueue_list_from_last(self, a_list):
        b_list = a_list[::-1]
        for b in b_list:
            self.enqueue(b)
        return self.items

carBrand = Queue()
carlist = ['Audi', 'Honda', 'Toyota', 'Mercedes']
carBrand.enqueue_list_from_last(carlist)
print(carBrand)
'''
#Q7
'''
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError(f"ERROR: The queue is empty!")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError(f"ERROR: The queue is empty!")
        return self.items[len(self.items)-1]

    def clear(self):
        self.items = []

    def __str__(self):
        data = str(self.items)
        data = data[1:-1]
        return f"-> |{data}| ->"

    def enqueue_list_from_last(self, a_list):
        b_list = a_list[::-1]
        for b in b_list:
            self.enqueue(b)
        return self.items
    
class Printer:
    def __init__(self, name, print_queue = None):
        self.name = name
        if print_queue == None:
            self.print_queue = Queue()
        else:
            self.print_queue = print_queue

    def enqueue_print_job(self, document):
        self.print_queue.enqueue(document)
        print(f"{self.name} is printing: {document}")

    def process_print_jobs(self):
        return self.print_queue.dequeue()
        #return self.print_queue.enqueue_list_from_last(self.name)


printer1 = Printer("Printer 1")
printer1.enqueue_print_job("Document A")
printer1.enqueue_print_job("Document B")
printer1.process_print_jobs()
print(type(printer1))
print(type(printer1.print_queue))

printer1 = Printer("Printer 1")
printer1.enqueue_print_job("Document A")
printer1.process_print_jobs()
'''
#Q10
'''
class CircularQueue:
    def __init__(self, capacity = None):
        if capacity == None:
            self.capacity = 8
        else:
            self.capacity = capacity


        self.items = [None] * self.capacity
        self.front = 0
        self.back = self.capacity - 1
        self.count = 0

    def is_empty(self):
        if self.items == [None]*self.capacity:
            return True
        return False

    def show_contents(self):
        return f"{self.items}, front:{self.front}, back:{self.back}, count:{self.count} "



q1 = CircularQueue(5)
print(q1.show_contents())

q1 = CircularQueue(4)
print(q1.show_contents())

q1 = CircularQueue()
print(q1.show_contents())
print(q1.is_empty())
print(type(q1))
'''
#Q11
'''
class CircularQueue:
    def __init__(self, capacity = None):
        if capacity == None:
            self.capacity = 8
        else:
            self.capacity = capacity

        self.items = [None] * self.capacity
        self.front = 0
        self.back = self.capacity - 1
        self.count = 0

    def is_empty(self):
        if self.items == [None]*self.capacity:
            return True
        return False

    def show_contents(self):
        return f"{self.items}, front:{self.front}, back:{self.back}, count:{self.count} "

    def is_full(self):
        for data in self.items:
            if data == None:
                return False
        return True

    def __str__(self):
        return f"-> |{self.items}| ->"

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("ERROR: The queue is full.")
        self.items.append(item)
        #if self.items.find(item) == len(selk.ietms)-1:
        if self.is_empty():
            self.items.find(item) == self.items.find(item) % self.capacity
        self.back += 1
        count += 1

    def dequeue(self):
        if self.items == [None] * self.capacity:
            raise IndexError(f"ERROR: The queue is empty.")
        current = self.items.pop(0)
        if self.is_empty():
            self.front += 1

        count += 1
        return self.items

q1 = CircularQueue(4)
print(q1)
q1.enqueue(1)
print(q1)
q1.enqueue(2)
print(q1)
q1.enqueue(3)
print(q1)
q1.enqueue(4)
print(q1)
print("Full?", q1.is_full())
print("Empty?", q1.is_empty())
'''
#--------------------------------------------------------------
#2023 S2 Test
#Q1
'''
def get_number_and_increment(username):
    data = int(username[-3:]) + 1
    return data

print(get_number_and_increment('mgra734'))
print(get_number_and_increment('dng004'))
print(get_number_and_increment('bcar035'))
'''
#Q2
'''
def get_words(usernames_list):
    return [name[:-3] for name in usernames_list]

print(get_words(['mgra734', 'dng004', 'bcar035']))
print(get_words(['myu134', 'dkim104']))
'''
#Q3
'''
def calculate_percentage_change(initial, revised):
    return round((-(initial - revised) / abs(initial))*100)
    
print(calculate_percentage_change(60, 71))
print(calculate_percentage_change(71, 60))
print(calculate_percentage_change(-60, -71))
print(calculate_percentage_change(-71, -60))
print(calculate_percentage_change(-7, 1))
print(calculate_percentage_change(2, -5))
'''
#Q4
'''
def calculate_percentage_change(initial, revised):
    return round((-(initial - revised) / abs(initial))*100)

def calculate_changes(numbers):
    a_list = []
    for i in range(1, len(numbers)):
        a_list.append(calculate_percentage_change(numbers[i - 1], numbers[i]))
    return a_list

print(calculate_changes([60, 71, 60]))
print(calculate_changes([-9, 3, 4, 6, 2]))
'''
#Q5
'''
def create_dictionary(usernames_list):
    a_dict = {}
    for name in usernames_list:
        if name[0] not in a_dict:
            a_dict[name[0]] = [name]
        else:
            a_dict[name[0]].append(name)
    return a_dict

data = create_dictionary(['mgra734', 'dng004', 'bcar035', 'myu134', 'dkim104'])
for key in sorted(data ):
    print(key, sorted(data[key]))
'''
#Q6
'''
def swap_space_with_target(string, target_letter):
    space_index = string.index(' ')
    target_letter_index = string.index(target_letter)
    string = list(string)
    string[space_index], string[target_letter_index] = string[target_letter_index], string[space_index]
    return ''.join(string)


print(swap_space_with_target("abcde fgh", 'b'))
print(swap_space_with_target("abcde fgh", 'g'))
print(swap_space_with_target("abcde fgh", 'h'))
print(swap_space_with_target("abcde fgh", 'a'))

'''
#Q7
'''
def validate(nhi_number):
    if len(nhi_number) != 7:
        raise ValueError(f"ERROR: '{nhi_number}' - Invalid length!")
    elif not nhi_number[:3].isalpha():
        raise ValueError(f"ERROR: '{nhi_number}' - does not start with 3 alphabetical letters!")
    elif not nhi_number[3:].isdigit():
        raise  ValueError(f"ERROR: '{nhi_number}' - does not end with 4 digits!")
    else:
        letter = nhi_number[:3]
        digit = int(nhi_number[3:])
        return (letter, digit)

data = validate('ach0455')
print(type(data), type(data[0]), type(data[1])) 
print(data[0], data[1]) 
try:
    print(validate('k1235'))
except ValueError as e:
    print(e)
else:
    print("Well done!")
'''
#Q8
'''
class Patient:
    def __init__(self, name, nhi_number):
        self.name = name
        self.nhi_number = nhi_number
    def __str__(self):
       return "{}({})".format(self.name, self.nhi_number)

    def __eq__(self, other):
        if isinstance(other, Patient):
            return self.nhi_number == other.nhi_number
        return False

    def __lt__(self, other):
        return self.nhi_number < other.nhi_number
        
patient1 = Patient("Alan Smith", "dsm1234")
patient2 = Patient("Michael Hill", "mhi2456")
patient3 = Patient("Vincent Smith", "vsm1234")
print(patient1 == patient2)
print(patient1 == patient3)
print(patient2 == patient3)
print(patient1 < patient2)
print(patient1 < patient3)
print(patient1 == 'mhi2456')
print(patient2 == 'mhi2456')
data = [patient1, patient2, patient3]
data.sort()
for person in data:
    print(person)
'''
#Q9
'''
class Patient:
    def __init__(self, name, nhi_number):
        self.name = name
        self.nhi_number = nhi_number
    def __str__(self):
       return "{}({})".format(self.name, self.nhi_number)

    def __eq__(self, other):
        if isinstance(other, Patient):
            return self.nhi_number == other.nhi_number
        return False

    def __lt__(self, other):
        return self.nhi_number < other.nhi_number

def selection_sort(patients):
    for position in range(len(patients)-1, 0, -1):
        largest_index = 0
        for index in range(1, position+1):
            if patients[index] > patients[largest_index]:
                largest_index = index
        patients[largest_index], patients[position] = patients[position], patients[largest_index]
    return patients

patient1 = Patient("Alan Smith", "dsm1234")
patient2 = Patient("Michael Hill", "mhi2456")
patient3 = Patient("Vincent Smith", "vsm1234")
print(patient1 < patient2)
print(patient1 < patient3)
data = [patient1, patient2, patient3]
selection_sort(data)
for person in data:
    print(person)
'''
#Q10
'''
class Patient:
    def __init__(self, name, nhi_number):
        self.name = name
        self.nhi_number = nhi_number
    def __str__(self):
       return "{}({})".format(self.name, self.nhi_number)

    def __eq__(self, other):
        if isinstance(other, Patient):
            return self.nhi_number == other.nhi_number
        return False

    def __lt__(self, other):
        return self.nhi_number < other.nhi_number

def selection_sort(patients):
    for position in range(len(patients)-1, 0, -1):
        largest_index = 0
        for index in range(1, position+1):
            if patients[index] > patients[largest_index]:
                largest_index = index
        patients[largest_index], patients[position] = patients[position], patients[largest_index]
    return patients

def linear_search_by_nhi(patients_list, target):
    count = 0
    for i in range(len(patients_list)):
        
        if patients_list[i].nhi_number > target:
            count += 1
            return (False, count)
        
        elif patients_list[i].nhi_number == target:
            count += 1
            return (True, count)
        
        else:
            count += 1
            pass
    return (False, len(patients_list))
            

data = [Patient("Raymond Ng", "aga2962"), Patient("Alice Kim", "akm2564"), Patient("John Zhang", "ara3443"),  Patient("Albert Mak", "bet9542"), Patient("David Chan", "bro2123")]
print(linear_search_by_nhi(data, 'akm2564'))
print(linear_search_by_nhi(data, 'bro2546'))
'''
#Q11
'''
class Course:
    def __init__(self, name = None, number_of_students = 0):
        if name == None:
            self.name = 'UNKNOWN'
        else:
            self.name = name
        self.number_of_students = number_of_students

    def __str__(self):
        return f"{self.name}({self.number_of_students})"

    def register(self):
        self.number_of_students += 1

    def un_register(self):
        if self.number_of_students != 0:
            self.number_of_students -= 1

course1 = Course()
course2 = Course('Python101')
print(course1)
print(course2)
print(type(course1))
print(type(course1.name)) #check the type
course1.register()
course1.register()
print(course1)
course1.un_register()
print(course1)        
'''
#Q12
'''
class Course:
    def __init__(self, name = None, number_of_students = 0):
        if name == None:
            self.name = 'UNKNOWN'
        else:
            self.name = name
        self.number_of_students = number_of_students

    def __str__(self):
        return f"{self.name}({self.number_of_students})"

    def register(self):
        self.number_of_students += 1

    def un_register(self):
        if self.number_of_students != 0:
            self.number_of_students -= 1

class Student:
    def __init__(self, name, username, max_count = 1):
        self.name = name
        self.username = username
        self.max_count = max_count
        self.course = []

    def enrol(self, course):
        if course not in self.course and len(self.course) < self.max_count:
            self.course.append(course)
            course.number_of_students += 1
            
    def un_enrol(self, course):
        if course in self.course:
            self.course.remove(course)
            course.number_of_students -= 1
            
    def __str__(self):
        if len(self.course) != 0:
            return f"{self.name} enrolled: [{', '.join(str(data) for data in self.course)}] course(s)."
        return f"{self.name}: Not enrolled in any courses."
        
course1 = Course('Python101')
student1 = Student("Dick Smith", "dsmil123")
student2 = Student("Michael Hill", "mhil456", 2)
student1.enrol(course1)
print(student1)
student2.enrol(course1)
print(student2)
print(course1)
student1.un_enrol(course1)
print(course1)
print(student1)


class Course:
    def __init__(self, name = None, number_of_students = 0):
        if name == None:
            self.name = 'UNKNOWN'
        else:
            self.name = name
        self.number_of_students = number_of_students

    def __str__(self):
        return f"{self.name}({self.number_of_students})"

    def register(self):
        self.number_of_students += 1

    def un_register(self):
        if self.number_of_students != 0:
            self.number_of_students -= 1

class Student:
    def __init__(self, name, username, max_count = 1):
        self.name = name
        self.username = username
        self.max_count = max_count
        self.course = []

    def enrol(self, course):
        if len(self.course) < self.max_count:
            self.course.append(course)
            course.number_of_students += 1

    def un_enrol(self, course):
        if course in self.course:
            self.course.remove(course)
            course.number_of_students -= 1

    def __str__(self):
        if len(self.course) != 0:
            return f"{self.name} enrolled: [{', '.join(str(data) for data in self.course)}] course(s)."
        return f"{self.name}: Not enrolled in any courses."
    
course1 = Course('Python101')
student1 = Student("Dick Smith", "dsmil123")
student2 = Student("Michael Hill", "mhil456", 2)
student1.enrol(course1)
print(student1)
student2.enrol(course1)
print(student2)
print(course1)
student1.un_enrol(course1)
print(course1)
print(student1)
'''

#--------------------------------------------------------------
#Lab 12
#Q1
'''
def calculate_percentage_change(initial, revised):
    current = round((((revised - initial) / abs(initial)) * 100))
    return current


print(calculate_percentage_change(60, 71))
print(calculate_percentage_change(71, 60))
print(calculate_percentage_change(-60, -71))
print(calculate_percentage_change(-71, -60))
print(calculate_percentage_change(-7, 1))
print(calculate_percentage_change(2, -5))
'''
#Q2
'''
def calculate_changes(numbers):
    a_list = []
    for i in range(1, len(numbers)):
        current = round(((numbers[i - 1] - numbers[i]) / abs(numbers[i - 1])) * 100)
        a_list.append(-current)
    return a_list

print(calculate_changes([60, 71, 60]))
print(calculate_changes([-9, 3, 4, 6, 2]))
'''
#Q3
'''
def swap_space_with_target(string, target_letter):
    space_index = string.index(' ')
    target_index = string.index(target_letter)

    string_list = list(string)

    string_list[space_index], string_list[target_index] = string_list[target_index], string_list[space_index]

    new_string = ''.join(string_list)

    return new_string

print(swap_space_with_target("abcde fgh", 'b'))
print(swap_space_with_target("abcde fgh", 'g'))
print(swap_space_with_target("abcde fgh", 'h'))
print(swap_space_with_target("abcde fgh", 'a'))
''' 
#Q4
'''
def validate(nhi_number):
    if len(nhi_number) != 7:
        raise ValueError(f"ERROR: '{nhi_number}' - Invalid length!")
    elif not nhi_number[:3].isalpha():
        raise ValueError(f"ERROR: '{nhi_number}' - does not start with 3 alphabetical letters!")
    elif not nhi_number[3:].isdigit():
        raise ValueError(f"ERROR: '{nhi_number}' - does not end with 4 digits!")
    else:
        letter = nhi_number[:3]
        digit = int(nhi_number[3:])
        return (letter, digit)

    


data = validate('ach0455')
print(type(data), type(data[0]), type(data[1])) 
print(data[0], data[1]) 
try:
    print(validate('k1235'))
except ValueError as e:
    print(e)
else:
    print("Well done!")

'''
#Q5
'''
class Patient:
    def __init__(self, name, nhi_number):
        self.name = name
        self.nhi_number = nhi_number
    def __str__(self):
       return "{}({})".format(self.name, self.nhi_number)

    def __eq__(self, other):
        if isinstance(other, Patient):
            return self.nhi_number == other.nhi_number
        return False

    def __lt__(self, other):
        return self.nhi_number < other.nhi_number

patient1 = Patient("Alan Smith", "dsm1234")
patient2 = Patient("Michael Hill", "mhi2456")
patient3 = Patient("Vincent Smith", "vsm1234")
print(patient1 == patient2)
print(patient1 == patient3)
print(patient2 == patient3)
print(patient1 < patient2)
print(patient1 < patient3)
print(patient1 == 'mhi2456')
print(patient2 == 'mhi2456')
data = [patient1, patient2, patient3]
data.sort()
for person in data:
    print(person)
'''
#Q6
'''
class Patient:
    def __init__(self, name, nhi_number):
        self.name = name
        self.nhi_number = nhi_number
    def __str__(self):
       return "{}({})".format(self.name, self.nhi_number)

    def __eq__(self, other):
        if isinstance(other, Patient):
            return self.nhi_number == other.nhi_number
        return False

    def __lt__(self, other):
        return self.nhi_number < other.nhi_number

def selection_sort(patients):
    for position in range(len(patients)-1, 0, -1):
        largest_index = 0
        for index in range(1, position+1):
            if patients[index] > patients[largest_index]:
                largest_index = index
                
        patients[largest_index], patients[position] = patients[position], patients[largest_index]


data = [Patient("David Chan", "bro2123"), Patient("Albert Mak", "bet9542"), Patient("Alice Kim", "akm2564"), Patient("Raymond Ng", 'aga2962'), Patient('John Zhang', 'ara3443')]
selection_sort(data)
for person in data:
    print(person)

patient1 = Patient("Alan Smith", "dsm1234")
patient2 = Patient("Michael Hill", "mhi2456")
patient3 = Patient("Vincent Smith", "vsm1234")
print(patient1 < patient2)
print(patient1 < patient3)
data = [patient1, patient2, patient3]
selection_sort(data)
for person in data:
    print(person)
'''
#Q7
'''
class Patient:
    def __init__(self, name, nhi_number):
        self.name = name
        self.nhi_number = nhi_number
    def __str__(self):
       return "{}({})".format(self.name, self.nhi_number)

    def __eq__(self, other):
        if isinstance(other, Patient):
            return self.nhi_number == other.nhi_number
        return False

    def __lt__(self, other):
        return self.nhi_number < other.nhi_number

def selection_sort(patients):
    for position in range(len(patients)-1, 0, -1):
        largest_index = 0
        for index in range(1, position+1):
            if patients[index] > patients[largest_index]:
                largest_index = index
                
        patients[largest_index], patients[position] = patients[position], patients[largest_index]

def linear_search_by_nhi(patients_list, target):
    
    for i in range(0, len(patients_list)):
        if patients_list[i].nhi_number == target:
            return (True, i + 1)
        elif patients_list[i].nhi_number > target:
            return (False, i)
        else:
            pass
    return (False, len(patients_list))
            
    
data = [Patient("Raymond Ng", "aga2962"), Patient("Alice Kim", "akm2564"), Patient("John Zhang", "ara3443"),  Patient("Albert Mak", "bet9542"), Patient("David Chan", "bro2123")]
print(linear_search_by_nhi(data, 'akm2564'))
print(linear_search_by_nhi(data, 'bro2546'))
data = [Patient("Raymond Ng", "aga2962"), Patient("Alice Kim", "akm2564"), Patient("John Zhang", "ara3443"),  Patient("Albert Mak", "bet9542"), Patient("David Chan", "bro2123")]
print(linear_search_by_nhi(data, 'ara3443'))
print(linear_search_by_nhi(data, 'wah5645'))
'''
#Q8
'''
class Course:
    def __init__(self, name = None, number_of_students = 0):
        if name == None:
            self.name = 'UNKNOWN'
        else:
            self.name = name
            
        self.number_of_students = number_of_students
        

    def __str__(self):
        return f"{self.name}({self.number_of_students})"

    def register(self):
        self.number_of_students += 1

    def un_register(self):
        if self.number_of_students > 0:
            self.number_of_students -= 1
            
course1 = Course()
course2 = Course('Python101')
print(course1)
print(course2)
print(type(course1))
print(type(course1.name)) #check the type
course1.register()
course1.register()
print(course1)
course1.un_register()
print(course1)

course1 = Course('Python101')
course1.un_register()
print(course1)
course1.un_register()
print(course1)
'''
#Q9
'''
class Course:
    def __init__(self, name = None, number_of_students = 0):
        if name == None:
            self.name = 'UNKNOWN'
        else:
            self.name = name
            
        self.number_of_students = number_of_students
        
    def __str__(self):
        return f"{self.name}({self.number_of_students})"

    def register(self):
        self.number_of_students += 1

    def un_register(self):
        if self.number_of_students > 0:
            self.number_of_students -= 1

class Student:
    def __init__(self, name, username, max_count = 1):
        self.name = name
        self.username = username
        self.max_count = max_count
        self.courses = []

    def enrol(self, course):
        if len(self.courses) < self.max_count:
            self.courses.append(course)
            course.number_of_students += 1

    def un_enrol(self, course):
        if course in self.courses:
            self.courses.remove(course)
            course.number_of_students -= 1

    def __str__(self):
        if len(self.courses) != 0:
            return f"{self.name} enrolled: [{''.join(str(course) for course in self.courses)}] course(s)."
        return f"{self.name}: Not enrolled in any courses."
        
course1 = Course('Python101')
student1 = Student("Dick Smith", "dsmil123")
student2 = Student("Michael Hill", "mhil456", 2)
student1.enrol(course1)
print(student1)
student2.enrol(course1)
print(student2)
print(course1)
student1.un_enrol(course1)
print(course1)
print(student1)

'''

#--------------------------------------------------------------
#Lab13
#Q1
'''
def print_upper(word, count = 0):

    if count == len(word):
        print('Go!')
    else:
        print(word[count].upper())
        return print_upper(word, count + 1)
        


print_upper('abc')
        
def print_upper(word):
    if len(word) == 0:
        print("Go!")
    else:
        print(word[0].upper())
        return print_upper(word[1:])


print_upper('abc')
'''

#Q2
'''
def count_multiples_of_5(numbers):
    if not numbers:
        return 0
    elif numbers[0] % 5 == 0:
        return 1 + count_multiples_of_5(numbers[1:])
    else:
        return count_multiples_of_5(numbers[1:])
        
    
print('%s : %d' % ([2], count_multiples_of_5([2])))
'''
#Q4
'''
def get_arithmetic_term(first_term, difference, n):
    if n == 0:
        return first_term - difference
    else:
        return difference + get_arithmetic_term(first_term, difference, n-1)
    

print(get_arithmetic_term(3, 2, 1))
print(get_arithmetic_term(1, 2, 3))
print(get_arithmetic_term(2, 4, 5))
print(get_arithmetic_term(2, 3, 4))
'''
#Q5
'''
def no_odds(numbers):
    if len(numbers) == 0:
        return True
    
    elif numbers[0] % 2 == 1:
        return False
    else:
        return no_odds(numbers[1:])


print(no_odds([2, 3, 5, 6]))
print(no_odds([2, 4, 6, 8, 10]))
print(no_odds([2]))
'''
#Q6
'''
def get_arithmetic_list(first_term, difference, n):
    if n == 0:
        return []
    else:
        return [first_term] + get_arithmetic_list(first_term + difference, difference, n - 1)
    

data = get_arithmetic_list(3, 2, 1)
print(type(data))
print(data)
'''
#Q10
'''
def get_arithmetic_list_count(first_term, difference, n):
    if n == 0:
        return [], 0
    else:
        number, count = get_arithmetic_list_count(first_term + difference, difference, n-1)
        return ([first_term] + number,  count + 1)


print(get_arithmetic_list_count(1, 2, 3))

'''

#--------------------------------------------------------------
#2023 S1 Test
#Q1
'''
def get_greeting(username):
    return f"Hello agent {username[-3:]}"

print(get_greeting('mgra734'))
print(get_greeting('dng134'))
print(get_greeting('bcar735'))
print(get_greeting('rliu061'))
'''
#Q2
'''
def remove_strings_by_len(words, target_length):
    for word in words.copy():
        if len(word) == target_length:
            words.remove(word)

words = ['hot', 'cat', 'over', 'index', 'own', 'are', 'and']
remove_strings_by_len(words, 3)
print(words)
remove_strings_by_len(words, 4)
print(words)
data = ['hot', 'cat', 'over', 'index', 'own', 'are', 'and']
remove_strings_by_len(data, 7)
print(data)
'''
#Q3
'''
def get_repeat_dictionary(word):
    letter_dict = {}
    for letter in word:
        if word.count(letter) > 1:
            letter_dict[letter] = word.count(letter)
    return letter_dict

print(get_repeat_dictionary('hello'))
print(get_repeat_dictionary('bubble'))
print(get_repeat_dictionary('value'))
data = get_repeat_dictionary('statistics')
for key in sorted(data):
    print(key, data[key])
'''
#Q4
'''
def create_2d_words_list(word):
    a_list = []
    for position in range(len(word), 0, -1):
        b_list = []
        for index in range(1, position+1):
            b_list.append(word[:index])
        a_list.append(b_list)
    return a_list

print(create_2d_words_list('cat'))
'''
#Q5
'''
def consecutive_sum(numbers, target):
    return [(numbers[i], numbers[i + 1]) for i in range(len(numbers) - 1) if numbers[i] + numbers[i + 1] == target]

print(consecutive_sum([3, 2, 1, 4], 5))
print(consecutive_sum([3, 2, 1, 4], 3))
print(consecutive_sum([4, 6, 2, 7, 3, 4], 10))
print(consecutive_sum([4, 6, 2, 7, 3, 4], 9))
'''
#Q6
'''
def collapse(numbers):
    try:
        for number in numbers:
            number = sum(int(number))
    except ValueError:
        pass
    return numbers

values = [1, 2, 3, 4, 5]
collapse(values)
print(values)

values = [1, [2, 3], ['4', 'ten'], 5]
collapse(values)
print(values)

'''
#Q7
'''
class WordScore:
    def __init__(self, word=""): #assume lowercase letters
        valid_letters = 'abcdefghijklmnopqrstuvwxyz'
        score = 0
        for letter in word:
            score += valid_letters.index(letter)
        self.score = score
        self.word = word

    def __str__(self):
        return f"{self.word}({self.score})"

    def __eq__(self, other):
        if isinstance(other, WordScore):
            return self.score == other.score
        return False

    def __lt__(self, other):
        return self.score < other.score
        

class WordScore:
    def __init__(self, word=""): #assume lowercase letters
        valid_letters = 'abcdefghijklmnopqrstuvwxyz'
        score = 0
        for letter in word:
            score += valid_letters.index(letter)
        self.score = score
        self.word = word

    def __str__(self):
        return f"{self.word}({self.score})"

    def __eq__(self, other):
        if isinstance(other, WordScore):
            return self.word == other.word
        return False

    def __lt__(self, other):
        if isinstance(other, WordScore):
            if self.score == other.score:
                return self.word < other.word
            return self.score < other.score
        return False

          
word_score1 = WordScore("bleats")
word_score2 = WordScore("stable")
word_score3 = WordScore("tables")
word_score4 = WordScore("beat")
print(word_score1, word_score2, word_score3, word_score4)
print(word_score1 == word_score2)
print(word_score2 == word_score3)
print(word_score1 == word_score4)
print(word_score1 < word_score2)
print(word_score1 < word_score3)
print(word_score1 < word_score4)
print(word_score2 < word_score3)
print(word_score2 < word_score4)
print(word_score3 < word_score4)


word_score1 = WordScore("bushes")
word_score2 = WordScore("waits")
word_score3 = WordScore("brown")
word_score4 = WordScore('standand')
print(word_score1 == word_score2)
print(word_score2 == word_score3)
print(word_score2 < word_score3)
print(word_score3 < word_score4)

'''
#Q8
'''
class WordScore:
    def __init__(self, word=""): #assume lowercase letters
        valid_letters = 'abcdefghijklmnopqrstuvwxyz'
        score = 0
        for letter in word:
            score += valid_letters.index(letter)
        self.score = score
        self.word = word

    def __str__(self):
        return f"{self.word}({self.score})"

    def __eq__(self, other):
        if isinstance(other, WordScore):
            return self.word == other.word
        return False

    def __lt__(self, other):
        if isinstance(other, WordScore):
            if self.score == other.score:
                return self.word < other.word
            return self.score < other.score
        return False

def selection_sort(a_list):
    a
'''





#--------------------------------------------------------------
#2022 S2 Test
#Q1
'''
def is_multiple_of_3(username):
    return int(username[-3:]) % 3 == 0

print(is_multiple_of_3('rliu061'))  # False
print(is_multiple_of_3('mgra734'))  # False
print(is_multiple_of_3('dng134'))   # False
print(is_multiple_of_3('bcar735'))  # True
'''
#Q2
'''
def get_first_digits(numbers):
    return [int(str(number)[0]) for number in numbers]


print(get_first_digits([20, 23, 16, 19, 16, 5]))
print(get_first_digits([146, 23, 1]))
'''
#Q3
'''
def cumulative_sum(numbers):
    for i in range(1, len(numbers)):
        numbers[i] = numbers[i] + numbers[i - 1]

numbers = [1, 2, 3, 4]
cumulative_sum(numbers)
print(numbers)
cumulative_sum(numbers)
print(numbers)
'''
#Q4
'''
def remove_ends_with_vowel(words_list):
    vowels = 'aeiou'
    for word in words_list.copy():
        if word[-1] in vowels:
            words_list.remove(word)


data = ["Hello", "World", "is", "nice", "weather"]
remove_ends_with_vowel(data)
print(data)

words = ["answer", "anna", "soda", "uncle", "acknowledge"]
remove_ends_with_vowel(words)
print(words)
words = ["hello", "goodbye", "yes", "no", "why"]
remove_ends_with_vowel(words)
print(words)
'''
#Q5
'''
def create_song_dictionary(song_list):
    a_dict = {}
    for data in song_list:
        name, author, duration = data.split(',')
        if author not in a_dict:
            a_dict[author] = [(name, int(duration))]
        else:
            a_dict[author].append((name, int(duration)))
    return a_dict
        
songs = ["We Own It,Wiz Khalifa,227", "See You Again,Wiz Khalifa,229", "New Face,PSY,190"]
songs_dict = create_song_dictionary(songs)
for key in sorted(songs_dict):
    print(key, sorted(songs_dict[key]))
print(type(songs_dict))
print(type(songs_dict['Wiz Khalifa']))
print(type(songs_dict['Wiz Khalifa'][0]))
'''
#Q6
'''
def print_total_durations(song_dictionary):
    for artist in sorted(song_dictionary):
        total_duration = sum(duration for _, duration in song_dictionary[artist])
        print(f"{artist} {total_duration}")

# Example usage:
song_dict = {'Wiz Khalifa': [('We Own It', 227), ('See You Again', 229)], 'PSY': [('New Face', 190)]}
print_total_durations(song_dict)
'''
#Q8
'''
class EvenNumbersList:
    def __init__(self, evens = None):
        if evens == None:
            self.numbers = []
        else:
            self.numbers = evens
    
    def add_number(self, value):
        if value % 2 == 0:
            self.numbers.append(value)
        
    def __str__(self):
        return str(self.numbers)    

d1 = EvenNumbersList()
d1.add_number(4)
print("d1:", d1)
d2 = EvenNumbersList()
d2.add_number(6)
print("d2:", d2)
d3 = EvenNumbersList()
d3.add_number(8)
print("d3:", d3)
'''
#Q9
'''
class Budget:
    def __init__(self, title, amount):
        self.title = title
        self.amount = amount
        self.parent_title = None

    def __str__(self):
        return f"{self.title}(${round(self.amount)})"

    def get_title(self):
        return self.title

    def get_amount(self):
        return self.amount

    def get_parent_title(self):
        return self.parent_title

budget1 = Budget("Electricity", 201.9)
print(budget1)
print(budget1.get_title())
print(budget1.get_amount())
print(budget1.get_parent_title())
print(budget1.get_parent_title() == None)
budget2 = Budget("Water", 102.2)
print(budget2)
'''
#Q10
'''
class GroupBudget:
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title

        
class Budget:
    def __init__(self, title, amount):
        self.title = title
        self.amount = amount
        self.parent_title = None

    def __str__(self):
        return f"{self.title}(${round(self.amount)})"

    def get_title(self):
        return self.title

    def get_amount(self):
        return self.amount

    def get_parent_title(self):
        return self.parent_title

    


The class should provide functionality to assign the title of the group parent budget to the budget. For example, the following code:
group1 = GroupBudget("Utility Bills")
budget1 = Budget("Electricity", 200)
print(budget1.get_parent_title())
budget1.assign(group1.get_title())
print(budget1.get_parent_title())
produces:
None
Utility Bills
'''

#--------------------------------------------------------------
#Assignment
'''
import math
class Point:
    def __init__(self, coord_x = 0, coord_y = 0):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.score = self.get_score()


    def distance_from_zero(self):
        return math.sqrt(self.coord_x ** 2 + self.coord_y ** 2)


    def get_score(self):
        distance = self.distance_from_zero()
        if distance <= 1:
            self.score = 100
        elif 1 < distance <= 2:
            self.score = 50
        elif 2 < distance <= 3:
            self.score = 20
        elif 3 < distance <= 4:
            self.score = 10
        else:
            self.score = 0
        return self.score
        

    def __str__(self):
        return f"({self.coord_x}, {self.coord_y})"


import random
import math
class Player:
    def __init__(self, name, seed=30):
        self.name = name
        self.points = []
        random.seed(seed)

    def make_throw(self):
        coord_x = random.randrange(-5, 6)
        coord_y = random.randrange(-5, 6)
        point = Point(coord_x, coord_y)
        self.points.append(point)
        print(f"{self.name}: The score for a dart throw at position ({coord_x}, {coord_y}) is {point.get_score()}.")
        
    def get_score(self):
        if self.points:
            return self.points[-1].get_score()
        else:
            return 0

    def get_total_score(self):
        return sum(point.get_score() for point in self.points)

    def get_name(self):
        return self.name

    def __str__(self):
        result = f"{self.name}'s total score is {self.get_total_score()}."
        for point in self.points:
            result += f"The score for a dart throw at position {point} is {point.get_score()}.\n"
        return result.rstrip()


class DartGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        print(f"***********************************************")
        print(f"Welcome to the simplified dart game simulation!")
        print(f"***********************************************")
        player_1 = None
        player_2 = None
        while player_1 != player1:
            player_1 = input("Enter player1 name: ")
        while player_2 != player2:
            player_2 = input("Enter player2 name: ")
        

    def play_game(self):
        player_1.


    def congratulate_player(self):
        


'''
'''
import math
import random

class Point:
    def __init__(self, coord_x=0, coord_y=0):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.score = self.get_score()

    def distance_from_zero(self):
        return math.sqrt(self.coord_x ** 2 + self.coord_y ** 2)

    def get_score(self):
        distance = self.distance_from_zero()
        if distance <= 1:
            return 100
        if 1 < distance <= 2:
            return 50
        if 2 < distance <= 3:
            return 20
        if 3 < distance <= 4:
            return 10
        else:
            return 0

    def __str__(self):
        return f"({self.coord_x}, {self.coord_y})"


class Player:
    def __init__(self, name, seed=30):
        self.name = name
        self.points = []
        random.seed(seed)

    def make_throw(self):
        coord_x = random.randrange(-5, 6)
        coord_y = random.randrange(-5, 6)
        point = Point(coord_x, coord_y)
        self.points.append(point)
        print(f"{self.name}: The score for a dart throw at position ({coord_x}, {coord_y}) is {point.get_score()}.")

    def get_score(self):
        if self.points:
            return self.points[-1].get_score()
        else:
            return 0

    def get_total_score(self):
        return sum(point.get_score() for point in self.points)

    def get_name(self):
        return self.name

    def __str__(self):
        result = f"{self.name}'s total score is {self.get_total_score()}.\n"
        for point in self.points:
            result += f"The score for a dart throw at position {point} is {point.get_score()}.\n"
        return result.rstrip()


class DartGame:
    def __init__(self, seed=30, max_score=51):
        print("***********************************************")
        print("Welcome to the simplified dart game simulation!")
        print("***********************************************")
        player1 = input("Enter player1 name: ")
        player2 = input("Enter player2 name: ")

        while True:
            if not player1.isalpha():
                player1 = input("Enter player1 name: ")
            if not player2.isalpha():
                player2 = input("Enter player2 name: ")
            else:
                break

        self.player1 = Player(player1, seed)
        self.player2 = Player(player2, seed)
        self.max_score = max_score
        self.rounds = 0
        print()

    def play_game(self):
        while True:
            self.player1.make_throw()
            self.player2.make_throw()
            self.rounds += 1

            if self.player1.get_total_score() >= self.max_score or self.player2.get_total_score() >= self.max_score:
                break

    def congratulate_player(self):
        score1 = self.player1.get_total_score()
        score2 = self.player2.get_total_score()

        if score1 > score2:
            winner = self.player1.get_name()
        elif score2 > score1:
            winner = self.player2.get_name()
        else:
            print("***********\nIt's a tie!\n***********")
            print(f"The total score of {self.player1.get_name()} is {score1}.")
            print(f"The total score of {self.player2.get_name()} is {score2}.")
            print(f"The number of rounds required is {self.rounds}.")
            return

        result = f"Congratulations! The winner is {winner}."
        print("*" * len(result))
        print(f"Congratulations! The winner is {winner}.")
        print("*" * len(result))
        print(f"The number of rounds required is {self.rounds}.")
        print(f"The total score of {self.player1.get_name()} is {score1}.")
        print(f"The total score of {self.player2.get_name()} is {score2}.")



game = DartGame()
game.play_game()
game.congratulate_player()

'''



#--------------------------------------------------------------
#Lab14
#Q7
'''
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
    def get_data(self):
        return self.data
        
    def get_next(self):
        return self.next
        
    def set_data(self, new_data):
        self.data = new_data
        
    def set_next(self, new_next):
        self.next = new_next
        
    def __str__(self):
        return str(self.data)



node2 = Node('world')
node1 = Node('hello', node2)
print(node1.get_data())
print(node1.get_next().get_data())
print(node1)
print(node2)

a_node = Node(1)
print(a_node)
print(a_node.get_next())
'''
#Q8
'''
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
    def get_data(self):
        return self.data
        
    def get_next(self):
        return self.next
        
    def set_data(self, new_data):
        self.data = new_data
        
    def set_next(self, new_next):
        self.next = new_next
        
    def __str__(self):
        return str(self.data)

    def add_after(self, value):
        new_node = Node(value, self.next)
        self.set_next(new_node)


a_node = Node('hello')
a_node.add_after('world')
print(a_node.get_data())
result = a_node.get_next()
print(result.get_data())
if not isinstance(result, Node):
    print("result must be an object of the Node class")
a_node.set_data('happy')
print(a_node.get_data())
'''
#Q9
'''
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
    def get_data(self):
        return self.data
        
    def get_next(self):
        return self.next
        
    def set_data(self, new_data):
        self.data = new_data
        
    def set_next(self, new_next):
        self.next = new_next
        
    def __str__(self):
        return str(self.data)

    def add_after(self, value):
        new_node = Node(value, self.next)
        self.set_next(new_node)

    def add_double(self):
        new_node = Node(self.data, self.next)
        self.set_next(new_node)

a_node = Node('a', Node('b'))
a_node.add_double()
result = a_node.get_next()
if not isinstance(result, Node):
    print("result must be an object of the Node class")
print(a_node.get_data())
print(result.get_data())
print(result.get_next().get_data())
'''
#Q10
'''
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
    def get_data(self):
        return self.data
        
    def get_next(self):
        return self.next
        
    def set_data(self, new_data):
        self.data = new_data
        
    def set_next(self, new_next):
        self.next = new_next
        
    def __str__(self):
        return str(self.data)

    def add_after(self, value):
        new_node = Node(value, self.next)
        self.set_next(new_node)

    def add_double(self):
        new_node = Node(self.data, self.next)
        self.set_next(new_node)

    def get_ascii_sum(self):
        string = ''
        string += self.data
        count = 0
        for i in string:
            count += ord(i)
        return count
        

node1 = Node('a')
print(node1.get_ascii_sum())
node2 = Node('ab')
print(node2.get_ascii_sum())
node3 = Node('abc')
print(node3.get_ascii_sum())
'''

#Q11
'''
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
    def get_data(self):
        return self.data
        
    def get_next(self):
        return self.next
        
    def set_data(self, new_data):
        self.data = new_data
        
    def set_next(self, new_next):
        self.next = new_next
        
    def __str__(self):
        return str(self.data)

    def add_after(self, value):
        new_node = Node(value, self.next)
        self.set_next(new_node)

    def add_double(self):
        new_node = Node(self.data, self.next)
        self.set_next(new_node)

    def get_ascii_sum(self):
        string = ''
        string += self.data
        count = 0
        for i in string:
            count += ord(i)
        return count


def print_node_chain(a_node):
    if a_node is None:
        print()
    else:
        print(f"{a_node}", end=' ')
        return print_node_chain(a_node.get_next())

node1 = Node('hello')
node2 = Node('world')
node3 = Node('goodbye')
node1.set_next(node2)
node2.set_next(node3)
print_node_chain(node1)
print("END")
'''
#Q12
'''
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next
        
    def set_data(self, new_data):
        self.data = new_data
        
    def set_next(self, new_next):
        self.next = new_next

    def __str__(self):
        return self.data

    def add_after(self, value):
        new_node = Node(value, self.next)
        self.set_next(new_node)

    def add_double(self):
        new_node = Node(self.data, self.next)
        self.set_next(new_node)

    def get_ascii_sum(self):
        string = ''
        string += self.data
        count = 0
        for i in string:
            count += ord(i)
        return count


def print_node_chain(a_node):
    if a_node == None:
        print()
    else:
        print(f"{a_node.get_data()}", end=' ')
        return print_node_chain(a_node.get_next())


def search_and_double(node_of_chain, target):
    if node_of_chain is None:
        return ''
    else:
        if node_of_chain.get_data() == target:
            node_of_chain.add_after(node_of_chain.get_data())
            target = None
        search_and_double(node_of_chain.get_next(), target)



value = Node('elderberry', Node('cherry', Node('banana', Node('apple'))))
search_and_double(value, 'apple')
print_node_chain(value)


value = Node('elderberry', Node('cherry', Node('banana', Node('apple'))))
search_and_double(value, 'cherry')
search_and_double(value, 'cherry')
print_node_chain(value)
'''
#--------------------------------------------------------------
#Lab15
#Q5
'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def add_after(self, value):
        new_node = Node(value,self.next )
        self.next = new_node

    def remove_after(self):
        self.next = self.next.get_next()

    def __str__(self):
        return str(self.data)

    
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    
    def size(self):
        return self.count

    def add(self, item):
        self.head = Node(item, self.head)
        self.count += 1

    def clear(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def __str__(self):
        result = 'Head: '
        current = self.head
        if current != None:
            while current is not None:
                result += f"{current} --> "
                current = current.get_next()

            return result[:-5]
        else:
            return ''
       
                
values = LinkedList()
print(values.is_empty())
values.add(1)
values.add(2)
print(values)
print(values.is_empty())
print(type(values))                           
            
values = LinkedList()
print(values.is_empty())
values.add(1)
values.add(2)
print(values)
print(values.is_empty())
print(type(values))

values = LinkedList()
values.add("hello")
values.add("world")
print(values)
values.clear()
print(values)
print(values.size())
'''
#Q6
'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def add_after(self, value):
        new_node = Node(value,self.next )
        self.next = new_node

    def remove_after(self):
        self.next = self.next.get_next()

    def __str__(self):
        return str(self.data)

    
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    
    def size(self):
        return self.count

    def add(self, item):
        self.head = Node(item, self.head)
        self.count += 1

    def clear(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def __str__(self):
        result = 'Head: '
        current = self.head
        if current != None:
            while current is not None:
                result += f"{current} --> "
                current = current.get_next()

            return result[:-5]
        else:
            return ''

    def search(self, search_value):
        current = self.head
        while current != None:
            if current.get_data()  == search_value:
                return True

            current = current.get_next()
        return False



values = LinkedList()
print(values.search('hello'))

values = LinkedList()
values.add('hello')
values.add('world')
print(values.search('hello'))
'''
#Q7
'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def add_after(self, value):
        new_node = Node(value,self.next )
        self.next = new_node

    def remove_after(self):
        self.next = self.next.get_next()

    def __str__(self):
        return str(self.data)

    
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    
    def size(self):
        return self.count

    def add(self, item):
        self.head = Node(item, self.head)
        self.count += 1

    def clear(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def __str__(self):
        result = 'Head: '
        current = self.head
        if current != None:
            while current is not None:
                result += f"{current} --> "
                current = current.get_next()

            return result[:-5]
        else:
            return ''

    def search(self, search_value):
        current = self.head
        while current != None:
            if current.get_data()  == search_value:
                return True

            current = current.get_next()
        return False

    def remove_first(self):
        data = self.head
        self.head = self.head.get_next()
        self.count -= 1
        return data
        

fruit = LinkedList()
fruit.add('cherry')
fruit.add('banana')
fruit.add('apple')
value = fruit.remove_first()
print(fruit)
print(value)
print(fruit.size())
print(type(fruit))

my_list = LinkedList()
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add(4)
print(my_list.remove_first())
my_list.add(5)
print(my_list)
'''
#Q8
'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def add_after(self, value):
        new_node = Node(value,self.next )
        self.next = new_node

    def remove_after(self):
        self.next = self.next.get_next()

    def __str__(self):
        return str(self.data)

    
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    
    def size(self):
        return self.count

    def add(self, item):
        self.head = Node(item, self.head)
        self.count += 1

    def clear(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def __str__(self):
        result = 'Head: '
        current = self.head
        if current != None:
            while current is not None:
                result += f"{current} --> "
                current = current.get_next()

            return result[:-5]
        else:
            return ''

    def search(self, search_value):
        current = self.head
        while current != None:
            if current.get_data()  == search_value:
                return True

            current = current.get_next()
        return False

    def remove_first(self):
        data = self.head
        self.head = self.head.get_next()
        self.count -= 1
        return data

    def remove_last(self):
        if self.head == None:
            return None

        current = self.head
        pervious = self.head.get_next()

        while current.get_next() != None:
            pervious = current
            current = current.get_next()

        if pervious != None:
           pervious.set_next = None
           self.count -= 1
           return current.get_data()
        else:
            current = None
            count = 0
            return current.get_data()

'''
'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def add_after(self, value):
        new_node = Node(value,self.next )
        self.next = new_node

    def remove_after(self):
        self.next = self.next.get_next()

    def __str__(self):
        return str(self.data)

    
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    
    def size(self):
        return self.count

    def add(self, item):
        self.head = Node(item, self.head)
        self.count += 1

    def clear(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def __str__(self):
        if self.head is None:
            return ''
        else:
            result = 'Head: '
            current = self.head
            while current != None:
                result += f'{current.get_data()} --> '
                current = current.get_next()
            return result[:-5]


    def search(self, search_value):
        current = self.head
        while current != None:
            if current.get_data() == search_value:
                return True
            current = current.get_next()
        return False


    def remove_first(self):
        current = self.head
        self.head = self.head.get_next()
        self.count -= 1
        return current


    def remove_last(self):
        if self.head == None:
            return None
        
        current = self.head
        pervious = None

        while current.get_next() != None:
            pervious = current
            current = current.get_next()

        if pervious != None:
            pervious.set_next(None)
            self.count -= 1
            return current.get_data()

        else:
            current = None
            self.count -= 1
            return current.get_data()


fruit = LinkedList()
fruit.add('cherry')
fruit.add('banana')
fruit.add('apple')
value = fruit.remove_last()
print(fruit)
print(value)
print(fruit.size())
print(type(fruit))
'''        

#Q9
'''
class OddNumberIterable:
    def __init__(self, upper_limit):
        self.upper_limit = upper_limit
        self.current_number = 1

    def __next__(self):
        if self.current_number <= self.upper_limit:
            result = self.current_number
            self.current_number += 2
            return result

        else:
            raise StopIteration

        
class OddNumber:
    def __init__(self, upper_limit):
        self.upper_limit = upper_limit

    def __iter__(self):
        return OddNumberIterable(self.upper_limit)


values = OddNumber(5)
for x in values:
    print(x)

'''
'''

class OddNumber:
    def __init__(self, upper_limit):
        self.upper_limit = upper_limit

    def __iter__(self):
        return OddNumberIterator(self.upper_limit)

class OddNumberIterator:
    def __init__(self, upper_limit):
        self.upper_limit = upper_limit
        self.current_number = 1

    def __next__(self):
        if self.current_number <= self.upper_limit:
            data = self.current_number
            self.current_number += 2
            return data
        else:
            raise StopIteration

values = OddNumber(5)
for x in values:
    print(x)
'''
'''
#Q10
class OddNumber:
    def __init__(self, upper_limit):
        self.upper_limit = upper_limit

    def __iter__(self):
        return OddNumberIterator(self.upper_limit)

class OddNumberIterator:
    def __init__(self, upper_limit):
        self.upper_limit = upper_limit
        self.current_number = 1

    def __next__(self):
        if self.current_number <= self.upper_limit:
            data = self.current_number
            self.current_number += 2
            return data
        else:
            raise StopIteration

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def add_after(self, value):
        new_node = Node(value,self.next )
        self.next = new_node

    def remove_after(self):
        self.next = self.next.get_next()

    def __str__(self):
        return str(self.data)
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    
    def size(self):
        return self.count

    def add(self, item):
        self.head = Node(item, self.head)
        self.count += 1

    def clear(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def __str__(self):
        if self.head is None:
            return ''
        else:
            result = 'Head: '
            current = self.head
            while current != None:
                result += f'{current.get_data()} --> '
                current = current.get_next()
            return result[:-5]


    def search(self, search_value):
        current = self.head
        while current != None:
            if current.get_data() == search_value:
                return True
            current = current.get_next()
        return False


    def remove_first(self):
        current = self.head
        self.head = self.head.get_next()
        self.count -= 1
        return current


    def remove_last(self):
        if self.head == None:
            return None
        
        current = self.head
        pervious = None

        while current.get_next() != None:
            pervious = current
            current = current.get_next()

        if pervious != None:
            pervious.set_next(None)
            self.count -= 1
            return current.get_data()

        else:
            current = None
            self.count -= 1
            return current.get_data()

    def __iter__(self):
        return LinkedListIterator(self.head)

class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __next__(self):
        if self.current is not None:
            result = self.current
            self.current = self.current.get_next()
            return result
        else:
            raise StopIteration


values = LinkedList()
values.add('cherry')
values.add('banana')
values.add('apple')
for value in values:
    print(value)
'''

#--------------------------------------------------------------
#Lab 16
#Q7
'''
class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

def create_a_bigger_tree():
    tree = BinaryTree(41, BinaryTree(20, BinaryTree(11), BinaryTree(29)), BinaryTree(65, BinaryTree(50), BinaryTree(91)))
    return tree
tree = create_a_bigger_tree()
print(tree.get_data())
print(tree.get_left().get_data())
print(tree.get_right().get_data())
print(tree.get_left().get_right().get_data())
'''
#Q8
'''
class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


def count_multiple_of_3(my_tree):
    count = 0

    if my_tree is not None:
        if my_tree.get_data() % 3 == 0:
            count += 1

    count += count_multiple_of_3(my_tree.get_left())
    count += count_multiple_of_3(my_tree.get_right())

    return count



def convert_tree_to_list(tree):
    a_list = []
    if tree == None:
        return None
    else:
        a_list.append(tree.get_data())

    a_list.append(convert_tree_to_list(tree.get_left()))
    a_list.append(convert_tree_to_list(tree.get_right()))
    return a_list


tree1 = BinaryTree(7, BinaryTree(2, BinaryTree(1), BinaryTree(5)), BinaryTree(9, None, BinaryTree(14)))

tree = BinaryTree(12345)
result = convert_tree_to_list(tree)
print(result)


result = convert_tree_to_list(tree1)
print(result)

'''

#Q9
'''
class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


def count_multiple_of_3(my_tree):
    count = 0

    if my_tree is not None:
        if my_tree.get_data() % 3 == 0:
            count += 1

    count += count_multiple_of_3(my_tree.get_left())
    count += count_multiple_of_3(my_tree.get_right())

    return count



def convert_tree_to_list(tree):
    a_list = []
    if tree == None:
        return None
    else:
        a_list.append(tree.get_data())

    a_list.append(convert_tree_to_list(tree.get_left()))
    a_list.append(convert_tree_to_list(tree.get_right()))
    return a_list


def create_tree_from_nested_list(a_list):
    if a_list == None:
        return None

    data = a_list[0]
    left = a_list[1]
    right = a_list[2]

    left_leaf = create_tree_from_nested_list(left)
    right_leaf = create_tree_from_nested_list(right)

    return BinaryTree(data, left_leaf, right_leaf)

tree1 = BinaryTree(7, BinaryTree(2, BinaryTree(1), BinaryTree(5)), BinaryTree(9, None, BinaryTree(14)))

tree = create_tree_from_nested_list([10, [5, None, None], None])
print_tree(tree, 0)
'''
#Q10
'''
class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


def count_multiple_of_3(my_tree):
    count = 0

    if my_tree is not None:
        if my_tree.get_data() % 3 == 0:
            count += 1

    count += count_multiple_of_3(my_tree.get_left())
    count += count_multiple_of_3(my_tree.get_right())

    return count



def convert_tree_to_list(tree):
    a_list = []
    if tree == None:
        return None
    else:
        a_list.append(tree.get_data())

    a_list.append(convert_tree_to_list(tree.get_left()))
    a_list.append(convert_tree_to_list(tree.get_right()))
    return a_list


def create_tree_from_nested_list(a_list):
    if a_list == None:
        return None

    data = a_list[0]
    left = a_list[1]
    right = a_list[2]

    left_leaf = create_tree_from_nested_list(left)
    right_leaf = create_tree_from_nested_list(right)

    return BinaryTree(data, left_leaf, right_leaf)


def print_inorder(tree):
    if tree is not  None:

        print_inorder(tree.left)
        print(tree.data, end=' ')
        print_inorder(tree.right)


tree1 = [7, [2, [1, None, None], [5, None, None]], [9, None, [14, None, None]]]
print_inorder(tree1)

'''

#redo
'''
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError(f"ERROR: The queue is empty!")
        return self.items.pop()


    def peek(self):
        if self.is_empty():
            raise IndexError(f"ERROR: The queue is empty!")
        return self.items[len(self.items)-1]

    def clear(self):
        self.items = []

    def __str__(self):
        data = str(self.items)
        data = data[1:-1]
        return f"-> |{data}| ->"

    def enqueue_list_from_last(self, a_list):
        b_list = a_list[::-1]
        for b in b_list:
            self.enqueue(b)
        return self.items
    
class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


def count_multiple_of_3(my_tree):
    count = 0
    if my_tree == None:
        return 0
    else:
        if my_tree.data % 3 == 0:
            count += 1
            
        count += count_multiple_of_3(my_tree.left)
        count += count_multiple_of_3(my_tree.right)

    return count


def convert_tree_to_list(tree):
    a_list = []
    if tree is None:
        return None

    a_list.append(tree.data)
    a_list.append(convert_tree_to_list(tree.left))
    a_list.append(convert_tree_to_list(tree.right))
    return a_list


def create_tree_from_nested_list(a_list):
    if a_list is None:
        return None
    data = a_list[0]
    left_child = a_list[1]
    right_child = a_list[2]

    left_subtree = create_tree_from_nested_list(a_list.left)
    right_subtree = create_tree_from_nested_list(a_list.right)
    return BinaryTree(data, left_subtree, right_subtree)



def print_level_order(tree):
    a_queue = Queue()
    a_queue.enqueue(tree)

    while not a_queue.is_empty():
        node = a_queue.dequeue()
        print(node.data, end=" ")

        if node.left:
            a_queue.enqueue(node.left)
        if node.right:
            a_queue.enqueue(node.right)



    
tree1 = BinaryTree(7, BinaryTree(2, BinaryTree(1), BinaryTree(5)), BinaryTree(9, None, BinaryTree(14)))


print_level_order(tree1)

'''
###
#redo
'''
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError(f"ERROR: The queue is empty!")
        return self.items.pop()


    def peek(self):
        if self.is_empty():
            raise IndexError(f"ERROR: The queue is empty!")
        return self.items[len(self.items)-1]

    def clear(self):
        self.items = []

    def __str__(self):
        data = str(self.items)
        data = data[1:-1]
        return f"-> |{data}| ->"

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert_left(self, new_data):
        if self.left == None:
            self.left = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, left=self.left)
            self.left = t

    def insert_right(self, new_data):
        if self.right == None:
            self.right = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, right=self.right)
            self.right = t

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

def print_tree(t, level):
    print(' ' * (level*4) + str(t.get_data())) 
    if t.get_left() != None:
        print('(L)', end = '')
        print_tree(t.get_left(), level + 1) 
    if t.get_right() != None: 
        print('(R)', end = '')
        print_tree(t.get_right(), level + 1) 


def count_multiple_of_3(my_tree):
    count = 0
    
    if my_tree != None:
        if my_tree.get_data() % 3 == 0:
            count += 1
    count += count_multiple_of_3(my_tree.get_left())
    count += count_multiple_of_3(my_tree.get_right())
    return count


tree1 = BinaryTree(7, BinaryTree(2, BinaryTree(1), BinaryTree(5)), BinaryTree(9, None, BinaryTree(14)))     
print(count_multiple_of_3(tree1))


def convert_tree_to_list(tree):
    a_list = []
    if tree == None:
        return None
    
    if tree != None:
        a_list.append(tree.data)
        a_list.append(convert_tree_to_list(tree.left))
        a_list.append(convert_tree_to_list(tree.right))
    return a_list
        
     

tree = BinaryTree(12345)
result = convert_tree_to_list(tree)
print(result)


def create_tree_from_nested_list(node_list):
    if node_list == None:
        return None
    root = node_list[0]
    left = node_list[1]
    right = node_list[2]

    left1 = create_tree_from_nested_list(left)
    right1 = create_tree_from_nested_list(right)
    return BinaryTree(root, left1, right1)


tree = create_tree_from_nested_list([10, [5, None, None], None])
print_tree(tree, 0)


def print_inorder(tree):
    if tree is None:
        return None
    print_inorder(tree.left)
    print(tree.data, end=' ')
    print_inorder(tree.right)


tree1 = BinaryTree(7, BinaryTree(2, BinaryTree(1), BinaryTree(5)), BinaryTree(9, None, BinaryTree(14)))     
print_inorder(tree1)


def print_level_order(tree):
    if tree is None:
        return None

    a_queue = Queue()
    a_queue.enqueue(tree)

    while not a_queue.is_empty():
        data = a_queue.dequeue()
        print(data.data, end=' ')

        if data.left:
            a_queue.enqueue(data.left)
        if data.right:
            a_queue.enqueue(data.right)


tree1 = BinaryTree(7, BinaryTree(2, BinaryTree(1), BinaryTree(5)), BinaryTree(9, None, BinaryTree(14)))     
print_level_order(tree1)
'''










#--------------------------------------------------------------

#Lab17
#Q7
'''
def print_tree(t, level):
    print(' ' * (level*4) + str(t.get_data())) 
    if t.get_left() != None:
        print('(L)', end = '')
        print_tree(t.get_left(), level + 1) 
    if t.get_right() != None: 
        print('(R)', end = '')
        print_tree(t.get_right(), level + 1)

        
class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def get_left(self):
        return self.left
        
    def get_right(self):
        return self.right
        
    def set_data(self, data):
        self.data = data
        
    def get_data(self):
        return self.data
        
    def set_left(self, left):
        self.left = left
        
    def set_right(self, right):
        self.right = right

    
    def insert(self, value):
        if value == self.data:
            return
        elif value < self.data:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
            
'''

#Q8
'''
def print_tree(t, level):
    print(' ' * (level*4) + str(t.get_data())) 
    if t.get_left() != None:
        print('(L)', end = '')
        print_tree(t.get_left(), level + 1) 
    if t.get_right() != None: 
        print('(R)', end = '')
        print_tree(t.get_right(), level + 1)

        
class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def get_left(self):
        return self.left
        
    def get_right(self):
        return self.right
        
    def set_data(self, data):
        self.data = data
        
    def get_data(self):
        return self.data
        
    def set_left(self, left):
        self.left = left
        
    def set_right(self, right):
        self.right = right

    
    def insert(self, value):
        if value == self.data:
            return
        elif value < self.data:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

def create_a_bigger_bst():
    a_tree = BinarySearchTree(7)
    a_tree.insert(3)
    a_tree.insert(1)
    a_tree.insert(4)
    a_tree.insert(10)
    a_tree.insert(8)
    a_tree.insert(13)
    return a_tree

def create_bst_from_list(values):
    a_tree = BinarySearchTree(values[0])
    for i in range(1, len(values)):
        a_tree.insert(values[i])
    return a_tree


def is_binary_search_tree(my_tree, min_value, max_value):
    if my_tree == None:
        return True

    if not (max_value >= my_tree.data >= min_value):
        return False

    if not my_tree.left == None and not my_tree.right == None:
        return my_tree.left.data < my_tree.data and my_tree.data < my_tree.right.data
    elif my_tree.left != None:
        return my_tree.left.data < my_tree.data
    elif my_tree.right.data != None:
        return my_tree.right.data > my_tree.data
    
    return is_binary_search_tree(my_tree.left, min_value, my_tree.data) and is_binary_search_tree(my_tree.right, my_tree.data, max_value)



def create_bst_from_sorted_list(sorted_list):
    if sorted_list == []:
        return None

    mid = len(sorted_list) // 2
    root = BinarySearchTree(sorted_list[mid])
    root.left = create_bst_from_sorted_list(sorted_list[:mid])
    root.right = create_bst_from_sorted_list(sorted_list[mid + 1:])

    return root

tree = create_bst_from_sorted_list([1, 3, 5, 7, 9, 11, 13])
print_tree(tree, 0)
print(type(tree))

'''
#
#

#--------------------------------------------------------------
#revision for Lab 14 node
'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = new_data
        
    def set_next(self, new_next):
        self.next = new_next
        
    def __str__(self):
        return str(self.data)

    def get_even(self):
        if self.data % 2 == 0:
            return self.data
        return 0

node1 = Node(1)
print(node1.get_even())
node2 = Node(2)
print(node2.get_even())
'''
'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = new_data
        
    def set_next(self, new_next):
        self.next = new_next
        
    def __str__(self):
        return str(self.data)

    def get_string_length(self):
        return len(self.data)

node1 = Node('abc')
print(node1.get_string_length())
node2 = Node('hello')
print(node2.get_string_length())

'''
'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def __str__(self):
        return str(self.data)

def get_count(node):
    count = 0
    current = node
    while current != None:
        count += 1
        current = current.next
    return count

node1 = Node('abc')
node2 = Node('def')
node1.set_next(node2)
print(get_count(node1))
print(get_count(node2))
'''
'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def __str__(self):
        return str(self.data)

def get_count(node):
    count = 0
    current = node
    while current != None:
        count += 1
        current = current.next
    return count


def no_evens(node):
    if node == None:
        return True
    if node.data % 2 == 0:
        return False

    return no_evens(node.next)


node1 = Node(1) 
node2 = Node(2)
node3 = Node(5)
node4 = Node(7)
node1.set_next(node2)
node2.set_next(node3)
node3.set_next(node4)
print(no_evens(node1)) #1, 2, 5, 7
print(no_evens(node3)) #5, 7
'''

#--------------------------------------------------------------
#Lab 18
#Q7
'''
def get_simple_numeric_hash(key, table_size):
    return int(str(key ** 2)[1:-1]) % table_size

print(get_simple_numeric_hash(655, 13))
print(get_simple_numeric_hash(654, 13))
print(get_simple_numeric_hash(653, 13))
'''
#Q8
'''
def get_weighted_hash(key, table_size):
    
    return sum((ord(key[i]) * (i+1)) for i in range(len(key))) % table_size

print(get_weighted_hash('cat', 13))
print(get_weighted_hash('dog', 13))
'''

#Q9
'''
class SimpleHashTable:
    def __init__(self, size = 7, slots = None):
        self.size = size
        self.slots = [None] * self.size

    def __str__(self):
        return f"{self.slots}"

    def get_hash_index(self, key):
        return key % self.size
        
my_hash_table = SimpleHashTable()
print(my_hash_table)
print(type(my_hash_table))
print(my_hash_table.get_hash_index(12))
'''

#Q10
'''
class SimpleHashTable:
    def __init__(self, size = 7, slots = None):
        self.size = size
        self.slots = [None] * self.size

    def __str__(self):
        return f"{self.slots}"

    def get_hash_index(self, key):
        return key % self.size

    def put(self, key):
        index = self.get_hash_index(key)
        if self.slots[index] == None:
            self.slots[index] = key
        else:
            while self.slots[index] != None:
                index = (index + 1) % self.size
            self.slots[index] = key
        return self.slots

my_hash_table = SimpleHashTable(13)
my_hash_table.put(13)
my_hash_table.put(26)
my_hash_table.put(14)
my_hash_table.put(15)
my_hash_table.put(16)
my_hash_table.put(17)
print(my_hash_table)

'''

#Q11
'''
class SimpleHashTable:
    def __init__(self, size = 7, slots = None):
        self.size = size
        self.slots = [None] * self.size

    def __str__(self):
        return f"{self.slots}"

    def get_hash_index(self, key):
        return key % self.size

    def put(self, key):
        if self.is_full():
            raise IndexError(f"ERROR: The hash table is full.")

        else:
            index = self.get_hash_index(key)
            if self.slots[index] == None:
                self.slots[index] = key
            else:
                while self.slots[index] != None:
                    index = (index + 1) % self.size
                self.slots[index] = key
            return self.slots


    def is_empty(self):
        for i in self.slots:
            if i != None:
                return False
        return True

    def is_full(self):
        for i in self.slots:
            if i == None:
                return False
        return True

    def clear(self):
        self.slots = [None] * self.size

    def __len__(self):
        return len(self.slots)


try:
    my_hash_table = SimpleHashTable(3)
    my_hash_table.put(13) 
    my_hash_table.put(26) 
    my_hash_table.put(39)
    my_hash_table.put(52)
except IndexError as e:
    print(e)
print(my_hash_table)
print(my_hash_table.is_empty())
my_hash_table.clear()
print(my_hash_table.is_empty())
'''

#Q12
'''
class SimpleHashTable:
    def __init__(self, size = 7, slots = None):
        self.size = size
        self.slots = [None] * self.size

    def __str__(self):
        return f"{self.slots}"

    def get_hash_index(self, key):
        return key % self.size

    def put(self, key):
        if self.is_full():
            raise IndexError(f"ERROR: The hash table is full.")

        else:
            index = self.get_hash_index(key)
            if self.slots[index] == None:
                self.slots[index] = key
            else:
                while self.slots[index] != None:
                    index = (index + 1) % self.size
                self.slots[index] = key
            return self.slots


    def is_empty(self):
        for i in self.slots:
            if i != None:
                return False
        return True

    def is_full(self):
        for i in self.slots:
            if i == None:
                return False
        return True

    def clear(self):
        self.slots = [None] * self.size

    def __len__(self):
        return len(self.slots)


class QuadraticHashTable:
    def __init__(self, size = 7, slots = None):
        self.size = size
        self.slots = [None] * self.size

    def __str__(self):
        return f"{self.slots}"

    def get_hash_index(self, key):
        return key % self.size

    def put(self, key):
        if self.is_full():
            raise IndexError(f"ERROR: The hash table is full.")

        else:
            index = self.get_hash_index(key)
            if self.slots[index] == None:
                self.slots[index] = key
            else:
                count = 1
                index_copy = index
                while self.slots[index] != None:
                    index = (index_copy + (count ** 2)) % self.size
                    count += 1
                self.slots[index] = key
            return self.slots


    def is_empty(self):
        for i in self.slots:
            if i != None:
                return False
        return True

    def is_full(self):
        for i in self.slots:
            if i == None:
                return False
        return True

    def clear(self):
        self.slots = [None] * self.size

    def __len__(self):
        return len(self.slots)




my_hash_table=QuadraticHashTable()
my_hash_table.put(1)
print(my_hash_table)
my_hash_table.put(8)
print(my_hash_table)
my_hash_table.put(15)
print(my_hash_table)
my_hash_table.put(22)
print(my_hash_table)
'''


#--------------------------------------------------------------
#Lab19
#Q8
'''
class PriorityQueue:
    def __init__(self):
        self.binary_heap = [0]
        self.size = 0
        self.number_of_swaps = 0

    def __str__(self):
        return str(self.binary_heap)

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size
        
    def add_all_ignore_order(self, a_list):
        for num in a_list:
            self.binary_heap.append(num)
            self.size += 1


priority_queue = PriorityQueue()
priority_queue.add_all_ignore_order([9, 5, 11, 4, 18])
print(priority_queue)
'''

#Q
'''class PriorityQueue:
    def __init__(self):
        self.binary_heap = [0]
        self.size = 0
        self.number_of_swaps = 0

    def __str__(self):
        return str(self.binary_heap)

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size
        
    def add_all_ignore_order(self, a_list):
        for num in a_list:
            self.binary_heap.append(num)
            self.size += 1

    def percolate_up(self, index):
        parent_index = index // 2
        new_index = None
        while self.binary_heap[parent_index] > self.binary_heap[index]:
            self.binary_heap[parent_index], self.binary_heap[index] = self.binary_heap[index], self.binary_heap[parent_index]
            self.number_of_swaps += 1
            new_index = parent_index

        if new_index:
            if self.binary_heap[1] > self.binary_heap[new_index]:
                self.binary_heap[1], self.binary_heap[new_index] = self.binary_heap[new_index], self.binary_heap[1]
                self.number_of_swaps += 1


    def insert(self, element):
        self.binary_heap.append(element)
        self.size += 1
        self.percolate_up(self.size)


    def get_smaller_child_index(self, index):
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.binary_heap[index * 2] < self.binary_heap[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1


    def percolate_down(self, index):
        while (index * 2) <= self.size:
            smallest_child = self.get_smaller_child_index(index)
            if self.binary_heap[index] > self.binary_heap[smallest_child]:
                tmp = self.binary_heap[index]
                self.binary_heap[index] = self.binary_heap[smallest_child]
                self.binary_heap[smallest_child] = tmp
                self.number_of_swaps += 1
            index = smallest_child
'''

#Q
'''
class PriorityQueue:
    def __init__(self):
        self.binary_heap = [0]
        self.size = 0
        self.number_of_swaps = 0

    def __str__(self):
        return str(self.binary_heap)

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size
        
    def add_all_ignore_order(self, a_list):
        for num in a_list:
            self.binary_heap.append(num)
            self.size += 1

    def percolate_up(self, index):
        parent_index = index // 2
        new_index = None
        while self.binary_heap[parent_index] > self.binary_heap[index]:
            self.binary_heap[parent_index], self.binary_heap[index] = self.binary_heap[index], self.binary_heap[parent_index]
            self.number_of_swaps += 1
            new_index = parent_index

        if new_index:
            if self.binary_heap[1] > self.binary_heap[new_index]:
                self.binary_heap[1], self.binary_heap[new_index] = self.binary_heap[new_index], self.binary_heap[1]
                self.number_of_swaps += 1


    def insert(self, element):
        self.binary_heap.append(element)
        self.size += 1
        self.percolate_up(self.size)


    def get_smaller_child_index(self, index):
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.binary_heap[index * 2] < self.binary_heap[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1


    def percolate_down(self, index):
        while (index * 2) <= self.size:
            smallest_child = self.get_smaller_child_index(index)
            if self.binary_heap[index] > self.binary_heap[smallest_child]:
                self.binary_heap[index], self.binary_heap[smallest_child] = self.binary_heap[smallest_child], self.binary_heap[index]
                self.number_of_swaps += 1
            index = smallest_child




    def create_heap_fast(self, values):
        for value in values:
            self.binary_heap.append(value)
            self.size += 1
            
        current_index = self.size // 2
        while current_index != 0:
            self.percolate_down(current_index)
            current_index -= 1



pq = PriorityQueue()
keys = [9, 5, 8, 6, 3, 2]
pq.create_heap_fast(keys)
print(pq)
print(pq.number_of_swaps)


data = [43, 75, 3, 76, 14, 25, 56, 27, 16]
pq2 = PriorityQueue()
pq2.create_heap_fast(data)
print(pq2)
print(pq2.number_of_swaps)

'''
#--------------------------------------------------------------
#Lab 20
#t2 = BinaryTree(41, BinaryTree(20, BinaryTree(11), BinaryTree(29)), BinaryTree(65, BinaryTree(50), BinaryTree(91)))
#t3 = BinaryTree('a', BinaryTree('b', BinaryTree('d', None, BinaryTree('f')), BinaryTree('e', None, BinaryTree('g'))), BinaryTree('c')) 
#Q1
'''
class Roman:
    roman_dict = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL':40, 'L': 50, 'XC':90, 'C': 100}

    def __init__(self, symbols):
        self.codes_list = symbols
        self.value = 0

        for symbol in self.codes_list:
            self.value += Roman.roman_dict[symbol]

    def __str__(self):
        return f"{''.join(self.codes_list)}({self.value})"

    def __lt__(self, other):
        return self.value < other.value




roman1 = Roman(['X', 'X', 'I'])
roman2 = Roman(['C', 'I'])
print(roman1, roman2)
print(type(roman1))
print(roman1 < roman2)
print(roman2 < roman1)
'''

#Q2
'''
class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if self.is_empty():
            raise IndexError('ERROR: The stack is empty!')
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError('ERROR: The stack is empty!')
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)[:-1] + ' <-'

   
def reverse_tokens(tokens):
    stack = Stack()
    a_list = []

    for char in tokens:
        if char != ']':
            stack.push(char)
        else:
            word = ''
            while stack.peek() != '[':
                word += stack.pop()
            a_list.append(word)
            stack.pop()
    return a_list


data = '[hello[happy]world]'
print(reverse_tokens(data))
print(reverse_tokens('[abc[def[gh]i]jk]'))
'''
'''
def reverse_tokens(tokens):
    a_stack = Stack()
    result = []

    for char in tokens:

        if char != ']':
            a_stack.push(char)
        else:
            word = ''
            while a_stack.peek() != '[':
                word += a_stack.pop()
            a_stack.pop()
            result.append(word)
    return result
'''


#Q3
'''
class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty!")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty!")
        return self.items[len(self.items)-1]
    
    def __str__(self):
        queue_str = "| ->"
        for i in range(len(self.items) - 1, -1, -1):
            if i == len(self.items) - 1:
                queue_str = str(self.items[i]) + queue_str
            else:
                queue_str = str(self.items[i]) + ", " + queue_str
        queue_str = "-> |" + queue_str
        return queue_str


def queue_reward(customer_queue, reward):
    
    for i in range(1, customer_queue.size()+1):
        value = customer_queue.dequeue()
        name, deposite = value

        deposite += 50 * i
        customer_queue.enqueue((name, deposite))


my_queue = Queue()
my_queue.enqueue(("Sarah", 100))
my_queue.enqueue(("Luca", 300))
my_queue.enqueue(("Lucy", 200))
print(my_queue)
queue_reward(my_queue, 50)
print(my_queue)
print(type(my_queue))

'''

#Q4
'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def add_after(self, value):
        new_node = Node(value)
        new_node.set_next(self.next)
        self.next = new_node

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def get_head(self):
        return self.head
    
    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def search(self, item):
        current = self.head 
        while current != None:
            if current.get_data() == item:
                return True
            else:
                current = current.get_next()
        return False

    def remove(self, item):
        found = False
        current = self.head
        previous = None
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if found:
            if previous == None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
            self.count -= 1
        else:
            raise ValueError("remove(" + str(item) + "). " + str(item) + " is not in list")

    def __str__(self):
        current = self.head
        string = ""
        while current != None:
            string += str(current.get_data())
            if current.get_next() != None:
                string += " --> "
            current = current.get_next()
        return string
    

    def remove_every_second_item(self):
        current = self.head
        if current is None or current.next is None:
            return current

        while current != None and current.next != None:
            current.next = current.next.next
            current = current.next


name_list = ["Angela", "Burkhard", "Ann"]
my_list = LinkedList()
for name in name_list:
    my_list.add(name)
print("Before:", my_list)
my_list.remove_every_second_item()
print("After:", my_list)
'''

#Q5
'''
class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert_left(self, new_data):
        if self.left == None:
            self.left = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, left=self.left)
            self.left = t

    def insert_right(self, new_data):
        if self.right == None:
            self.right = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, right=self.right)
            self.right = t

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right
     
def create_tree_from_nested_list(node_list):
    if node_list:
        result = BinaryTree(node_list[0])
        left = create_tree_from_nested_list(node_list[1])
        right = create_tree_from_nested_list(node_list[2])
        if left != None:
            result.set_left(left)
        if right != None:
            result.set_right(right)
        return result

def print_tree(t, level):
    print(' ' * (level*4) + str(t.get_data())) 
    if t.get_left() != None:
        print('(l)', end = '')
        print_tree(t.get_left(), level + 1) 
    if t.get_right() != None: 
        print('(r)', end = '')
        print_tree(t.get_right(), level + 1)
        



def same_structure(binary_tree1, binary_tree2):
    if binary_tree1 is None and binary_tree2 is None:
        return True
    elif binary_tree1 is None or binary_tree2 is None:
        return False

    left = same_structure(binary_tree1.left, binary_tree2.left)
    right = same_structure(binary_tree2.right, binary_tree2.right)

    return left and right


tree1 = create_tree_from_nested_list([5, None, None])
tree2 = create_tree_from_nested_list([4, [2, None, [3, None, None]], [7, None, None]])
tree3 = create_tree_from_nested_list([4, None, [7, None, [10, None, [12, None, None]]]])
tree4 = create_tree_from_nested_list([4, [2, [1, [0, None, None], None], None], None])
tree5 = create_tree_from_nested_list([5, [2, [1, None, None], None], [7, None, None]])
tree6 = create_tree_from_nested_list([5, [2, None, [3, None, None]], [7, None, None]])
tree7 = create_tree_from_nested_list([8, [3, None, [4, None, None]], [10, None, [11, None, None]]])
tree8 = create_tree_from_nested_list([7, [3, [1, None, None], [4, None, None]], [10, None, [11, None, None]]])
tree9 = create_tree_from_nested_list([7, [3, [1, [0, None, None], [2, None, None]], [4, None, None]], [9, [8, None, None], [11, None, None]]])


print("First tree:")
print_tree(tree3,0)
print("Second tree:")
print_tree(tree4,0)
print("Same structure: ",same_structure(tree3, tree4))
'''

#Q6
'''
class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def insert_left(self, new_data):
        if self.left == None:
            self.left = BinarySearchTree(new_data)
        else:
            tree = BinarySearchTree(new_data, left=self.left)
            self.left = tree
            
    def insert_right(self, new_data):
        if self.right == None:
            self.right = BinarySearchTree(new_data)
        else:
            tree = BinarySearchTree(new_data, right=self.right)
            self.right = tree
            
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def set_data(self, data):
        self.data = data
        
    def get_data(self):
        return self.data
    
    def insert(self, new_data):
        if new_data == self.data:
            return
        elif new_data < self.data:
            if self.left == None:
                self.left = BinarySearchTree(new_data)
            else:
                self.left.insert(new_data)
        else:
            if self.right == None:
                self.right = BinarySearchTree(new_data)
            else:
                self.right.insert(new_data)
                
    def search(self, find_data):
        if self.data == find_data:
            return True
        elif find_data < self.data and self.left != None:
            return self.left.search(find_data)
        elif find_data > self.data and self.right != None:
            return self.right.search(find_data)
        else:
            return False


def bst_path_inorder_predecessor(bst):
    a_list = []
    if bst == None or bst.left is None:
        return []
    a_list.append(bst.data)
    a_list.append(bst.left.data)
    current = bst.left
    if current.right is None:
        return a_list
    
    while current.right != None:
        current = current.right
        a_list.append(current.data)
    return a_list



t = BinarySearchTree(70)
t.insert(31)
t.insert(85)
t.insert(14)
t.insert(73)
t.insert(94)
t.insert(11)
t.insert(23)
t.insert(86)
t.insert(35)
t.insert(39)
t.insert(37)
print(bst_path_inorder_predecessor(t))
'''

#Q7

'''
class PriorityQueue:
    def __init__(self):
        self.binary_heap = [0]
        self.size = 0
        self.number_of_swaps = 0

    def __str__(self):
        return str(self.binary_heap)

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def percolate_up(self, i):
        while i // 2 > 0 and self.binary_heap[i] < self.binary_heap[i//2]:
            self.binary_heap[i], self.binary_heap[i//2] = self.binary_heap[i//2], self.binary_heap[i]
            self.number_of_swaps += 1
            i = i // 2

    def insert(self, item):
        self.binary_heap.append(item)
        self.size += 1
        self.percolate_up(self.size)

    def get_smaller_child_index(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.binary_heap[i*2] < self.binary_heap[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def percolate_down(self, i):
        while (i * 2) <= self.size:
            mc = self.get_smaller_child_index(i)
            if self.binary_heap[i] > self.binary_heap[mc]:
                self.binary_heap[mc], self.binary_heap[i] = self.binary_heap[i], self.binary_heap[mc]
                self.number_of_swaps += 1
            i = mc

    def delete_minimum(self):
        minimum_value = self.binary_heap[1]
        self.binary_heap[1] = self.binary_heap[self.size]
        self.binary_heap.pop()
        self.size -= 1
        self.percolate_down(1)
        return minimum_value

    def create_heap_fast(self, values):
        for index in range(len(values)):
            self.binary_heap.append(values[index])
            self.size += 1
        for index in range(len(self.binary_heap)//2, 0, -1):
            self.percolate_down(index)



def kth_smallest_element(numbers, k):
    pq = PriorityQueue()
    pq.create_heap_fast(numbers)

    current = None
    for i in range(k):
        current = pq.delete_minimum()
    return current, pq.number_of_swaps
        





numbers = [83,41,77,43]
k = 1
print("Compute the " + str(k) + "th smallest element of " + str(numbers))
(num, number_of_swaps) = kth_smallest_element(numbers, k)
print("Answer: " + str(num) + " in " + str(number_of_swaps) + " steps!")


numbers = [83,41,77,43]
k = 2
print("Compute the " + str(k) + "th smallest element of " + str(numbers))
(num, number_of_swaps) = kth_smallest_element(numbers, k)
print("Answer: " + str(num) + " in " + str(number_of_swaps) + " steps!")


numbers = [23,42,77,43,3,25,78]
k = 2
print("Compute the " + str(k) + "th smallest element of " + str(numbers))
(num, number_of_swaps) = kth_smallest_element(numbers, k)
print("Answer: " + str(num) + " in " + str(number_of_swaps) + " steps!")

'''

#Q8
'''
class DoubleHashTable:
    def __init__(self, size=7, secondary_hash_value=5):
        self.size = size
        self.slots = [None] * size
        self.secondary_hash_value = secondary_hash_value

    def __str__(self):
        return str(self.slots)

    def get_hash_index(self, key):
        return key % self.size

    def clear(self):
        self.slots = [None] * self.size

    def is_empty(self):
        return self.__len__() == 0

    def __len__(self):
        return sum([1 if item != None else 0 for item in self.slots])

    def put(self, key):
        original_index = index = self.get_hash_index(key)
        step = 1
        step_size = 7 - (key % 7)
        while self.slots[index] != None:
            index = (original_index + step * step_size) % self.size
            step += 1
        self.slots[index]=key
        return (step-1)

    def longest_cluster(self):
        max_cluster = 0
        current_cluster = 0
        
        for i in range(self.size * 2):
            i = i % self.size
            if self.slots[i] != None:
                current_cluster += 1
            else:
                if current_cluster > max_cluster:
                    max_cluster = current_cluster
                    current_cluster = 0
                else:
                    current_cluster = 0
        return max_cluster

hash_value = 5
table_values = [9, 4, 13]
ht = DoubleHashTable(hash_value)
for i in table_values:
    ht.put(i)
print(ht)
print("Longest cluster = ", ht.longest_cluster())


hash_value = 11
table_values = [11,15,43,9,45]
ht = DoubleHashTable(hash_value)
for i in table_values:
    ht.put(i)
print(ht)
print("Longest cluster = ", ht.longest_cluster())

'''

#Q9
'''
def nested_recursion(n, count=0):
    if n <= 0:
        return 1, count
    else:
        count += 1
        if n % 2 == 0:
            inner_result, inner_count = nested_recursion(n // 2 - 1, count+1)
            return nested_recursion(inner_result, inner_count + 1)
        else:
            return nested_recursion(n - 1, count + 1)

'''
'''
def nested_recursion(n, count=0):
    if n <= 0:
        return 1, count
    else:
        #count += 1
    
        if n % 2 == 0:
            inner_result, inner_count = nested_recursion(n // 2 - 1, count+n)
            return nested_recursion(inner_result, inner_count+1)
        else:
            return nested_recursion(n - 1, count+n)


'''
'''
(result, steps) = nested_recursion(2)
print(f"nested_recursion(2)={result} in {steps} steps")

(result, steps) = nested_recursion(3)
print(f"nested_recursion(3)={result} in {steps} steps")
'''

#--------------------------------------------------------------
#2023S0
#Q7

'''
def print_text_block(word):
    for i in range(len(word)):
        data = word[i:]+word[:i]
        print(data)

print_text_block('hello')

'''
#Q8
'''
def get_weighted_scores_list(word):
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    return [(i * valid_letters.index(word[i])) for i in range(len(word))]

print(get_weighted_scores_list('hello'))
print(get_weighted_scores_list('big'))
print(get_weighted_scores_list('data'))
'''

#Q9
''''
def create_terrier_registration_dict(filename):
    try:
        a_dict = {}
        f = open(filename, 'r')
        content = f.readlines()
        f.close()
        for line in content:
            a_list = []
            line = line.split(':')
            numbers = line[1].split()
            for number in numbers:
                a_list.append(int(number))
            a_dict[line[0]] = a_list
        return a_dict



    except FileNotFoundError:
        print(f"ERROR: The file '{filename}' does not exist.")

        
data = create_terrier_registration_dict('terrier1.txt')
for key in sorted(data):
    print(key, data[key])
print(type(data))
print(type(data['Airedale Terrier']))
print(type(data['Airedale Terrier'][0]))



data = create_terrier_registration_dict('errors.txt')
'''

#Q10
'''
def get_registration_sum(registration_dictionary, target_breed):

    try:
        count = 0
        for number in registration_dictionary[target_breed]:
            try:
                count += int(number)
            except ValueError:
                pass
        return count

    except KeyError:
        print(f"The breed: '{target_breed}' is invalid.")
        return 0


# Use try-except to handle the following cases:
registrations = {'Airedale Terrier': [600, '555', 610, 659, 654, 683, 601, 562, 482, 817], 'Australian Terrier': [30, 33, 27, 'twenty', 44, 22, 23, 23, 37, 43]}
print(get_registration_sum(registrations , 'Airedale Terrier')) #accept '555'
print(get_registration_sum(registrations , 'Australian Terrier')) #ignore 'twenty'
print(get_registration_sum(registrations , 'Terrier')) #not found

data = {'Airedale Terrier': [600, 555, 610, 659, 654, 683, 601, 562, 482, 817], 'Australian Terrier': [30, 33, 27, 27, 44, 22, 23, 23, 37, 43], 'Bedlington Terrier': [506, 482, 462, 395, 411, 483, 307, 333, 364, 463], 'Border Terrier': [6577, 6390, 5988, 5426, 5150, 5130, 5245, 4353, 4587, 5930], 'Bull Terrier': [2132, 1825, 1567, 1477, 1370, 1542, 1611, 1282, 1502, 2431], 'Bull Terrier (Miniature)': [192, 161, 189, 183, 172, 189, 221, 200, 185, 364], 'Cairn Terrier': [1035, 1085, 908, 835, 683, 589, 567, 464, 443, 498], 'Cesky Terrier': [26, 26, 31, 31, 30, 36, 19, 43, 38, 41], 'Dandie Dinmont Terrier': [120, 105, 144, 88, 91, 130, 145, 109, 87, 124], 'Fox Terrier (Smooth)': [94, 122, 142, 148, 118, 82, 126, 112, 122, 151], 'Fox Terrier (Wire)': [669, 604, 676, 672, 511, 668, 575, 458, 485, 623], 'Glen of Imaal Terrier': [57, 55, 74, 79, 76, 48, 48, 85, 36, 83], 'Irish Terrier': [306, 362, 371, 290, 326, 362, 384, 338, 389, 457], 'Jack Russell Terrier': ['ten', 136, 205, 266, 391, 355]}
print(get_registration_sum(data, 'Fox Terrier'))
print(get_registration_sum(data, 'Fox Terrier (Wire)'))
'''

#Q11
'''
class PlayingCard:

    def __init__(self, suit_index = 0, value_index = 0):
        suit = ['None', 'Clubs', 'Diamonds', 'Hearts', 'Spades']
        value = ['None', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.suit = suit[suit_index+1]
        self.value = value[value_index+1]
        self.score = (suit_index+1)*(value_index+1)

    def get_score(self):
        return self.score

    def __str__(self):
        return f"{self.suit}-{self.value}({self.score})"


card1 = PlayingCard(3, 12)
print(card1)
print(PlayingCard(0, 0))
print(PlayingCard(2, 8))

card1 = PlayingCard(1, 10)
print(card1)
card2 = PlayingCard(2, 11)
print(card2)
card3 = PlayingCard()
print(card3)
print(type(card1))
print(card1.suit) #for validation purpose, should not access .suit directly
print(card1.value) #for validation purpose

'''

#Q12
'''
class PlayingCard:
    def __init__(self, suit_index = 0, value_index = 0):
        suit = ['None', 'Club', 'Diamonds', 'Hearts', 'Spades']
        value = ['None', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
        self.suit = suit[suit_index+1]
        self.value = value[value_index+1]
        self.score = (suit_index+1) * (value_index+1)

    def get_score(self):
        return self.score

    def __str__(self):
        return f"{self.suit}-{self.value}({self.score})"



import random
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def play_turn(self):
        suit_index = random.randrange(1, 3)
        value_index = random.randrange(1, 12)
        self.cards.append(PlayingCard(suit_index, value_index))

    def get_total_score(self):
        total = sum(card.score for card in self.cards)
        return total


    def __str__(self):
        cards_info = "\n".join(str(card) for card in self.cards)
        total_score = self.get_total_score()
        return f"{self.name}\n{cards_info}\nTotal = {total_score}"

        
random.seed(40)
player1 = Player('Bob')
player1.play_turn()
player1.play_turn()
print(player1)
print(type(player1))        

random.seed(50)
player1 = Player('Bob')
player1.play_turn()
print(player1)
print(type(player1.cards)) #for validation only. should not access the cards attributes directly.
print(type(player1.cards[0])) #for validation only. It must be a playing card object
'''

#Q13
'''
class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if self.is_empty():
            raise IndexError('ERROR: The stack is empty!')
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError('ERROR: The stack is empty!')
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)[:-1] + ' <-'
    
    def clear(self):
        self.__items = []
        
    def push_list(self, mylist):
        for i in range(len(mylist)):
           self.push(mylist[i])
           
def create_characters_stack(characters):
    a_stack = Stack()
    for char in characters:
        a_stack.push(char)
    return a_stack

def split_digits_letters(a_stack):
    letter_stack = Stack()
    digit_stack = Stack()
    while not

    a_stack.is_empty():
        if a_stack.peek().isdigit():
            digit_stack.push(a_stack.pop())
        else:
            letter_stack.push(a_stack.pop())
    return digit_stack, letter_stack


a_stack = create_characters_stack(['A', 'g', 'e', 'n', 
                                   't', '0', '0', '7'])
a_tuple = split_digits_letters(a_stack)
print(a_tuple[0])
print(a_tuple[1])
print(type(a_tuple))
print(type(a_tuple[0]))
print(type(a_tuple[1]))     

a_stack = create_characters_stack(['1', '9', '8', '4'])
a_tuple = split_digits_letters(a_stack)
print(a_tuple[0])
print(a_tuple[1])
print(type(a_tuple))
print(type(a_tuple[0]))
print(type(a_tuple[1]))
'''
#Q14
'''
def caesar_cipher(word, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    data = ''
    if word == '':
        return data

    
    index = (alphabet.find(word[0])+key)%26
    data += alphabet[index]
    
    return data + caesar_cipher(word[1:], key)

print(caesar_cipher('caesar', 5))
'''
#Q15
'''
class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def get_left(self):
        return self.left
        
    def get_right(self):
        return self.right
        
    def set_data(self, data):
        self.data = data
        
    def get_data(self):
        return self.data
        
    def set_left(self, left):
        self.left = left
        
    def set_right(self, right):
        self.right = right

    def get_bst_postorder_list(self):
        a_list = []
        if self.left:
            a_list.extend(self.left.get_bst_postorder_list())
        if self.right:
            a_list.extend(self.right.get_bst_postorder_list())
        a_list.append(self.data)

        return a_list

def print_tree(t, level=0):
    print(' ' * (level*4) + str(t.get_data())) 
    if t.get_left() != None:
        print('(L)', end = '')
        print_tree(t.get_left(), level + 1) 
    if t.get_right() != None: 
        print('(R)', end = '')
        print_tree(t.get_right(), level + 1)



tiny_tree = BinarySearchTree('b')
tiny_tree.set_left(BinarySearchTree('a'))
tiny_tree.set_right(BinarySearchTree('c'))
print_tree(tiny_tree)

tree2_left_left = BinarySearchTree(10)
tree2_left_right = BinarySearchTree(19)
tree2_right_left = BinarySearchTree(31)
tree2_right_right = BinarySearchTree(42)
tree2_left = BinarySearchTree(14, tree2_left_left, tree2_left_right)
tree2_right = BinarySearchTree(35, tree2_right_left, tree2_right_right)
tree2 = BinarySearchTree(27, tree2_left, tree2_right)
print_tree(tree2, 0)

print_tree(tiny_tree)
post_order_list = tiny_tree.get_bst_postorder_list()
print(post_order_list)

print_tree(tree2)
post_order_list = tree2.get_bst_postorder_list()
print(post_order_list)
print(type(post_order_list))
'''

#Q16
'''
class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def get_left(self):
        return self.left
        
    def get_right(self):
        return self.right
        
    def set_data(self, data):
        self.data = data
        
    def get_data(self):
        return self.data
        
    def set_left(self, left):
        self.left = left
        
    def set_right(self, right):
        self.right = right

    def get_bst_postorder_list(self):
        a_list = []
        if self.left:
            a_list.extend(self.left.get_bst_postorder_list())
        if self.right:
            a_list.extend(self.right.get_bst_postorder_list())
        a_list.append(self.data)

        return a_list

def print_tree(t, level=0):
    print(' ' * (level*4) + str(t.get_data())) 
    if t.get_left() != None:
        print('(L)', end = '')
        print_tree(t.get_left(), level + 1) 
    if t.get_right() != None: 
        print('(R)', end = '')
        print_tree(t.get_right(), level + 1)

class BinarySearchTreePostOrderIterator:
    def __init__(self, tree):
        self.tree = tree
        self.poster_list = self.tree.get_bst_postorder_list()
        self.index = 0
        
    def __next__(self):
        if self.index < len(self.)
''' 


#Q19
'''
def is_binary_max_heap(a_list):
    length = len(a_list)
    for i in range(length-1, (length)//2-1, -1):
        parent = i // 2 - 1
        if a_list[parent] > a_list[i]:
            return False
    return True
'''
'''
def is_binary_max_heap(a_list):
    length = len(a_list)
    
    for i in range(2, length):
        if a_list[i] > a_list[(i // 2)]:
            return False
    
    for i in range(1, length // 2 + 1):
        left_child = 2 * i
        right_child = 2 * i + 1
        
        if left_child < length and a_list[i] < a_list[left_child]:
            return False
        if right_child < length and a_list[i] < a_list[right_child]:
            return False
    
    return True

print(is_binary_max_heap([0, 10, 9, 8, 7, 3, 2, 6, 1]))
print(is_binary_max_heap([0, 6, 7, 8, 9, 22, 45, 12, 16, 27, 36]))
print(is_binary_max_heap([0, 7, 6]))
'''

#--------------------------------------------------------------
#2023S2
#Q8
'''
user_input = int(input("Enter an integer: "))
for i in range(1, user_input+1):
    print('X'*i)
'''

#Q9
'''
def convert_tuples(list_of_tuples):
    return [sum(data) for data in list_of_tuples]
        
data = [ (1,), (2, 3), (4, 5, 6), ()]
result = convert_tuples(data)
print(type(result))
print(type(result[0]))
print(result)
'''

#Q10
'''
def create_code_dictionary(usernames_list):
    a_dict = {}
    for name in usernames_list:
        if not name[-3:].isdigit() or not name[:-3].isalpha():
            print(f"ERROR: {name} is invalid.")
    for name in sorted(usernames_list):
        try:
            if name[-3:].isdigit() and name[:-3].isalpha():
                key = 0
                for num in name[-3:]:
                    key += int(num)

                if key not in a_dict:
                    a_dict[key] = [name]
                else:
                    a_dict[key].append(name)
        except (ValueError, TypeError):
            pass
    return a_dict


values = ['eli923', 'trob', 'brob123', 'agas321', 'aana554', 'nbro495', 'hcho402', 'afin02', 'jchu086']

code_dict = create_code_dictionary(values)
for key in sorted(code_dict):
    print(key, code_dict[key])  

'''

#Q11
'''
class Roman:    
    def __init__(self, symbols):
        roman_dict = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL':40, 'L': 50, 'XC':90, 'C': 100}

        self.codes_list = symbols
        self.value = sum(roman_dict[symbol] for symbol in symbols)

    def __str__(self):
        return f"{''.join(self.codes_list)}-({self.value})"

    def __lt__(self, other):
        return self.value < other.value


roman1 = Roman(['X', 'X', 'I'])
roman2 = Roman(['C', 'I'])
print(roman1, roman2)
print(type(roman1))
print(roman1 < roman2)
print(roman2 < roman1)
'''
#Q12
'''
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)                

    def pop(self):
        if self.is_empty():
            raise IndexError('ERROR: The stack is empty!')
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError('ERROR: The stack is empty!')
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)        

    def __str__(self):
        return str(self.items)[:-1] + ' <-'

    def clear(self):
        self.items = []


def reverse_tokens(tokens):
    stack = Stack()
    a_list = []
    for char in tokens:
        if char != ']':
            stack.push(char)
        else:
            word = ''
            while stack.peek() != '[':
                word += stack.pop()
            a_list.append(word)
            stack.pop()

    return a_list


data = '[hello[happy]world]'
print(reverse_tokens(data))
print(reverse_tokens('[abc[def[gh]i]jk]'))

'''

#Q13
'''
class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0,item)
        
    def dequeue(self):
        if self.is_empty():
            raise IndexError('ERROR: The queue is empty!')
        return self.items.pop()
    
    def size(self):
        
        return len(self.items)
    def peek(self):
        if self.is_empty():
            raise IndexError('ERROR: The queue is empty!')
        return self.items[len(self.items)-1]
    
    def __str__(self):
        return '-> |' + str(self.items)[1:-1] + '| ->'
    
    def clear(self):
        self.items = []


def queue_reward(customer_queue, reward):
    queue = Queue()

    for i in range(1, customer_queue.size()+1):
        data = customer_queue.dequeue()
        name, deposite = data
        deposite = deposite + 50 * i
        customer_queue.enqueue((name, deposite))


my_queue = Queue()
my_queue.enqueue(("Sarah", 100))
my_queue.enqueue(("Luca", 300))
my_queue.enqueue(("Lucy", 200))
print(my_queue)
queue_reward(my_queue, 50)
print(my_queue)
print(type(my_queue))
'''

#Q14
'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def add_after(self, value):
        new_node = Node(value)
        new_node.set_next(self.next)
        self.next = new_node

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def get_head(self):
        return self.head
    
    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def search(self, item):
        current = self.head 
        while current != None:
            if current.get_data() == item:
                return True
            else:
                current = current.get_next()
        return False

    def remove(self, item):
        found = False
        current = self.head
        previous = None
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if found:
            if previous == None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
            self.count -= 1
        else:
            raise ValueError("remove(" + str(item) + "). " + str(item) + " is not in list")

    def __str__(self):
        current = self.head
        string = ""
        while current != None:
            string += str(current.get_data())
            if current.get_next() != None:
                string += " --> "
            current = current.get_next()
        return string

    def remove_every_second_item(self):
        current = self.head
        if current is None or current.next is None:
            return ''
        while current is not None and current.next is not None:
            current.next = current.next.next
            current = current.next


my_list = LinkedList()
my_list.add("Angela")
my_list.add("Burkhard")
print("Before:", my_list)
my_list.remove_every_second_item()
print("After:", my_list)

'''

#Q15
'''
class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert_left(self, new_data):
        if self.left == None:
            self.left = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, left=self.left)
            self.left = t

    def insert_right(self, new_data):
        if self.right == None:
            self.right = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, right=self.right)
            self.right = t

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right
     
def create_tree_from_nested_list(node_list):
    if node_list:
        result = BinaryTree(node_list[0])
        left = create_tree_from_nested_list(node_list[1])
        right = create_tree_from_nested_list(node_list[2])
        if left != None:
            result.set_left(left)
        if right != None:
            result.set_right(right)
        return result

def print_tree(t, level):
    print(' ' * (level*4) + str(t.get_data())) 
    if t.get_left() != None:
        print('(l)', end = '')
        print_tree(t.get_left(), level + 1) 
    if t.get_right() != None: 
        print('(r)', end = '')
        print_tree(t.get_right(), level + 1)
        
tree1 = create_tree_from_nested_list([5, None, None])
tree2 = create_tree_from_nested_list([4, [2, None, [3, None, None]], [7, None, None]])
tree3 = create_tree_from_nested_list([4, None, [7, None, [10, None, [12, None, None]]]])
tree4 = create_tree_from_nested_list([4, [2, [1, [0, None, None], None], None], None])
tree5 = create_tree_from_nested_list([5, [2, [1, None, None], None], [7, None, None]])
tree6 = create_tree_from_nested_list([5, [2, None, [3, None, None]], [7, None, None]])
tree7 = create_tree_from_nested_list([8, [3, None, [4, None, None]], [10, None, [11, None, None]]])
tree8 = create_tree_from_nested_list([7, [3, [1, None, None], [4, None, None]], [10, None, [11, None, None]]])
tree9 = create_tree_from_nested_list([7, [3, [1, [0, None, None], [2, None, None]], [4, None, None]], [9, [8, None, None], [11, None, None]]])



def same_structure(binary_tree1, binary_tree2):
    if binary_tree1 is None and binary_tree2 is None:
        return True
    elif binary_tree1 is None or binary_tree2 is None:
        return False

    left = same_structure(binary_tree1.left, binary_tree2.left)
    right = same_structure(binary_tree1.right, binary_tree2.right)
    return left and right


print("First tree:")
print_tree(tree4,0)
print("Second tree:")
print_tree(tree4b,0)
print("Same structure: ",same_structure(tree4, tree4b))

print("First tree:")
print_tree(tree3,0)
print("Second tree:")
print_tree(tree4,0)
print("Same structure: ",same_structure(tree3, tree4))
'''

#Q16
'''
class PriorityQueue:
    def __init__(self):
        self.binary_heap = [0]
        self.size = 0
        self.number_of_swaps = 0

    def __str__(self):
        return str(self.binary_heap)

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def percolate_up(self, i):
        while i // 2 > 0 and self.binary_heap[i] < self.binary_heap[i//2]:
            self.binary_heap[i], self.binary_heap[i//2] = self.binary_heap[i//2], self.binary_heap[i]
            self.number_of_swaps += 1
            i = i // 2

    def insert(self, item):
        self.binary_heap.append(item)
        self.size += 1
        self.percolate_up(self.size)

    def get_smaller_child_index(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.binary_heap[i*2] < self.binary_heap[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def percolate_down(self, i):
        while (i * 2) <= self.size:
            mc = self.get_smaller_child_index(i)
            if self.binary_heap[i] > self.binary_heap[mc]:
                self.binary_heap[mc], self.binary_heap[i] = self.binary_heap[i], self.binary_heap[mc]
                self.number_of_swaps += 1
            i = mc

    def delete_minimum(self):
        minimum_value = self.binary_heap[1]
        self.binary_heap[1] = self.binary_heap[self.size]
        self.binary_heap.pop()
        self.size -= 1
        self.percolate_down(1)
        return minimum_value

    def create_heap_fast(self, values):
        for index in range(len(values)):
            self.binary_heap.append(values[index])
            self.size += 1
        for index in range(len(self.binary_heap)//2, 0, -1):
            self.percolate_down(index)


def  bst_path_inorder_predecessor(bst):
    a_list = []
    if bst is None or bst.left is None:
        return []
    else:
        a_list.append(bst.data)
        current = bst.left
        while current != None:
            a_list.append(current.data)
            current = current.right
    return a_list

t = BinarySearchTree(7)
t.insert(2)
t.insert(9)
t.insert(1)
t.insert(5)
print(bst_path_inorder_predecessor(t))
'''

#Q17
'''
class PriorityQueue:
    def __init__(self):
        self.binary_heap = [0]
        self.size = 0
        self.number_of_swaps = 0

    def __str__(self):
        return str(self.binary_heap)

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def percolate_up(self, i):
        while i // 2 > 0 and self.binary_heap[i] < self.binary_heap[i//2]:
            self.binary_heap[i], self.binary_heap[i//2] = self.binary_heap[i//2], self.binary_heap[i]
            self.number_of_swaps += 1
            i = i // 2

    def insert(self, item):
        self.binary_heap.append(item)
        self.size += 1
        self.percolate_up(self.size)

    def get_smaller_child_index(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.binary_heap[i*2] < self.binary_heap[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def percolate_down(self, i):
        while (i * 2) <= self.size:
            mc = self.get_smaller_child_index(i)
            if self.binary_heap[i] > self.binary_heap[mc]:
                self.binary_heap[mc], self.binary_heap[i] = self.binary_heap[i], self.binary_heap[mc]
                self.number_of_swaps += 1
            i = mc

    def delete_minimum(self):
        minimum_value = self.binary_heap[1]
        self.binary_heap[1] = self.binary_heap[self.size]
        self.binary_heap.pop()
        self.size -= 1
        self.percolate_down(1)
        return minimum_value

    def create_heap_fast(self, values):
        for index in range(len(values)):
            self.binary_heap.append(values[index])
            self.size += 1
        for index in range(len(self.binary_heap)//2, 0, -1):
            self.percolate_down(index)


def kth_smallest_element(numbers, k):
    pq = PriorityQueue()
    pq.create_heap_fast(numbers)

    current = 0
    for i in range(k):
        current = pq.delete_minimum()
    return current, pq.number_of_swaps


numbers = [83,41,77,43]
k = 1
print("Compute the " + str(k) + "th smallest element of " + str(numbers))
(num, number_of_swaps) = kth_smallest_element(numbers, k)
print("Answer: " + str(num) + " in " + str(number_of_swaps) + " steps!")
'''

#Q18
'''
class DoubleHashTable:
    def __init__(self, size=7, secondary_hash_value=5):
        self.size = size
        self.slots = [None] * size
        self.secondary_hash_value = secondary_hash_value

    def __str__(self):
        return str(self.slots)

    def get_hash_index(self, key):
        return key % self.size

    def clear(self):
        self.slots = [None] * self.size

    def is_empty(self):
        return self.__len__() == 0

    def __len__(self):
        return sum([1 if item != None else 0 for item in self.slots])

    def put(self, key):
        original_index = index = self.get_hash_index(key)
        step = 1
        step_size = 7 - (key % 7)
        while self.slots[index] != None:
            index = (original_index + step * step_size) % self.size
            step += 1
        self.slots[index]=key
        return (step-1)


    def longest_cluster(self):
        max_count = 0
        current_count = 0
        for index in range(self.size * 2):
            i = index % self.size
            if self.slots[i] != None:
                current_count += 1
            else:
                if current_count > max_count:
                    max_count = current_count
                    current_count = 0
                else:
                    current_count = 0
        return max_count
        

hash_value = 5
table_values = [9, 4, 13]
ht = DoubleHashTable(hash_value)
for i in table_values:
    ht.put(i)
print(ht)
print("Longest cluster = ", ht.longest_cluster())

'''

#2023S0

#Q7
'''
def print_text_block(word):
    for i in range(len(word)):
        print(word[i:] + word[:i])

print_text_block('hello')
'''

#Q8
'''
def get_weighted_scores_list(word):
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    return [(i*valid_letters.find(word[i])) for i in range(len(word))]


        
print(get_weighted_scores_list('hello'))
print(get_weighted_scores_list('big'))
print(get_weighted_scores_list('data'))
'''

#Q9
def create_terrier_registration_dict(filename):
     

































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































