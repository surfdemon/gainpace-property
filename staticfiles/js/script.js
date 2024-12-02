document.addEventListener('DOMContentLoaded', () =>{
    console.log('Page Loaded');
    setTimeout(() => {
        var messages = document.querySelectorAll('.alert');
        messages.forEach((message) => {
            message.style.display = 'none';
        });
    }, 10000);
});