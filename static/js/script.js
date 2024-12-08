document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById('fileUploadForm');
    const fileInputs = document.querySelectorAll('input[type="file"]');
    const errorContainer = document.createElement('div');
    errorContainer.className = 'alert alert-danger mt-3 d-none';
    form.appendChild(errorContainer);

    form.addEventListener('submit', function (event) {
        let valid = true;
        errorContainer.classList.add('d-none');
        errorContainer.textContent = ''; // Clear any previous error messages

        fileInputs.forEach(input => {
            const file = input.files[0];
            if (!file || !file.name.toLowerCase().endsWith('.xlsx')) {
                valid = false;
                input.classList.add('is-invalid');
            } else {
                input.classList.remove('is-invalid');
                input.classList.add('is-valid');
            }
        });

        if (!valid) {
            event.preventDefault();
            event.stopPropagation();
            errorContainer.textContent = 'Please upload valid Excel files (.xlsx only).';
            errorContainer.classList.remove('d-none');
        }

        form.classList.add('was-validated');
    });
});
