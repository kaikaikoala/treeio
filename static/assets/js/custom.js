$(document).ready(function(){
	$("#btn1").click(function(){
		$("#navbarTitle").text( ($("#navTitle").val() ) ) ;
		$("#navItem1").text( ($("#item1").val() )) ;
		$("#navItem2").text( ($("#item2").val() )) ;
		$("#navItem3").text( ($("#item3").val() )) ;
		$("#navItem4").text( ($("#item4").val() )) ;
	});

	$("#btn2").click(function(){
		$("#jumboh1").text( ($("#jumboTitle").val() ));
		$("#jumbop").text( ($("#jumboSub").val() ));

	});

});
