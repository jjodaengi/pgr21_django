$(document).ready(function() {

	/* 상단 메뉴 */
	$('.mm1').mouseenter(function() {
		$('#overDiv').removeClass().addClass('m1');
	});
	$('.mm2').mouseenter(function() {
		$('#overDiv').removeClass().addClass('m2');
	});
	$('.mm3').mouseenter(function() {
		$('#overDiv').removeClass().addClass('m3');
	});
	$('.mm4').mouseenter(function() {
		$('#overDiv').removeClass().addClass('m4');
	});
	$('.mm0, .mm5').mouseenter(function() {
		$('#overDiv').removeClass();
	});
	$('#mobileNav a.home').click(function() {
		$('#overDiv .menu1').toggle();
	});

});