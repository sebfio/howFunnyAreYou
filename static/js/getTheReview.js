$(function() {
    $('button').click(function() {
        $.ajax({
            url: "/updateResult",
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                var res = JSON.parse(response);
                $("#yelpPercent").html(res['yelp'] + "%" );
                $("#normFunnyPercent").html(res['norm'] + "%");
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
