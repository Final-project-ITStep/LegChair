$(document).ready(() => {

    $('.cart-wish button').click((e) => {
        let cart_wish = $(e.target).attr('class');
        let user_id = $('#user_id').val();
        console.log('chair - ' + $(e.target).val());
        if (user_id === 'None' & cart_wish === 'add_wish') {
            $('#regModal').modal('show');
        }
    })
})