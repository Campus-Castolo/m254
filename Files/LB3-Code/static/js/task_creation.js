document.addEventListener('DOMContentLoaded', function() {
    const createTaskForm = document.getElementById('taskForm');
    if (createTaskForm) {
        createTaskForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const taskName = document.getElementById('taskName').value;
            const taskDescription = document.getElementById('taskDescription').value;
            const startDate = document.getElementById('startDate').value;
            const assignUser = document.getElementById('assignUser').value;
            const createdBy = document.getElementById('createdBy').value;
            const priorityId = document.getElementById('priorityId').value;

            const formData = new URLSearchParams();
            formData.append('name', taskName);
            formData.append('description', taskDescription);
            formData.append('start_date', startDate);
            formData.append('assign_user', assignUser);
            formData.append('created_by', createdBy);
            formData.append('priority_id', priorityId);

            fetch('/create_task', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: formData.toString()
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }
});
