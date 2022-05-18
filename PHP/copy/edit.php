<?php
$number = $_GET["number"];
$f = 'id.txt'; //文件名

$a = file($f); //把文件的所有内容获取到数组里面

$n = count($a); //获得总行数

$rnd_line = $a[$number]; //获得行

echo $rnd_line;