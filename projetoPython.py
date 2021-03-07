lancamentos = input('Deseja iniciar os lançamentos de nota? (Digite S para Sim ou N para Não): ').upper()
while (lancamentos.upper() != 'S' and lancamentos.upper() != 'N'):
    print('Opção Inválida!')
    lancamentos = input('Informe S - Sim ou N - Não: ').upper()

totalDeAlunos = 0
fAprovados = 0
mAprovados = 0
fDeExame = 0
mDeExame = 0
fReprovado = 0
mReprovado = 0

while (lancamentos == 'S'):
    totalDeAlunos +=1

    nome = input('Informe o nome do aluno: ')

    sexo = input('Informe o sexo do aluno (F/M): ').upper()
    while (sexo != 'M' and sexo != 'F'):
        print('Opção Inválida!')
        sexo = input('Informe M - Masculino ou F - Feminino: ').upper()

    for cont in range(1,4):
        if cont ==1:
            nota1 = int(input('Informe a primeira nota: '))
            while nota1 <0 or nota1>10:
                nota1 = int(input('Nota 1 inválida, o valor deve ser entre 0 e 10: '))

        elif cont ==2:
            nota2 = int(input('Informe a segunda nota: '))
            while nota2<0 or nota2 >10:
                nota2 = int(input('Nota 2 inválida, o valor deve ser entre 0 e 10: '))

        else:
            nota3 = int(input('Informe a terceira nota: '))
            while nota3 <0 or nota3 >10:
                nota3 = int(input('Nota 3 inválida, o valor deve ser entre 0 e 10: '))


    media = (nota1 + nota2 +nota3)/3
    print(str(media))

    if media >= 7 and sexo == 'F':
        fAprovados += 1

    elif media >= 4 and sexo == 'F':
        fDeExame += 1

    else:
        if sexo == 'F':
            fReprovado +=1

    if media >= 7 and sexo == 'M':
        mAprovados += 1

    elif media >= 4 and sexo == 'M':
        mDeExame += 1

    else:
        if sexo == 'M':
            mReprovado += 1

    continuar = input('Deseja efetuar outro lançamento de notas? (S-Sim ou N-Não): ').upper()
    while (continuar != 'S' and continuar!= 'N'):
        print('Opção Inválida!')
        continuar = input('Informe S - Sim ou N - Não: ').upper()

    if continuar == 'N':
        lancamentos = "N"

else:
    print('Notas Lançadas!')


print('Total de alunos cadastrados: ',totalDeAlunos)
print('Total de alunas aprovadas: ',fAprovados)
print('Total de alunas de exame: ',fDeExame)
print('Total de alunas reprovadas: ',fReprovado)

print('Total de alunos aprovados: ',mAprovados)
print('Total de alunos de exame: ',mDeExame)
print('Total de alunos reprovados: ',mReprovado)

print('Porcertagem, de alunos aprovados: ', ((mAprovados+fAprovados)*100)/totalDeAlunos, '%')
print('Porcentagem de alunos de exame: ',((mDeExame+fDeExame)*100)/totalDeAlunos, '%')
print('Porcentagem de alunos reprovados: ',((mReprovado+fReprovado)*100)/totalDeAlunos, '%')
