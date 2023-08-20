function generateFields() {
            var candidateCount = document.getElementById("candidateCount").value;
            var candidateFieldsContainer = document.getElementById("candidateFields");
            candidateFieldsContainer.innerHTML = "";
            var form = document.getElementById('candidateForm');
            for (var i = 0; i < candidateCount; i++) {
                var inputField = document.createElement("input");
                inputField.type = "text";
                inputField.name = "candidate" + i;
                inputField.placeholder = "Candidate " + (i + 1) + " Name";
                inputField.className = "form-control candidate-field"; // Added "form-control" class
                candidateFieldsContainer.appendChild(inputField);
            }

            var hiddenInput = document.createElement('input');
            hiddenInput.type = 'hidden';
            hiddenInput.name = 'candidate_count';
            hiddenInput.value = `${candidateCount}`;

            form.appendChild(hiddenInput);
        }