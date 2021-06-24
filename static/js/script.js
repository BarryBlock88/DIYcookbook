$(document).ready(function(){
    $('select').formSelect();
    $(".sidenav").sidenav({edge: "right"});
    $('.tabs').tabs();
    $('.modal').modal();
    $('.pic').slick({
      arrows: false,
      fade: true,
      dots: false,
      accessibility: false,
      autoplay: true,
      speed: 3000,
      centerMode: true
    });
  });
