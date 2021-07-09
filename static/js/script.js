$(document).ready(function(){
    $('select').formSelect();
    $(".sidenav").sidenav({edge: "right"});
    $('.tabs').tabs();
    $('.modal').modal();
    $('.carousel.carousel-slider').carousel({
      fullWidth: true
    });
    setInterval(function() {
        $('#auto-slide').carousel('next');
      }, 3000);  
  });
