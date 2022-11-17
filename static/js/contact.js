$(document).ready(function(){
    
    (function($) {
        "use strict";

    
        jQuery.validator.addMethod('answercheck', function (value, element) {
            return this.optional(element) || /^\bcat\b$/.test(value)
        }, "type the correct answer -_-");

        // validate contactForm form
        $(function() {
            $('#contactForm').validate({
                rules: {
                    name: { required: true, minlength: 2 },
                    subject: { required: true, minlength: 5 },
                    number: { required: true, minlength: 5 },
                    email: { required: true, email: true },
                    message: { required: true, minlength: 20 }
                },
                messages: {
                    name: {
                        required: "у вас же є <strong>Ім\'я</strong>, чи не так?",
                        minlength: "ім\'я повинo містити більше <strong>2</strong> символів"
                    },
                    subject: {
                        required: "у вас же є Тема повідомлення, чи не так?",
                        minlength: "тема повідомлення повина містити більше <strong>5</strong> символів"
                    },
                    number: {
                        required: "come on, you have a number, don't you?",
                        minlength: "your Number must consist of at least 5 characters"
                    },
                    email: {
                        required: "намає E-mail - не буде Повідомлення"
                    },
                    message: {
                        required: "ммм..., вам потрібно написати щось, щоби надіслати повідомлення.",
                        minlength: "це все? дійсно!?"
                    }
                }
            })
        })
        
    })(jQuery)
})