document.addEventListener("DOMContentLoaded", init);
const URL_API = "http://localhost:3000/api/"


function init() {
    search()
}

async function search(){
    const url = URL_API + 'customers'
    const response = await fetch(url, {
        "method": 'GET',
        "headers": {
            "Content-Type": 'application/json'
        }
    })
    const resultado = await response.json();

    console.log(resultado)

    const row = `<tr>
    <td>Cecilia Moctezuma</td>
    <td>Francisco Chang</td>
    <td>cmocfchange@gmail.com</td>
    <td>8055485161</td>
    <td>
        <a href="#" class="btnedit">Editar</a>
        <a href="#" class="btnedelete">Eliminar</a>
    </td>
  </tr>`

  document.querySelector('#customers > tbody').outerHTML = row
}

