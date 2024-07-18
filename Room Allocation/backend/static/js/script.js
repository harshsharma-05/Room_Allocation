document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    let formData = new FormData();
    formData.append('groupFile', document.getElementById('groupFile').files[0]);
    formData.append('hostelFile', document.getElementById('hostelFile').files[0]);
    
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        let resultDiv = document.getElementById('result');
        resultDiv.innerHTML = '<h2>Allocation Result:</h2>';
        data.forEach(result => {
            resultDiv.innerHTML += `<p>Group ID: ${result['Group ID']}, Hostel: ${result['Hostel Name']}, Room: ${result['Room Number']}, Members Allocated: ${result['Members Allocated']}</p>`;
        });
    })
    .catch(error => console.error('Error:', error));
});
