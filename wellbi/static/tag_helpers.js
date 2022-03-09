
$(document).ready(function() {
    $('#add_tag').click(function(){
        var tag_div = document.getElementById('tags')
        var count_div = document.getElementById('count_div')
        const tag_field = document.createElement('input')
        const br = document.createElement('br')
        const new_count = Number(count_div.innerHTML) + 1

        tag_field.setAttribute('name', 'tags-' + new_count) 
        tag_field.setAttribute('class', 'form-control limit-input') 
        tag_div.appendChild(tag_field)
        tag_div.appendChild(br)

        if (new_count == 4){
            var button = document.getElementById('add_tag')
            button.remove()
        }
        count_div.innerHTML = new_count
    });
});

// $(document).ready(function() {
//     $('#remove_tag').click(function(){
//         var tag_div = document.getElementById('tags')
//         var count_div = document.getElementById('count_div')
//         const tag_field = document.createElement('input')
//         const br = document.createElement('br')
//         const new_count = Number(count_div.innerHTML) + 1

//         tag_field.setAttribute('name', 'tags-' + new_count) 
//         tag_div.appendChild(tag_field)
//         tag_div.appendChild(br)

//         if (new_count == 4){
//             var button = document.getElementById('add_tag')
//             button.remove()
//         }
//         count_div.innerHTML = new_count
//     });
// });