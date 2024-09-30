import pycamunda.task

# Set up the base URL for your Camunda REST API
base_url = 'http://localhost:8080/engine-rest'

# Create a GetList object to fetch tasks
get_tasks = pycamunda.task.GetList(url=base_url)

# Execute the request to fetch tasks
tasks = get_tasks()

# Print the fetched tasks
for task in tasks:
    print(f'Task ID: {task.id_}')
    print(f'Task Name: {task.name}')
    print(f'Assignee: {task.assignee}')
    print('-------------------')
