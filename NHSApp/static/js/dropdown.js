// NHS/NHSApp/static/js/dropdown.js start
$(document).ready(function(){
    console.log("dropdown.js loaded");
    $('#dropdownMenuButton1').click(function(){
        console.log("Button clicked!");
    });
    
    $('.dropdown-item').click(function(event){
        event.preventDefault();
        var selectedText = $(this).text();
        $('#dropdownMenuButton1').text(selectedText);
    });
});
// NHS/NHSApp/static/js/dropdown.js end