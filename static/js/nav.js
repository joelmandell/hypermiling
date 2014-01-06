$(document).ready(function () {

    //If-check för att se vilken sajt vi är på och markera aktiv sajt med att färga länken blå!
    if(document.location.href.indexOf("forum")!==-1)
    {
        $('#forum').css("background-color", "#2a89fc");
    } else if (document.location.href.indexOf("Review") !== -1) {
        $('#review').css("background-color", "#2a89fc");
    } else if (document.location.href.indexOf("Member") !== -1) {
        $('#member').css("background-color", "#2a89fc");
    } else {
        $('#home').css("background-color", "#2a89fc");
    }

    //Gör inte bara texten klickbar utan även så att när man klickar på "knappen" så skickas man dit!
    $("ul.links li").click(function (event) {
        event.stopPropagation();
        location.href=$(this).find("a").attr("href");
    })

});

