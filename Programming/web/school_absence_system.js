const form = document.querySelector('form');
const tableBody = document.querySelector('#absence-table');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  
  const name = document.querySelector('#student-name').value;
  const date = document.querySelector('#date').value;
  const reason = document.querySelector('#reason').value;
  
  const newRow = document.createElement('tr');
  newRow.innerHTML = `
    <th scope="row">${tableBody.children.length + 1}</th>
    <td>${name}</td>
    <td>${date}</td>
    <td>${reason}</td>
  `;
  
  tableBody.appendChild(newRow);
  
  form.reset();
});
