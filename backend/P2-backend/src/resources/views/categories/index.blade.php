@extends('layout')

@section('conteudo')

<div class="d-flex justify-content-between align-items-center mb-3">
    <h2 class="mb-0">Lista de Categorias</h2>
    <a href="{{ route('categorias.create') }}" class="btn btn-primary">
        + Nova Categoria
    </a>
</div>

<table class="table table-striped table-hover">
    <thead class="table-dark">
        <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Descrição</th>
            <th class="text-end">Ações</th>
        </tr>
    </thead>
    <tbody>
        @foreach($categories as $category)
        <tr>
            <td>{{ $category->id }}</td>
            <td><strong>{{ $category->nome }}</strong></td>
            <td>{{ $category->descricao }}</td>
            <td class="text-end">
                <a href="{{ route('categorias.show', $category->id) }}" class="btn btn-sm btn-info text-white">Ver</a>
                <a href="{{ route('categorias.edit', $category->id) }}" class="btn btn-sm btn-warning">Editar</a>
                
                <form action="{{ route('categorias.destroy', $category->id) }}" method="POST" style="display:inline;">
                    @csrf
                    @method('DELETE')
                    <button type="submit" class="btn btn-sm btn-danger" onclick="return confirm('Tem certeza?')">Excluir</button>
                </form>
            </td>
        </tr>
        @endforeach
    </tbody>
</table>

@endsection