/*global $, alert, console*/

$(function (){
    'use strict';

    // Add Scroll Top Button

    var btn = $('#button');

    $(window).scroll(function() {
        if ($(window).scrollTop() > 300) {
            btn.addClass('show');
        } else {
            btn.removeClass('show');
        }
    });

    btn.on('click', function(e) {
        e.preventDefault();
        $('html, body').animate({scrollTop:0}, '300');
    });


    //Navbar Sticky

    /*$(window).on('scroll',function(){
        if($(window).scrollTop()){
          $('#top-navbar').addClass('sticky');
        }else {
          $('#top-navbar').removeClass('sticky');
        }
      })

    //Links Add Active Class

    $('.links li a').click(function () {
        $(this).parent().addClass('active').siblings().removeClass('active');
    });

    //Smoth Scroll To Div

    $('.links li a').click(function () {
        $('html , body').animate({
            scrollTop: $('#' + $(this).data('value')).offset().top

        }, 1000);
    });*/



}); 