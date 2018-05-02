#!/usr/bin/python3
'''
Retrieves information about all
employees and their To-do lists
through a RESTful API and then
Exports this data into a JSON file
'''
if __name__ == "__main__":
    import collections
    import json
    import requests
    from sys import argv

    all_employees = requests.get(
        'https://jsonplaceholder.typicode.com/users'
        ).json()
    dictionary = {}
    for employee in all_employees:
        todo_list = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(employee['id'])).json()

        user_id = employee['id']
        lst = []
        dct = collections.OrderedDict()
        for obj in todo_list:
            dct["username"] = employee["username"]
            dct["task"] = obj["title"]
            dct["completed"] = obj["completed"]
            lst.append(dict(dct))
        dictionary[user_id] = lst
    with open('todo_all_employees.json', 'w') as todos:
        json.dump(dictionary, todos)
