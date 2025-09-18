import math

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaLigada:
    #Permite adicionar (append), exibir (display), contar (count) e buscar (find).
    def __init__(self):
        self.head = None

    def append(self, data):
        #Adiciona um novo nó ao final da lista."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        # Percorre a lista até encontrar o último nó
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        """
        Exibe todos os dados da lista.
        Retorna True se a lista não estiver vazia, e False caso contrário.
        """
        current_node = self.head
        if current_node is None:
            return False # Retorna False para indicar que a lista está vazia
        
        while current_node:
            print(str(current_node.data))
            current_node = current_node.next
        return True # Retorna True se tiver elementos

    def find_by_inscricao(self, num_inscricao):
        #Encontra a inscrição baseada no nó
        current_node = self.head
        while current_node:
            # Garante que o objeto no nó tenha a inscrição
            if hasattr(current_node.data, 'inscricao') and current_node.data.inscricao == num_inscricao:
                return current_node.data
            current_node = current_node.next
        return None
        
    def count(self):
        """Conta o número de nós na lista."""
        total = 0
        current_node = self.head
        while current_node:
            total += 1
            current_node = current_node.next
        return total


class Vestibulando:
   
    _contador_inscricao = 1

    def __init__(self, nome, cpf, curso, boleto_pago):
        self.inscricao = Vestibulando._contador_inscricao
        self.nome = nome
        self.cpf = cpf
        if curso.upper() in ["IA", "ESG"]:
            self.curso = curso.upper()
        else:
            raise ValueError("Curso inválido. Escolha entre IA e ESG.")
        self.efetivada = boleto_pago
        
        Vestibulando._contador_inscricao += 1

    def __str__(self):
        status = "Efetivada" if self.efetivada else "Pendente"
        return f"[Inscrição: {self.inscricao}, Nome: {self.nome}, CPF: {self.cpf}, Curso: {self.curso}, Status: {status}]"

class Aplicador:
    #Armazena os dados dos aplicadores de prova
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

    def __str__(self):
        return f"[Nome: {self.nome}, Cargo: {self.cargo}]"

class Aprovado:
    #Armazena os dados dos alunos aprovados
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"[Nome: {self.nome}, CPF: {self.cpf}]"

