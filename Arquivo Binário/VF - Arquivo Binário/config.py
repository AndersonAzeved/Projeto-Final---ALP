import random, time, os, pickle
from datetime import datetime
lista_numero = []

def informacoes():
  print("""
   --------------------------------------------------------------------   
  |                                                                    |
  |  UFRN CERES - CAICÓ                                                |
  |  Projeto Final da Disciplica - Algoritmos e Lógica de Programação  |
  |  Docente: Flavius da Luz e Gorgônio                                |
  |                                                                    |
  |  SIG-Inventory: Um Sistema de Controle de Estoques                 |
  |                                                                    |
  |  Curso                                                             |
  |    Bacharelado em Sistemas de Informação                           |
  |    Período 1 - 2022.1                                              |
  |                                                                    |
  |  Discentes                                                         |
  |    Anderson Azevedo da Silva - 20220026825                         |
  |    Melque Rodrigues da Trindade Santos - 20220039190               |
  |                                                                    |
   --------------------------------------------------------------------
        """)
  time.sleep(10)
  os.system('cls') or None

def clear():
  segundos = 5
  while segundos:
    print("\nAguarde 5 segundos para continuar!")
    contador = '\t\t\t{:02d}s'.format(segundos)
    print(contador)
    time.sleep(1)
    os.system('cls') or None
    segundos -= 1
  time.sleep(0)
  os.system('clear') or None

def ler_arquivo(nome_arquivo,dicionario):
  try:
    arquivo = open(nome_arquivo, "rb")
    dicionario = pickle.load(arquivo)
    arquivo.close()
    
  except:
    arquivo = open(nome_arquivo, "wb")
    arquivo.close()

  return dicionario
  
def salvar_arquivo(nome_arquivo, dicionario):
  arquivo = open(nome_arquivo, "wb")
  pickle.dump(dicionario, arquivo)
  arquivo.close()

def menu_principal():
  #os.system('clear')
  menu = input("""
        ============================================================
        |                      MENU PRINCIPAL                      |
        ============================================================
        |                       BEM - VINDO                        |
        |----------------------------------------------------------|
        |       --------------           -------------------       |
        |    1- |  PRODUTOS  |        2- |   FORNECEDOR    |       |
        |       --------------           -------------------       |
        |       --------------           -------------------       |
        |    3- |   VENDAS   |        4- | DESENVOLVEDORES |       |
        |       --------------           -------------------       |
        |       --------------           -------------------       |
        |    0- |  ENCERRAR  |        5- |      LIXEIRA    |       |
        |       --------------           -------------------       |
        |==========================================================|
        Opção: """)
  return menu

def menu_cadastro():
  #os.system('clear')
  menu = input("""
        =====================================================
        |                    MENU PRODUTOS                  |
        =====================================================
        |       --------------         ----------------     |
        |    1- |  CADASTRO  |      4- |    DELETAR   |     |
        |       --------------         ----------------     |
        |       --------------         ----------------     |
        |    2- |  RECUPERAR |      5- |   PESQUISAR  |     |
        |       --------------         ----------------     |
        |       --------------         ----------------     |
        |    3- |  ATUALIZAR |      6- |    LISTAR    |     |
        |       --------------         ----------------     |
        |       ------------------                          |
        |    0- | MENU PRINCIPAL |                          |
        |       ------------------                          |
        |===================================================|
        Opção: """)
  return menu

def menu_fornecedor():
  #os.system('clear')
  menu = input("""
        =====================================================
        |                  MENU FORNECEDOR                  |
        =====================================================
        |       --------------         ----------------     |
        |    1- |  CADASTRO  |      4- |    DELETAR   |     |
        |       --------------         ----------------     |
        |       --------------         ----------------     |
        |    2- |  RECUPERAR |      5- |   PESQUISAR  |     |
        |       --------------         ----------------     |
        |       --------------         ----------------     |
        |    3- |  ATUALIZAR |      6- |    LISTAR    |     |
        |       --------------         ----------------     |
        |       ------------------                          |
        |    0- | MENU PRINCIPAL |                          |
        |       ------------------                          |
        |===================================================|
        Opção: """)
  return menu

def menu_vendas():
  #os.system('clear')
  
  menu = input("""
        =====================================================
        |                    MENU VENDAS                    |
        =====================================================
        |       --------------         ----------------     |
        |    1- |  CADASTRO  |      4- |    DELETAR   |     |
        |       --------------         ----------------     |
        |       --------------         ----------------     |
        |    2- |  RECUPERAR |      5- |   PESQUISAR  |     |
        |       --------------         ----------------     |
        |       --------------         ----------------     |
        |    3- |  ATUALIZAR |      6- |    LISTAR    |     |
        |       --------------         ----------------     |
        |       ------------------                          |
        |    0- | MENU PRINCIPAL |                          |
        |       ------------------                          |
        |===================================================|
        Opção: """)
  return menu

