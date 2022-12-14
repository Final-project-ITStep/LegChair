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
    var user_id = $('#user_id').val();
    if (user_id !== 'None') {
        var class_paste = ['.shopping-cart', '.shopping-wish'];
        $.ajax({
            url: '/cart/ajax_cart_display',
            data: `uid=${user_id}`,
            success: (data) => {
                for (var i = 0; i < 2; i++) {
                    $(class_paste[i]).find('.p-count').text(data.count[i]);
                    $(class_paste[i]).find('.p-amount').text(data.amount[i]);
                    $('.' + class_paste[i].substring(10) + ' i').addClass('g-count').attr('data-content', data.count[i]);
                }
            }
        });
    }
    
    // Add cart item
    $('.cart-wish button').click((e) => {
        var cart_wish = $(e.currentTarget).attr('class').split(' ')[0];
        var product_id = $(e.currentTarget).parent().attr('id');
        var user_id = $('#user_id').val();
        // console.log('chair - ' + cart_wish + '-' + product_id + '-' + user_id);
        if (user_id === 'None') {
            $('#regModal').modal('show');
        } else {
            $.ajax({
                url: '/cart/ajax_cart',
                data: `uid=${user_id}&pid=${product_id}&sid=${cart_wish}`,
                success: (data) => {
                    var what_to_add = cart_wish === 'add_cart' ? 0 : 1
                    var class_paste = cart_wish === 'add_cart' ? '.shopping-cart' : '.shopping-wish';
                    $(class_paste).find('.p-count').text(data.count[what_to_add]);
                    $(class_paste).find('.p-amount').text(data.amount[what_to_add]);
                    $('.' + class_paste.substring(10) + ' i.g-count').attr('data-content', data.count[what_to_add]);
                    $('#myToast').toast('show').toast({delay: 30000}).find('span').text(' Товар додано!');
                }
            });
        }
    })

    // Delete cart item
    $('button.delete').click((e) => {
        console.log(e.target.id);
        $(e.target).parent().remove();
    });

    // Calculate pre-order

})