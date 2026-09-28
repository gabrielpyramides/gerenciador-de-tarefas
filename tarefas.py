lista_tarefas = []


def criar_tarefa():
    while True:
        nome_tarefa = str(input('Digite a tarefa que gostaria de adicionar: '))
        concluida = False
        lista_tarefas.append({'Título': nome_tarefa, 'concluida?': concluida})
        adicionar_novamente = input('Deseja adicionar mais uma tarefa?(s/n)')
        if adicionar_novamente.lower().strip() == 's':
            continue
        else:
            return lista_tarefas

def listar_tarefas(tarefas):
    for indice, tarefa in enumerate(tarefas, start=1):
        concluido = 'Concluída' if tarefa['concluida?'] else 'Não Realizada'
        print(f'{indice}. Título: {tarefa['Título']} | Status: {concluido} ')
    
  
def editar_tarefa(tarefas):
    listar_tarefas(tarefas)
    indice = int(input('Digite o número da tarefa que deseja editar:')) - 1
    if 0 <= indice < len(tarefas):
        titulo_ou_status = input('Você deseja editar o título ou o status da tarefa?\n1 - Editar Título\n2- Editar Status: ').lower().strip()
        if titulo_ou_status == '1':
            novo_titulo = input('Novo título: ')
            tarefas[indice]['Título'] = novo_titulo
            print('tarefa editada com sucesso!')
        elif titulo_ou_status == '2':
            tarefas[indice]['concluida?'] = not tarefas[indice]['concluida?']
            print('Status atualizado com sucesso!')
    else:
        print("número inválido.")

def excluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    indice = int(input('Digite o número da tarefa que deseja excluir:')) - 1
    if 0 <= indice < len(tarefas):
        tarefas.remove(tarefas[indice])
        print('Tarefa removida!')
    else:
        print('Número inválido!')



