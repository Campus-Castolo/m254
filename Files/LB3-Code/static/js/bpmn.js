// In register.js
$.ajax({
    url: '/start-account-creation',  // Adjusted URL
    method: 'POST',
    contentType: 'application/x-www-form-urlencoded',
    data: {
        username: username,
        email: email,
        password: password,
        confirm_password: confirmPassword
    },
    success: function(response) {
        $('#message').text(response.message).removeClass().addClass(response.status);
        console.log("Registration response:", response);
    },
    error: function(response) {
        $('#message').text(response.responseJSON.message).removeClass().addClass('text-danger');
        console.log("Registration error:", response);
    }
});

// In verify.js
fetch("/start-email-verification", {  // Adjusted endpoint
    method: "POST",
    body: new URLSearchParams({
        token: token
    }),
    headers: {
        "Content-Type": "application/x-www-form-urlencoded"
    }
})
.then(response => response.json())
.then(data => {
    alert(data.message);
    if (data.status === "text-success") {
        // Account verified successfully, redirect or show success message
    }
})
.catch(error => {
    console.error("Error:", error);
});
