<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Category extends Model
{
    use HasFactory;

    // Define quais campos podem ser preenchidos via formulário
    protected $fillable = ['nome', 'descricao'];
}