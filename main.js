
//** Almacenar la datatable
let dataTable;

//** saber si la datatable está inicializada. 
//**es importante por que 
//**cuando necesitamos recrear una tabla en la cual hacemos lectura de datos 
//**se hace de manera dinamica y cuando queremos volver a crearla tenemos
//** que destruir.  por lo tanto esta variable nos ayuda en que no haya errores.
let dataTableInitialized = false;

const dataTableOptions = {
    //scrollX:"950px",
    columnDefs: [
        {className: "centered", targets: [0,2,3,4,5,6] },
        {orderable: false, target:[5,6]},
        {searchable: false, targets:[0,2,3,4,5,6]},
       //    {width: "50%", targets:[0]},
    ],
    pageLength: 3,
    destroy: true,
    language: {
        lengthMenu: "Mostrar _MENU_ registros por página",
        zeroRecords:"Ningún usuario encontrado",
        info: "Mostrando de _START_ a _END_ de un total de  _TOTAL_ registros",
        infoEmpty: "Ningún usuario encontrado",
        infoFiltered: "(filtrados desde _MAX_ registros totales)",
        search: "Buscar",
        loadingRecords: "Cargando...",
        paginate: {
            first:"Primero",
            last: "Último",
            next: "Siguiente",
            previous: "Anterior"
        }
    }
}




const listVentas= async() => {
    try {
        console.log("listVentas");
        const response = await fetch("consulta.php");
        console.log(response);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        console.log("adntes_del_json");
        const ventas = await response.json();
        console.log("depues_de_json");
        let content = '';
        ventas.forEach((venta, index) => {
            console.log(venta);
            let fecha = new Date(venta.exp.date);
            let dia = fecha.getDate();
            let mes = fecha.getMonth();
            let ano = fecha.getFullYear();
            let fechaEnString = `${dia}/${mes+1}/${ano}`;
            console.log(venta.exp);
            content +=`
                <tr>
                    <td>${index+1}</td>  
                    <td>${venta.name}</td>  
                    <td>${venta.company}</td>  
                    <td>${venta.plan}</td>  
                    <td>${venta.pin}</td>
                    <td>${fechaEnString}</td>
                    <td>${venta.po}</td>
                    <td>${venta.order}</td>
                    <td><i class="fa-solid fa-check" style="color:green;"></i></td>
                    <td>
                        <button class="btn btn-sm btn-primary"><i class="fa-solid fa-pencil"></i></button>
                        <button class="btn btn-sm btn-danger"><i class="fa-solid fa-trash"></i></button>
                    </td>
                </tr>`;
        });

        $("#tableBody_users").html(content);

    } catch (error) {
        console.error("Error fetching data:", error);
        alert("An error occurred while fetching data. Please try again later.");
    }
};

window.addEventListener("load", async() =>{
    await listVentas();
});
