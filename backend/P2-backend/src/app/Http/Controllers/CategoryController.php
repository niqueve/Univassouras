<?php

namespace App\Http\Controllers;

use App\Models\Category;
use Illuminate\Http\Request;

class CategoryController extends Controller
{
    /**
     * Lista todas as categorias
     */
    public function index()
    {
        $categories = Category::all();
        return view('categories.index', compact('categories'));
    }

    /**
     * Mostra o formulário de criar
     */
    public function create()
    {
        return view('categories.create');
    }

    /**
     * Salva a nova categoria no banco
     */
    public function store(Request $request)
    {
        // Cria usando os dados do formulário
        Category::create($request->all());
        
        // Redireciona para a lista
        return redirect()->route('categorias.index');
    }

    /**
     * Mostra uma categoria específica (CORRIGIDO)
     */
    public function show(string $id)
    {
        // Busca pelo ID ou falha (dá erro 404) se não encontrar
        $category = Category::findOrFail($id);
        
        return view('categories.show', compact('category'));
    }

    /**
     * Mostra o formulário de edição (CORRIGIDO)
     */
    public function edit(string $id)
    {
        $category = Category::findOrFail($id);
        return view('categories.edit', compact('category'));
    }

    /**
     * Atualiza os dados no banco (CORRIGIDO)
     */
    public function update(Request $request, string $id)
    {
        $category = Category::findOrFail($id);
        $category->update($request->all());
        
        return redirect()->route('categorias.index');
    }

    /**
     * Remove a categoria do banco (CORRIGIDO)
     */
    public function destroy(string $id)
    {
        $category = Category::findOrFail($id);
        $category->delete();
        
        return redirect()->route('categorias.index');
    }
}