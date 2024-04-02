# ------------ inicio das variaveis locais -------------------
lista_colaboradores = []
id_global = 0


# ------------ fim das variaveis locais ----------------------

# inicio funcao cadastrar_colaborador(id)
def cadastrar_colaborador(id):
    print('******************************************************************************* \n' +
          '---------------------- MENU CADASTRAR COLABORADOR ----------------------------- \n')

    nome_colaborador = input('Digite o NOME do colaborador: ')
    setor_colaborador = input('Digite o SETOR do colaborador: ')
    salario_colaborador = int(input('Digite o SALÁRIO (R$) do colaborador: '))

    dicionario_colaborador = {'codigo': id,
                              'nome': nome_colaborador,
                              'setor': setor_colaborador,
                              'salario': salario_colaborador}

    lista_colaboradores.append(dicionario_colaborador.copy())


# fim funcao cadastrar_colaborador(id)

# inicio funcao consultar_colaborador
def consultar_colaborador():
    while True:
        opcao_menu_consultar = input(
            '******************************************************************************* \n' +
            '---------------------- MENU CONSULTAR COLABORADOR ----------------------------- \n' +
            'Escolha a opção desejada: \n' +
            '1 - Consultar Todos os Colaboradores \n' +
            '2 - Consultar Colaborador por ID \n' +
            '3 - Consultar Colaborador(es) por Setor \n' +
            '4 - Retornar \n' +
            '>>')
        print('')

        if opcao_menu_consultar == '1':
            print('Você escolheu a opção Consultar TODOS os Colaboradores')
            for colaborador in lista_colaboradores:  # colaborador vai varrer toda a lista de colaboradores
                print('------------------------------------------------------')
                for key, value in colaborador.items():  # varrer todos os conjuntos de chave e valor do dicionario colaborador
                    print('{}: {}'.format(key, value))
                print('------------------------------------------------------')
                print(' ')

        elif opcao_menu_consultar == '2':
            print('Você escolheu Consultar Colaborador por ID')
            print(' ')

            id_desejado = int(input('Entre com o ID de Colaborador desejado: '))

            for colaborador in lista_colaboradores:
                if colaborador[
                    'codigo'] == id_desejado:  # o valor do campo codigo desse dicionario é igual ao id_desejado?
                    print('------------------------------------------------------')
                    for key, value in colaborador.items():  # varrer todos os conjuntos de chave e valor do dicionario produto
                        print('{}: {}'.format(key, value))
                print('------------------------------------------------------')
                print(' ')

        elif opcao_menu_consultar == '3':
            print('Você escolheu Consultar Colaborador por SETOR')
            print(' ')
            setor_desejado = input('Entre com o SETOR desejado: ')
            for colaborador in lista_colaboradores:
                if colaborador[
                    'setor'] == setor_desejado:  # o valor do campo codigo desse dicionario é igual ao setor_desejado?
                    print('------------------------------------------------------')
                    for key, value in colaborador.items():  # varrer todos os conjuntos de chave e valor do dicionario colaborador
                        print('{}: {}'.format(key, value))
                print('------------------------------------------------------')
                print(' ')

        elif opcao_menu_consultar == '4':
            return  # sai da funcao consultar e volta para o MENU PRINCIPAL

        else:
            print('Opção inválida! Tente novamente')
            continue  # volta para o inicio do laço


# fim funcao consultar_colaborador()

# inicio funcao remover_colaborador()
def remover_colaborador():
    print('')
    id_desejado = int(input('Entre com o ID de Colaborador que você deseja remover: '))
    for colaborador in lista_colaboradores:
        if colaborador['codigo'] == id_desejado:  # o valor do campo codigo desse dicionario é igual ao id_desejado?
            lista_colaboradores.remove(colaborador)
            print('Colaborador Removido')


# fim funcao remover_colaborador()

# ------------- PROGRAMA PRINCIPAL ----------------------------

# Exercicio 04 de 04 da atividade prática
print('---------------- Bem vindo à Empresa do Matheus Alves de Souza ----------------')
print('')
while True:
    print(' ')
    opcao_menu_principal = input('******************************************************************************* \n' +
                                 '----------------------------- MENU PRINCIPAL ---------------------------------- \n' +
                                 'Escolha a opção desejada: \n' +
                                 '1 - Cadastrar Colaborador \n' +
                                 '2 - Consultar Colaborador(es) \n' +
                                 '3 - Remover Colaborador \n' +
                                 '4 - Sair \n' +
                                 '>>')
    print('')

    if opcao_menu_principal == '1':
        id_global += 1
        cadastrar_colaborador(id_global)
    elif opcao_menu_principal == '2':
        consultar_colaborador()
    elif opcao_menu_principal == '3':
        remover_colaborador()
    elif opcao_menu_principal == '4':
        break  # encerra e sai do laço
    else:
        print('Opção inválida! Tente novamente')
        continue  # volta para o inicio do laço
