import random, time, os
from datetime import datetime

from pyparsing import dict_of
lista_numero = []
dic_produtos = 'produtos.txt'
dic_rec_produtos ='recupera_produto.txt'
dic_fornecedor = 'fornecedor.txt'
dic_rec_fornecedor ='recupera_fornecedor.txt'
dic_vendas = 'vendas.txt'
dic_rec_vendas ='recupera_vendas.txt'


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

def menu_principal():
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

        OPÇÃO: """)
  return menu

def menu_cadastro():
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

        OPÇÃO: """)
  return menu

def menu_fornecedor():
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

        OPÇÃO: """)
  return menu

def menu_vendas():
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

        OPÇÃO: """)
  return menu

def verificar_carater(variavel): ### FUNÇÃO VERIFACA EMAIL
    if "#" in variavel:
        return True
    else:
        return False

def while_caracter(caracter): ### FUNÇÃO VERIFICAR O EMAIL E LOOP ENQUANTO O EMAIL NÃO TIVER CORRETO
    caracter_esta = verificar_carater(caracter)
    if caracter_esta == True:
        while caracter_esta == True:
            print("ERRO, Entrada inválida!")
            caracter = input("Informe uma nova entrada válida: ").upper()
            caracter_esta = verificar_email(caracter)
    return caracter

def verifica_opcao(menu):   ### VERIFICA A VALIDADE DAS OPÇÕES
  tupla = ('1','2','3','4','5','6','0')
  while not(menu in tupla):
    print("Opção Inválida, tente novamente")
    menu = menu_cadastro()
  return menu

def calcula_preco(produtos,referencia,quantidade):  ### CALCULA PREÇO TOTAL DE UMA COMPRA
  preco = float(produtos[referencia][1])
  quanidade = int(quantidade)
  valor_total = preco*quanidade
  return str(valor_total)
     
def desconta_estoque(produtos,referencia,quantidade):  ### DESCONTA AS UNIDADES COMPRADAS NO ESTOQUE 
    estoque = int(produtos[referencia][2])
    quantidade = int(quantidade)
    estoque-=quantidade
    produtos[referencia][2] = str(estoque)


def listar_fornecedor(fornecedor):   ### INFORMA QUAIS FORNECEDORES ESTÃO CADASTRADOS 
  for pessoa in fornecedor:
    nome = (fornecedor.get(pessoa))[0]
    print("""
    CPF: %s
    Nome: %s
          """%(pessoa,nome))

def valida_cpf(cpf):   ### FUNÇÃO VERIFICA SE O CPF É VÁLIDO
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

def verificar_data(data): ### FUNÇÃO DE VALIDAR A DATA
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

def while_data(data): ### VERIFICAR A SE A FORMATAÇÃO DA DATA É VÁLIDA
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

def verificar_indice(dicionario,indice): ### VERIFICA SE DETERMINADO ELEMENTO ESTÁ CONTIDO NO DICIONÁRIO
  if indice in dicionario:
    return True
  else:
    return False

def while_referencia_v2(referencia,produtos): ### VERIFICA SE O PRODUTO ESTÁ NO SISTEMA. P/MÓDULO DE VENDAS
  referencia_esta = verificar_indice(produtos,referencia)
  if referencia_esta == False:
    while referencia_esta == False:
      print("Erro, a referência não está cadastrada!")
      referencia = input("Informe uma nova referencia: ").upper()
      referencia_esta = verificar_indice(produtos,referencia)
  return referencia

def while_referencia(referencia,produtos): ### VERIFICA SE O PRODUTO ESTÁ NO SISTEMA. P/MÓDULO DE PRODUTOS
  referencia_esta = verificar_indice(produtos,referencia)
  if referencia_esta == True:
    while referencia_esta == True:
      print("A referência já está cadastrada!")
      referencia = input("Informe uma nova referencia: ").upper()
      referencia_esta = verificar_indice(produtos,referencia)
  return referencia

def while_fornecedor(fornecedor, cpf): ### VERIFICA SE O FORNECEDOR ESTÁ NO SISTEMA
  verificar = verificar_indice(fornecedor,cpf)
  if verificar == False:
    while verificar == False:
      listar_fornecedor(fornecedor)
      cpf = input("Fornecedor não cadastrado, digite um fornecedor válido: ").upper()
      verificar = verificar_indice(fornecedor,cpf)
  return cpf

def while_cpf(cpf):  ### FUNÇÃO DE LAÇO PARA CPF's  INVÁLIDOS
  valor = valida_cpf(cpf)
  if valor == False:
    while valor == False:
      print("O CPF informado não é válido!")
      cpf = input("Informe um novo CPF: ")
      valor = valida_cpf(cpf)
  return cpf

##################################### MÓDULO DE PRODUTOS #########################################

def joga_no_dic(dicionario,arquivo): ### FUNÇÃO DE ABRIR O DICIONÁRIO DE FORNECEDORES
    try:
        arq = open(arquivo, 'r')
        for linha in arq.readlines():
            linha = linha.replace('\n', '')
            coluna = linha.split('#')
            dado_1 = coluna[0]
            dado_2 = coluna[1]
            dado_3 = coluna[2]
            dado_4 = coluna[3]
            dado_5 = coluna[4]
            dado_6 = coluna[5]
            dicionario[dado_1] = [dado_2,dado_3,dado_4,dado_5,dado_6]
        arq.close()
    except FileNotFoundError:
        pass

