"""
Script for importing students by course in Canvas.
"""
from keys import canvas_key
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




