$(document).ready(function(){
  $('.product-carousel').slick({
    // This shows how many images are displayd
    slidesToShow: 5,
    // How much they move with scroll
    slidesToScroll: 3,
    responsive: [
      {
        // breakpoint when display shows 1 item
        breakpoint: 992,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        }
      }
    ]
  });
});