# def prod_vai_rec_prodtxt(recuperar_produtos_L): ### FUNÇÃO DE TRANSFERIR DADOS EXCLUÍDOS PARA O ARQUIVO.TXT
#   arq = open('recupera_produtos.txt', 'at')
#   for dado in recuperar_produtos_L:
#     arq.write('%s#%s#%s#%s#%s#%s\n'%(recuperar_produtos_L[0],recuperar_produtos_L[1],recuperar_produtos_L[2],recuperar_produtos_L[3],recuperar_produtos_L[4],recuperar_produtos_L[5]))
#     recuperar_produtos_L.clear()
#   arq.close()

def cadastrar_produto(fornecedor_D,produtos_D,produtos_L): ### FUNÇÃO DE CADASTRAR PRODUTOS
    joga_no_dic(produtos_D,dic_produtos)
    joga_no_dic(fornecedor_D,dic_fornecedor)
    referencia = input("Referência do produto: ").upper()
    referencia = while_caracter(referencia)
    referencia = while_referencia(referencia,produtos_D)
    nome_produto = input("Nome do produto: ").upper()
    nome_produto = while_caracter(nome_produto)
    valor_produto = input("Valor do produto: ").upper()
    valor_produto = while_caracter(valor_produto)
    estoque = input('Quantidade em estoque: ')
    estoque = while_caracter(estoque)
    marca_produto = input("Marca e Nome do veículo (FORMATO: FIAT/TOURO): ").upper()
    marca_produto = while_caracter(marca_produto)
    fornecedor_produto = input("CPF do Fornecedor: ").upper()
    fornecedor_produto = while_cpf(fornecedor_produto)
    fornecedor_produto = while_fornecedor(fornecedor_D, fornecedor_produto)
    produtos_L.append(referencia)
    produtos_L.append(nome_produto)
    produtos_L.append(valor_produto)
    produtos_L.append(estoque)
    produtos_L.append(marca_produto)
    produtos_L.append(fornecedor_produto)

    arq = open('produtos.txt', 'at')
    for dado in produtos_L:
        arq.write('%s#%s#%s#%s#%s#%s\n'%(produtos_L[0],produtos_L[1],produtos_L[2],produtos_L[3],produtos_L[4],produtos_L[5]))
        produtos_L.clear()
    produtos_D.clear()
    arq.close()
    print("Produto Cadastrado com Sucesso!")

def recuperar_produto(recuperar_produtos_D,recuperar_produtos_L,produtos_D,produtos_L): ### FUNÇÃO DE RECUPERAR PRODUTOS
    joga_no_dic(recuperar_produtos_D,dic_rec_produtos)
    joga_no_dic(produtos_D,dic_produtos)
    produto_recuperar = input('Informe a referência do produto: ').upper()
    verificar = verificar_indice(recuperar_produtos_D,produto_recuperar)
    if verificar == True:
        print('')
        print('REFERÊNCIA: ',produto_recuperar)
        print('NOME: {}'.format(recuperar_produtos_D[produto_recuperar][0]))
        print('VALOR: {}'.format(recuperar_produtos_D[produto_recuperar][1]))
        print('ESTOQUE: {}'.format(recuperar_produtos_D[produto_recuperar][2]))
        print('MARCA: {}'.format(recuperar_produtos_D[produto_recuperar][3]))
        print('FORNECEDOR: {}'.format(recuperar_produtos_D[produto_recuperar][4]))
        op_conf = input('Deseja Realmente recuperar este produto? S-(sim) N-(não) ')
        if op_conf.upper() == 'S':
            produto = recuperar_produtos_D[produto_recuperar]
            nome = produto[0]
            valor = produto[1]
            estoque = produto[2]
            marca = produto[3]
            fornecedor = produto[4]
            produtos_L.append(produto_recuperar)
            produtos_L.append(nome)
            produtos_L.append(valor)
            produtos_L.append(estoque)
            produtos_L.append(marca)
            produtos_L.append(fornecedor)
            lista_vai_arqtxt(produtos_L,dic_produtos)
            recuperar_produtos_D.pop(produto_recuperar)
            devolve_pro_arq(recuperar_produtos_D,recuperar_produtos_L,dic_rec_produtos)
            print('O produto foi recuperado com sucesso!')
    else:
        print('O produto informado não foi encontrado na lixeira do sistema!')

def atualizar_produto(produtos_D,fornecedor_D,produtos_L): ### FUNÇÃO DE ATUALIZAR DADOS DOS PRODUTOS
    joga_no_dic(produtos_D,dic_produtos)
    joga_no_dic(fornecedor_D,dic_fornecedor)
    produto_atualizar = input("Informe a referência do produto: ").upper()
    verificar = verificar_indice(produtos_D,produto_atualizar)
    if verificar == True:
        nome_produto = input("Novo nome do produto: ").upper()
        nome_produto = while_caracter(nome_produto)
        valor_produto = input("Novo valor do produto: ").upper()
        valor_produto = while_caracter(valor_produto)
        estoque_produto = input("Nova quantidade em estoque do produto: ").upper()
        estoque_produto = while_caracter(estoque_produto)
        marca_produto = input("Nova marca e Nome do veículo (FORMATO: FIAT/TOURO): ").upper()
        marca_produto = while_caracter(marca_produto)
        fornecedor_produto = input("Novo CPF do Fornecedor: ").upper()
        fornecedor_produto = while_cpf(fornecedor_produto)
        fornecedor_produto = while_fornecedor(fornecedor_D, fornecedor_produto)
        produtos_D[produto_atualizar][0] = nome_produto
        produtos_D[produto_atualizar][1] = valor_produto
        produtos_D[produto_atualizar][2] = estoque_produto
        produtos_D[produto_atualizar][3] = marca_produto
        produtos_D[produto_atualizar][4] = fornecedor_produto
        devolve_pro_arq(produtos_D,produtos_L,dic_produtos)
        print("Produto Cadastrado com Sucesso!")
    else:
        print('O produto informado não esta cadastrado no sistema!')

