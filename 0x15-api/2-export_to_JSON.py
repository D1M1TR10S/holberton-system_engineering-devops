#!/usr/bin/python3
'''
Retrieves information about a given
employee's To-do list progress through
RESTful API.
Exports this data into a JSON file
'''
if __name__ == "__main__":
    import collections
    import json
    import requests
    from sys import argv

    if argv[1].isdigit():
        employee = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'
            .format(argv[1])).json().get('username')
        todo_list = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(argv[1])).json()

        lst = []
        user_id = argv[1]
        dct = collections.OrderedDict()
        for obj in todo_list:
            dct["task"] = obj["title"]
            dct["completed"] = obj["completed"]
            dct["username"] = employee
            lst.append(dct)
        with open('{}.json'.format(argv[1]), 'w') as todos:
            json.dump({user_id: lst}, todos)
