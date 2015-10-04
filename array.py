iniciar = raw_input('Digite 1 para iniciar o sistema e 0 para sair: ')

while iniciar == '1':

    array = []
    resultado = []
    saida = ''

    raw_input('Vamos configurar o sistema!(Tecle ENTER para iniciar)')

    try:
        quantidade_testes = int(raw_input('Digite quantos testes deseja realizar: '))

        if quantidade_testes >= 1 and quantidade_testes <= 10:
            for teste in range(0,quantidade_testes):
                tamanho = int(raw_input('Digite o tamanho para o array %d: ' % teste))
                if tamanho >= 1 and tamanho <= 10**5:
                    valores = str(raw_input('Digite os valores do array separados por espacos em branco: ')).split()
                    if len(valores) == tamanho:
                        array.append(valores)
                    else:
                        print 'Quantidade de elementos no array diferente do configuradio. \n ... o sistema sera reiniciado ...'
                        break
                else:
                    print 'O tamanho do array deve ser maior que 1 e menor que 100000.\n ... o sistema sera reiniciado ...'
                    break
        else:
            print 'Quantidade de testes deve ser maior que 1 e menor que 10.\n ... o sistema sera reiniciado ...'

    except:
        print 'Valor informado invalido para o sistema'

    # convertendo valores para inteiro
    for i in range(0, len(array)):
        for b in range(0, len(array[i])):
            array[i][b] = int(array[i][b])

    for i in range(0, len(array)):
        for b in range(0, len(array[i])):

            soma_equerda = 0
            soma_direita = 0

            for c in range(0, b):
                soma_equerda += array[i][c]

            for c in range(b+1, len(array[i])):
                soma_direita += array[i][c]

            if soma_equerda == soma_direita:
                resultado.append('SIM')
            else:
                resultado.append('NAO')

            for result in range(1, len(resultado)-1):
                if resultado[result] == 'SIM':
                    saida = 'SIM'
                else:
                    saida = 'NAO'

        print saida

    iniciar = raw_input('Digite 1 para iniciar o sistema e 0 para sair: : ')

print '... Obrigado por usar o sistema ...'