def pesquisar_produto(produtos_D): ### FUNÇÃO DE PESQUISAR POR PRODUTO ESPECÍFICO
    joga_no_dic(produtos_D,dic_produtos)
    produto_pesquisar = input("Informe a referência do produto: ").upper()
    verificar = verificar_indice(produtos_D,produto_pesquisar)
    if verificar == True:
        print('')
        print('REFERÊNCIA: ',produto_pesquisar)
        print('NOME: {}'.format(produtos_D[produto_pesquisar][0]))
        print('VALOR: {}'.format(produtos_D[produto_pesquisar][1]))
        print('ESTOQUE: {}'.format(produtos_D[produto_pesquisar][2]))
        print('MARCA: {}'.format(produtos_D[produto_pesquisar][3]))
        print('FORNECEDOR: {}'.format(produtos_D[produto_pesquisar][4]))
    else:
        print('O produto informado não esta cadastrado no sistema!')

def deletar_produto(produtos_D,produtos_L,recuperar_produtos_D,recuperar_produtos_L): ### FUNÇÃO DE DELETAR PRODUTO
    joga_no_dic(produtos_D,dic_produtos)
    joga_no_dic(recuperar_produtos_D,dic_rec_produtos)
    produto_deletar = input("Informe a referência do produto: ").upper()
    verificar = verificar_indice(produtos_D,produto_deletar)
    if verificar == True:
        print('')
        print('REFERÊNCIA: ',produto_deletar)
        print('NOME: {}'.format(produtos_D[produto_deletar][0]))
        print('VALOR: {}'.format(produtos_D[produto_deletar][1]))
        print('ESTOQUE: {}'.format(produtos_D[produto_deletar][2]))
        print('MARCA: {}'.format(produtos_D[produto_deletar][3]))
        print('FORNECEDOR: {}'.format(produtos_D[produto_deletar][4]))
        op_conf = input('Deseja realmente excluir o produto acima? S-(sim) N-(não)')
        if op_conf.upper() == 'S':
            referencia = produtos_D[produto_deletar]
            nome = referencia[0]
            valor = referencia[1]
            estoque = referencia[2]
            marca = referencia[3]
            fornecedor = referencia[4]
            recuperar_produtos_L.append(produto_deletar)
            recuperar_produtos_L.append(nome)
            recuperar_produtos_L.append(valor)
            recuperar_produtos_L.append(estoque)
            recuperar_produtos_L.append(marca)
            recuperar_produtos_L.append(fornecedor)
            lista_vai_arqtxt(recuperar_produtos_L,dic_rec_produtos)
            produtos_D.pop(produto_deletar)
            devolve_pro_arq(produtos_D,produtos_L,dic_produtos)
            print('Produto deletado com sucesso!')
        else:
            print('O produto não foi deletado!')
    else:
        print('O produto informado não esta cadastrado no sistema!')

def listar_produto(produtos_D): ### FUNÇÃO DE LISTAR TODOS OS PRODUTOS DO SISTEMA
    joga_no_dic(produtos_D,dic_produtos)
    if len(produtos_D) > 0:
        cont = 1
        for item in produtos_D:
            print('')
            print('Produto: ', cont)
            print('REFERÊNCIA: ',item)
            print('NOME: {}'.format(produtos_D[item][0]))
            print('VALOR: {}'.format(produtos_D[item][1]))
            print('ESTOQUE: {}'.format(produtos_D[item][2]))
            print('MARCA: {}'.format(produtos_D[item][3]))
            print('FORNECEDOR: {}'.format(produtos_D[item][4]))
            cont += 1
    else:
        print('Não há produtos cadastrados no sistema!')

##################################### MÓDULO DE FORNECEDORES #########################################

def verificar_email(email): ### FUNÇÃO VERIFACA EMAIL
    if "@" in email:
        return True
    else:
        return False

def while_email(email): ### FUNÇÃO VERIFICAR O EMAIL E LOOP ENQUANTO O EMAIL NÃO TIVER CORRETO
    email_esta = verificar_email(email)
    if email_esta == False:
        while email_esta == False:
            print("O E-mail digitado não é válido!")
            email = input("Informe um novo E-mail: ").upper()
            email_esta = verificar_email(email)
    return email

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

def while_cnpj(cnpj):  ### FUNÇÃO DE LAÇO PARA CNPJ's  INVÁLIDOS
  valor = validar_cnpj(cnpj)
  if valor == False:
    while valor == False:
      print("O CNPJ informado não é válido!")
      cnpj = input("Informe um novo CNPJ: ")
      valor = valida_cpf(cnpj)
  return cnpj

