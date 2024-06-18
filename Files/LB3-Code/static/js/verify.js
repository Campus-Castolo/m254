document.getElementById("verificationForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var token = document.getElementById("token").value;
    verifyAccount(token);
});

function verifyAccount(token) {
    fetch("/verify/verify", {  // Adjusted endpoint to match the verify blueprint
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
}
