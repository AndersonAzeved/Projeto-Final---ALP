import config

# DICIONÁRIOS E LISTA

produtos_L = []
produtos_D = {
 #'REFERÊNCIA':[NOME,VALOR,ESTOQUE,MARCA,FORNECEDOR]
}

recuperar_produtos_L = []
recuperar_produtos_D = {
  #'REFERÊNCIA':[NOME,VALOR,ESTOQUE,MARCA,FORNECEDOR]
}

fornecedor_L = []
fornecedor_D = {
  #'REFERÊNCIA_FORNECEDOR':[NOME,DATA-NASCIMENTO,EMPRESA,TELEFONE,E-MAIL]
}

recuperar_fornecedor_L = []
recuperar_fornecedor_D = {
  #'REFERÊNCIA_FORNECEDOR':[NOME,DATA-NASCIMENTO,EMPRESA,TELEFONE,E-MAIL]
}

vendas_L =[]
vendas_D = {
  #'NOTA FISCAL':[CPF_CLIENTE,REFERENCIA_PRODUTO,NOME_PRODUTO,VALOR_PRODUTO,QUANTIDADES_COMPRADAS,MARCA_PRODUTO,FORNECEDOR,DATA_DA_COMPRA]
}

recuperar_vendas_L = []
recuperar_vendas_D = {
  #'NOTA FISCAL':[CPF_CLIENTE,REFERENCIA_PRODUTO,NOME_PRODUTO,VALOR_PRODUTO,QUANTIDADES_COMPRADAS,MARCA_PRODUTO,FORNECEDOR,DATA_DA_COMPRA]
}

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
      config.cadastrar_produto(fornecedor_D,produtos_D,produtos_L)

    elif menu_cadastro == "2":
      print("Modulo de recuperação de produto")
      config.recuperar_produto(recuperar_produtos_D,recuperar_produtos_L, produtos_D,produtos_L)
    
    elif menu_cadastro == "3":
      print("Módulo de atualização de produto")
      config.atualizar_produto(produtos_D,fornecedor_D,produtos_L)
      
    elif menu_cadastro == "4":
      print("Módulo de excluir produto")
      config.deletar_produto(produtos_D,produtos_L,recuperar_produtos_D,recuperar_produtos_L)

    elif menu_cadastro == "5":
      print('Módulo de Pesquisa')
      config.pesquisar_produto(produtos_D)

    elif menu_cadastro == '6':
      print('Módulo de Relatório')
      config.listar_produto(produtos_D)
    
    elif menu_cadastro == "0":
      print("Voltando ao menu principal")
      
  # MÓDULO FORNECEDOR
  elif opcao_menu == "2":
    print("Módulo de Cadastro de Fornecedor")
    menu_fornecedor = config.menu_fornecedor()
    menu_fornecedor = config.verifica_opcao(menu_fornecedor)

    if menu_fornecedor == "1":
      print("Cadastrar Fornecedor")
      config.cadastrar_fornecedor(fornecedor_D,fornecedor_L)
      
    elif menu_fornecedor == '2': 
      print('Recuperar Fornecedor')
      config.recuperar_fornecedor(fornecedor_D,recuperar_fornecedor_D,recuperar_fornecedor_L,fornecedor_L)

    elif menu_fornecedor == '3': 
      print('Atualizar Fornecedor')
      config.atualizar_fornecedor(fornecedor_D,fornecedor_L)

    elif menu_fornecedor == '4': 
      print('Deletar Fornecedor')
      config.deletar_fornecedor(fornecedor_D,recuperar_fornecedor_L,fornecedor_L,recuperar_fornecedor_D)

    elif menu_fornecedor == '5': 
      print("Pesquisar Fornecedor")
      config.pesquisar_fornecedor(fornecedor_D)

    elif menu_fornecedor == '6': 
      print("Impressão dos Fornecedores")
      config.listar_todos_fornecedor(fornecedor_D)

    elif menu_fornecedor == '0':
      print('Voltando ao menu principal')
      
  # MÓDULO VENDAS
  elif opcao_menu == "3":
    print("Módulo de Vendas")
    menu_vendas = config.menu_vendas()
    menu_vendas = config.verifica_opcao(menu_vendas)

    if menu_vendas == "1":
      print("Cadastrar Vendas")
      config.cadastrar_vendas(vendas_D,produtos_D,fornecedor_D,vendas_L,produtos_L)

    elif menu_vendas == "2": 
      print("Recuperar venda")
      config.recuperar_vendas(vendas_D,recuperar_vendas_D,vendas_L,recuperar_vendas_L)

    elif menu_vendas == "3": 
      print("Atualizar venda")
      config.atualizar_vendas(vendas_D,fornecedor_D,vendas_L,produtos_D,produtos_L)

    elif menu_vendas == "4":  
      print("Deletar venda")
      config.deletar_vendas(vendas_D,recuperar_vendas_D,recuperar_vendas_L,vendas_L)

    elif menu_vendas == "5": 
      print("Pesquisar venda")
      config.pesquisar_vendas(vendas_D)

    elif menu_vendas == '6':
      print('Listar Notas Fiscais')
      config.listar_vendas(vendas_D)
      
  # MÓDULO DOS DESENVOLVEDORES
  elif opcao_menu == "4":
    print("Módulo de Informações dos Desenvolvedores")
    config.informacoes()

  # MÓDULO DE LIXEIRA
  elif opcao_menu == "5":
    print("Lixeira do Sistema")
    config.lixeira(recuperar_produtos_D,recuperar_fornecedor_D,recuperar_vendas_D)

  elif opcao_menu == "0":
    print("Módulo Encerramento")
  
  else:
    print("Opção Inválida!")
print("Sistema Encerrado!")