def cadastrar_fornecedor(fornecedor_D,fornecedor_L): ### FUNÇÃO DE CADASTRAR FORNECEDOR
    joga_no_dic(fornecedor_D,dic_fornecedor)
    cpf_fornecedor = input("Informe seu CPF (000.000.000-00): ").upper()
    cpf_fornecedor = while_cpf(cpf_fornecedor)
    cpf_esta = verificar_indice(fornecedor_D,cpf_fornecedor) 
    if cpf_esta == True:
        while cpf_esta == True:
            print("CPF já cadastrado por outro fornecedor!")
            cpf_fornecedor = input("Informe um novo CPF (000.000.000-00): ").upper()
            cpf_esta = verificar_indice(fornecedor_D,cpf_fornecedor)
    nome_fornecedor = input("Informe seu nome: ").upper()
    nome_fornecedor = while_caracter(nome_fornecedor)
    data_fornecedor = input("Informe sua data de nascimento (AA/AA/AAAA): ").upper()
    data_fornecedor = while_caracter(data_fornecedor)
    data_fornecedor = while_data(data_fornecedor)
    empresa_fornecedor = input("Informe sua empresa (NOME/CNPJ): ").upper()
    empresa_fornecedor = while_cnpj(empresa_fornecedor)
    fone_fornecedor = input("Informe seu telefone (9 DÍGITOS): ").upper()
    fone_fornecedor = while_caracter(fone_fornecedor)
    email_fornecedor = input("Informe seu e-mail: ").upper()
    email_fornecedor = while_caracter(email_fornecedor)
    email_fornecedor = while_email(email_fornecedor)
    fornecedor_L.append(cpf_fornecedor)
    fornecedor_L.append(nome_fornecedor)
    fornecedor_L.append(data_fornecedor)
    fornecedor_L.append(empresa_fornecedor)
    fornecedor_L.append(fone_fornecedor)
    fornecedor_L.append(email_fornecedor)

    arq = open('fornecedor.txt', 'at')
    for dado in fornecedor_L:
        arq.write('%s#%s#%s#%s#%s#%s\n'%(fornecedor_L[0],fornecedor_L[1],fornecedor_L[2],fornecedor_L[3],fornecedor_L[4],fornecedor_L[5]))
        fornecedor_L.clear()
    fornecedor_D.clear()
    arq.close()
    print("Cadastrado com Sucesso!")

def lista_vai_arqtxt(lista,arquivo):  ### FUNÇÃO DE TRANSFERIR DADOS EXCLUÍDOS PARA O ARQUIVO.TXT
    arq = open(arquivo, 'at')
    for dado in lista:
        arq.write('%s#%s#%s#%s#%s#%s\n'%(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5]))
        lista.clear()
    arq.close()

def devolve_pro_arq(dicionario,lista,arquivo): ### SALVA OS DADOS DO DICIONÁRIO DE VOLTA PARA O ARQUIVO.TXT
    arq = open(arquivo, 'w')
    arq.close()
    for item in dicionario:
        dado1 = item
        lista.append(dado1)
        dado2 = dicionario[item][0]
        lista.append(dado2)
        dado3 = dicionario[item][1]
        lista.append(dado3)
        dado4 = dicionario[item][2]
        lista.append(dado4)
        dado5 = dicionario[item][3]
        lista.append(dado5)
        dado6 = dicionario[item][4]
        lista.append(dado6)

        arq = open(arquivo, 'at')
        for dado in lista:
            arq.write('%s#%s#%s#%s#%s#%s\n'%(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5]))
            lista.clear()
        arq.close()

def deletar_fornecedor(fornecedor_D,recuperar_fornecedor_L,fornecedor_L,recuperar_fornecedor_D): ### FUNÇÃO DE DELETAR FORNECEDOR
  joga_no_dic(fornecedor_D,dic_fornecedor)
  joga_no_dic(recuperar_fornecedor_D,dic_rec_fornecedor)
  fornecedor_deletar = input("Informe o CPF do fornecedor: ").upper()
  fornecedor_deletar = while_cpf(fornecedor_deletar)
  verificar = verificar_indice(fornecedor_D,fornecedor_deletar)
  if verificar == True:
      print('')
      print('CPF: ',fornecedor_deletar)
      print('NOME: {}'.format(fornecedor_D[fornecedor_deletar][0]))
      print('DATA DE NASCIMENTO: {}'.format(fornecedor_D[fornecedor_deletar][1]))
      print('EMPRESA/CNPJ: {}'.format(fornecedor_D[fornecedor_deletar][2]))
      print('TELEFONE: {}'.format(fornecedor_D[fornecedor_deletar][3]))
      print('EMAIL: {}'.format(fornecedor_D[fornecedor_deletar][4]))
      op_conf = input('Deseja realmente excluir o fornecedor acima? S-(sim) N-(não): ')
      if op_conf.upper() == 'S' or op_conf.upper() == 'SIM':
          forn = fornecedor_D[fornecedor_deletar]
          nome = forn[0]
          data = forn[1]
          empresa = forn[2]
          telefone = forn[3]
          email = forn[4]
          recuperar_fornecedor_L.append(fornecedor_deletar)
          recuperar_fornecedor_L.append(nome)
          recuperar_fornecedor_L.append(data)
          recuperar_fornecedor_L.append(empresa)
          recuperar_fornecedor_L.append(telefone)
          recuperar_fornecedor_L.append(email)
          lista_vai_arqtxt(recuperar_fornecedor_L,dic_rec_fornecedor)
          fornecedor_D.pop(fornecedor_deletar)
          devolve_pro_arq(fornecedor_D,fornecedor_L,dic_fornecedor)
          print('Fornecedor deletado com sucesso!')
      else:
          print('O fornecedor não foi deletado!')
  else:
      print('O fornecedor informado não esta cadastrado no sistema!')

