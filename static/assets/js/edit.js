/* global $*/

$(document).ready(function() {
	/*navbar*/
	$("#toolboxAddNav").click(function() {
		$("#canvasNavBar").after("<nav id=\"siteNav\" class=\"navbar navbar-default \" role=\"navigation\"><div ><!-- Logo and responsive toggle --><div class=\"navbar-header\"><button type=\"button\" class=\"navbar-toggle\" data-toggle=\"collapse\" data-target=\"#navbar\"><span class=\"sr-only\">Toggle navigation</span><span class=\"icon-bar\"></span><span class=\"icon-bar\"></span><span class=\"icon-bar\"></span></button><a id=\"navTitle\" class=\"navbar-brand\" href=\"#\"><i class=\"fa fa-tree\"></i>Organization</a></div><!-- Navbar links --><div class=\"collapse navbar-collapse\" id=\"navbar\"><ul class=\"nav navbar-nav navbar-right\"><li ><a href=\"#\"id=\"navItem1\">Item 1</a></li><li ><a href=\"#\"id=\"navItem2\">Item 2</a></li><li ><a href=\"#\"id=\"navItem3\">Item 3</a></li><li><a class=\"btn-primary\"id=\"navButton\" href=\"\">Button 1</a></li></ul></div><!-- /.navbar-collapse --></div><!-- /.container --></nav>");
		$("#toolboxAddNav").remove();
	});
	$("#tbNavApply").click(function() {
		$("#navTitle").text(($("#tbNavTitle").val()));
		$("#navItem1").text(($("#tbNavItem1").val()));
		$("#navItem2").text(($("#tbNavItem2").val()));
		$("#navItem3").text(($("#tbNavItem3").val()));
		$("#navButton").text(($("#tbNavButton").val()));
	});
	/*end navbar*/
	/*Title*/
	$("#toolboxAddTitle").click(function() {
		$("#canvasTitle").after("<div class=\"jumbotron\"><h1 id=\"titleTitle\">Organization</h1><h3 id=\"titleSubtitle\">Optional moto</h3></div>");
		$("#toolboxAddTitle").remove();
	});
	$("#tbTitleApply").click(function() {
		$("#titleTitle").text(($("#tbTitleTitle").val()));
		$("#titleSubtitle").text(($("#tbTitleSubtitle").val()));
	});
	/*end title*/
	/*add news card*/
	$("#toolboxAddNewsCard").click(function(){
		alert("fucking hell");
		$("#tbNewsCardToggle").removeClass("collapse") ;
		$("#canvasNews").after("<h1>Dick</h1>") ;
	});
	/*end news card*/
	/*contact*/
	$("#toolboxAddContact").click(function() {
	    $("#canvasContact").after("<div class=\"jumbotron\"><a id=\"contactFacebook\" href=\"#\">Facebook</a></div>");
	    $("#toolboxAddContact").remove();
	});
	$("#tbContactApply").click(function(){
		$("#tbContactEmail").text(($("#tbContactEmail").val()));
		$("#tbContactPhone").text(($("#tbContactNumber").val()));
		$("#contactFacebook").attr("href",($("#tbContactFacebook").val()));
		$("#tbContactEmail").text(($("#tbContactTwitter").val()));
		$("#tbContactEmail").text(($("#tbContactInstagram").val()));
		$("#tbContactEmail").text(($("#tbContactGithub").val()));
		$("#tbContactEmail").text(($("#tbContactWebsite").val()));
	})
	/*end contact*/
	/*More Less Toggle*/
	$("#tbNavToggle").click(function() {
		if ($("#tbNavToggle").text() == "More") {
			$("#tbNavToggle").text("Less");
		} else {
			$("#tbNavToggle").text("More");
		}
	});
	$("#tbTitleToggle").click(function() {
		if ($("#tbTitleToggle").text() == "More") {
			$("#tbTitleToggle").text("Less");
		} else {
			$("#tbTitleToggle").text("More");
		}
	});
	/* end More Less Toggle*/
});
