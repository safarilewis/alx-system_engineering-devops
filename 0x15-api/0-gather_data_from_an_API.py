#!/usr/bin/python3
"""
Returns info about an employee
"""
import json
import sys
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    r = requests.get(url + sys.argv[1])
    dict = json.loads(r.text)
    name = dict.get('name')
    resp = requests.get("https://jsonplaceholder.typicode.com/todos/" +
                            "?userId=" + sys.argv[1])
    todos =  json.loads(resp.text)
    tasks = len(todos)
    completed = [task for task in todos if task.get('completed')]
    done = len(completed)
    print("Employee {} is done with tasks({}/{})".format(name, done, tasks))
    for task in completed:
        print("\t", task.get('title'))
