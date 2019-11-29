
document.addEventListener('DOMContentLoaded', function() {

    var options = {
         data: {
        "Apple": null,
        "Microsoft": null,
        "Google": 'https://placehold.it/250x250'
      },
      limit: 5,
    }


listaClientes();



////////////////////////////////////////////////////////////////////


});

    var clientes

    function listaClientes(){
        var c
        console.log('sdfgh')
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                clientes = JSON.parse(xhttp.responseText);
                     //for (var i = 0; i < clientes.length; i++) {
                     //   clientes[i].fields.nombre: null
                     // },


            }
        };
            xhttp.open("GET","/ord/", true);
            xhttp.send();
    }