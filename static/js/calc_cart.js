const calculate = () => {
    var page_id = $('#page_id').val().substring(6);
    var totalPrice = 0;
    var selItemsList = '';
    if (page_id !== 'wish') {
        for (var c of $('.check:checked')) {
            totalPrice += parseFloat($(c).parent().parent().parent().find('h5.item-price').text());
            selItemsList += $(c).val() + ',';
        }
        selItemsList += totalPrice;
        $('#bill-btn').attr('href', `/orders/order/${selItemsList}`);
    } else {
        for (var c of $('h5.item-price')) {
            totalPrice += parseFloat($(c).text());
        }
    }
    // console.log(selItemsList);
    $('h4.item-total').text(`${totalPrice.toFixed(2)}`);
};

$(document).ready(() => {
    calculate();

    $('.check').click(() => {
        calculate();
    })
    // Delete item from Cart/Wish List
    $('button.btn-del').click((e) => {
        $.ajax({
            url: '/cart/ajax_cart_delete',
            data: `item=${e.currentTarget.value}`,
            success: (data) => {
                console.log(data.report);
                window.location = $('#page_id').val().substring(6) == 'wish' ? '/cart/wish' : '/cart';
            }
        });
    })
    // Add wishes to Cart
    $('button.btn-cart').click((e) => {
        $.ajax({
            url: '/cart/ajax_wish_update',
            data: `item=${e.currentTarget.value}`,
            success: (data) => {
                console.log(data.report);
                window.location = '/cart/wish';
            }
        });
    })
})