def recuperar_fornecedor(fornecedor_D,recuperar_fornecedor_D,recuperar_fornecedor_L,fornecedor_L): ### FUNÇÃO DE RECUPERAR FORNECEDOR
    joga_no_dic(fornecedor_D,dic_fornecedor)
    joga_no_dic(recuperar_fornecedor_D,dic_rec_fornecedor)
    cpf = input("Informe o CPF do fornecedor: ").upper()
    cpf = while_cpf(cpf)
    verificar = verificar_indice(recuperar_fornecedor_D,cpf)
    if verificar == True:
        print('')
        print('CPF: ',cpf)
        print('NOME: {}'.format(recuperar_fornecedor_D[cpf][0]))
        print('DATA DE NASCIMENTO: {}'.format(recuperar_fornecedor_D[cpf][1]))
        print('EMPRESA/CNPJ: {}'.format(recuperar_fornecedor_D[cpf][2]))
        print('TELEFONE: {}'.format(recuperar_fornecedor_D[cpf][3]))
        print('EMAIL: {}'.format(recuperar_fornecedor_D[cpf][4]))
        op_conf = input('Deseja realmente restaurar o fornecedor acima? S-(sim) N-(não): ')
        if op_conf.upper() == 'S' or op_conf.upper() == 'SIM':
            forn = recuperar_fornecedor_D[cpf]
            nome = forn[0]
            data = forn[1]
            empresa = forn[2]
            telefone = forn[3]
            email = forn[4]
            fornecedor_L.append(cpf)
            fornecedor_L.append(nome)
            fornecedor_L.append(data)
            fornecedor_L.append(empresa)
            fornecedor_L.append(telefone)
            fornecedor_L.append(email)
            lista_vai_arqtxt(fornecedor_L,dic_fornecedor)
            recuperar_fornecedor_D.pop(cpf)
            devolve_pro_arq(recuperar_fornecedor_D,recuperar_fornecedor_L,dic_rec_fornecedor)
            print('Fornecedor restaurado com sucesso!')
        else:
            print('O fornecedor não foi restaurado!')
    else:
        print('O fornecedor informado não esta cadastrado no sistema!')

def atualizar_fornecedor(fornecedor_D,fornecedor_L): ### FUNÇÃO DE ATUALIZAR FORNECEDOR
    joga_no_dic(fornecedor_D,dic_fornecedor)
    cpf = input("Informe o CPF do fornecedor: ").upper()
    cpf = while_cpf(cpf)
    verificar = verificar_indice(fornecedor_D,cpf)
    if verificar == True:
        nome = input("Nome do fornecedor: ").upper()
        nome = while_caracter(nome)
        data = input("Data de Nascimento (aa/aa/aaaa): ").upper()
        data = while_caracter(data)
        data = while_data(data)
        empresa = input("Empresa/CNPJ (NOME/CNPJ): ").upper()
        empresa = while_cnpj(empresa)
        telefone = input("Telefone (FORMATO: DDD/TELEFONE): ").upper()
        telefone = while_caracter(telefone)
        email = input("EMAIL: ").upper()
        email = while_caracter(email)
        email = while_email(email)
        fornecedor_D[cpf][0] = nome
        fornecedor_D[cpf][1] = data
        fornecedor_D[cpf][2] = empresa
        fornecedor_D[cpf][3] = telefone
        fornecedor_D[cpf][4] = email
        devolve_pro_arq(fornecedor_D,fornecedor_L,dic_fornecedor)
        print("Fornecedor Cadastrado com Sucesso!")
    else:
        print('O fornecedor informado não esta cadastrado no sistema!')
    
def listar_todos_fornecedor(fornecedor_D): ### FUNÇÃO DE LISTAR TODOS OS FORNECEDORES CADASTRADOS
    joga_no_dic(fornecedor_D,dic_fornecedor)
    if len(fornecedor_D) > 0:
        cont = 1
        for item in fornecedor_D:
            print('')
            print('FORNECEDOR: ', cont)
            print('CPF: ',item)
            print('NOME: {}'.format(fornecedor_D[item][0]))
            print('DATA DE NASCIMENTO: {}'.format(fornecedor_D[item][1]))
            print('EMPRESA/CNPJ: {}'.format(fornecedor_D[item][2]))
            print('TELEFONE: {}'.format(fornecedor_D[item][3]))
            print('EMAIL: {}'.format(fornecedor_D[item][4]))
            cont += 1
    else:
        print('Não há fornecedores cadastrados no sistema!')

def pesquisar_fornecedor(fornecedor_D): ### FUNÇÃO DE PESQUISAR POR FORNECEDOR ESPECÍFICO
    joga_no_dic(fornecedor_D,dic_fornecedor)
    fornecedor_pesquisar = input("Informe o CPF do fornecedor: ").upper()
    fornecedor_pesquisar = while_cpf(fornecedor_pesquisar)
    verificar = verificar_indice(fornecedor_D,fornecedor_pesquisar)
    if verificar == True:
        print('')
        print('CPF: ',fornecedor_pesquisar)
        print('NOME: {}'.format(fornecedor_D[fornecedor_pesquisar][0]))
        print('DATA DE NASCIMENTO: {}'.format(fornecedor_D[fornecedor_pesquisar][1]))
        print('EMPRESA/CNPJ: {}'.format(fornecedor_D[fornecedor_pesquisar][2]))
        print('TELEFONE: {}'.format(fornecedor_D[fornecedor_pesquisar][3]))
        print('EMAIL: {}'.format(fornecedor_D[fornecedor_pesquisar][4]))
    else:
        print('O fornecedor informado não esta cadastrado no sistema!')

####################################### MÓDULO DE VENDAS ###########################################

def joga_no_dic_mod_vendas(dicionario,arquivo): ### FUNÇÃO DE ABRIR O DICIONÁRIO DE VENDAS
    try:
        arq = open(arquivo, 'r')
        for linha in arq.readlines():
            linha = linha.replace('\n', '')
            coluna = linha.split('#')
            dado1 = coluna[0]
            dado2 = coluna[1]
            dado3 = coluna[2]
            dado4 = coluna[3]
            dado5 = coluna[4]
            dado6 = coluna[5]
            dado7 = coluna[6]
            dado8 = coluna[7]
            dado9 = coluna[8]

            dicionario[dado1] = [dado2,dado3,dado4,dado5,dado6,dado7,dado8,dado9]    
        arq.close()
    except FileNotFoundError:
        pass

