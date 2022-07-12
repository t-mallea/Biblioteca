import {csrftoken} from "./cookiesDjango.js";


	fetch("/probando",{
            method:"GET",
            headers:{
                "X-CSRFToken":csrftoken,
                "X-Requestd-With":"XMLGttpRequest"//Con esto indicamos que es una peticion ajax
            }

    //Promesa de javascript
    }).then(
        function(response){
            return response.json();
            //console.log(response.data);
        }
    ).then(
        function(data){
            console.log(data.FondoIndex);

            
            document.body.style.backgroundImage = "url("+data.FondoIndex+")";
            //document.body.style.backgroundPosition = "center";
            document.body.style.backgroundRepeat = "no-repeat";
            document.body.style.backgroundSize = "100% 100%";
            document.body.style.backgroundAttachment = "fixed";

        }
    )
		
