iniciar = raw_input('Digite 1 para iniciar o sistema e 0 para sair: ')

while iniciar == '1':

    raw_input('Vamos configurar o sistema!(Tecle ENTER para iniciar)')
    dados = raw_input('Digite um valor inteiro para quantidade de produtos do sistema e separado por espaco digite o valor que tem na carteira: ')
    valores = raw_input('Digite os valores do produto separando por espaco os valores entre si: ')

    # transformando as entradas em array para manipulacao dos dados
    dados = dados.split(' ')
    valores = valores.split(' ')

    # convertento os dados do array para Inteiro para melhor execucao do sistema
    for a in range(0, len(dados)):
        dados[a] = int(dados[a])

    for a in range(0, len(valores)):
        valores[a] = int(valores[a])

    # organizando meu array para melhor experiencia do usuario
    brinquedos = list(set(valores))
    brinquedos.sort()

    quant_compra = 0

    if dados[0] >= 1 and dados[0] <= 10**5:

        if dados[1] >= 1 and dados[1] <= 10**9:

            try:
                if dados[0] >= len(brinquedos):
                    # varrendo minha loja e escolhendo os brinquedos considerando os criterios de maximizar as compras definidos na questao
                    for valor in brinquedos:
                        if dados[1] >= valor:
                            quant_compra+=1
                            dados[1] = dados[1]-valor
                    print 'Sobra para mim R$ '+str(dados[1])
                    print 'E possivel comprar '+str(quant_compra)+' brinquedos. \n ... o sistema foi reiniciado ...'
                else:
                    print 'Quantidade de brinquedos diferente do informado nas configuracoes.\n ... o sistema foi reiniciado ...'

            except:
                print 'Valores invalidos para configurar o sistema \n ... o sistema foi reiniciado ...'
        else:
            print 'O valor na minha carteira de Marco deve ser maior ou igual a 1 e menor ou igual que 1000000000 \n ... o sistema foi reiniciado ...'

    else:
        print 'A quantidade de brinquedos da loja deve ser maior ou igual a 1 e menor ou igual que 100000 \n ... o sistema foi reiniciado ...'

    iniciar = raw_input('Digite 1 para iniciar o sistema e 0 para sair : ')

print '... Obrigado por usar o sistema ...'