def verifica_opcao(menu):
  tupla = ('1','2','3','4','5','6','0')
  while not(menu in tupla):
    print("Opção Inválida, tente novamente")
    menu = menu_cadastro()
  return menu

def verificar_indice(dicionario,indice):
  if indice in dicionario:
    return True
  else:
    return False

def calcula_preco(produtos,referencia,quantidade):
  preco = float(produtos[referencia][1])
  quanidade = int(quantidade)
  valor_total = preco*quanidade
  return valor_total
     
def verificar_vendas(produtos,referencia,quantidade):
  if referencia in produtos:
    estoque = int(produtos[referencia][2])
    if estoque > 0:
      quantidade = int(quantidade)
      estoque-=quantidade
      produtos[referencia][2] = str(estoque)
    return True
  else:
    return False

def listar_fornecedor(fornecedor):
  for pessoa in fornecedor:
    nome = (fornecedor.get(pessoa))[0]
    print("""
    CPF: %s
    Nome: %s
          """%(pessoa,nome))

def valida_cpf(cpf):
  cpf = cpf.replace('.', '')
  cpf = cpf.replace('-', '')
  cpf = cpf.replace(' ', '')
  tam = len(cpf)
  soma = 0
  d1 = 0
  d2 = 0
  if tam != 11:
    return False
  for i in range(11):
    if (cpf[i] < '0') or (cpf[i] > '9'):
      return False
  for i in range(9):
    soma += (int(cpf[i]) * (10 - i))
  d1 = 11 - (soma % 11)
  if (d1 == 10 or d1 == 11):
    d1 = 0
  if d1 != int(cpf[9]):
    return False
  soma = 0
  for i in range(10):
    soma += (int(cpf[i]) * (11 - i))
  d2 = 11 - (soma%11)
  if (d2 == 10 or d2 == 11):
    d2 = 0
  if d2 != int(cpf[10]):
    return False
  return True

def validar_cnpj(empresa):
    str_cnpj = ""
    tupla = ('1','2','3','4','5','6','7','8','9','0')
    verific = any(chr.isdigit() for chr in empresa)
    if verific == False:
        return False
    for i in empresa:
      if i in tupla:
        str_cnpj = str_cnpj + i
    if len(str_cnpj) != 14:
        return False
    cont = 0
    for i in empresa:
        if i in tupla:
            str_cnpj = str_cnpj + i
            cont+=1
    dig_1 = int(str_cnpj[12])
    dig_2 = int(str_cnpj[13])
    cnpj = str_cnpj[0:12]
    cont = 0
    soma = 0 
    soma = (int(cnpj[0])*5) + (int(cnpj[1])*4) + (int(cnpj[2])*3) + (int(cnpj[3])*2) + (int(cnpj[4])*9) + (int(cnpj[5])*8) + (int(cnpj[6])*7)
    soma = soma + (int(cnpj[7])*6) + (int(cnpj[8])*5) + (int(cnpj[9])*4) + (int(cnpj[10])*3) + (int(cnpj[11])*2)

    resto = soma%11
    num_dig2 = (2,3,4,5,6,7,8,9,10)
    dif = 11 - resto
    if (resto == 0 or resto == 1) and dig_1 != 0:
        return False
    elif resto in num_dig2:
        if dif != dig_1:
            return False
    soma = 0
    cnpj = str_cnpj[0:13]
    soma = (int(cnpj[0])*6) + (int(cnpj[1])*5) + (int(cnpj[2])*4) + (int(cnpj[3])*3) + (int(cnpj[4])*2) + (int(cnpj[5])*9) + (int(cnpj[6])*8)
    soma = soma + (int(cnpj[7])*7) + (int(cnpj[8])*6) + (int(cnpj[9])*5) + (int(cnpj[10])*4) + (int(cnpj[11])*3) + (int(cnpj[12])*2)
    
    resto = soma%11
    dif = 11 - resto    
    if (resto == 0 or resto == 1) and dig_2 != 0:
        return False
    elif resto in num_dig2:
        dif = int(dif)
        if dif != dig_2:
            return False
    return True

