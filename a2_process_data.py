#######################################################
### Please ignore the lines of code in this section.
### It loads the contents of a CSV file for you.
### The file's name should be a2_input.csv.
### You do not need to know how it works.
#######################################################

import csv

contents = []
with open("a2_input.csv") as input_file:
    for row in csv.reader(input_file):
        contents = contents + [row]

#######################################################
### Do your data processing below.
### The below code gives some examples
### of how to access the data.
### Print your results using the print function.
#######################################################

html_base='''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>%s</title>
        %s
    </head>
    <body>
        %s
        %s
    </body>
</html>
'''

        
def calculate_the_sum(list):
    total=0.0
    for element in list:
        total += float(element)
    return total

def get_column_as_a_list(index_of_column):
    column_list = []
    for row in range(len(contents)):
        column_list += [contents[row][index_of_column]]
    return column_list

def get_row(index):
    row = ""
    for column in range(len(contents[index])):
        row += "				<td>" + str(contents[index][column]) + "</td>\n"
    return row

def get_table_code():
    base_table = '''
    	<table>
        %s
    	</table>
    '''
    rows_of_table = '''
			<tr>
				<th>Movies About Time Travel</th>
				<th>Year</th>
				<th>IMDb</th>
				<th>Duration</th>
			</tr>
    	'''
    for index in range(len(contents)):
        rows_of_table += "	<tr>\n" + get_row(index) + "\n			</tr>\n		"
    return base_table % (rows_of_table)

average_of_imdb = calculate_the_sum(get_column_as_a_list(2))/len(contents)

def number_of_movies_in_a_year(year):
    index = 0
    total=0
    while index < len(contents):
        if str(contents[index][1])==str(year):
            total += 1
        index += 1
    return total

def number_of_movies_longer(min):
    index = 0
    total=0
    while index < len(contents):
        if int(contents[index][3]) > min:
            total += 1
        index += 1
    return total

def get_some_content():
    list='''
        <ul>
            <li>%s</li>
            <li>%s</li>
            <li>%s</li>
        </ul>
    '''
    return list % ("Number of Movies About Time Travel in 2016: " + str(number_of_movies_in_a_year(2016)), "Average of IMDb: " + str(average_of_imdb), "Number of Movies that is longer than 120 mins: " + str(number_of_movies_longer(120)))
    

style_code = '''<style>
            td{
                border:2px solid black;
                padding:3px;
            }
            th{
                border:2px solid black;
                padding:3px;
            }
        </style>
'''
sum_of_durations = calculate_the_sum(get_column_as_a_list(3))
thirty_third_line_of_content = "Movie: " + contents[33][0] + "\nYear: " + contents[33][1] + "\nImdb: " + contents[33][2] + "\nDuration: " + contents[33][3]
product_of_string_and_integer = contents[143][0]*3

# print("The below is variable contents")
# print(contents)
# print("The below is the first row of variable contents")
# print(contents[0])
# print("The below is entry which is in both first row and first column")
# print(contents[0][0])
# print("The below is the type of the variable contents")
# print(type(contents))
# print("The below is the type of the first row in the contents")
# print(type(contents[0]))
# print("The below is the type of the entry which is in both first row and first column")
# print(type(contents[0][0]))
# print("The below is the entry which is in second row and third column")
# print(contents[2][3])
# print("The below is the type of the entry which is in third row and second column")
# print(type(contents[3][2]))
# print("The below is sum of durations")
# print(sum_of_durations)
# print("The below is average of imdb")
# print(average_of_imdb)
# print(contents[10][10]) There is an error because the value doesn't exist. Error message: list index out of range
# print(thirty_third_line_of_content)
# print(contents[1][0] + 3) There is an error because string can not be added an integer. Error message: must be str, not int
# print("The below is product of string and integer")
# print(product_of_string_and_integer)
# print(type(sum_of_durations))
# print(type(average_of_imdb))
# print(type(product_of_string_and_integer))
# help(average_of_imdb)

print(html_base % ("Movies About Time Travel", style_code, get_some_content(), get_table_code()))
