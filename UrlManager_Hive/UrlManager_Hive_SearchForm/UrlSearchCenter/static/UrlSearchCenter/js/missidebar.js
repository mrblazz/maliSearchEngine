document.write('<div class="side-bar-title"><a>Module</a></div>'
+'<ul class="nav nav-tabs">'
+'<div class="mydiv">'
+'<h4 class="panel-title">'
+'<a>Taxpayer Verification</a>'
+'</h4>'
+'</div>'
+'<div class="mydiv02">'
+'</div>'
+'<div class="mydiv">'
+'<h4 class="panel-title">'
+'<a>Deductor Verification</a>'
+'</h4>'
+'</div>'
+'<div class="mydiv02">'
+'</div>'
+'<div class="mydiv">'
+'<h4 class="panel-title">'
+'<a>Reporting Compliance Management</a>'
+'</h4>'
+'</div>'
+'<div class="mydiv02">'
+'							</div>'
+'							<div class="mydiv">'
+'								<h4 class="panel-title">'
+'									<a>Group Verification</a>'
+'								</h4>'
+'							</div>'
+'							<div class="mydiv02">'
+'						</div>'
+'							<div class="mydiv">'
+'								<h4 class="panel-title">'
+'									<a>Data Processing Verification</a>'
+'								</h4>'
+'							</div>'
+'							<div class="mydiv02">'
+'								</div>'
+'							<div class="mydiv">'
+'							<h4 class="panel-title">'
+'								<a>Insight Hub</a>'
+'							</h4>'
+'						</div>'
+'<div class="mydiv02">'
+'						</div>'
+'							<div class="mydiv">'
+'								<h4 class="panel-title">'
+'									<a>CMCPC</a>'
+'								</h4>'
+'							</div>'
+'							<div class="mydiv02">'
+'						</div>'
+'							<div class="mydiv">'
+'								<h4 class="panel-title">'
+'									<a>INTRAC</a>'
+'								</h4>'
+'							</div>'
+'							<div class="mydiv02">'								
+'							</div>');					
var regex = new RegExp(/[0-9 a-z\-\_]+\.html/i);
var url=regex.exec(window.location.href)[0];
url=$('#screenHtmlURL').val();
var anchor=$('.side-bar li > a[href="'+url+'"]');
anchor.parents('li').addClass('active'); 
var divFirst=$(anchor.parents('div')[0])
$(anchor.parents('div')[0]).addClass('in');
divFirst.parent().prev().find('a').removeClass('collapsed')
$(document).ready(function() {
	
 document.getElementById("scrolloff").style.display = "none";
	document.getElementById("scrollon").style.display = "block";
})
function openNav() {
if (screen.width >= 993) {
    document.getElementById("mySidenav").style.width = "18.5%";
	document.getElementById("main").style.width = "78%";
}
if (screen.width < 993) {
    document.getElementById("mySidenav").style.width = "42%";
	document.getElementById("main").style.width = "95%";
}
if (screen.width < 420) {
    document.getElementById("mySidenav").style.width = "75%";
}
	document.getElementById("scrollon").style.display = "none";
	document.getElementById("scrolloff").style.display = "block";
	document.getElementById("mySidenav").style.overflow = "visible";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
	if (screen.width >= 993) {
   document.getElementById("main").style.width = "95%";
  }
   document.getElementById("scrolloff").style.display = "none";
	document.getElementById("scrollon").style.display = "block";
	document.getElementById("mySidenav").style.overflow = "hidden";
}

var sidebarheight = document.getElementById('mySidenav').offsetHeight;
$('.wholewrap').css('min-height', sidebarheight);
