#!/usr/bin/python3
'''
Returns information about a given
employee's TODO list progress.
Call the JSON placeholder REST api.
'''
import requests
import sys


if __name__ == "__main__":
    if sys.argv[1].isdigit():
        staff = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
        employee = staff.json()['name']
        user_id = staff.json()['id']
        todo_list = requests.get('https://jsonplaceholder.typicode.com/todos')
        done = []
        fin = total = 0
        for dct in todo_list.json():
            if dct['userId'] == user_id:
                if dct['completed'] == True:
                    done.append(dct['title'])
                    fin += 1
                total += 1
        print("Employee {} is done with tasks({}/{}):".format(employee, fin, total))
        for i in done:
            print("\t " + i)
