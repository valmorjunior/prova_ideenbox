quant_usuarios = raw_input('Digite quantos usuarios deseja validar ou digite x para sair: ')

while quant_usuarios != 'x':
    try:
        usuarios = []
        if int(quant_usuarios) >=1 and int(quant_usuarios) <= 100:

            for q in range(0, int(quant_usuarios)):
                usuarios.append(str(raw_input('Digite os nomes de usuarios: ')))

            for r in usuarios:
                validar = list(r)

                # print '------teste-------'
                # for t in validar:
                #     try:
                #         if int(t):
                #             print 'Temos um  problema'
                #     except:
                #         print 'Nao e inteiro'
                # print '------teste-------'

                if validar[0] == '_' or validar[0] == '.':
                    try:
                        if int(validar[1]):
                            print 'USUARIO: '+r+' | VALIDO'
                    except:
                        print 'USUARIO: '+r+' | INVALIDO\n Obs.: O segundo caracter do usuario deve ser um numero entre 0 e 9'
                else:
                    print 'USUARIO: '+r+' | INVALIDO\n Obs.: Seu usuario deve comecar com UNDERSCORE Ex.: _001teste'

        else:
            print 'Quantidade de usuario invalida para o sistema.'
    except:
        print 'Valor Digitado e invalido para o sistema'

    quant_usuarios = raw_input('Digite quantos usuarios deseja validar ou digite x para sair: : ')

print 'Obrigado por usar o sistema ...'