def verificar_data(data):
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:10])
    ano_atual = datetime.today().year
    mes_atual= datetime.today().month
    dia_atual = datetime.today().day
    meses_31 = (1,3,5,7,8,10,12)
    meses_30 = (4,6,9,11)
    if ano <= ano_atual:
        if (ano < ano_atual) or (mes <= mes_atual and dia <= dia_atual and ano <= ano_atual):
            if not(ano > ano_atual or (ano > ano_atual and mes > mes_atual) or (ano > ano_atual and mes > mes_atual and dia > dia_atual)):
                if dia >= 1 and dia <= 31 and mes in meses_31:
                    return True
                elif dia >= 1 and dia <=30 and mes in meses_30:
                    return True
                elif (((ano % 4) == 0) and ((ano % 100) !=0)) or ((ano % 400) == 0):
                    if dia >=1 and dia <=29 and mes == 2:
                        return True
                    else:
                        return False
                elif not(((ano % 4) == 0) and ((ano % 100) !=0)) or ((ano % 400) == 0):
                    if dia >=1 and dia <=28 and mes == 2:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def while_data(data): #TESTAR
  tam = len(data)
  if tam != 10:
    while tam != 10:
      data = input("Digite uma data válida (AA/AA/AAAA): ")
      tam = len(data)
  data_esta = verificar_data(data)
  if data_esta == False:
    while data_esta == False:
      print("A data informada não é válida!")
      data = input("Informe uma nova data: ").upper()
      data_esta = verificar_data(data)
  return data

def while_referencia(referencia,produtos): #TESTAR
  referencia_esta = verificar_indice(produtos,referencia)
  if referencia_esta == True:
    while referencia_esta == True:
      print("A referência já está cadastrada!")
      referencia = input("Informe uma nova referencia: ").upper()
      referencia_esta = verificar_indice(produtos,referencia)
  return referencia

def while_fornecedor(fornecedor, fornecedor_produto): #TESTAR
  verificar = verificar_indice(fornecedor,fornecedor_produto)
  while verificar == False:
    listar_fornecedor(fornecedor)
    fornecedor_produto = input("Fornecedor não cadastrado, digite um fornecedor válido: ").upper()
    verificar = verificar_indice(fornecedor,fornecedor_produto)
  return fornecedor_produto

def while_cpf(cpf):
  valor = valida_cpf(cpf)
  if valor == False:
    while valor == False:
      print("O CPF informado não é válido!")
      cpf = input("Informe um novo CPF: ")
      valor = valida_cpf(cpf)
  return cpf

def while_cnpj(empresa):
  valor = validar_cnpj(empresa)
  if valor == False:
    while valor == False:
      print("O CNPJ informado não é válido!")
      empresa = input("Informe um novo CNPJ, juntamente com o nome da empresa (EMPRESA/CNPJ): ")
      valor = validar_cnpj(empresa)
  return empresa

# def while_telefone(telefone):
#   tam = telegf
      
################### FUNÇÕES DO MÓDULO DE PRODUTOS ###############
def cadastrar_produto(fornecedor,produtos):
  # MÉTODO DE SEGURANÇA, EVITAR CADASTRAMENTO DE PRODUTO COM FORNECEDOR NÃO CADASTRADO
  if len(fornecedor) > 0:
    referencia = input("Referência do produto: ").upper()
    referencia = while_referencia(referencia,produtos)
    nome_produto = input("Nome do produto: ").upper()
    valor_produto = input("Valor do produto: ").upper()
    estoque = input('Quantidade em estoque: ')
    marca_produto = input("Marca e Nome do veículo (FORMATO: FIAT/TOURO): ").upper()
    fornecedor_produto = input("CPF do Fornecedor: ").upper()
    fornecedor_produto = while_cpf(fornecedor_produto)
    fornecedor_produto = while_fornecedor(fornecedor, fornecedor_produto)
    produtos[referencia] = [nome_produto,valor_produto,estoque,marca_produto,fornecedor_produto]
    print("Produto Cadastrado com Sucesso!")
  else:
    print("Nenhum fornecedor cadastrado, por favor cadastre ao menos um fornecedor no Módulo Fornecedor!")

def recuperar_produto(recuperar_produtos,produtos):
  # USUÁRIO DIGITA UMA REFERÊNCIA OU NOME DO PRODUTO, VERIFICA SE O PRODUTO ESTÁ NO DICIONÁRIO DE RECUPERAÇÃO.
  # -SE ESTIVER, ADICIONA DE NOVO OS DADOS NO DICIONÁRIO PRODUTO
  # -CASO NÃO, INFORMAR QUE O PRODUTO NÃO FOI ENCONTRADO 
  produto_recuperar = input('Informe a referência do produto: ').upper()
  verificar = verificar_indice(recuperar_produtos,produto_recuperar)
  if verificar == True:
    print('')
    print('REFERÊNCIA: ',produto_recuperar)
    print('NOME: {}'.format(recuperar_produtos[produto_recuperar][0]))
    print('VALOR: {}'.format(recuperar_produtos[produto_recuperar][1]))
    print('ESTOQUE: {}'.format(recuperar_produtos[produto_recuperar][2]))
    print('MARCA: {}'.format(recuperar_produtos[produto_recuperar][3]))
    print('FORNECEDOR: {}'.format(recuperar_produtos[produto_recuperar][4]))
    op_conf = input('Deseja Realmente recuperar este produto? S-(sim) N-(não) ')
    if op_conf.upper() == 'S':
      produto = recuperar_produtos[produto_recuperar]
      nome = produto[0]
      valor = produto[1]
      estoque = produto[2]
      marca = produto[3]
      fornecedor = produto[4]
      produtos[produto_recuperar] = [nome,valor,estoque,marca,fornecedor]
      recuperar_produtos.pop(produto_recuperar)
      print('O produto foi recuperado com sucesso!')
  else:
    print('O produto informado não foi encontrado na lixeira do sistema!')

