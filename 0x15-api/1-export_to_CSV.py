#!/usr/bin/python3
"""Retrieve and display employee TODO list progress."""
import csv
import requests
import sys

API = "https://jsonplaceholder.typicode.com"


def get_employee_info(employee_id):
    response = requests.get(f"{API}/users/{employee_id}")
    if not response.ok:
        sys.exit()
    return response.json()


def get_employee_todos(employee_id):
    response = requests.get(f"{API}/todos?userId={employee_id}")
    if not response.ok:
        sys.exit()
    return response.json()


def export_to_csv(employee_id, employee_info, employee_todos):
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME",
                        "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in employee_todos:
            writer.writerow([employee_id, employee_info['username'],
                            todo['completed'], todo['title']])
    print(f"Data exported to {filename}")


def main():
    if len(sys.argv) != 2:
        sys.exit()

    employee_id = sys.argv[1]

    try:
        employee_id = int(employee_id)
    except ValueError:
        sys.exit()

    employee_info = get_employee_info(employee_id)
    employee_todos = get_employee_todos(employee_id)

    export_to_csv(employee_id, employee_info, employee_todos)


if __name__ == "__main__":
    main()
