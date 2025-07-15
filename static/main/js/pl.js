// Enhanced dropdown functionality
const selected = document.getElementById('selected');
const options = document.getElementById('options');

selected.addEventListener('click', () => {
    options.classList.toggle('show');
    selected.classList.toggle('active');
});

document.addEventListener('click', (e) => {
    if (!document.getElementById('programmingLanguage').contains(e.target)) {
        options.classList.remove('show');
        selected.classList.remove('active');
    }
});

// Option selection
document.querySelectorAll('.option').forEach(option => {
    option.addEventListener('click', () => {
        selected.textContent = option.textContent;
        options.classList.remove('show');
        selected.classList.remove('active');
        
        // Update selected state
        document.querySelectorAll('.option').forEach(opt => opt.classList.remove('selected'));
        option.classList.add('selected');
        localStorage.setItem('programming_language', option.dataset.value);

        restartTest(false);
    });
});

// Focus management
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        options.classList.remove('show');
        selected.classList.remove('active');
    }
});