def atualizar_produto(fornecedor,produtos):
  # USUÁRIO DIGITA A REFERÊNCIA OU NOME DO PRODUTO, E O SISTEMA PERGUNTA O QUE ELE DESEJA ATUALIZAR E ATUALIZA OS DADOS NO DICIONÁRIO PRODUTOS
  produto_atualizar = input("Informe a referência do produto: ").upper()
  verificar = verificar_indice(produtos,produto_atualizar)
  if verificar == True:
    nome_produto = input("Novo nome do produto: ").upper()
    valor_produto = input("Novo valor do produto: ").upper()
    estoque_produto = input("Nova quantidade em estoque do produto: ").upper()
    marca_produto = input("Nova marca e Nome do veículo (FORMATO: FIAT/TOURO): ").upper()
    fornecedor_produto = input("Novo CPF do Fornecedor: ").upper()
    fornecedor_produto = while_cpf(fornecedor_produto)
    fornecedor_produto = while_fornecedor(fornecedor, fornecedor_produto)
    produtos[produto_atualizar][0] = nome_produto
    produtos[produto_atualizar][1] = valor_produto
    produtos[produto_atualizar][2] = estoque_produto
    produtos[produto_atualizar][3] = marca_produto
    produtos[produto_atualizar][4] = fornecedor_produto
    print("Produto Cadastrado com Sucesso!")
  else:
    print('O produto informado não esta cadastrado no sistema!')

def pesquisar_produto(produtos):
  produto_pesquisar = input("Informe a referência do produto: ").upper()
  verificar = verificar_indice(produtos,produto_pesquisar)
  if verificar == True:
    print('')
    print('REFERÊNCIA: ',produto_pesquisar)
    print('NOME: {}'.format(produtos[produto_pesquisar][0]))
    print('VALOR: {}'.format(produtos[produto_pesquisar][1]))
    print('ESTOQUE: {}'.format(produtos[produto_pesquisar][2]))
    print('MARCA: {}'.format(produtos[produto_pesquisar][3]))
    print('FORNECEDOR: {}'.format(produtos[produto_pesquisar][4]))
  else:
    print('O produto informado não esta cadastrado no sistema!')

def deletar_produto(produtos, recuperar_produtos):
  produto_deletar = input("Informe a referência do produto: ").upper()
  verificar = verificar_indice(produtos,produto_deletar)
  if verificar == True:
    print('')
    print('REFERÊNCIA: ',produto_deletar)
    print('NOME: {}'.format(produtos[produto_deletar][0]))
    print('VALOR: {}'.format(produtos[produto_deletar][1]))
    print('ESTOQUE: {}'.format(produtos[produto_deletar][2]))
    print('MARCA: {}'.format(produtos[produto_deletar][3]))
    print('FORNECEDOR: {}'.format(produtos[produto_deletar][4]))
    op_conf = input('Deseja realmente excluir o produto acima? S-(sim) N-(não)')
    if op_conf.upper() == 'S':
      referencia = produtos[produto_deletar]
      nome = referencia[0]
      valor = referencia[1]
      estoque = referencia[2]
      marca = referencia[3]
      fornecedor = referencia[4]
      recuperar_produtos[produto_deletar] = [nome,valor,estoque,marca,fornecedor]
      produtos.pop(produto_deletar)
      print('Produto deletado com sucesso!')
    else:
      print('O produto não foi deletado!')
  else:
      print('O produto informado não esta cadastrado no sistema!')

def listar_produto(produtos):
  if len(produtos) > 0:
    cont = 1
    for item in produtos:
      print('')
      print('Produto: ', cont)
      print('REFERÊNCIA: ',item)
      print('NOME: {}'.format(produtos[item][0]))
      print('VALOR: {}'.format(produtos[item][1]))
      print('ESTOQUE: {}'.format(produtos[item][2]))
      print('MARCA: {}'.format(produtos[item][3]))
      print('FORNECEDOR: {}'.format(produtos[item][4]))
      cont += 1
  else:
    print('Não há produtos cadastrados no sistema!')

    
