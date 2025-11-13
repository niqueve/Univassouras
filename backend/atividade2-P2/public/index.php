<?php

use Illuminate\Foundation\Application;
use Illuminate\Http\Request;

define('LARAVEL_START', microtime(true));

// If running in Docker and SHOW_OLA_MUNDO is set, short-circuit and show message.
// This lets us run the project in a container to simply display "Ola Mundo"
// without bootstrapping the entire framework (useful for demos/tests).
if (getenv('SHOW_OLA_MUNDO') === '1') {
    echo 'Ola Mundo';
    exit;
}

// Determine if the application is in maintenance mode...
if (file_exists($maintenance = __DIR__.'/../storage/framework/maintenance.php')) {
    require $maintenance;
}

// Register the Composer autoloader...
require __DIR__.'/../vendor/autoload.php';

// Bootstrap Laravel and handle the request...
/** @var Application $app */
$app = require_once __DIR__.'/../bootstrap/app.php';

$app->handleRequest(Request::capture());
