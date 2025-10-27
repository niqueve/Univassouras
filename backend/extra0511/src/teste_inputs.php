<?php
require_once 'conexao.php';

$name = $email = "";
$message = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = test_input($_POST["name"]);
    $email = test_input($_POST["email"]);
    
    try {
        // Prepare and execute the SQL query
        $stmt = $pdo->prepare("INSERT INTO users (name, email) VALUES (:name, :email)");
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':email', $email);
        $stmt->execute();
        
        $message = "User registered successfully!";
    } catch (PDOException $e) {
        $message = "Error: " . $e->getMessage();
    }
}

function test_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Registration Result</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            margin: 40px;
        }
        .success {
            color: green;
            padding: 10px;
            border: 1px solid green;
            background-color: #dff0d8;
        }
        .error {
            color: red;
            padding: 10px;
            border: 1px solid red;
            background-color: #f2dede;
        }
        .button {
            display: inline-block;
            padding: 10px 15px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h2>Registration Result</h2>
    <?php if ($message): ?>
        <div class="<?php echo strpos($message, 'Error') !== false ? 'error' : 'success'; ?>">
            <?php echo $message; ?>
        </div>
    <?php endif; ?>
    
    <?php if ($name && $email): ?>
        <h3>Submitted Information:</h3>
        <p>Name: <?php echo $name; ?></p>
        <p>Email: <?php echo $email; ?></p>
    <?php endif; ?>
    
    <a href="index.html" class="button">Back to Registration</a>
</body>
</html>