################## FUNÇÕES DO MÓDULO DE FORNCEDORES ##############
# FUNÇÃO VERIFACA EMAIL
def verificar_email(email):
  if "@" in email:
    return True
  else:
    return False

# FUNÇÃO VERIFICAR O EMAIL E LOOP ENQUANTO O EMAIL NÃO TIVER CORRETO
def while_email(email):
  email_esta = verificar_email(email)
  if email_esta == False:
    while email_esta == False:
      print("O E-mail digitado não é válido!")
      email = input("Informe um novo E-mail: ").upper()
      email_esta = verificar_email(email)
  return email

def cadastrar_fornecedor(fornecedor):
  cpf_fornecedor = input("Informe seu CPF (000.000.000-00): ").upper()
  cpf_fornecedor = while_cpf(cpf_fornecedor)
  cpf_esta = verificar_indice(fornecedor,cpf_fornecedor) 
  if cpf_esta == True:
    while cpf_esta == True:
      print("CPF já cadastrado por outro fornecedor!")
      cpf_fornecedor = input("Informe um novo CPF (000.000.000-00): ").upper()
      cpf_esta = verificar_indice(fornecedor,cpf_fornecedor)
  nome_fornecedor = input("Informe seu nome: ").upper()
  data_fornecedor = input("Informe sua data de nascimento (AA/AA/AAAA): ").upper()
  data_fornecedor = while_data(data_fornecedor)
  empresa_fornecedor = input("Informe sua empresa (NOME/CNPJ): ").upper()
  empresa_fornecedor = while_cnpj(empresa_fornecedor)
  fone_fornecedor = input("Informe seu telefone (9 DÍGITOS): ").upper()
  email_fornecedor = input("Informe seu e-mail: ").upper()
  email_fornecedor = while_email(email_fornecedor)
  fornecedor[cpf_fornecedor] = [nome_fornecedor,data_fornecedor,empresa_fornecedor,fone_fornecedor,email_fornecedor]
  print("Cadastrado com Sucesso!")

def deletar_fornecedor(fornecedor,recuperar_fornecedor):
  fornecedor_deletar = input("Informe o CPF do fornecedor: ").upper()
  fornecedor_deletar = while_cpf(fornecedor_deletar)
  verificar = verificar_indice(fornecedor,fornecedor_deletar)
  if verificar == True:
    print('')
    print('CPF: ',fornecedor_deletar)
    print('NOME: {}'.format(fornecedor[fornecedor_deletar][0]))
    print('DATA DE NASCIMENTO: {}'.format(fornecedor[fornecedor_deletar][1]))
    print('EMPRESA/CNPJ: {}'.format(fornecedor[fornecedor_deletar][2]))
    print('TELEFONE: {}'.format(fornecedor[fornecedor_deletar][3]))
    print('EMAIL: {}'.format(fornecedor[fornecedor_deletar][4]))
    op_conf = input('Deseja realmente excluir o fornecedor acima? S-(sim) N-(não): ')
    if op_conf.upper() == 'S' or op_conf.upper() == 'SIM':
      forn = fornecedor[fornecedor_deletar]
      nome = forn[0]
      data = forn[1]
      empresa = forn[2]
      telefone = forn[3]
      email = forn[4]
      recuperar_fornecedor[fornecedor_deletar] = [nome,data,empresa,telefone,email]
      fornecedor.pop(fornecedor_deletar)
      print('Fornecedor deletado com sucesso!')
    else:
      print('O fornecedor não foi deletado!')
  else:
      print('O fornecedor informado não esta cadastrado no sistema!')

def recuperar_fornecedor(fornecedor,recuperar_fornecedor):
  cpf = input("Informe o CPF do fornecedor: ").upper()
  cpf = while_cpf(cpf)
  verificar = verificar_indice(recuperar_fornecedor,cpf)
  if verificar == True:
    print('')
    print('CPF: ',cpf)
    print('NOME: {}'.format(recuperar_fornecedor[cpf][0]))
    print('DATA DE NASCIMENTO: {}'.format(recuperar_fornecedor[cpf][1]))
    print('EMPRESA/CNPJ: {}'.format(recuperar_fornecedor[cpf][2]))
    print('TELEFONE: {}'.format(recuperar_fornecedor[cpf][3]))
    print('EMAIL: {}'.format(recuperar_fornecedor[cpf][4]))
    op_conf = input('Deseja realmente restaurar o fornecedor acima? S-(sim) N-(não): ')
    if op_conf.upper() == 'S' or op_conf.upper() == 'SIM':
      forn = recuperar_fornecedor[cpf]
      nome = forn[0]
      data = forn[1]
      empresa = forn[2]
      telefone = forn[3]
      email = forn[4]
      fornecedor[cpf] = [nome,data,empresa,telefone,email]
      recuperar_fornecedor.pop(cpf)
      print('Fornecedor deletado com sucesso!')
    else:
      print('O fornecedor não foi deletado!')
  else:
      print('O fornecedor informado não esta cadastrado no sistema!')

