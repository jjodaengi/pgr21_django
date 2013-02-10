<div class='header'>

	<!-- header -->
	<div>
		<a id="logoimg" href="/"><h1>PGR21.com</h1></a>
	</div>


<?if(eregi("&no=", $_SERVER["REQUEST_URI"])){?>
<style>
@media all and (max-width: 1024px) {#floatingNav, #mbNav {<?=$btn_h?><?=$btn_v?>}}
</style>
<div id="floatingNav">
	<a class="navUp" title="스크롤 업 (단축키 : Alt + a )" accesskey="a"></a>
	<a class="navDown" title="스크롤 다운 (단축키 : Alt + z )" accesskey="z"></a>
</div>
<div id="mbNav">
	<div class="circle-container">
		<span id="mbBtn" class="circle">✖</span>
	</div>
	<ul class="items">
	  <li data-icon1="&#xe028;" class="navDown"></li>
	  <li data-icon1="&#xe021;" class="navRef"></li>
	  <li data-icon1="&#xe027;" class="navUp"></li>
	</ul>
</div>
<link rel="StyleSheet" HREF="/path<?=$btn_pos?>.css?v=0103" type="text/css">
<?}?>

	<div id="nav">
		<a href='/' class='wt mm0'>Home</a><span class="wt"> / </span>
		<A href="#" class='wt mm1'>게시판</a><span class="wt"> / </span>
		<A href="#" class='wt mm2'>Links</a><span class="wt"> / </span>
		<!-- <A href="#" class='wt mm3'>Teams</a><span class="wt"></span> -->
		<A href="#" class='wt mm4'>About</a><span class="wt"> / </span>
		<A href="/pb/viewscrap.php" class='wt mm5'>스크랩</a>
		<?if($member[no]) echo '<span class="wt"> / </span><A href="/setting.html" class="wt mm6">개인화</a>';?>
	</div>
	<div id="mobileNav">
		<a class="home">PGR21.com</a>
	</div>

	<div id="overDiv">

		<div class="menu1">
			<!-- 게시판 -->
			<ul>
<?
	if($member[level] == 1) echo '<li><a href="/pb/pb.php?id=master">운영진</a></li><li><a href="/pb/pb.php?id=deleted">삭게</a></li>';
?>
				<li><a href="/pb/pb.php?id=recommend">추천</a></li>
				<li><a href="/pb/pb.php?id=ace">ACE</a></li>
				<li><a href="/pb/pb.php?id=daku">전략</a></li>
				<li><a href="/pb/pb.php?id=newvod">게임리포트</a></li>
				<li><a href="/pb/pb.php?id=discuss">토론</a></li>
				<li><a href="/pb/pb.php?id=free2">게임</a></li>
				<li><a href="/pb/pb.php?id=freedom">자유</a></li>
				<li><a href="/pb/pb.php?id=bug">질문</a></li>
				<li><a href="/pb/pb.php?id=humor">유머</a></li>
				<li><a href="/pb/pb.php?id=bulpan">불판</a></li>
				<li><a href="/pb/pb.php?id=gamenews">게임뉴스</a></li>
				<li><a href="/pb/pb.php?id=interview">인터뷰</a></li>
				<li><a href="/pb/pb.php?id=series">연재</a></li>
				<li><a href="/pb/pb.php?id=proposal">건의</a></li>
				<li class="mobile"><a href="/pb/viewscrap.php">스크랩</a></li>
				<li class="mobile"><a href="/staff.html">운영진소개</a></li>
<?
	if($member[level] < 10) echo '<li class="mobile"><a href="/setting.html">개인화</a></li>';
?>
			</ul>
		</div>

		<div class="menu2">
			<!-- Links -->
			<ul>
				<li><a href="http://www.blizzard.co.kr/" target="_blank">블리자드</a></li>
				<!-- <li><a href="http://www.e-sports.or.kr/" target="_blank">KeSPA</a></li> -->
				<li><a href="http://www.ongamenet.com/" target="_blank">온게임넷</a></li>
				<li><a href="http://www.fomos.kr" target="_blank">포모스</a></li>
				<li><a href="http://www.ygosu.com" target="_blank">와이고수</a></li>
				<li><a href="http://nicegame.tv" target="_blank">나이스게임TV</a></li>
				<li><a href="http://esports.gomtv.com" target="_blank">곰TV e스포츠</a></li>
				<li><a href="http://eschosun.com" target="_blank">e스포츠조선</a></li>
				<li><a href="http://www.thisisgame.com/esports" target="_blank">디스이즈게임</a></li>
				<li><a href="http://esports.dailygame.co.kr" target="_blank">데일리e스포츠</a></li>
				<li><a href="http://esports.inven.co.kr/" target="_blank">e스포츠 인벤</a></li>
				<li><a href="http://www.teamliquid.net/" target="_blank">Teamliquid</a></li>
				<li><a href="http://www.playxp.com/" target="_blank">PlayXP</a></li>
			</ul>
		</div>

		<div class="menu3">
		  <!-- Teams -->
		</div>

		<div class="menu4">
		  <!-- About -->
		  <ul>
			  <!-- <li><a href="/pb/pb.php?id=faq">도움말</a></li>
			  <li><a href="/pb/pb.php?id=making">제작후기</a></li> -->
			  <li><a href="/sign.html">광고문의</a></li>
			  <li><a href="/staff.html">운영진소개</a></li>
		  </ul>
		</div>

	</div><!-- /overDiv -->

</div><!-- /header -->