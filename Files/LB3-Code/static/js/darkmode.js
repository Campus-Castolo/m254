document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('toggleButton');

    function setCookie(name, value, days) {
        let expires = "";
        if (days) {
            const date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toUTCString();
        }
        document.cookie = name + "=" + (value || "") + expires + "; path=/";
    }

    function getCookie(name) {
        const nameEQ = name + "=";
        const ca = document.cookie.split(';');
        for(let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) == ' ') c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
        }
        return null;
    }

    toggleButton.addEventListener('click', function() {
        const html = document.documentElement;
        const currentTheme = html.getAttribute('data-bs-theme');

        if (currentTheme === 'dark') {
            html.setAttribute('data-bs-theme', 'light');
            setCookie('theme', 'light', 7);
            toggleButton.textContent = '🌙 Switch to Dark Mode';
        } else {
            html.setAttribute('data-bs-theme', 'dark');
            setCookie('theme', 'dark', 7);
            toggleButton.textContent = '🌕Switch to Light Mode';
        }
    });

    // Initialize the button text based on the current theme
    const html = document.documentElement;
    const currentTheme = html.getAttribute('data-bs-theme');
    if (currentTheme === 'dark') {
        toggleButton.textContent = 'Switch to Light Mode';
    } else {
        toggleButton.textContent = 'Switch to Dark Mode';
    }
});
