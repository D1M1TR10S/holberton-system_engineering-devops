#!/usr/bin/python3
'''
Returns information about a given
employee's TODO list progress.
Call the JSON placeholder REST api.
'''
import requests
from sys import argv


if __name__ == "__main__":
    if argv[1].isdigit():
        staff = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
        employee = staff.json().get('name')
        todo_list = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(argv[1])).json()
        done = []
        fin = 0
        for dct in todo_list:
            if dct.get('completed') is True:
                done.append(dct['title'])
                fin += 1
        print("Employee {} is done with tasks({}/{}):".format(employee, fin, len(todo_list)))
        for i in done:
            print("\t " + i)