def sorteio_nota(cpf,lista_numero): ### FUNÇÃO DE GERAR A CHAVE DA NOTA FISCAL
    for i in range(4):
        numero = random.randint(1,100)
        lista_numero.append(str(numero))
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    cpf = cpf.replace(' ', '')
    nota_fiscal = lista_numero[0]+lista_numero[2]+cpf+lista_numero[1]+lista_numero[3]
    lista_numero.clear()
    return nota_fiscal

def devolve_pro_arq_mod_vendas(dicionario,lista,arquivo): ### SALVA OS DADOS DO DICIONÁRIO DE VOLTA PARA O ARQUIVO.TXT
    arq = open(arquivo, 'w')
    arq.close()
    for item in dicionario:
        nota_fiscal = item
        lista.append(nota_fiscal)
        cpf_cliente = dicionario[item][0]
        lista.append(cpf_cliente)
        ref_pro = dicionario[item][1]
        lista.append(ref_pro)
        nome_pro = dicionario[item][2]
        lista.append(nome_pro)
        valor_pro = dicionario[item][3]
        lista.append(valor_pro)
        qtd_compra = dicionario[item][4]
        lista.append(qtd_compra)
        marca = dicionario[item][5]
        lista.append(marca)
        fornecedor = dicionario[item][6]
        lista.append(fornecedor)
        data_compra = dicionario[item][7]
        lista.append(data_compra)

        arq = open('vendas.txt', 'at')
        for dado in lista:
            arq.write('%s#%s#%s#%s#%s#%s#%s#%s#%s\n'%(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8]))
            lista.clear()
        arq.close()

def lista_vai_arq_mod_vendastxt(lista,arquivo): ### FUNÇÃO DE TRANSFERIR DADOS RECUPERADOS PARA O ARQUIVO.TXT
  arq = open(arquivo, 'at')
  for dado in lista:
    arq.write('%s#%s#%s#%s#%s#%s#%s#%s#%s\n'%(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8]))
    lista.clear()
  arq.close()

def cadastrar_vendas(vendas_D,produtos_D,fornecedor_D,vendas_L,produtos_L): ### FUNÇÃO DE CADASTRAR NOTA FISCAL
    joga_no_dic_mod_vendas(vendas_D,dic_vendas)
    joga_no_dic(produtos_D,dic_produtos)
    joga_no_dic(fornecedor_D,dic_fornecedor)
    referencia = input("Informe a referencia do produto: ").upper()
    referencia = while_caracter(referencia)
    referencia = while_referencia_v2(referencia,produtos_D)
    if int(produtos_D[referencia][2]) > 0:
        quantidade = input('Quantidades Compradas: ')
        quantidade = while_caracter(quantidade)
        quantidade = int(quantidade)
        if quantidade <= int(produtos_D[referencia][2]):
            desconta_estoque(produtos_D,referencia,quantidade)
            hora_da_compra = datetime.today().strftime('%d-%m-%y %H:%M:%S')
            cpf_cliente = input("Informe o CPF do cliente: ").upper()
            cpf_cliente = while_cpf(cpf_cliente)
            nota_fical = sorteio_nota(cpf_cliente,lista_numero)
            nome_produto = produtos_D[referencia][0]
            valor_produto = calcula_preco(produtos_D,referencia,quantidade)
            marca_produto = produtos_D[referencia][3]
            fornecedor_produto = produtos_D[referencia][4]
            vendas_L.append(nota_fical)
            vendas_L.append(cpf_cliente)
            vendas_L.append(referencia)
            vendas_L.append(nome_produto)
            vendas_L.append(valor_produto)
            vendas_L.append(quantidade)
            vendas_L.append(marca_produto)
            vendas_L.append(fornecedor_produto)
            vendas_L.append(hora_da_compra)

            arq = open('vendas.txt', 'at')
            for dado in vendas_L:
                arq.write('%s#%s#%s#%s#%s#%s#%s#%s#%s\n'%(vendas_L[0],vendas_L[1],vendas_L[2],vendas_L[3],vendas_L[4],vendas_L[5],vendas_L[6],vendas_L[7],vendas_L[8]))
                vendas_L.clear()
            vendas_D.clear()
            arq.close()
            devolve_pro_arq(produtos_D,produtos_L,dic_produtos)
            print("Produto Cadastrado com Sucesso!")
        else:
            print('Erro, a quantidade de compra é superior que a do estoque!')
            op = input('''
            Opções: 1-  VOLTAR AO MENU PRINCIAL
                    2-  TENTAR NOVAMENTE            R: ''')
            if op == '1':
                pass
            else:
                cadastrar_vendas(vendas_D,produtos_D,fornecedor_D,vendas_L,produtos_L)
    else:
        print('Erro, produto está em falta no estoque!')

