<?php

use App\Http\Controllers\CategoryController;

Route::get('/', function () {
    return redirected('/categorias');
});

Route::resource('categorias', CategoryController::class);

Route::get('/', function () {
    // Redireciona direto para a listagem
    return redirect()->route('categorias.index');
});