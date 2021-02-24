const mapForm = document.querySelector('#map-form')
const searchBtn = document.querySelector('#seacrhBtn')
const weatherData = document.querySelector('#weatherData')
const city = document.querySelector('#map')
const csrf = document.querySelector('csrfmiddlewaretoken')
const messages = document.querySelector('.message')
const saveData = document.querySelector('#saveData')	



const handleAlerts = (type, text) => {
	alertBox.innerHTML = `<div class="alert alert-${type}" role="alert">
							${text}
							</div>`
	
}
$(document).on('submit', mapForm, function(e) {
    $.ajax({
        type:'POST',
        url: "{% url 'home' %}",
        data: JSON.stringify({
            location:$('#map').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        }),
        success:function(response){
            document.getElementById("getWeather").hide();
            document.getElementById("weatherData").show();
        },
        error:function(error) {
            handleAlerts('danger', 'oops... something went wrong!')
            setTimeout(() => {
                alertBox.innerHTML = '';
                mapForm.innerHTML = '';
            }, 5000)
        }
    });
});
