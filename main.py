from vetores import vetor

print (30 * "-", "Menu", 30 * "-")
print ("1 - Vetores")
print ("2 - Listas Ligadas")

menu = int(input("Digite a opção desejada: "))

if menu == 1:
    vetor_teste = vetor.Vetor(0)
    vetor_teste.inserir_elemento_posicoes(1, 0)
    vetor_teste.inserir_elemento_posicoes(7, 1)
    vetor_teste.inserir_elemento_posicoes(5, 2)
    vetor_teste.inserir_elemento_posicoes(1, 3)
    vetor_teste.inserir_elemento_posicoes(4, 2)


    print(vetor_teste.listar_elementos(0))
    print(vetor_teste.listar_elementos(1))
    print(vetor_teste.listar_elementos(2))
    print(vetor_teste.listar_elementos(3))
    print(vetor_teste.listar_elementos(4))
    print('------------------------------')
    print(vetor_teste.contem(8))
    print('------------------------------')


    print(vetor_teste.indice(8))
    print('------------------------------')
    print(vetor_teste)



