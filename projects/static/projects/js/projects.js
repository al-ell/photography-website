// Local JS file
// From https://fancyapps.com/fancybox/
Fancybox.bind('[data-fancybox]', {
  compact: false,
  idle: false,
  dragToClose: false,
  commonCaption: true,

  Images: {
    zoom: false,
  },
  showClass: 'f-fadeIn',

  Toolbar: {
    absolute: false,
    display: {
      left: ['close', 'thumbs', 'fullscreen'],
      middle: [],
      right: [],
    },
  },
  tpl: {
    main: `<div class="fancybox__container" role="dialog" aria-modal="true" aria-label="{{MODAL}}" tabindex="-1">
          <div class="fancybox__backdrop"></div>
          <div class="fancybox__carousel"></div>
          <div class="fancybox__caption"></div>
          <div class="fancybox__toolbar"></div>
          <div class="fancybox__footer"></div>
          </div>`,
  },
});


// Add back to top functions to Project app
$('.btt-link').click(function(e) {
  window.scrollTo(0,0)
})