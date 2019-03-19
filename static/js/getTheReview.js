$(function() {
    $('button').click(function() {
        $.ajax({
            url: "/updateResult",
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                var res = JSON.parse(response);
                $("#yelpPercent").html(res['yelp'].toFixed(4) + "%" );
                $("#normFunnyPercent").html(res['norm'].toFixed(4) + "%");
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
