import config

# PROJETO FINAL DA DISCIPLINA - PARTE 3/3
#ALUNOS:
# - ANDERSON AZEVEDO DA SILVA - 20220026825
# - MELQUE RODRIGUES DA TRINDADE SANTOS - 20220039190


# DICIONÁRIOS/EXEMPLOS_PRÉ-DEFINIDOS
produtos = {
 #'REFERÊNCIA':[NOME,VALOR,ESTOQUE,MARCA,FORNECEDOR]
}

recuperar_produtos = {
  #'REFERÊNCIA':[NOME,VALOR,ESTOQUE,MARCA,FORNECEDOR]
}

fornecedor = {
  #'REFERÊNCIA_FORNECEDOR':[NOME,DATA-NASCIMENTO,EMPRESA,TELEFONE,E-MAIL]
}

recuperar_fornecedor = {
  #'REFERÊNCIA_FORNECEDOR':[NOME,DATA-NASCIMENTO,EMPRESA,TELEFONE,E-MAIL]
}

vendas = {
  #'NOTA FISCAL':[CPF_CLIENTE,REFERENCIA_PRODUTO,NOME_PRODUTO,VALOR_PRODUTO,QUANTIDADES_COMPRADAS,MARCA_PRODUTO,FORNECEDOR,DATA_DA_COMPRA,NOME-CLIENTE]
}

recuperar_vendas = {
  #'NOTA FISCAL':[CPF_CLIENTE,REFERENCIA_PRODUTO,NOME_PRODUTO,VALOR_PRODUTO,QUANTIDADES_COMPRADAS,MARCA_PRODUTO,FORNECEDOR,DATA_DA_COMPRA,NOME-CLIENTE]
}

### CRIANDO/LENDO OS ARQUIVOS  
produtos = config.ler_arquivo("produtos.dat",produtos)
recuperar_produtos = config.ler_arquivo("recuperar_produtos.dat",recuperar_produtos)
fornecedor = config.ler_arquivo("fornecedor.dat",fornecedor)
recuperar_fornecedor = config.ler_arquivo("recuperar_fornecedor.dat",recuperar_fornecedor)
vendas = config.ler_arquivo("venda.dat",vendas)
recuperar_vendas = config.ler_arquivo("recuperar_vendas.dat",recuperar_vendas)

opcao_menu = ''

