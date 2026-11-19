numeroCasoDeTeste = int(input())


for i in range(numeroCasoDeTeste):
  qtdDeProdutosDispo = int(input())
  listaProdutos = []
  listaProdutosDesejados = []

  for j in range(qtdDeProdutosDispo):
      produto, precoProduto = input().split()
      precoProdutoFormatado = float(precoProduto.replace(',', '.'))
      listaProdutos.append((produto, precoProdutoFormatado))

  qtdDeProdutosDesejados = int(input())

  for j in range(qtdDeProdutosDesejados):
     nomeProdutoDesejado, precoProdutoDesejado = input().split()
     precoProdutoDesejado = int(precoProdutoDesejado)
     listaProdutosDesejados.append((nomeProdutoDesejado, precoProdutoDesejado))

  soma:float = 0.00

  for produtoDesejado in listaProdutosDesejados:
      for produtoDisponivel in listaProdutos:
          if produtoDesejado[0] == produtoDisponivel[0]:
              soma += produtoDisponivel[1] * produtoDesejado[1]

  print(f"R$ {soma:.2f}")
