"""
The Customer Service Represetatives (CSRs) in the marketing department with a security clearance of 'TS' were able
to thwart an attack on the server and for that management has decided to reward them with a 10% increase in their salary. 
To evaluate the impact on the budget, you have been asked to run a report on the employee file and display the results 
of BEFORE AND AFTER the salary increase. Also calculate the total difference between the old salary and the new
salary (as shown in the image).

You will create a dictionary that has the full employee name as the key and only their NEW salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as shown in the image)
"""

import csv

# dict = {}

# open the file

with open("./employee_data.csv", "r") as infile:
    reader = csv.reader(infile)
    next(reader)
    # create an empty dictionary

    emp_salary = {}

    # use a loop to iterate through the csv file
    for col in reader:
        # check if the employee fits the search criteria
        if col[9] == "TS":
            Updates = {
                "Employee Name": col[1] + " " + col[2],
                "New Salary": round((float(col[5]) * 1.10), 2),
            }

            if "Updated_Salary" in emp_salary:
                emp_salary["Updated_Salary"].append(Updates)
            else:
                emp_salary["Updated_Salary"] = [Updates]

print(emp_salary)


print()
print("=========================================")
print()

# iternate through the dictionary and print out the key and value as per image

for k, v in emp_salary.items():
    print("Employee Name:", v[Updated_Salary[0]])


"""  
          
print()
print('=========================================')
print()
"""

# print out the total difference between the old salary and the new salary as per image.
