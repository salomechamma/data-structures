def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called "houses" that holds those names.

        ex. houses = set([ "Hufflepuff",
                    "Slytherin",
                    "Ravenclaw",
                    "Gryffindor",
                    "Dumbledore's Army"
            ])

    """

    houses = set()

    with open(filename) as text_file:
        for line in text_file:
            line = line.rstrip()
            line = line.split("|")
            houses.add(line[2])

    return houses


def sort_by_cohort(filename):
    """TODO: Sort students by cohort, skipping instructors.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name. Put ghosts into a separate list entitled "ghosts".
    Returns a list of these lists.

        ex. fall_15 = ["Colin Creevey", "Dennis Creevey", "Seamus Finnigan", ""Hermione Granger", ... ]
        ex. all_students = [["Colin Creevey", "Dennis Creevey", "Seamus Finnigan", ...],
        ["Lee Jordan", "Andrew Kirke", "Neville Longbottom", ...],
        ["Cormac McLaggen", "Parvati Patil", "Jimmy Peakes", ...], 
        ["Euan Abercrombie", "Katie Bell", "Lavender Brown", ...]]

    """

    all_students = []
    winter_16 = []
    spring_16 = []
    summer_16 = []
    fall_15 = []
    ghosts = []

    with open(filename) as text_file:
        for line in text_file:
            line = line.rstrip()
            line = line.split("|")
            student_name = line[0] + " " + line[1]
            cohort = line[4] 
            if cohort == "Winter 2016":
                winter_16.append(student_name)
            elif cohort == "Summer 2016":
                summer_16.append(student_name)
            elif cohort == "Spring 2016":
                spring_16.append(student_name)
            elif cohort == "Fall 2015":
                fall_15.append(student_name)
            elif cohort == "G":
                ghosts.append(student_name)

        all_students = [sorted(winter_16), sorted(spring_16), sorted(summer_16), sorted(fall_15),sorted(ghosts)]

    return all_students


def students_by_house(filename):
    """TODO: Sort students by house.


    Iterate over the data to create a list for each house, and sort students
    into their appropriate houses by last name. Sort ghosts into a list called "ghosts"
    and instructors into a list called "instructors".
    Return all lists in one list of lists.

        ex. gryffindor = ["Abercrombie", "Bell", "..." ]
        ex. ghosts = ["Baron", "Friar", "..."]
        ex. all_students = [ hufflepuff,
                    gryffindor,
                    ravenclaw,
                    slytherin,
                    dumbledores_army,
                    ghosts,
                    instructors
        ]

    """

    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    ravenclaw = []
    ghosts = []
    instructors = []

    with open(filename) as text_file:
        for line in text_file:
            line = line.rstrip()
            line = line.split("|")
            
            student_name = line[1]
            house = line[2]
            non_student = line[4]
            
            if house == "Slytherin":
                slytherin.append(student_name)
            elif house == "Gryffindor":
                gryffindor.append(student_name)
            elif house == "Dumbledore's Army":
                dumbledores_army.append(student_name)
            elif house == "Ravenclaw":
                ravenclaw.append(student_name)
            elif house == "Hufflepuff":
                hufflepuff.append(student_name)
            elif non_student == "G":
                ghosts.append(student_name)
            elif non_student == "I":
                instructors.append(student_name)

        all_students = [sorted(gryffindor), sorted(hufflepuff), sorted(slytherin), sorted(dumbledores_army),sorted(instructors), sorted(ravenclaw), sorted(ghosts)]

    return all_students


def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. student_list = [
                ("Euan Abercrombie", "Gryffindor", "McGonagall", "Summer 2016"),
                ("Katie Bell", "Gryffindor", "McGonagall", "Summer 2016"),
                # ...
            ]
    """

    student_list = []
    with open(filename) as text_file:
        for line in text_file:
            line = line.rstrip()
            line = line.split("|")
            student_list.append((line[0] + ' ' + line[1], line[2], line[3],line[4]))

    return student_list


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Use the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name from the command line, returns that
    student's cohort, or returns "Student not found." when appropriate. """

    name_of_student = raw_input("Enter first name and last name: ")

    for student in student_list:
        if student[0] == name_of_student:
            return student[3]

    return "Student not found."


##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student last names that have duplicates.

    Iterates over the data to find any last names that exist across all cohorts.
    Uses set operations (set math) to create a set of these names.
    NOTE: Do not include staff -- or do, if you want a greater challenge.

       ex. duplicate_names = set(["Weasley"])cohort

    """

    duplicate_names = set()

    # Code goes here

    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that prompts the user for a name via the command line
    and when given a name, print a statement of everyone in their house in their cohort.

    Use the list of tuples generated by all_students_tuple_list to make a small function
    that, when given a student's first and last name, print students that are in both
    that student's cohort and that student"s house.

    ex: Choose a student: Hermione Granger
        Hermione Granger was in house Gryffindor in the Fall 2015
        cohort.
        The following students are also in their house:
        Seamus Finnigan
        Angelina Johnson
        Harry Potter
        Ron Weasley
        Oliver Wood


    """

    # Code goes here

    return


#########################################################################################

# Here is some useful code to run these functions!

print unique_houses("cohort_data.txt")
print "\n"
print sort_by_cohort("cohort_data.txt")
print "\n"
print students_by_house("cohort_data.txt")
print "\n"
all_students_data = all_students_tuple_list("cohort_data.txt")
print all_students_data
print find_cohort_by_student_name(all_students_data)
# print find_name_duplicates("cohort_data.txt")
# find_house_members_by_student_name(all_students_data)
