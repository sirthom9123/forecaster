//  TODO: 
// Function for map location
// Function for save 

$(document).ready(function() {
    $('button').click( function() {
        var weatherData = new Array();
        $('#outputData div').each(function(span, p){
            weatherData[span]={
                "city" : $(span).find('span').val(), 
                "temperature" :$(span).find('span').val(), 
                "humidity" : $(p).find('p', this).val(), 
                "wind" : $(p).find('p', this).val(), 
                "description" : $(p).find('p', this).val()
            }    
        }); 
        alert(weatherData);
        $.ajax({
            type: "POST",
            url: "{% url 'create_forecast' %}",
            dataType: 'json',
            data: JSON.stringify({'weatherData': weatherData}),
            success: function(msg){
                alert(msg);
            }
        });
        return false;
    } );
});