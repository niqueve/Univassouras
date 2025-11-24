@extends('layout')

@section('conteudo')

<div class="mb-3">
    <h2>Editar Categoria</h2>
</div>

<form action="{{ route('categorias.update', $category->id) }}" method="POST">
    @csrf
    @method('PUT')
    
    <div class="mb-3">
        <label for="nome" class="form-label">Nome da Categoria</label>
        <input type="text" class="form-control" name="nome" value="{{ $category->nome }}" required>
    </div>

    <div class="mb-3">
        <label for="descricao" class="form-label">Descrição</label>
        <textarea class="form-control" name="descricao" rows="3">{{ $category->descricao }}</textarea>
    </div>

    <button type="submit" class="btn btn-warning">Atualizar</button>
    <a href="{{ route('categorias.index') }}" class="btn btn-secondary">Cancelar</a>
</form>

@endsection