while opcao_menu!="0":
  opcao_menu = config.menu_principal()

  # MÓDULO PRODUTOS
  if opcao_menu == "1":
    print("Módulo de Cadastro de Produtos")
    menu_cadastro = config.menu_cadastro()
    menu_cadastro = config.verifica_opcao(menu_cadastro)

    if menu_cadastro == "1":
      print("Cadastrar Produto!")
      fornecedor = config.ler_arquivo("fornecedor.dat",fornecedor)
      produtos = config.ler_arquivo("produtos.dat",produtos)
      config.cadastrar_produto(fornecedor,produtos)
      config.salvar_arquivo("fornecedor.dat",fornecedor)
      config.salvar_arquivo("produtos.dat",produtos)
      ##config.clear()

    elif menu_cadastro == "2":
      print("Modulo de recuperação de produto")
      recuperar_produtos = config.ler_arquivo("recuperar_produtos.dat",recuperar_produtos)
      produtos = config.ler_arquivo("produtos.dat",produtos)
      config.recuperar_produto(recuperar_produtos, produtos)
      config.salvar_arquivo("produtos.dat",produtos)
      config.salvar_arquivo("recuperar_produtos.dat",recuperar_produtos)
      ##config.clear()
    
    elif menu_cadastro == "3":
      print("Módulo de atualização de produto")
      produtos = config.ler_arquivo("produtos.dat",produtos)
      fornecedor = config.ler_arquivo("fornecedor.dat",fornecedor)
      config.atualizar_produto(fornecedor,produtos)
      config.salvar_arquivo("fornecedor.dat",fornecedor)
      config.salvar_arquivo("produtos.dat",produtos)
      ##config.clear()
      
    elif menu_cadastro == "4":
      print("Módulo de excluir produto")
      produtos = config.ler_arquivo("produtos.dat",produtos)
      recuperar_produtos = config.ler_arquivo("recuperar_produtos.dat",recuperar_produtos)
      config.deletar_produto(produtos, recuperar_produtos)
      config.salvar_arquivo("produtos.dat",produtos)
      config.salvar_arquivo("recuperar_produtos.dat",recuperar_produtos)
      #config.clear()

    elif menu_cadastro == "5":
      print('Módulo de Pesquisa')
      produtos = config.ler_arquivo("produtos.dat",produtos)
      config.pesquisar_produto(produtos)
      #config.clear()

    elif menu_cadastro == '6':
      print('Módulo de Relatório')
      produtos = config.ler_arquivo("produtos.dat",produtos)
      config.listar_produto(produtos)
      #config.clear()
    
    elif menu_cadastro == "0":
      print("Voltando ao menu principal")
      #config.clear()
      
  # MÓDULO FORNECEDOR
  elif opcao_menu == "2":
    print("Módulo de Cadastro de Fornecedor")
    menu_fornecedor = config.menu_fornecedor()
    menu_fornecedor = config.verifica_opcao(menu_fornecedor)

    if menu_fornecedor == "1":
      print("Cadastrar Fornecedor")
      fornecedor = config.ler_arquivo('fornecedor.dat',fornecedor)
      config.cadastrar_fornecedor(fornecedor)
      config.salvar_arquivo('fornecedor.dat',fornecedor)
      #config.clear()
      
    elif menu_fornecedor == '2': 
      print('Recuperar Fornecedor')
      fornecedor = config.ler_arquivo('fornecedor.dat',fornecedor)
      recuperar_fornecedor = config.ler_arquivo("recuperar_fornecedor.dat",recuperar_fornecedor)
      config.recuperar_fornecedor(fornecedor,recuperar_fornecedor)
      config.salvar_arquivo("fornecedor.dat",fornecedor)
      config.salvar_arquivo("recuperar_fornecedor.dat",recuperar_fornecedor)
      #config.clear()

    elif menu_fornecedor == '3': 
      print('Atualizar Fornecedor')
      fornecedor = config.ler_arquivo("fornecedor.dat",fornecedor)
      config.atualizar_fornecedor(fornecedor)
      config.salvar_arquivo("fornecedor.dat",fornecedor)
      #config.clear()

    elif menu_fornecedor == '4': 
      print('Deletar Fornecedor')
      fornecedor = config.ler_arquivo("fornecedor.dat",fornecedor)
      recuperar_fornecedor = config.ler_arquivo("recuperar_fornecedor.dat",recuperar_fornecedor)
      config.deletar_fornecedor(fornecedor,recuperar_fornecedor)
      config.salvar_arquivo("fornecedor.dat",fornecedor)
      config.salvar_arquivo("recuperar_fornecedor.dat",recuperar_fornecedor)
      #config.clear()

    elif menu_fornecedor == '5': 
      print("Pesquisar Fornecedor")
      fornecedor = config.ler_arquivo("fornecedor.dat",fornecedor)
      config.pesquisar_fornecedor(fornecedor)
      #config.clear()

    elif menu_fornecedor == '6': 
      print("Impressão dos Fornecedores")
      fornecedor = config.ler_arquivo("fornecedor.dat",fornecedor)
      config.listar_todos_fornecedor(fornecedor)
      #config.clear()

    elif menu_fornecedor == '0':
      print('Voltando ao menu principal')
      

  # MÓDULO VENDAS
  elif opcao_menu == "3":
    print("Módulo de Vendas")
    menu_vendas = config.menu_vendas()
    menu_vendas = config.verifica_opcao(menu_vendas)

    if menu_vendas == "1":
      print("Cadastrar Vendas")
      produtos = config.ler_arquivo("produtos.dat",produtos)
      fornecedor = config.ler_arquivo("fornecedor.dat",fornecedor)
      vendas = config.ler_arquivo("venda.dat",vendas)
      config.cadastrar_vendas(produtos,fornecedor,vendas)
      config.salvar_arquivo("produtos.dat",produtos)
      config.salvar_arquivo("fornecedor.dat",fornecedor)
      config.salvar_arquivo("venda.dat",vendas)
      #config.clear()

    elif menu_vendas == "2": 
      print("Recuperar venda")
      vendas = config.ler_arquivo("venda.dat",vendas)
      recuperar_vendas = config.ler_arquivo("recuperar_vendas.dat",recuperar_vendas)
      config.recuperar_vendas(vendas,recuperar_vendas)
      config.salvar_arquivo("venda.dat",vendas)
      config.salvar_arquivo("recuperar_vendas.dat",recuperar_vendas)
      #config.clear()

    elif menu_vendas == "3": 
      print("Atualizar venda")
      produtos = config.ler_arquivo("produtos.dat",produtos)
      vendas = config.ler_arquivo("venda.dat",vendas)
      fornecedor = config.ler_arquivo("fornecedor.dat",fornecedor)
      config.atualizar_vendas(produtos,vendas,fornecedor)
      config.salvar_arquivo("produtos.dat",produtos)
      config.salvar_arquivo("fornecedor.dat",fornecedor)
      config.salvar_arquivo("venda.dat",vendas)
      #config.clear()

    elif menu_vendas == "4":  
      print("Deletar venda")
      vendas = config.ler_arquivo("venda.dat",vendas)
      recuperar_vendas = config.ler_arquivo("recuperar_vendas.dat",recuperar_vendas)
      config.deletar_vendas(vendas,recuperar_vendas)
      config.salvar_arquivo("venda.dat",vendas)
      config.salvar_arquivo("recuperar_vendas.dat",recuperar_vendas)
      #config.clear()

    elif menu_vendas == "5": 
      print("Pesquisar venda")
      vendas = config.ler_arquivo("venda.dat",vendas)
      config.pesquisar_vendas(vendas)
      #config.clear()

    elif menu_vendas == '6':
      print('Listar Notas Fiscais')
      vendas = config.ler_arquivo("venda.dat",vendas)
      config.listar_vendas(vendas)
      #config.clear()

  # MÓDULO DOS DESENVOLVEDORES
  elif opcao_menu == "4":
    print("Módulo de Informações dos Desenvolvedores")
    config.informacoes()
  
  elif opcao_menu == "5":
    print("Lixeira do Sistema")
    recuperar_produtos = config.ler_arquivo("recuperar_produtos.dat",recuperar_produtos)
    recuperar_fornecedor = config.ler_arquivo("recuperar_fornecedor.dat",recuperar_fornecedor)
    recuperar_vendas = config.ler_arquivo("recuperar_vendas.dat",recuperar_vendas)
    config.lixeira(recuperar_produtos,recuperar_fornecedor,recuperar_vendas)
    config.salvar_arquivo("recuperar_produtos.dat",recuperar_produtos)
    config.salvar_arquivo("recuperar_fornecedor.dat",recuperar_fornecedor)
    config.salvar_arquivo("recuperar_vendas.dat",recuperar_vendas)

  elif opcao_menu == "0":
    print("Módulo Encerramento")
  
  else:
    print("Opção Inválida!")

print("Sistema Encerrado!")