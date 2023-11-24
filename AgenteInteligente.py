import random

# Definir parâmetros do algoritmo genético
POPULATION_SIZE = 10
GENERATIONS = 100
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.2

# Definir a equipe de desenvolvimento e as tarefas do projeto
equipe = ['Desenvolvedor1', 'Desenvolvedor2', 'Desenvolvedor3']
tarefas = ['Tarefa1', 'Tarefa2', 'Tarefa3']

# Inicializar população aleatória
def initialize_population():
    return [random.sample(tarefas, len(tarefas)) for _ in range(POPULATION_SIZE)]

# Função de aptidão
def fitness(programacao):
    # Implemente sua função de aptidão aqui
    # Pode levar em consideração a adequação de habilidades, interdependência de tarefas, prazos, etc.
    return random.uniform(0, 1)

# Seleção de pais usando torneio
def select_parents(population):
    tournament_size = 3
    parents = []
    for _ in range(2):
        tournament = random.sample(population, tournament_size)
        winner = max(tournament, key=fitness)
        parents.append(winner)
    return parents

# Operador de crossover (ponto de corte único)
def crossover(parent1, parent2):
    point = random.randint(1, len(tarefas) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Operador de mutação (troca de tarefas)
def mutate(individual):
    if random.uniform(0, 1) < MUTATION_RATE:
        idx1, idx2 = random.sample(range(len(tarefas)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

# Algoritmo genético principal
def genetic_algorithm():
    population = initialize_population()

    for generation in range(GENERATIONS):
        population = sorted(population, key=fitness, reverse=True)

        # Seleção, crossover e mutação
        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent1, parent2 = select_parents(population)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.extend([child1, child2])

        population = new_population

    # Retornar a melhor programação encontrada
    return max(population, key=fitness)

# Executar o algoritmo genético
melhor_programacao = genetic_algorithm()
print("Melhor Programação:", melhor_programacao)