def atualizar_fornecedor(fornecedor):
  cpf = input("Informe o CPF do fornecedor: ").upper()
  cpf = while_cpf(cpf)
  verificar = verificar_indice(fornecedor,cpf)
  if verificar == True:
    nome = input("Nome do fornecedor: ").upper()
    data = input("Data de Nascimento (aa/aa/aaaa): ").upper()
    data = while_data(data)
    empresa = input("Empresa/CNPJ (NOME/CNPJ): ").upper()
    empresa = while_cnpj(empresa)
    telefone = input("Telefone (FORMATO: DDD/TELEFONE): ").upper()
    email = input("EMAIL: ").upper()
    email = while_email(email)
    fornecedor[cpf][0] = nome
    fornecedor[cpf][1] = data
    fornecedor[cpf][2] = empresa
    fornecedor[cpf][3] = telefone
    fornecedor[cpf][4] = email
    print("Fornecedor Cadastrado com Sucesso!")
  else:
    print('O fornecedor informado não esta cadastrado no sistema!')

def listar_todos_fornecedor(fornecedor):
  if len(fornecedor) > 0:
    cont = 1
    for item in fornecedor:
      print('')
      print('FORNECEDOR: ', cont)
      print('CPF: ',item)
      print('NOME: {}'.format(fornecedor[item][0]))
      print('DATA DE NASCIMENTO: {}'.format(fornecedor[item][1]))
      print('EMPRESA/CNPJ: {}'.format(fornecedor[item][2]))
      print('TELEFONE: {}'.format(fornecedor[item][3]))
      print('EMAIL: {}'.format(fornecedor[item][4]))
      cont += 1
  else:
    print('Não há fornecedores cadastrados no sistema!')

def pesquisar_fornecedor(fornecedor):
  fornecedor_pesquisar = input("Informe o CPF do fornecedor: ").upper()
  fornecedor_pesquisar = while_cpf(fornecedor_pesquisar)
  verificar = verificar_indice(fornecedor,fornecedor_pesquisar)
  if verificar == True:
    print('')
    print('CPF: ',fornecedor_pesquisar)
    print('PRODUTO: {}'.format(fornecedor[fornecedor_pesquisar][0]))
    print('DATA DE NASCIMENTO: {}'.format(fornecedor[fornecedor_pesquisar][1]))
    print('EMPRESA/CNPJ: {}'.format(fornecedor[fornecedor_pesquisar][2]))
    print('TELEFONE: {}'.format(fornecedor[fornecedor_pesquisar][3]))
    print('EMAIL: {}'.format(fornecedor[fornecedor_pesquisar][4]))
  else:
    print('O fornecedor informado não esta cadastrado no sistema!')

    
################## FUNÇÕES DO MÓDULO DE VENDAS ###################
def cadastrar_vendas(produtos,fornecedor,vendas):
  if len(fornecedor) > 0 or len(produtos) > 0:
    hora_da_compra = datetime.today().strftime('%d-%m-%y %H:%M:%S')
    cpf_cliente = input("Informe o CPF do cliente: ").upper()
    cpf_cliente = while_cpf(cpf_cliente)
    quantidade = input('Quantidades Compradas: ')
    nota_fical = sorteio_nota(cpf_cliente,lista_numero)
    referencia = input("Informe a referencia do produto: ").upper()
    quantidade = int(quantidade)
    verificar_produto = verificar_vendas(produtos,referencia,quantidade)
    if verificar_produto == False:
      while verificar_produto == False:
        referencia = input("O produto não está cadastrado, digite um produto válido: ").upper()
        verificar_produto = verificar_vendas(produtos,referencia,quantidade)
    nome_produto = produtos[referencia][0]
    valor_produto = calcula_preco(produtos,referencia,quantidade)
    marca_produto = produtos[referencia][3]
    fornecedor_produto = produtos[referencia][4]
    vendas[nota_fical] = [cpf_cliente,referencia,nome_produto,valor_produto,quantidade,marca_produto,fornecedor_produto,hora_da_compra]
    print("Produto Cadastrado com Sucesso!")
  else:
    print("Nenhum fornecedor ou produto cadastrado, por favor realize os cadastramentos!")

