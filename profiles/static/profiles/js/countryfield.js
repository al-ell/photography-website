// Local JS for profile app
let countrySelected = $('#id_default_country').val();
        if(!countrySelected) {
            $('#id_default_country').css('color', '#495057');
        }
        $('#id_default_country').change(function() {
            countrySelected = $(this).val();
            if(!countrySelected) {
                $(this).css('color', '#495057');
            } else {
                $('#id_default_country').css('color', '#000');
            }
        });