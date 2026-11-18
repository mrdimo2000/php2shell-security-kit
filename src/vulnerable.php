<?php
if(isset($_POST['submit'])){
    $filename = $_FILES['uploadfile']['name'];
    $tempname = $_FILES['uploadfile']['tmp_name'];
    $folder = "uploads/" . $filename;
    move_uploaded_file($tempname, $folder);
}
?>
