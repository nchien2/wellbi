$(document).ready(function() {
    $('.like_button').click(function(ev){
        var id = $(ev.currentTarget).attr('data-id');
        var count = $(this)[0].textContent;
        if($(this)[0].classList.contains('upvote_button')){ 
            $(this)[0].innerHTML='<i class="bi bi-hand-thumbs-up-fill"></i> ' + (Number(count) + 1);
        }else{
            $(this)[0].innerHTML='<i class="bi bi-hand-thumbs-up"></i> ' + (Number(count) - 1);
        }

        $(this).toggleClass('upvote_button');
        $(this).toggleClass('downvote_button');
        $.get( "/forum/like/" + id, function( data ) {
        });

    });
});

$(document).ready(function() {
    $('.comment_like').click(function(ev){
        var id = $(ev.currentTarget).attr('data-id');
        var count = $(this)[0].textContent;
        console.log(count)
        if($(this)[0].classList.contains('upvote_button')){ 
            $(this)[0].innerHTML='<i class="bi bi-hand-thumbs-up-fill"></i> ' + (Number(count) + 1);
        }else{
            $(this)[0].innerHTML='<i class="bi bi-hand-thumbs-up"></i> ' + (Number(count) - 1);
        }
        $(this).toggleClass('upvote_button');
        $(this).toggleClass('downvote_button');
        $.get( "/forum/comment/like/" + id, function( data ) {

        });

    });
});