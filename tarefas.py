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
    
  
def editar_tarefa():
    pass

def excluir_tarefa():
    pass

criar_tarefa()
listar_tarefas(lista_tarefas)

