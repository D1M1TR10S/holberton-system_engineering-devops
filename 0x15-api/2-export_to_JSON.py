#!/usr/bin/python3
'''
Retrieves information about a given
employee's To-do list progress through
RESTful API.
Exports this data into a JSON file
'''
import requests
from sys import argv
import json


if __name__ == "__main__":
    if argv[1].isdigit():
        employee = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'
            .format(argv[1])).json().get('name')
        todo_list = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(argv[1])).json()

        with open('{}.json'.format(argv[1]), 'w') as todos:
            dictus = {}
            lst = []
            info = {}
            for item in range(len(todo_list)):
                for do in todo_list:
                    info["task"] = do["title"]
                    info["completed"] = do["completed"]
                    info["username"] = do["username"]
                lst.append(info)
                info = {}
            dictus["{}".format(argv[1])] = lst
            json.dump(dictus, outfile)
