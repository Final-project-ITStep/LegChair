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
})