
    $('#carousel-example-generic').on('slide.bs.carousel', function() {
      if ($('.carousel-inner .item:last').hasClass('active')) {
         
        $('.carousel-inner .item:first').addClass('animated zoomInDown');
      } else {
        $('.item.active').next().addClass('animated zoomInDown');
      }
      $('.item.active').addClass('animated zoomOutDown');
    });

    $('#carousel-example-generic').on('slid.bs.carousel', function() {
      $('.item').removeClass('animated zoomInDown zoomOutDown')
    });

    $('.left').click(function() {
      if ($('.carousel-inner .item:first').hasClass('active')) {
        $('.carousel-inner .item:last').addClass('animated zoomInDown');
      } else {
        $('.item.active').prev().addClass('animated zoomInDown');
      }
    });

    $('.carousel-indicators > li').click(function() {
      $('.item').addClass('animated zoomInDown');
    }); 