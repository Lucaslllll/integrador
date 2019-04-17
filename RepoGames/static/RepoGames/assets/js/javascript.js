$(window).scroll(function(){
	valor_atual = $(document).scrollTop(); 
	var div = $("#fixar");
	if (valor_atual >= 580){
		div.addClass("sticky-top");
	}
	else{
		div.removeClass("sticky-top");
	}
});