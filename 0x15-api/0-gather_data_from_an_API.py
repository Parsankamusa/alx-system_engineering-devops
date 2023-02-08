import requests

# The API endpoint to get the employee information
EMPLOYEE_API = "https://jsonplaceholder.typicode.com/users/{}"
# The API endpoint to get the TODO list of an employee
TODO_API = "https://jsonplaceholder.typicode.com/todos?userId={}"

def get_employee_name(employee_id):
    """Returns the name of the employee with the given ID"""
    response = requests.get(EMPLOYEE_API.format(employee_id))
    return response.json()["name"]

def get_todo_list(employee_id):
    """Returns the TODO list of the employee with the given ID"""
    response = requests.get(TODO_API.format(employee_id))
    return response.json()

def main(employee_id):
    """Displays the employee TODO list progress"""
    employee_name = get_employee_name(employee_id)
    todo_list = get_todo_list(employee_id)
    done_tasks = [task for task in todo_list if task["completed"]]
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{len(todo_list)}):")
    for task in done_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    # Example usage
    main(1)
