from persistencia import carregar_tarefas
from tarefas import criar_tarefa, listar_tarefas, editar_tarefa, excluir_tarefa


def  exibir_menu_inicial():
    print('''
    1 - Criar tarefa
    2 - Listar tarefas
    3 - Editar tarefa
    4 - Excluir tarefa
    5 - Sair
      ''')
    escolha = int(input('Digite o número da ação que deseja realizar: '))
    return escolha
    

def inciar_programa():
    lista_tarefas = carregar_tarefas()  
    while True:
        try:
            escolha = exibir_menu_inicial()
        except ValueError:
            print("Digite apenas números.")
            continue
        if escolha == 1:
            criar_tarefa(lista_tarefas)
        elif escolha == 2:
            listar_tarefas(lista_tarefas)
        elif escolha == 3:
            editar_tarefa(lista_tarefas)
        elif escolha == 4:
            excluir_tarefa(lista_tarefas)
        elif escolha == 5:
            break
        else:
            print('Opção inválida!')
    
inciar_programa()