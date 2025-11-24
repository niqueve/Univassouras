@extends('layout')

@section('conteudo')

<div class="mb-3">
    <h2>Nova Categoria</h2>
</div>

<form action="{{ route('categorias.store') }}" method="POST">
    @csrf
    
    <div class="mb-3">
        <label for="nome" class="form-label">Nome da Categoria</label>
        <input type="text" class="form-control" name="nome" required placeholder="Ex: Eletrônicos">
    </div>

    <div class="mb-3">
        <label for="descricao" class="form-label">Descrição</label>
        <textarea class="form-control" name="descricao" rows="3" placeholder="Detalhes da categoria..."></textarea>
    </div>

    <button type="submit" class="btn btn-success">Salvar Cadastro</button>
    <a href="{{ route('categorias.index') }}" class="btn btn-secondary">Cancelar</a>
</form>

@endsection