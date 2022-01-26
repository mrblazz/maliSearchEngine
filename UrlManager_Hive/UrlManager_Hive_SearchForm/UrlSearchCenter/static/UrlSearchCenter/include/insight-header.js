document.write('<div class="container container-white">'
+'		<div class="row">'
+'			<a href="insight-home-menu.html" class="portal-logo"><img src="img/portal-logo.png"></a>'
+'			<a class="insight-logo"><img src="img/insight-logo.png"></a>'
+'		</div>'
+'	</div>'
+'	<div class="container container-white">'
+'		<div class="row header-two">'
+'			<div class="navbar">'
+'				<div id="mynav" class="navbar-collapse collapse">'
+'								<ul class="nav navbar-nav">'

+'									<li style="border-right:1px solid #fff;"><a href="insight-home-menu.html"><img src="img/icon-home02.png"></a></li>'
/* +'									<li style="border-right:1px solid #fff;"><a href="profile-taxpayer-search.html" id="">Modules</a></li>' */
+'									<li style="border-right:1px solid #fff;"><a href="workspace.html">Workspace</a></li>'
/* +'									<li style="border-right:1px solid #fff;"><a href="mis1.html">MIS</a></li>' */
+'									<li style="border-right:1px solid #fff;"><a href="user-directory.html">Users</a></li>'
+'									<li style="border-right:1px solid #fff;"><a href="km-dashboard.html">Knowledge Hub</a></li>'
+'									<li style="border-right:1px solid #fff;"><a href="">Learning Hub</a></li>'
+'									<li style="border-right:1px solid #fff;"><a href="">Helpdesk</a></li>'
+'								</ul>'
+'								<div class="topnav" id="myTopnav">'
 +'                             <a href="javascript:void(0);" class="icon" onclick="topnav()">&#9776;</a>'
+'									<a href="insight-home-menu.html"><img src="img/icon-home.png"></a>'
+'									<a href="profile-taxpayer-search.html" id="">Modules</a>'
+'									<a href="workspace.html">Workspace</a>'
+'									<a href="mis.html">MIS</a>'
+'									<a href="user-directory.html">Users</a>'
+'									<a href="">Helpdesk</a>'
+'									<a href="">LMS</a>'
+'									<a href="km-dashboard.html">Knowledge Hub</a>'
+'								</div>'
+'								<ul class="six-icons02">'
+'									<li><a href="#"><img src="img/icon-pending02.png"><span class="showformula">Pending Tasks</span></a></li>'
+'									<li><a href="#"><img src="img/icon-message.png"><span class="showformula">Messages</span></a></li>'
+'									<li><a href="notifications.html"><img src="img/icon-bell.png"><span class="showformula">Notifications</span></a></li>'
+'									<li><a style="cursor:pointer" onclick="window.location.reload()"><img src="img/icon-refresh.png"><span class="showformula">Refresh</span></a></li>'
+'								</ul>'
+'								<ul class="six-iconssmall">'

+'									<li><a href="#"><img src="img/icon-refresh.png"><span class="showformula">Refresh</span></a></li>'
+'									<li class="dropdown more-icons">'
+'										<a class="dropdown-toggle" href="#" data-toggle="dropdown" aria-expanded="false"><img src="img/icon-more03.png"><span class="showformula">More</span></a>'
+'										<ul class="dropdown-menu">'
+'										<li><a href="#"><img src="img/icon-pending01.png"><span class="showformula">Pending Tasks</span></a></li>'
+'										<li><a href="#"><img src="img/icon-message01.png"><span class="showformula">Messages</span></a></li>'
+'										<li><a href="notifications.html"><img src="img/icon-bell01.png"><span class="showformula">Notifications</span></a></li>'
+'											<li class="more-icons-li">'
+'												<a href="doc-repo-main.html" class="more-rep"><span class="showformula">Doc Repository</span></a>'
+'											</li>'
+'											<li class="more-icons-li">'
+'												<a href="discus-main.html" class="more-forums"><span class="showformula">Discussion Forums</span></a>'
+'											</li>'
+'											<li class="more-icons-li">'
+'												<a href="wiki-main.html" class="more-wiki"><span class="showformula">Insight Wiki</span></a>'
+'											</li>'
+'											<li class="more-icons-li">'
+'												<a href="#" class="more-courses"><span class="showformula">LMS Courses</span></a>'
+'											</li>'
+'											<li class="more-icons-li">'
+'												<a href="#" class="more-suggest"><span class="showformula">FAQ</span></a>'
+'											</li>'
+'											<li class="more-icons-li">'
+'												<a href="aprobsol-02.html" class="more-feedback"><span class="showformula">QnA Forums</span></a>'
+'											</li>'
									
+'										</ul>'
+'							</div>'
+'			</div>'
+'		</div>'
+'	</div>'
+'	<div class="container">'
+'		<div class="row header-three" style="padding-top: 8px;">'
+'			<a class="welcome">Welcome,<span>Kartik Mehta, DIT (I&CI), Delhi</span></a>'
+'			<a href="" class="btn-logout button2" type="submit" style="margin: 0px 12px">Logout</a>'
+'		</div>'
+'	</div>');
var regex = new RegExp(/[0-9 a-z\-\_]+\.html/i);
var url=regex.exec(window.location.href)[0];
url=$('#screenHtmlURL1').val();
if (screen.width >= 740) {
var anchor=$('#mynav li > a[href="'+url+'"]');
anchor.parents('li').addClass('active'); 
}
if (screen.width < 740) {
var anchor=$('#myTopnav > a[href="'+url+'"]');
anchor.addClass('active'); 
}
function topnav() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}