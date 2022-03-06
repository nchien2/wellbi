$(document).ready(function() {
    $('.like_button').click(function(ev){
        var id = $(ev.currentTarget).attr('data-id');
        $(this).toggleClass('upvote_button');
        $(this).toggleClass('downvote_button');
        $.get( "/forum/like/" + id, function( data ) {
            window.location.reload();
        });

    });
});

$(document).ready(function() {
    $('.comment_like').click(function(ev){
        var id = $(ev.currentTarget).attr('data-id');
        // var index = $(ev.currentTarget).attr('data-index');
        $(this).toggleClass('upvote_button');
        $(this).toggleClass('downvote_button');
        $.get( "/forum/comment/like/" + id, function( data ) {
            window.location.reload();
        });

    });
});