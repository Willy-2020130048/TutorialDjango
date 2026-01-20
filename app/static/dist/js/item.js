import { getCookie } from './utils.js';

const csrftoken = getCookie('csrftoken');

window.deleteItem = function(id) {
    if (!confirm("Yakin ingin menghapus item ini?")) return;

    fetch(`/item/delete/${id}`, {
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
            alert("Gagal menghapus item!");
        }
    })
    .catch(error => console.error("Error:", error));
};