def listar_vendas(vendas):
  if len(vendas) > 0:
    for item in vendas:
      print('')
      print('''
      |----------------------------------------------|
      |                   NOTA FISCAL                |
      |----------------------------------------------|
      |              PARELHAS AUTOPEÇAS              |
      |           RUA BRASILINO GOMES MEIRA          |
      |      MARIA TERCEIRA PARELHAS-RN 59360000     |
      |            CNPJ: 89.786.412/0070-55          |
      |----------------------------------------------|
      | {}                                           |
      |----------------------------------------------|
      |NOTA FISCAL: {}
      |REFERÊNCIA DO PRODUTO: {} 
      |CPF DO CLIENTE: {}
      |PRODUTO: {}  
      |UNIDADES COMPRADAS: {} 
      |MARCA: {} 
      |VALOR TOTAL: {}  
      |----------------------------------------------|
      '''.format(vendas[item][6],item,vendas[item][1],vendas[item][0],vendas[item][2],vendas[item][4],vendas[item][5],vendas[item][3]))

# FUNÇÃO DE GERAR AUTOMATICAMENTE A CHAVE DA NOTA FISCAL 
def sorteio_nota(cpf_cliente,lista_numero):
  for i in range(4):
    numero = random.randint(1,100)
    lista_numero.append(str(numero))
  cpf = cpf_cliente.replace('.', '')
  cpf = cpf_cliente.replace('-', '')
  cpf = cpf_cliente.replace(' ', '')
  nota_fiscal = lista_numero[0]+lista_numero[2]+cpf+lista_numero[1]+lista_numero[3]
  lista_numero.clear()
  return nota_fiscal  

def recuperar_vendas(vendas,recuperar_vendas): # TESTAR
  venda_recuperar = input("Informe a nota fiscal: ").upper()
  verificar = verificar_indice(recuperar_vendas,venda_recuperar)
  if verificar == True:
    print('')
    print('NOTA FISCAL: ',venda_recuperar)
    print('CPF DO CLIENTE: {}'.format(recuperar_vendas[venda_recuperar][0]))
    print('REFERÊNCIA: {}'.format(recuperar_vendas[venda_recuperar][1]))
    print('PRODUTO: {}'.format(recuperar_vendas[venda_recuperar][2]))
    print('VALOR: {}'.format(recuperar_vendas[venda_recuperar][3]))
    print('QUANTIDADE: {}'.format(recuperar_vendas[venda_recuperar][4]))
    print('MARCA: {}'.format(recuperar_vendas[venda_recuperar][5]))
    print('FORNECEDOR: {}'.format(recuperar_vendas[venda_recuperar][6]))
    print('DATA DA COMPRA: {}'.format(recuperar_vendas[venda_recuperar][7]))
    op_conf = input('Deseja realmente recuperar a nota fiscal acima? S-(sim) N-(não): ')
    if op_conf.upper() == 'S' or op_conf.upper() == 'SIM':
      venda = recuperar_vendas[venda_recuperar]
      cpf_cliente = venda[0]
      referencia = venda[1]
      nome_produto = venda[2]
      valor_produto = venda[3]
      quantidade = venda[4]
      marca_produto = venda[5]
      fornecedor_produto = venda[6]
      data_compra = venda[7]
      vendas[venda_recuperar] = [cpf_cliente,referencia,nome_produto,valor_produto,quantidade,marca_produto,fornecedor_produto,data_compra]
      recuperar_vendas.pop(venda_recuperar)
      print('Nota fiscal recuperada com sucesso!')
    else:
      print('A Nota fiscal não foi recuperada!')
  else:
      print('A Nota fiscal informada não esta cadastrada no sistema!')

def atualizar_vendas(produtos,vendas,fornecedor): # TESTAR
  nota_fiscal = input("Informe a nota fiscal: ").upper()
  verificar = verificar_indice(vendas,nota_fiscal)
  if verificar == True:
    cpf_cliente = input("CPF do clinte: ").upper()
    cpf_cliente = while_cpf(cpf_cliente)
    referencia = input("Referência: ").upper()
    referencia_esta = verificar_indice(produtos,referencia)
    if referencia_esta == False:
      while referencia_esta == False:
        print("A referência é inválida!")
        referencia = input("Informe uma nova referencia: ").upper()
        referencia_esta = verificar_indice(produtos,referencia)
    nome_produto = produtos[referencia][0]
    quantidade = input("Quantidade: ")
    quantidade = int(quantidade)
    while quantidade < 0:
      quantidade = input("Informe uma quantidade válida: ")
      quantidade = int(quantidade)
    estoque_ant = int(vendas[nota_fiscal][4])
    if estoque_ant > quantidade:
      estoque1 = int(quantidade)
      estoque2 = int(vendas[nota_fiscal][4])
      estoque3 = abs(estoque1-estoque2)
      estoque = int(produtos[referencia][2])
      estoque+=estoque3
      produtos[referencia][2] = estoque
    elif quantidade == 0:
      estoque1 = int(produtos[referencia][2])
      estoque2 = int(vendas[nota_fiscal][4])
      estoque = estoque1 + estoque2
      produtos[referencia][2] = estoque
    elif estoque_ant == quantidade:
      valor_produto = calcula_preco(produtos,referencia,quantidade)
    else:
      estoque_ant = int(vendas[nota_fiscal][4])
      estoque1 = abs(estoque_ant - quantidade)
      estoque2 = int(produtos[referencia][2])
      estoque = abs(estoque1 - estoque2)
      produtos[referencia][2] = estoque
    valor_produto = calcula_preco(produtos,referencia,quantidade)
    marca_produto = produtos[referencia][3]
    fornecedor_produto = produtos[referencia][4]
    vendas[nota_fiscal][0] = cpf_cliente
    vendas[nota_fiscal][1] = referencia
    vendas[nota_fiscal][2] = nome_produto
    vendas[nota_fiscal][3] = valor_produto
    vendas[nota_fiscal][4] = quantidade
    vendas[nota_fiscal][5] = marca_produto
    vendas[nota_fiscal][6] = fornecedor_produto
    print("Nota fiscal Cadastrada com Sucesso!")
  else:
    print('A nota fiscal informada não esta cadastrada no sistema!')

