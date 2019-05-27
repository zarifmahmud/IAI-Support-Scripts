"""
Script for importing students by course in Canvas.
"""
from keys import canvas_key
import csv
import requests


def course_students(course_id: int):
    """
    Takes in a course's ID, and returns a list of students in the course, containing dictionaries with their name and
    Quercus ID.
    """
    url = 'https://q.utoronto.ca/api/v1/courses/' + str(course_id) + '/students' + '?access_token=' + canvas_key
    r = requests.get(url)
    convert = r.json()
    trimmed_list = []
    for student in convert:
        trimmed_dict = {}
        trimmed_dict["sortable_name"] = student["sortable_name"]
        trimmed_dict["id"] = student["id"]
        trimmed_list.append(trimmed_dict)
    return trimmed_list


def student_list_to_csv(student_list, file_name: str):
    """
    Takes in list of students as input, and writes to a CSV file with given name.
    (If the file doesn't exist, it creates it). CSV file contains info on students.
    """
    file = file_name + '.csv'
    with open(file, mode='w') as student_file:
        student_writer = csv.writer(student_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for student in student_list:
            student_name = student["sortable_name"]
            split_name = student_name.split(", ")
            last_name, first_name = split_name[0], split_name[1]
            student_id = student["id"]
            student_writer.writerow([student_name, first_name, last_name, student_id])


def course_students_csv(course_id: int, file_name: str):
    """
    Takes in a the ID of a course as an int, and returns a CSV file with file_name as desired name,
    containing information about the students enrolled in the course:
    Student's full name, first name, last name, and Quercus ID.
    """
    student_list = course_students(course_id)
    student_list_to_csv(student_list, file_name)

