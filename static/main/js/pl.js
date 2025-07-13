const selected = document.getElementById('selected');
const options = document.getElementById('options');

selected.addEventListener('click', () => {
  options.style.display = options.style.display === 'block' ? 'none' : 'block';
  inputField.focus();
});

options.querySelectorAll('.option').forEach(opt => {
  opt.addEventListener('mousedown', () => {
    selected.textContent = opt.textContent;
    selected.dataset.value = opt.dataset.value;
    options.style.display = 'none';
    restartTest(false);
  });
});

document.addEventListener('click', e => {
  if (!document.getElementById('programmingLanguage').contains(e.target)) {
    options.style.display = 'none';
    inputField.focus();
  }
});