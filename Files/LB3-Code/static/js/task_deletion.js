document.addEventListener('DOMContentLoaded', function() {
    const deleteTaskForm = document.getElementById('deleteTaskForm');
    if (deleteTaskForm) {
        deleteTaskForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const taskId = document.getElementById('taskId').value;

            const formData = new URLSearchParams();
            formData.append('id', taskId);

            fetch('/delete_task', {
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
