<?php
$uploadDir = __DIR__ . '/secure_uploads/';
if (!file_exists($uploadDir)) { mkdir($uploadDir, 0550, true); }
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['secure_file'])) {
    $file = $_FILES['secure_file'];
    $allowedExtensions = ['jpg', 'jpeg', 'png'];
    $fileExtension = strtolower(pathinfo($file['name'], PATHINFO_EXTENSION));
    $finfo = new finfo(FILEINFO_MIME_TYPE);
    $mimeType = $finfo->file($file['tmp_name']);
    if (in_array($fileExtension, $allowedExtensions, true) && in_array($mimeType, ['image/jpeg', 'image/png'], true)) {
        $newFileName = bin2hex(random_bytes(32)) . '.' . $fileExtension;
        move_uploaded_file($file['tmp_name'], $uploadDir . $newFileName);
        echo "فایل با موفقیت و به صورت امن ذخیره شد.";
    }
}
?>
