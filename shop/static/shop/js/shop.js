// Local JS for shop sorting function
$('#sort-selector').change(function() {
    var selector = $(this)
    var currentUrl = new URL(window.location);

    var selectedVal = selector.val();
    if (selectedVal == "category_asc" | "category_desc") {
        if(selectedVal != "reset") {
            var sort = selectedVal.split("_")[0];
            var direction = selectedVal.split("_")[1];

            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.delete("sort", sort);
            currentUrl.searchParams.delete("direction", direction);

            window.location.replace(currentUrl);
        }
    } else {
        // Organise the direction of the results
        // Extra if/else statement as the name of the data being filtered has two '_'
        if(selectedVal != "reset") {
            if(selectedVal == 'friendly_name_asc') {
                var sort = selectedVal.slice(0, -4);
                var direction = selectedVal.split("_")[2];
            } else {
                var sort = selectedVal.slice(0, -5);
                var direction = selectedVal.split("_")[2];
            }

            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.delete("sort", sort);
            currentUrl.searchParams.delete("direction", direction);

            window.location.replace(currentUrl);
        }
    }
});

// Alter image input
$('#new-image').change(function () {
    var file = $('#new-image')[0].files[0];
    $('#filename').text(`Image will be set to ${file.name}`);
})

// Display price depending on selected size
// JS adapted from https://www.youtube.com/watch?v=m2UzB9JL--c
$("#id_selected_size").change(function() {

    var val = $(this).val();
    if (val == 'a5') {
        $('#price').html('£80')
    } else if (val == 'a4') {
        $('#price').html('£120')
    } else {
        $('#price').html()
    }
});