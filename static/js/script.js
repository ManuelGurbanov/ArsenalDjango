const { createApp } = Vue
//slider
createApp({
    data() {
        return {
            sponsors: ['static/inicio/img/esco.webp',
                'static/inicio/img/lanueva.webp',
                'static/inicio/img/chevallier.webp',
                'static/inicio/img/elsurco.webp',
                'static/inicio/img/multiled.webp',
                'static/inicio/img/secco.webp',
                'static/inicio/img/codo.webp',
                'static/inicio/img/cbse.webp']
        }
    }
}).mount('#slider')


//burguer menu
createApp({
    methods: {
        toggle_menu() {
            const menuIcon = this.$refs.burguerMenu
            const pageContainer = this.$refs.pageContainer
            pageContainer.classList.toggle('active');
            menuIcon.classList.toggle('active');
        }
    }
}).mount('#navMenu')

//muestra y esconde spinner
function mostrarContent() {
    setTimeout(() => {
        document.getElementById("spinner").style.display = "none";
        document.getElementById("content").style.display = "contents";
    }, 2000)
}

//expresiones regulares para nombres y mail
var regexNom = /^([A-Za-zÑñÁáÉéÍíÓóÚú]+['\-]{0,1}[A-Za-zÑñÁáÉéÍíÓóÚú]+)(\s+([A-Za-zÑñÁáÉéÍíÓóÚú]+['\-]{0,1}[A-Za-zÑñÁáÉéÍíÓóÚú]+))*$/;
var regexEmail = /^\S+@\S+\.\S+$/;

//validaciones formulario contacto
function sendForm() {

    var errorsAmount = 0;
    var errorMessages = [];
    var nombre = document.getElementById('fullName');
    var email = document.getElementById('email');
    var tel = document.getElementById('telefono');
    var msj = document.getElementById('mensaje');
    var fail = document.getElementById('fail');
    var success = document.getElementById('success');

    if (nombre.value === null || nombre.value.trim() === "") {
        errorMessages.push("Es necesario ingresar un nombre.");
        errorsAmount++;
    } else if (!regexNom.test(nombre.value)) {
        errorMessages.push("Debe ingresar caracteres válidos para su nombre.");
        errorsAmount++;
    }

    if (email.value === null || email.value.trim() === "") {
        errorMessages.push("Es necesario ingresar una dirección de correo.");
        errorsAmount++;
    } else if (!regexEmail.test(email.value)) {
        errorMessages.push("Debe ingresar un formato válido de email.");
        errorsAmount++;
    }

    if (tel.value === null || tel.value.trim() === "") {
        errorMessages.push("Es necesario ingresar un número de teléfono.");
        errorsAmount++;
    } else if (Number.isInteger(tel.value) || toString(tel.value).length > 10 || /^[0-9]/.test(toString(tel.value))) {
        errorMessages.push("Debe ingresar un formato válido de teléfono.");
        errorsAmount++;
    }

    if (msj.value === null || msj.value.trim() === "") {
        errorMessages.push("Es necesario ingresar un mensaje.");
        errorsAmount++;
    } else if (msj.value.length > 300) {
        errorMessages.push("Reduzca la cantidad de caracteres a 300, sea más conciso con su mensaje.");
        errorsAmount++;
    }

    fail.innerHTML = errorMessages.join(" ");

    if (errorsAmount === 0) {
        success.textContent = "Enviado con éxito!";
    }
}

//vue app para stats 
createApp({
    data() {
        return{
            equipos: [],
            arsenal: [],
            dataReady:false
        }
    },
    computed: {
        porcGanados() {
            return Math.round(this.arsenal.pg * 100 / this.arsenal.pj)
        },
        porcEmpates() {
            return Math.round(this.arsenal.pe * 100 / this.arsenal.pj)
        },
        porcPerdidos() {
            return Math.round(this.arsenal.pp * 100 / this.arsenal.pj)
        },
    },
    async mounted() {
        await fetch("https://sheetdb.io/api/v1/iytkr3w8su554?sort_by=pts&sort_order=desc", {
        "method": "GET",
        "headers": {
            "Authorization": "Bearer mz57b87ucpzxw97akldiiepf7x9yobnqitf5om80"
        }
    })
        .then(response => response.json())
        .then((data) => {
            this.equipos = data
            for(let element of this.equipos){
                if (element['eq']== "Arsenal Sarandí"){
                    this.arsenal = element
                    break
                }
            }
        }
        )
        .catch(err => {
            console.log(err);
        })
        .finally(()=>{
            this.dataReady = true;
            //this.$forceUpdate();
        });
    }
}).mount('#statsArsenal')