def deletar_vendas(vendas,recuperar_vendas):  # TESTAR
  venda_deletar = input("Informe a nota fiscal: ").upper()
  verificar = verificar_indice(vendas,venda_deletar)
  if verificar == True:
    print('')
    print('NOTA FISCAL: ',venda_deletar)
    print('CPF DO CLIENTE: {}'.format(vendas[venda_deletar][0]))
    print('REFERÊNCIA: {}'.format(vendas[venda_deletar][1]))
    print('PRODUTO: {}'.format(vendas[venda_deletar][2]))
    print('VALOR: {}'.format(vendas[venda_deletar][3]))
    print('QUANTIDADE: {}'.format(vendas[venda_deletar][4]))
    print('MARCA: {}'.format(vendas[venda_deletar][5]))
    print('FORNECEDOR: {}'.format(vendas[venda_deletar][6]))
    print('DATA DA COMPRA: {}'.format(vendas[venda_deletar][7]))
    op_conf = input('Deseja realmente excluir a nota fiscal acima? S-(sim) N-(não): ')
    if op_conf.upper() == 'S' or op_conf.upper() == 'SIM':
      venda = vendas[venda_deletar]
      cpf_cliente = venda[0]
      referencia = venda[1]
      nome_produto = venda[2]
      valor_produto = venda[3]
      quantidade = venda[4]
      marca_produto = venda[5]
      fornecedor_produto = venda[6]
      data_compra = venda[7]
      recuperar_vendas[venda_deletar] = [cpf_cliente,referencia,nome_produto,valor_produto,quantidade,marca_produto,fornecedor_produto,data_compra]
      vendas.pop(venda_deletar)
      print('Nota fiscal deletada com sucesso!')
    else:
      print('A Nota fiscal não foi deletada!')
  else:
      print('A Nota fiscal informada não esta cadastrada no sistema!')

def pesquisar_vendas(vendas): # TESTAR
  venda_pesquisar = input("Informe a nota fiscal: ").upper()
  verificar = verificar_indice(vendas,venda_pesquisar)
  if verificar == True:
    print('')
    print('NOTA FISCAL: ',venda_pesquisar)
    print('CPF DO CLIENTE: {}'.format(vendas[venda_pesquisar][0]))
    print('REFERÊNCIA: {}'.format(vendas[venda_pesquisar][1]))
    print('PRODUTO: {}'.format(vendas[venda_pesquisar][2]))
    print('VALOR: {}'.format(vendas[venda_pesquisar][3]))
    print('QUANTIDADE: {}'.format(vendas[venda_pesquisar][4]))
    print('MARCA: {}'.format(vendas[venda_pesquisar][5]))
    print('FORNECEDOR: {}'.format(vendas[venda_pesquisar][6]))
    print('DATA DA COMPRA: {}'.format(vendas[venda_pesquisar][7]))
  else:
    print('A Nota fiscal informada não esta cadastrada no sistema!')
    

########### LIXEIRA DO SISTEMA
def lixeira(recuperar_produtos,recuperar_fornecedor,recuperar_vendas):
  print("""
    ---------------------
    | PRODUTOS EXLUÍDOS |  
    ---------------------""")
  listar_produto(recuperar_produtos)
  
  print("""
    -----------------------
    | FORNECEDOR EXLUÍDOS |  
    -----------------------""")
  listar_fornecedor(recuperar_fornecedor)
  
  print("""
    -----------------------
    |    VENDAS EXLUÍDOS   |  
    -----------------------""")
  listar_vendas(recuperar_vendas)