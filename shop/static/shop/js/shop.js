
// Add back to top functions to Project app

$('.btt-link').click(function(e) {
    window.scrollTo(0,0)
  })

  $('.btt-link').click(function(e) {
    window.scrollTo(0,0)
})


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