$(document).ready(() => {

    // Page number for Menu
    let i = 0;
    let menuItem = $('li.nav-item');
    let page = parseInt($('#page-name').val());
    for (let nav of menuItem) {
        if (page === i) {
            $(nav).addClass('active');
        }
        i += 1;
    }

    //Check to see if the window is top if not then display button
    $(window).scroll(() => {
        if ($(this).scrollTop() > 200) {
            $('.back-to-top').addClass('active');
        } else {
            $('.back-to-top').removeClass('active');
        }
    });
    $('.back-to-top').click(() => {
        $('body,html').animate({scrollTop: 0}, 400);
        return false;
    });

    // Cart count
    let count = 4;
    $('.main_menu .cart i').addClass('g-count').attr('data-content', count);
    $('.shopping-cart-count span#c-count').text(count);
    // Delete cart item
    $('button.delete').click((e) => {
        console.log($(e.Target).parent().attr());
    });

    // Login and signup
    //$('#signup').on('click', (e) => {
    //    e.preventDefault();
    //    $('#modal-signup').modal('show');
    //});

})