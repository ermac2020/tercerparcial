$(document).ready(function ($) {
    'use strict';


/* ---------------------------------------------
     page  Prealoader
     --------------------------------------------- */
     $(window).on('load', function () {
        $("#loading-center-page").fadeOut();
        $("#loading-page").delay(400).fadeOut("slow");
    });




 /* ---------------------------------------------
     Sticky header
     --------------------------------------------- */
     $(window).on('scroll', function () {
        var scroll_top=$(window).scrollTop();

        if (scroll_top > 40){
            $('.navbar').addClass('sticky');

        }
        else{
          $('.navbar').removeClass('sticky');  
      }

  });

/*--------------------
Slick  JS
----------------------*/

$('.service-slider').slick({
  dots: true,
  padding: 0,
  slidesPerRow: 5,
  rows: 1,
  arrows: false,
  centerMode: true,
  margin: 20,
  slidesToShow:5,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll:3,
        infinite: true,

      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
  ]

});

$('.testimonial-slider').slick({
    dots: false,
    arrows: true,
    prevArrow: "<button type='button' class='slick-prev'><i class='dripicons-arrow-thin-right'></i></button>",
    nextArrow: "<button type='button' class='slick-next'><i class='dripicons-arrow-thin-left'></i></button>",
     centerMode: true,
    slidesToShow: 1,
    slidesToScroll: 1,
   cssEase: 'linear',

  
});
 
 
 
 
 
/* ---------------------------------------------
 Back top page scroll up
 --------------------------------------------- */


 $.scrollUp({
    scrollText: '<i class="dripicons-chevron-up"></i>',
    easingType: 'linear',
    scrollSpeed: 900,
    animation: 'fade'
});


/* ---------------------------------------------
 WoW plugin
 --------------------------------------------- */

 new WOW().init({
    mobile: true,
});

/* ---------------------------------------------
 Smooth scroll
 --------------------------------------------- */

 $('a.section-scroll[href*="#"]:not([href="#"])').on('click', function (event) {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') ||
        location.hostname == this.hostname) {

        var target = $(this.hash);
    target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
    
    if (target.length) {
            // Only prevent default if animation is actually gonna happen
        
            event.preventDefault();
            $('html,body').animate({
                scrollTop: target.offset().top
            }, 750);
            return false;
        }
    }

});



/*----------------------------------------
 Newsletter Subscribe
 --------------------------------------*/

 $(".subscribe-mail").ajaxChimp({
    callback: mailchimpCallRep,
    url: "mailchimp-post-url" //Replace this with your own mailchimp post URL. Just paste the url inside "".
});

 function mailchimpCallRep(resp) {
    if (resp.result === "success") {
        $(".sucess-message").html(resp.msg).fadeIn(1000);
        $(".error-message").fadeOut(500);
    } else if (resp.result === "error") {
        $(".error-message").html(resp.msg).fadeIn(1000);
    }
}

});