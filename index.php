<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<title>USBWebServer</title>
	<meta name="keywords" content="" />
	<meta name="description" content="" />
	<link href="style.css" rel="stylesheet" type="text/css" media="screen" />
</head>
<body>
	<div id="container">
		<img id="header" src="images/header.png">
		<ul id="menu">
			<li>
				<div id="menuleft"></div>
				<a id="menua" href="https://usbwebserver.yura.mk.ua/">
					usbwebserver.yura.mk.ua
				</a>
				<div id="menuright"></div>
			</li>
			<li>
				<div id="menuleft"></div>
				<a id="menua" href="https://yura.mk.ua">
					yura.mk.ua
				</a>
				<div id="menuright"></div>
			</li>
		</ul>
		<div id="topcontent"></div>
		<div id="content">
			<div id="contentleft">

				<h1>USBWebserver V8.6.5</h1>
				<p>
					<ul>
						<li>14 different languages</li>
						<li>DPI bug fixed</li>
						<li>PHP <?php echo phpversion(); ?></li>
						<li>Httpd <?php echo apache_get_version(); ?></li>
						<li>PhpMyAdmin 5.1.3</li>
						<li>MySQL 5.7.36</li>
					</ul>
				</p>
				<h1>PHP <?php echo phpversion(); ?> info</h1>
				<?php
					ob_start();
					phpinfo();
					$i = ob_get_contents();
					ob_end_clean();
					
					echo ( str_replace ( "module_Zend Optimizer", "module_Zend_Optimizer", preg_replace ( '%^.*<body>(.*)</body>.*$%ms', '$1', $i ) ) ) ;
				?>
			
			</div>
			<a href="https://usbwebserver.yura.mk.ua/" id="banner"></a>
			<br style="clear:both">
		</div>
	</div>
</body>
</html>
		