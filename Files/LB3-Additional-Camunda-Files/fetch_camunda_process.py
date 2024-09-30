import pycamunda.processinst

# Set up the base URL for your Camunda REST API
base_url = 'http://localhost:8080/engine-rest'

# Create a GetList object to fetch process instances
get_processes = pycamunda.processinst.GetList(url=base_url)

# Execute the request to fetch process instances
process_instances = get_processes()

# Print the fetched process instances
for process_instance in process_instances:
    print(f'Process Instance ID: {process_instance.id_}')
    print(f'Definition ID: {process_instance.definition_id}')
    print(f'Business Key: {process_instance.business_key}')
    print(f'Case Instance ID: {process_instance.case_instance_id}')
    print(f'Suspended: {process_instance.suspended}')
    print('-------------------')
