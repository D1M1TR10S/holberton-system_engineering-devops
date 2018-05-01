#!/usr/bin/python3
'''
Retrieves information about a given
employee's To-do list progress.
Exports this data into a CSV file
'''
import requests
from sys import argv
import csv


if __name__ == "__main__":
    if argv[1].isdigit():
        user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'
            .format(argv[1])).json()
        employee = user.get('name')
        todo_list = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(argv[1])).json()

        with open('{}.csv'.format(argv[1]), 'w') as todos:
            fieldnames = ["userId", "username", "completed", "title"]
            writer = csv.DictWriter(todos, fieldnames=fieldnames,
                                    delimiter=',', quoting=csv.QUOTE_ALL,
                                    extrasaction='ignore')
            
            for dct in todo_list:
                dct['username'] = employee
                writer.writerow(dct)