class SistemaVestibular:

    #Gerencia todas as operações do vestibular, como inscrições, cálculos e aprovações.

    def __init__(self):
        self.lista_de_inscritos = ListaLigada()
        self.lista_de_aplicadores = ListaLigada()
        self.aprovados_ia = ListaLigada()
        self.aprovados_esg = ListaLigada()

    def inscrever_candidato(self, nome, cpf, curso, boleto_pago):
        #Realiza a inscrição de um novo candidato
        try:
            novo_candidato = Vestibulando(nome, cpf, curso, boleto_pago)
            self.lista_de_inscritos.append(novo_candidato)
            print(f"Candidato '{nome}' inscrito com sucesso! Número de inscrição: {novo_candidato.inscricao}")
        except ValueError as e:
            print(f"Erro na inscrição: {e}")

    def editar_candidato(self, num_inscricao, novo_nome, novo_cpf, novo_curso):
        candidato = self.lista_de_inscritos.find_by_inscricao(num_inscricao)
        if candidato:
            print(f"Editando dados do candidato {candidato.nome}...")
            try:
                if novo_curso.upper() not in ["IA", "ESG"]:
                    raise ValueError("Curso inválido. Escolha entre IA e ESG.")
                candidato.nome = novo_nome
                candidato.cpf = novo_cpf
                candidato.curso = novo_curso.upper()
                print("Dados alterados com sucesso!")
                print(candidato)
            except ValueError as e:
                print(f"Erro na edição: {e}")
        else:
            print(f"Candidato com número de inscrição {num_inscricao} não encontrado.")

    def cadastrar_aplicador(self, nome, cargo):
        novo_aplicador = Aplicador(nome, cargo)
        self.lista_de_aplicadores.append(novo_aplicador)
        print(f"Aplicador '{nome}' cadastrado com sucesso.")

    def calcular_salas_necessarias(self):
        print("\n--- Calculando Salas Necessárias ---")
        contador_efetivados = 0
        current_node = self.lista_de_inscritos.head

        while current_node:
            candidato = current_node.data
            #Verifica se o candidato esta efetivado para fazer a prova
            if candidato.efetivada:
                contador_efetivados += 1
            current_node = current_node.next

        if contador_efetivados == 0:
            print("Nenhum candidato com inscrição efetivada para realizar a prova.")
            return 0
        
        salas_necessarias = math.ceil(contador_efetivados / 30.0)

        print(f"Total de candidatos com inscrição efetivada: {contador_efetivados}")
        print(f"Serão necessárias {salas_necessarias} sala(s) de aula.")
        return salas_necessarias

    def distribuir_candidatos_em_salas(self):
        print("\n--- Distribuição de Candidatos por Sala ---")
        
        num_sala = 1
        candidatos_na_sala = 0
        houve_distribuicao = False
        
        current_node = self.lista_de_inscritos.head
        
        while current_node:
            candidato = current_node.data
            
            if candidato.efetivada:
                if candidatos_na_sala == 0:
                    print(f"\n====== SALA {num_sala} ======")
                
                print(f"- {candidato.nome} (Inscrição: {candidato.inscricao})")
                candidatos_na_sala += 1
                houve_distribuicao = True
                if candidatos_na_sala == 30:
                    num_sala += 1
                    candidatos_na_sala = 0
            
            current_node = current_node.next

        if not houve_distribuicao:
            print("Nenhum candidato com inscrição efetivada para distribuir.")

    def calcular_relacao_candidato_vaga(self):
        print("\n--- Relação Candidato/Vaga ---")
        total_ia = 0
        efetivados_ia = 0
        total_esg = 0
        efetivados_esg = 0

        current_node = self.lista_de_inscritos.head
        while current_node:
            candidato = current_node.data
            if candidato.curso == "IA":
                total_ia += 1
                if candidato.efetivada:
                    efetivados_ia += 1
            elif candidato.curso == "ESG":
                total_esg += 1
                if candidato.efetivada:
                    efetivados_esg += 1
            current_node = current_node.next
        vagas = 40.0
        print("\nCurso: IA ")
        if total_ia > 0:
            print(f"  Inscrições totais: {total_ia} ({total_ia / vagas:.2f} candidatos por vaga)")
        if efetivados_ia > 0:
            print(f"  Inscrições efetivadas: {efetivados_ia} ({efetivados_ia / vagas:.2f} candidatos por vaga)")

        print("\nCurso: ESG")
        if total_esg > 0:
            print(f"  Inscrições totais: {total_esg} ({total_esg / vagas:.2f} candidatos por vaga)")
        if efetivados_esg > 0:
            print(f"  Inscrições efetivadas: {efetivados_esg} ({efetivados_esg / vagas:.2f} candidatos por vaga)")
    
    def aprovar_candidato(self, num_inscricao):
        candidato = self.lista_de_inscritos.find_by_inscricao(num_inscricao)
        
        if not candidato:
            print(f"Erro: Candidato com inscrição {num_inscricao} não encontrado.")
            return
            
        if not candidato.efetivada:
            print(f"Erro: A inscrição de {candidato.nome} não está efetivada. Apenas quem realizou a prova pode ser aprovado.")
            return

        novo_aprovado = Aprovado(candidato.nome, candidato.cpf)
        
        if candidato.curso == "IA":
            if self.aprovados_ia.count() < 40:
                self.aprovados_ia.append(novo_aprovado)
                print(f"Candidato {candidato.nome} aprovado com sucesso em IA!")
            else:
                print("Erro: Turma de IA já está com 40 alunos. Não há mais vagas.")
        
        elif candidato.curso == "ESG":
            if self.aprovados_esg.count() < 40: 
                self.aprovados_esg.append(novo_aprovado)
                print(f"Candidato {candidato.nome} aprovado com sucesso em ESG!")
            else:
                print("Erro: Turma de ESG já está com 40 alunos. Não há mais vagas.")

    def mostrar_aprovados(self):
        print("\n--- LISTA DE APROVADOS IA ---")
        if not self.aprovados_ia.display():
             print("Nenhum aluno aprovado neste curso até o momento.")
             
        print("\n--- LISTA DE APROVADOS: ESG ---")
        if not self.aprovados_esg.display():
             print("Nenhum aluno aprovado neste curso até o momento.")
