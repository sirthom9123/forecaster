const mapForm = document.querySelector('#map-form')
const searchBtn = document.querySelector('#seacrhBtn')
const weatherData = document.querySelector('#weatherData')
const city = document.querySelector('#map')
const csrf = document.querySelector('csrfmiddlewaretoken')
const messages = document.querySelector('.message')
const saveData = document.querySelector('#saveData')	
const alertBox = document.querySelector('#messages')



const handleAlerts = (type, text) => {
	alertBox.innerHTML = `<div class="alert alert-${type}" role="alert">${text}</div>`
	
}
$(document).on('submit', mapForm, function(e) {
    // e.preventDefault();
    $.ajax({
        type:'POST',
        url: "{% url 'home' %}",
        data: JSON.stringify({
            location:$('#map').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        }),
        success:function(response){
            $("getWeather").hide();
            $("weatherData").show();
        },
        error:function(error) {
            handleAlerts('danger', 'oops... something went wrong!')
            setTimeout(() => {
                alertBox.innerHTML = '';
            }, 5000)
        }
    });
});

$(document).on('click', saveData, function(e) {
    $.ajax({
        type:'POST',
        url: "{% url 'home' %}",
        data: JSON.stringify({
            hourly:$('#hourly').val(),
            icon:$('#img_icon').val(),
            temperature:$('#temp').val(),
            wind:$('#wind').val(),
            description:$('#desc').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        }),
        success:function(response){
            $("container").reset();
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
