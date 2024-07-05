document.addEventListener('DOMContentLoaded', function() {
    const createTaskForm = document.getElementById('taskForm');
    createTaskForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const taskName = document.getElementById('taskName').value;
        const taskDescription = document.getElementById('taskDescription').value;
        const startDate = document.getElementById('startDate').value;
        const assignUser = document.getElementById('assignUser').value;
        const createdBy = document.getElementById('createdBy').value;
        const priorityId = document.getElementById('priorityId').value;

        fetch('/create_task', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 
                name: taskName,
                description: taskDescription,
                start_date: startDate,
                assign_user: assignUser,
                created_by: createdBy,
                priority_id: priorityId
            })
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    const deleteTaskForm = document.getElementById('deleteTaskForm');
    deleteTaskForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const taskId = document.getElementById('taskId').value;

        fetch('/delete_task', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id: taskId })
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
