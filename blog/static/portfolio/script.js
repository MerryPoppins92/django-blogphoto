$(document).ready(function() { 
	$('h1').click(function(){

		$(this).css('background-color', '#ff0000');

	});

    $('.js--wp-1').waypoint(function(direction) {
    	$('.js--wp-1').addClass('animated fadeIn');
	}, {
		offset: '50%'
	});

    $('.js--wp-2').waypoint(function(direction) {
    	$('.js--wp-2').addClass('animated bounceInLeft');
	}, {
		offset: '50%'
	});	


    $('.js--wp-3').waypoint(function(direction) {
    	$('.js--wp-3').addClass('animated bounceInRight');
	}, {
		offset: '50%'
	});	

    $('.js--wp-4').waypoint(function(direction) {
    	$('.js--wp-4').addClass('animated bounceInUp');
	}, {
		offset: '50%'
	});

});

// $(document).ready(function() { backInLeft

// 	$('h1').click(function() {
// 		$(this).css('background-color', '#ff0000');
// 	});

// 	    /* For the sticky navigation */
//     $('.js--section-features').waypoint(function(direction) { /* arriver a ce point on lance le waypoint*/
//         if (direction == "down") { /* si la direction est vers le bas*/
//             $('nav').addClass('sticky'); /* on ajoute a nav la class sticky */
//         } else {
//             $('nav').removeClass('sticky');
//         }
//     }, {
//       offset: '60px;'
//     });

//     	/* Scroll buttons*/
//     $('.js--scroll-to-plans').click(function () { /* on selection js-- avec $ puis on definit l'action click*/
//        $('html, body').animate({scrollTop: $('.js--section-plans').offset().top}, 1000);
//     });

//     $('.js--scroll-to-start').click(function () {
//        $('html, body').animate({scrollTop: $('.js--section-features').offset().top}, 1000); 
//     });

//     /* Navigation scroll */
//     $(function() {
//       $('a[href*=\\#]:not([href=\\#])').click(function() {
//         if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
//           var target = $(this.hash);
//           target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
//           if (target.length) {
//             $('html,body').animate({
//               scrollTop: target.offset().top
//             }, 1000);
//             return false;
//           }
//         }
//       });
//     });

//     $('.js--wp-1').waypoint(function(direction) {
//     	$('.js--wp-1').addClass('animated fadeIn');
// 	}, {
// 		offset: '50%'
// 	});

// 	$('.js--wp-2').waypoint(function(direction) {
//     	$('.js--wp-2').addClass('animated fadeInUp');
// 	}, {
// 		offset: '50%'
// 	});

// 	$('.js--wp-3').waypoint(function(direction) {
//     	$('.js--wp-3').addClass('animated fadeIn');
// 	}, {
// 		offset: '50%'
// 	});

// 	$('.js--wp-4').waypoint(function(direction) {
//     	$('.js--wp-4').addClass('animated pulse');
// 	}, {
// 		offset: '50%'
// 	});
// });
