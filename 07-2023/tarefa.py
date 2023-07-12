class Tarefa:
    def __init__(self, id, descricao, concluida=False):
        self.id = id
        self.descricao = descricao
        self.concluida = concluida

class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def remover_tarefa(self, id):
        for tarefa in self.tarefas:
            if tarefa.id == id:
                self.tarefas.remove(tarefa)

    def listar_tarefas(self):
        for tarefa in self.tarefas:
            print(f"{tarefa.id}: {tarefa.descricao} ({'concluída' if tarefa.concluida else 'não concluída'})")