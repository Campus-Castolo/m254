$(document).ready(function() {
    $('#register-form').on('submit', function(e) {
        e.preventDefault();
        let username = $('#register-username').val();
        let email = $('#register-email').val();
        let password = $('#register-password').val();
        let confirmPassword = $('#register-confirm-password').val();

        $.ajax({
            url: '/api/register',  // Ensure the URL matches the registered blueprint route
            method: 'POST',
            contentType: 'application/x-www-form-urlencoded',  // Change Content-Type to application/x-www-form-urlencoded
            data: {
                username: username,
                email: email,
                password: password,
                confirm_password: confirmPassword
            },
            success: function(response) {
                $('#message').text(response.message).removeClass().addClass(response.status);
            },
            error: function(response) {
                $('#message').text(response.responseJSON.message).removeClass().addClass('text-danger');
            }
        });
    });
});
