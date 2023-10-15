from prettytable import PrettyTable
from itertools import chain

def find_faculty_with_unique_subjects(faculty_mem):
    # Fill your code here

    sub_lst = []
    res_lst = []
    for ele in faculty_mem:
        a = list(ele.get('Subjects Handled'))
        sub_lst.append(a)
    flatten_list = list(chain.from_iterable(sub_lst))
    # print(flatten_list)
    for ele in flatten_list:
        if flatten_list.count(ele) == 1:
            res_lst.append(ele)
    # print(res_lst)
    res_lst.sort()
    for i in range(len(res_lst)):
        print("Subject:-", res_lst[i])
        for ele in faculty_mem:
            # print(obj.get('Subjects Handled'))
            if res_lst[i] in ele.get('Subjects Handled'):
                cols = ['Name', 'Position', 'Subjects Handled', 'Period']
                myTable = PrettyTable(cols)
                lst = [ele.get('name'), ele.get('position'), ele.get('Subjects Handled'), ele.get('period')]
                myTable.add_row(lst)
                print(myTable)


def find_faculty_in_given_period(faculty_mem, period):
    # Fill your code here

    cols = ['Name', 'Position', 'Subjects Handled', 'Period']
    myTable = PrettyTable(cols)
    a, b = map(int, period.split('-'))
    for ele in faculty_mem:
        val = ele.get('period')
        startyear, endyear = map(int, val.split('-'))
        # mean = (startyear + endyear) / 2

        if (startyear <= a and a <= endyear) or (startyear <= b and endyear >= b):
            lst = [ele.get('name'), ele.get('position'), ele.get('Subjects Handled'), ele.get('period')]
            myTable.add_row(lst)
            # print(ele)

    print(myTable)


faculty_members = [
    {'name': 'Ram', 'position': 'Professor', 'Subjects Handled': {'CA', 'DBMS'}, 'period': '1990-1994'},
    {'name': 'Kavi', 'position': 'Assistant Professor', 'Subjects Handled': {'SE', 'DBMS'}, 'period': '2015-2017'},
    {'name': 'Anu', 'position': 'Lecturer', 'Subjects Handled': {'OOAD', 'SE'}, 'period': '2011-2014'},
    {'name': 'Neha', 'position': 'Assistant Professor', 'Subjects Handled': {'SE', 'Python'}, 'period': '2008-2012'},
    {'name': 'Emily', 'position': 'Lecturer', 'Subjects Handled': {'C Programming', 'DS'}, 'period': '2017-2020'},
    {'name': 'Anitha', 'position': 'Professor', 'Subjects Handled': {'OOAD', 'Machine Learning', 'Data Science'},
     'period': '2019-2023'}
]

ch = 'y'
while ch == 'y':
    d = {}
    print("Enter faculty details to add:")
    d["name"] = input("Enter faculty name\n")
    d["position"] = input("Enter the position of the staff member\n")
    d["Subjects Handled"] = set(input("Enter subjects in comma separated format\n").split(","))
    d["period"] = input("Enter the period of time the staff worked\n")
    faculty_members.append(d)
    ch = input("Do you want to continue?(y/n)\n")
while True:
    print("1.Faculties handled unique subjects\n2.Faculty members who are in service in the given period\n3.Exit")
    c = int(input("Enter your choice\n"))
    if c == 1:
        find_faculty_with_unique_subjects(faculty_members)
    elif c == 2:
        print("Enter the period (start_year-end_year):")
        period = input()
        print("Faculty members in service during the given period:")
        find_faculty_in_given_period(faculty_members, period)
    elif c == 3:
        print("Thank You")
        break
    else:
        print("Invalid Choice, Please enter correct choice")
