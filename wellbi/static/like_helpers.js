$(document).ready(function() {
    $('.like_button').click(function(ev){
        var id = $(ev.currentTarget).attr('data-id');
        countEle = $(ev.currentTarget)[0].nextSibling
        if($(this)[0].classList.contains('upvote_button')){
            countEle.nodeValue = Number(countEle.nodeValue) + 1
            $(this)[0].textContent='Unlike'
        }else{
            countEle.nodeValue = Number(countEle.nodeValue) - 1
            $(this)[0].textContent='Like'
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
        countEle = $(ev.currentTarget)[0].nextSibling
        if($(this)[0].classList.contains('upvote_button')){
            countEle.nodeValue = Number(countEle.nodeValue) + 1
            $(this)[0].textContent='Unlike'
        }else{
            countEle.nodeValue = Number(countEle.nodeValue) - 1
            $(this)[0].textContent='Like'
        }

        $(this).toggleClass('upvote_button');
        $(this).toggleClass('downvote_button');
        $.get( "/forum/comment/like/" + id, function( data ) {

        });

    });
});