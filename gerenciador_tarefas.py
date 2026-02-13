import json, os

def carregar_dados(arquivo):
    if not os.path.exists(arquivo):
        return []
    with open(arquivo,"r",encoding="utf-8") as f:
        return json.load(f)

def salvar_dados(arquivo,dados):
    with open(arquivo,"w",encoding="utf-8") as f:
        json.dump(dados,f,indent=4,ensure_ascii=False)

def adicionar_tarefa():
    tarefas = carregar_dados("tarefas.json")
    descricao = input("Descrição da tarefa: ")
    tarefa = {"id": len(tarefas)+1, "descricao": descricao, "concluida": False}
    tarefas.append(tarefa)
    salvar_dados("tarefas.json", tarefas)
    print("Tarefa adicionada!")

def listar_tarefas():
    tarefas = carregar_dados("tarefas.json")
    for t in tarefas:
        status = "✅" if t["concluida"] else "❌"
        print(f"{t['id']}: {t['descricao']} [{status}]")

def concluir_tarefa():
    tarefas = carregar_dados("tarefas.json")
    listar_tarefas()
    id_t = int(input("ID da tarefa a concluir: "))
    tarefa = next((t for t in tarefas if t["id"]==id_t), None)
    if tarefa:
        tarefa["concluida"] = True
        salvar_dados("tarefas.json", tarefas)
        print("Tarefa concluída!")
    else:
        print("Tarefa não encontrada!")

def remover_tarefa():
    tarefas = carregar_dados("tarefas.json")
    listar_tarefas()
    id_t = int(input("ID da tarefa a remover: "))
    tarefas = [t for t in tarefas if t["id"]!=id_t]
    salvar_dados("tarefas.json", tarefas)
    print("Tarefa removida!")

def menu():
    while True:
        print("\n1- Adicionar tarefa\n2- Listar tarefas\n3- Concluir tarefa\n4- Remover tarefa\n5- Sair")
        opcao = input("Escolha: ")
        if opcao=="1": adicionar_tarefa()
        elif opcao=="2": listar_tarefas()
        elif opcao=="3": concluir_tarefa()
        elif opcao=="4": remover_tarefa()
        elif opcao=="5": break
        else: print("Opção inválida!")

if __name__=="__main__":
    menu()
