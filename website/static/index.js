function deleteNote(noteId){
    fetch('/delete-note',{
        method: 'POST',
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href = "/";
    });
}

const search = () => {
    const searchbox = document.getElementById("search-item").value.toUpperCase();
    const product = document.querySelectorAll(".product");
    const pname = document.getElementsByTagName("h2");

    for (let i = 0; i < pname.length; i++) {
        let match = product[i].getElementsByTagName('h2')[0];

        if (match) {
            let textvalue = match.textContent || match.innerHTML;

            if (textvalue.toUpperCase().indexOf(searchbox) > -1) {
                // Show product and retain its styles
                product[i].style.display = "flex";  // Set it back to flex instead of block
            } else {
                // Hide product
                product[i].style.display = "none";
            }
        }
    }
};

