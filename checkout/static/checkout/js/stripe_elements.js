// Process stripe payments
var stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
var clientSecret = $("#id_client_secret").text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: "#000",
        fontFamily: "'Helvetica Neue', Helvetica, sans-serif",
        "::placeholder": {
            color: "#aab7c4"
        },
        fontSize: "16px",
        fontSmoothing: "antialiased"
    },
    invalid: {
        color: "#dc3545",
        iconColor: "#dc3545"
    }
};
var card = elements.create("card");
card.mount("#card-element");

card.addEventListener("change", function(e) {
    var errorDiv = document.getElementById("card-errors");
    if (e.error) {
        var html = `
        <span role="alert">
        <i class="fa-regular fa-circle-xmark danger"></i>
        </span>
        <span>${e.error.message}</span>`;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = "";
    }
});

var form = document.getElementById("payment-form");

form.addEventListener("submit", function(ev) {
    ev.preventDefault();
    card.update({ "disabled": true});
    $("#submit-button").attr("disabled", true);
    $("#payment-form").fadeToggle(100);
    $("#loading-overlay").fadeToggle(100);

    var saveInfo = Boolean($("#id-save-info").attr("checked"));
    var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
    var postData = {
        "csrfmiddlewaretoken": csrfToken,
        "client_secret": clientSecret,
        "save_info": saveInfo
    }
    var url = "/checkout/cache_checkout_data/";

    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address:{
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.city_or_town.value),
                        state: $.trim(form.county.value),
                        country: $.trim(form.country.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address:{
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.city_or_town.value),
                    state: $.trim(form.county.value),
                    postal_code: $.trim(form.postcode.value),
                    country: $.trim(form.country.value),
                }
            }
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById("card-errors");
                var html = `
                    <span role="alert">
                    <i class="fa-regular fa-circle-xmark danger"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $("#payment-form").fadeToggle(100);
                $("#loading-overlay").fadeToggle(100);
                card.update({ "disabled": false});
                $("#submit-button").attr("disabled", false);
            } else {
                if (result.paymentIntent.status === "succeeded") {
                    form.submit();
                }
            }
        });
    }).fail(function() {
        location.reload();
    })    
})