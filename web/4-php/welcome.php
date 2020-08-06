<?php
    if(!isset($_COOKIE['super_secret_password']))setcookie('super_secret_password','b0ctf{hunter3}',time()+600,"/");
?>
<html>
    <body>
        Welcome: <?php echo $_GET['name'];?><br>
        Your comment is: <?php echo $_GET['comment'];?>
    </body>
</html> 