def listar_vendas(vendas_D): ### FUNÇÃO DE LISTAR TODAS AS NOTAS FICAIS DO SISTEMA
    joga_no_dic_mod_vendas(vendas_D,dic_vendas)
    if len(vendas_D) > 0:
        for item in vendas_D:
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
            |NOME DO PRODUTO: {}  
            |UNIDADES COMPRADAS: {} 
            |MARCA: {} 
            |VALOR TOTAL: R$ {}  
            |----------------------------------------------|
            '''.format(vendas_D[item][7],item,vendas_D[item][1],vendas_D[item][2],vendas_D[item][4],vendas_D[item][5],vendas_D[item][3]))

def recuperar_vendas(vendas_D,recuperar_vendas_D,vendas_L,recuperar_vendas_L): ### FUNÇÃO DE RECUPERAR NOTAS FISCAIS
    joga_no_dic_mod_vendas(vendas_D,dic_vendas)
    joga_no_dic_mod_vendas(recuperar_vendas_D,dic_rec_vendas)
    venda_recuperar = input("Informe a nota fiscal: ").upper()
    verificar = verificar_indice(recuperar_vendas_D,venda_recuperar)
    if verificar == True:
        print('')
        print('NOTA FISCAL: ',venda_recuperar)
        print('CPF DO CLIENTE: {}'.format(recuperar_vendas_D[venda_recuperar][0]))
        print('REFERÊNCIA: {}'.format(recuperar_vendas_D[venda_recuperar][1]))
        print('PRODUTO: {}'.format(recuperar_vendas_D[venda_recuperar][2]))
        print('VALOR: {}'.format(recuperar_vendas_D[venda_recuperar][3]))
        print('QUANTIDADE: {}'.format(recuperar_vendas_D[venda_recuperar][4]))
        print('MARCA: {}'.format(recuperar_vendas_D[venda_recuperar][5]))
        print('FORNECEDOR: {}'.format(recuperar_vendas_D[venda_recuperar][6]))
        print('DATA DA COMPRA: {}'.format(recuperar_vendas_D[venda_recuperar][7]))
        op_conf = input('Deseja realmente recuperar a nota fiscal acima? S-(sim) N-(não): ')
        if op_conf.upper() == 'S' or op_conf.upper() == 'SIM':
            venda = recuperar_vendas_D[venda_recuperar]
            cpf_cliente = venda[0]
            referencia = venda[1]
            nome_produto = venda[2]
            valor_produto = venda[3]
            quantidade = venda[4]
            marca_produto = venda[5]
            fornecedor_produto = venda[6]
            data_compra = venda[7]
            vendas_L.append(venda_recuperar)
            vendas_L.append(cpf_cliente)
            vendas_L.append(referencia)
            vendas_L.append(nome_produto)
            vendas_L.append(valor_produto)
            vendas_L.append(quantidade)
            vendas_L.append(marca_produto)
            vendas_L.append(fornecedor_produto)
            vendas_L.append(data_compra)
            lista_vai_arq_mod_vendastxt(vendas_L,dic_vendas)
            recuperar_vendas_D.pop(venda_recuperar)
            devolve_pro_arq_mod_vendas(recuperar_vendas_D,recuperar_vendas_L,dic_rec_vendas)
            print('Nota fiscal recuperada com sucesso!')
        else:
            print('A Nota fiscal não foi recuperada!')
    else:
        print('A Nota fiscal informada não esta cadastrada no sistema!')

def devolve_estoque_mod_vend(dicionario,indice,dicionario_2,indice_2): ### DEVOLVE A QUANTIDADE DE PRODUTOS COMPRADOS AO ESTOQUE EM CASO DE ATUALIZAÇÃO DA NOTA DISCAL
    estoque = int(dicionario[indice][2])
    quantidae_anterior = int(dicionario_2[indice_2][4])
    devolve = estoque + quantidae_anterior
    dicionario[indice][2] = str(devolve)

def atualizar_vendas(vendas_D,fornecedor_D,vendas_L,produtos_D,produtos_L): ### FUNÇÃO DE ATUALIZAR NOTAS FISCAIS
    joga_no_dic_mod_vendas(vendas_D,dic_vendas)
    joga_no_dic(fornecedor_D,dic_fornecedor)
    joga_no_dic(produtos_D,dic_produtos)
    nota_fiscal = input("Informe a nota fiscal: ").upper()
    verificar = verificar_indice(vendas_D,nota_fiscal)
    if verificar == True:
        cpf_cliente = input("CPF do clinte: ").upper()
        cpf_cliente = while_cpf(cpf_cliente)
        referencia = vendas_D[nota_fiscal][1]
        devolve_estoque_mod_vend(produtos_D,referencia,vendas_D,nota_fiscal)
        quantidade = input("Quantidade: ")
        quantidade = while_caracter(quantidade)
        quantidade = int(quantidade)
        if quantidade <= int(produtos_D[referencia][2]):
            desconta_estoque(produtos_D,referencia,quantidade)
            novo_valor = calcula_preco(produtos_D,referencia,quantidade)
            vendas_D[nota_fiscal][3] = novo_valor
            vendas_D[nota_fiscal][0] = cpf_cliente
            vendas_D[nota_fiscal][1] = referencia
            vendas_D[nota_fiscal][4] = quantidade
            devolve_pro_arq_mod_vendas(vendas_D,vendas_L,dic_vendas)
            devolve_pro_arq(produtos_D,produtos_L,dic_produtos)
            print("Nota fiscal Cadastrada com Sucesso!")
        else:
            print('Erro, a quantidade de compra é superior que a do estoque!')
            op = input('''
            Opções: 1-  VOLTAR AO MENU PRINCIAL
                    2-  TENTAR NOVAMENTE            R: ''')
            if op == '1':
                pass
            else:
                atualizar_vendas(vendas_D,fornecedor_D,vendas_L,produtos_D,produtos_L)
    else:
        print('A nota fiscal informada não esta cadastrada no sistema!')

def deletar_vendas(vendas_D,recuperar_vendas_D,recuperar_vendas_L,vendas_L):  ### FUNÇÃO DE DELETAR NOTAS FISCAIS 
    joga_no_dic_mod_vendas(vendas_D,dic_vendas)
    joga_no_dic_mod_vendas(recuperar_vendas_D,dic_rec_vendas)
    venda_deletar = input("Informe a nota fiscal: ").upper()
    verificar = verificar_indice(vendas_D,venda_deletar)
    if verificar == True:
        print('')
        print('NOTA FISCAL: ',venda_deletar)
        print('CPF DO CLIENTE: {}'.format(vendas_D[venda_deletar][0]))
        print('REFERÊNCIA: {}'.format(vendas_D[venda_deletar][1]))
        print('PRODUTO: {}'.format(vendas_D[venda_deletar][2]))
        print('VALOR: {}'.format(vendas_D[venda_deletar][3]))
        print('QUANTIDADE: {}'.format(vendas_D[venda_deletar][4]))
        print('MARCA: {}'.format(vendas_D[venda_deletar][5]))
        print('FORNECEDOR: {}'.format(vendas_D[venda_deletar][6]))
        print('DATA DA COMPRA: {}'.format(vendas_D[venda_deletar][7]))
        op_conf = input('Deseja realmente excluir a nota fiscal acima? S-(sim) N-(não): ')
        if op_conf.upper() == 'S' or op_conf.upper() == 'SIM':
            venda = vendas_D[venda_deletar]
            cpf_cliente = venda[0]
            referencia = venda[1]
            nome_produto = venda[2]
            valor_produto = venda[3]
            quantidade = venda[4]
            marca_produto = venda[5]
            fornecedor_produto = venda[6]
            data_compra = venda[7]
            recuperar_vendas_L.append(venda_deletar)
            recuperar_vendas_L.append(cpf_cliente)
            recuperar_vendas_L.append(referencia)
            recuperar_vendas_L.append(nome_produto)
            recuperar_vendas_L.append(valor_produto)
            recuperar_vendas_L.append(quantidade)
            recuperar_vendas_L.append(marca_produto)
            recuperar_vendas_L.append(fornecedor_produto)
            recuperar_vendas_L.append(data_compra)
            lista_vai_arq_mod_vendastxt(recuperar_vendas_L,dic_rec_vendas)
            vendas_D.pop(venda_deletar)
            devolve_pro_arq_mod_vendas(vendas_D,vendas_L,dic_vendas)
            print('Nota fiscal deletada com sucesso!')
        else:
            print('A Nota fiscal não foi deletada!')
    else:
        print('A Nota fiscal informada não esta cadastrada no sistema!')

def pesquisar_vendas(vendas_D): ### FUNÇÃO DE PESQUISAR NOTAS FISCAIS
    joga_no_dic_mod_vendas(vendas_D,dic_vendas)
    venda_pesquisar = input("Informe a nota fiscal: ").upper()
    verificar = verificar_indice(vendas_D,venda_pesquisar)
    if verificar == True:
        print('')
        print('NOTA FISCAL: ',venda_pesquisar)
        print('CPF DO CLIENTE: {}'.format(vendas_D[venda_pesquisar][0]))
        print('REFERÊNCIA: {}'.format(vendas_D[venda_pesquisar][1]))
        print('PRODUTO: {}'.format(vendas_D[venda_pesquisar][2]))
        print('VALOR: {}'.format(vendas_D[venda_pesquisar][3]))
        print('QUANTIDADE: {}'.format(vendas_D[venda_pesquisar][4]))
        print('MARCA: {}'.format(vendas_D[venda_pesquisar][5]))
        print('FORNECEDOR: {}'.format(vendas_D[venda_pesquisar][6]))
        print('DATA DA COMPRA: {}'.format(vendas_D[venda_pesquisar][7]))
        
    else:
        print('A Nota fiscal informada não esta cadastrada no sistema!')

###################################### MÓDULO DE LIXEIAR ######################################

def lixeira(recuperar_produtos,recuperar_fornecedor,recuperar_vendas):
    print("""
---------------------
| PRODUTOS EXLUÍDOS |  
---------------------""")
    joga_no_dic(recuperar_produtos,dic_rec_produtos)
    for item in recuperar_produtos:
            print('REFERÊNCIA: ',item)
            print('NOME: {}'.format(recuperar_produtos[item][0]))
            print('VALOR: {}'.format(recuperar_produtos[item][1]))
            print('ESTOQUE: {}'.format(recuperar_produtos[item][2]))
            print('MARCA: {}'.format(recuperar_produtos[item][3]))
            print('FORNECEDOR: {}'.format(recuperar_produtos[item][4]))
            print('')

    print("""
-----------------------
| FORNECEDOR EXLUÍDOS |  
-----------------------""")
    joga_no_dic(recuperar_fornecedor,dic_rec_fornecedor)
    for item in recuperar_fornecedor:
            print('CPF: ',item)
            print('NOME: {}'.format(recuperar_fornecedor[item][0]))
            print('DATA DE NASCIMENTO: {}'.format(recuperar_fornecedor[item][1]))
            print('EMPRESA/CNPJ: {}'.format(recuperar_fornecedor[item][2]))
            print('TELEFONE: {}'.format(recuperar_fornecedor[item][3]))
            print('EMAIL: {}'.format(recuperar_fornecedor[item][4]))
            print('')
  
    print("""
-----------------------
|    VENDAS EXLUÍDOS   |  
-----------------------""")
    joga_no_dic_mod_vendas(recuperar_vendas,dic_rec_vendas)
    for nota in recuperar_vendas:
        print('NOTA FISCAL: ',nota)
        print('CPF DO CLIENTE: {}'.format(recuperar_vendas[nota][0]))
        print('REFERÊNCIA: {}'.format(recuperar_vendas[nota][1]))
        print('PRODUTO: {}'.format(recuperar_vendas[nota][2]))
        print('VALOR: {}'.format(recuperar_vendas[nota][3]))
        print('QUANTIDADE: {}'.format(recuperar_vendas[nota][4]))
        print('MARCA: {}'.format(recuperar_vendas[nota][5]))
        print('FORNECEDOR: {}'.format(recuperar_vendas[nota][6]))
        print('DATA DA COMPRA: {}'.format(recuperar_vendas[nota][7]))
        print('')