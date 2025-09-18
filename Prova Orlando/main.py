# Arquivo: bateria_de_testes.py
# Script para simular o uso real do sistema de vestibular da Fatec.

import random
from estdedados import SistemaVestibular

# --- Início da Execução ---
if __name__ == "__main__":

    # Vamos começar instanciando o sistema que vai gerenciar tudo
    sistema = SistemaVestibular()

    # ETAPA 1: Preparando o ambiente do vestibular (Cadastrando os aplicadores)
    # Primeiro, vamos cadastrar a equipe que vai aplicar a prova.
    print("--- ETAPA 1: Cadastrando a equipe de aplicação ---")
    sistema.cadastrar_aplicador("Prof. Carlos Silva", "Docente Responsável")
    sistema.cadastrar_aplicador("Profa. Ana Medeiros", "Docente de Apoio")
    sistema.cadastrar_aplicador("Marcos Andrade", "Fiscal de Sala")
    sistema.cadastrar_aplicador("Beatriz Costa", "Coordenadora Geral")
    print("--------------------------------------------------\n")


    # ETAPA 2: Período de Inscrições (Simulando 95 novos candidatos)
    # Agora, vamos simular o período de inscrições com dados mais realistas.
    print("--- ETAPA 2: Simulando o período de inscrições ---")
    
    # Listas de nomes para gerar candidatos mais realistas
    primeiros_nomes = ["Lucas", "Julia", "Pedro", "Mariana", "Gabriel", "Beatriz", "Matheus", "Laura", "Guilherme", "Sofia"]
    sobrenomes = ["Silva", "Souza", "Costa", "Santos", "Oliveira", "Pereira", "Rodrigues", "Almeida", "Nascimento", "Lima"]
    
    total_de_candidatos = 95
    for _ in range(total_de_candidatos):
        nome_completo = f"{random.choice(primeiros_nomes)} {random.choice(sobrenomes)}"
        cpf_aleatorio = f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}-{random.randint(10, 99)}"
        curso_escolhido = random.choice(["IA", "ESG"])
        
        # Simulando que cerca de 85% dos candidatos pagam o boleto
        pagou_o_boleto = random.random() > 0.15 
        
        sistema.inscrever_candidato(nome_completo, cpf_aleatorio, curso_escolhido, pagou_o_boleto)
    print("---------------------------------------------------\n")


    # ETAPA 3: Ajustes Cadastrais (Testando a Edição)
    print("--- ETAPA 3: Testando a função de edição de cadastro ---")
    print("\n>>> Editando um candidato que existe (Inscrição Nº 5)...")
    sistema.editar_candidato(5, "Maria Joaquina (Cadastro Corrigido)", "123.456.789-00", "ESG")
    
    print("\n>>> Tentando editar um candidato que não existe (Inscrição Nº 999)...")
    sistema.editar_candidato(999, "Candidato Fantasma", "000.000.000-00", "IA")
    print("-------------------------------------------------------\n")


    # ETAPA 4: Organização do Dia da Prova
    print("--- ETAPA 4: Organizando a logística do dia da prova ---")
    salas_necessarias = sistema.calcular_salas_necessarias()

    if salas_necessarias > 0:
        sistema.distribuir_candidatos_em_salas()
    
    sistema.calcular_relacao_candidato_vaga()
    print("------------------------------------------------------\n")


    # ETAPA 5: Processo de Aprovação (Casos de teste)
    print("--- ETAPA 5: Testando a funcionalidade de aprovação ---")
    print("\n>>> Aprovando alguns candidatos que pagaram a inscrição...")
    sistema.aprovar_candidato(1)
    sistema.aprovar_candidato(2)
    
    print("\n>>> Tentando aprovar um candidato com pagamento PENDENTE (Inscrição Nº 16)...")
    # O candidato 16 tem chance de ter sido criado com boleto_pago = False
    sistema.aprovar_candidato(16)
    
    print("\n>>> Tentando aprovar um candidato que NÃO EXISTE (Inscrição Nº 1000)...")
    sistema.aprovar_candidato(1000)
    print("--------------------------------------------------------\n")


    # ETAPA 6: Teste de Estresse (Verificando o limite de 40 vagas)
    print("--- ETAPA 6: Teste de estresse do limite de vagas (Curso de IA) ---")
    
    # while para preencher as vagas de IA até o limite de 40
    id_atual = 1
    vagas_preenchidas_ia = sistema.aprovados_ia.count()
    while vagas_preenchidas_ia < 40 and id_atual <= total_de_candidatos:
        candidato = sistema.lista_de_inscritos.find_by_inscricao(id_atual)
        if candidato and candidato.curso == "IA" and candidato.efetivada:
            sistema.aprovar_candidato(id_atual)
            vagas_preenchidas_ia = sistema.aprovados_ia.count()
        id_atual += 1

    print(f"\n>>> Todas as {sistema.aprovados_ia.count()} vagas de IA foram preenchidas.")
    print(">>> Agora, tentando aprovar um candidato extra para forçar o erro...")
    
    # Procura o próximo candidato válido de IA para tentar a aprovação extra
    id_extra = -1
    for i in range(id_atual, total_de_candidatos + 1):
        candidato = sistema.lista_de_inscritos.find_by_inscricao(i)
        if candidato and candidato.curso == "IA" and candidato.efetivada:
            id_extra = i
            break
    
    if id_extra != -1:
        sistema.aprovar_candidato(id_extra)
    else:
        print("Não foi possível encontrar outro candidato de IA para o teste de estouro.")
    print("-----------------------------------------------------------------\n")

    
    # ETAPA FINAL: Divulgação dos Resultados
    print("--- ETAPA FINAL: Exibindo a lista final de aprovados ---")
    sistema.mostrar_aprovados()
    print("--------------------------------------------------------")