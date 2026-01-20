import { getCookie } from './utils.js';

const csrftoken = getCookie('csrftoken');

window.deleteCustomer = function(id) {
    if (!confirm("Yakin ingin menghapus customer ini?")) return;

    fetch(`/customer/delete/${id}`, {
        method: "POST",
        headers: {
            "X-CSRFToken": csrftoken,
            "X-Requested-With": "XMLHttpRequest"
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const row = document.getElementById(`row-${id}`);
            row.remove();
        } else {
            alert("Gagal menghapus customer!");
        }
    })
    .catch(error => console.error("Error:", error));
};