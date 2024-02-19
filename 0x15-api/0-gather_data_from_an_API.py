#!/usr/bin/python3
"""Retrieve and display employee TODO list progress."""
import requests
import sys

API = "https://jsonplaceholder.typicode.com"


def get_employee_info(employee_id):
    response = requests.get(f"{API}/users/{employee_id}")
    if not response.ok:
        sys.exit("Failed to retrieve employee information.")
    employee_info = response.json()
    return employee_info


def get_employee_todos(employee_id):
    response = requests.get(f"{API}/todos?userId={employee_id}")
    if not response.ok:
        sys.exit("Failed to retrieve employee TODO list.")
    todos = response.json()
    return todos


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 script.py <employee_id>")

    employee_id = sys.argv[1]
    employee_info = get_employee_info(employee_id)
    employee_todos = get_employee_todos(employee_id)

    completed_tasks = [todo for todo in employee_todos if todo['completed']]
    total_tasks = len(employee_todos)
    num_completed_tasks = len(completed_tasks)

    print(f"Employee {employee_info['name']}\
            is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    main()
