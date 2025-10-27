<?php
$host = 'db';
$dbname = 'aula_php';
$user = 'user';
$password = '1234';

try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $user, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "<h2>Conexão com o banco de dados realizada com sucesso!</h2>";
} catch (PDOException $e) {
    echo "Erro: " . $e->getMessage();
}
?>