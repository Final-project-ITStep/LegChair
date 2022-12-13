const calculate = () => {
    var checkedCells = $('.check:checked');
    var totalPrice = 0;
    var selItemsList = '';
    for (var c of checkedCells) {
        totalPrice += parseFloat($(c).parent().parent().parent().find('h5.item-price').text());
        selItemsList += $(c).val() + ',';
    }
    selItemsList += totalPrice;
    // console.log(selItemsList);
    $('h4.item-total').text(`${totalPrice.toFixed(2)}`);
    $('#bill-btn').attr('href', `/orders/order/${selItemsList}`);
};

$(document).ready(() => {
    calculate();

    $('.check').click(() => {
        calculate();
    })

    $('button.btn-del').click((e) => {
        $.ajax({
            url: '/cart/ajax_cart_delete',
            data: `item=${e.target.value}`,
            success: (response) => {
                console.log(response.report);
                window.location = '/cart'
            }
        });
    })
})