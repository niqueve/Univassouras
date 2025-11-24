@extends('layout')

@section('conteudo')

<div class="mb-4">
    <h2>Detalhes da Categoria</h2>
</div>

<div class="card border-0">
    <div class="card-body">
        
        <h4 class="card-title text-primary">{{ $category->nome }}</h4>
        <h6 class="card-subtitle mb-3 text-muted">ID: {{ $category->id }}</h6>
        
        <p class="card-text">
            <strong>Descrição:</strong><br>
            {{ $category->descricao ?? 'Nenhuma descrição informada.' }}
        </p>

        <hr>

        <div class="row text-muted small">
            <div class="col-md-6">
                <strong>Criado em:</strong> 
                {{ $category->created_at?->format('d/m/Y H:i') ?? '-' }}
            </div>
            <div class="col-md-6">
                <strong>Atualizado em:</strong> 
                {{ $category->updated_at?->format('d/m/Y H:i') ?? '-' }}
            </div>
        </div>
    </div>
</div>

<div class="mt-4">
    <a href="{{ route('categorias.index') }}" class="btn btn-secondary">Voltar para a Lista</a>
    <a href="{{ route('categorias.edit', $category->id) }}" class="btn btn-warning">Editar Categoria</a>
</div>

@endsection