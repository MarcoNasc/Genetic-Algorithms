import matplotlib.pyplot as plt
import numpy as np
import numpy.random as npr
import random as rd
import copy as cp


class Cromossomo(object):
    def __init__(self, tamCromossomo=None):
        self._fitness = None
        if tamCromossomo is None:
            self._gene = None
        else:
            self._gene=np.random.rand(tamCromossomo)

    @property
    def gene(self):
        return self._gene

    @gene.setter
    def gene(self, valor):
        self._gene = valor

    @property
    def fitness(self):
        return self._fitness

    @fitness.setter
    def fitness(self, valor):
        self._fitness = valor

    def mutacaoGauss(self,desvpad, probMut):
        for locus in range(self.gene.size):
            if np.random.random() < probMut:
                aleloMutado = np.random.normal(self.gene[locus], desvpad)
                if aleloMutado < 0:

                    aleloMutado = 0

                elif aleloMutado > 1:

                    aleloMutado = 1

                self.gene[locus] = aleloMutado

    def __eq__(self, other):
        return self.fitness == other.fitness

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __gt__(self, other):
        return self.fitness > other.fitness

    def __str__(self):
        return "fit:"+str(self.fitness)+" "+"".join(["{0:.3f} ".format(gene) for gene in self.gene])


class Populacao(list):
    def __init__(self, tamPop=None, tamCromossomo=None):
        listapop = []
        if tamPop is not None:
            for i in range(tamPop):
                listapop.append(Cromossomo(tamCromossomo))
        super(Populacao, self).__init__(listapop)


pop = Populacao(15, 10)
print("pop inicial")


def printPop(pop):
    for i in pop:
        print(i)


printPop(pop)


def crossAritmeticoCorte(self, cromossomo1, cromossomo2):
    """Realiza crossover aritmetico em todos os genes do cromossomo"""
    beta = np.random.random()
    corte = np.random.randint(len(cromossomo1.gene))

    novogene1 = np.concatenate(
        (cromossomo1.gene[: corte], beta * cromossomo1.gene[corte:] + (1 - beta) * cromossomo2.gene[corte:]))
    novogene2 = np.concatenate(
        (cromossomo2.gene[: corte], beta * cromossomo2.gene[corte:] + (1 - beta) * cromossomo1.gene[corte:]))
    novocromo1 = Cromossomo()
    novocromo2 = Cromossomo()
    novocromo1.gene = novogene1
    novocromo2.gene = novogene2
    return novocromo1, novocromo2


# Tabelas

table_indv = {'DC': 1, 'CC': 0.67, 'DD': 0.33, 'CD': 0}
table_group = {'CC': 1, 'CD': 0.5, 'DC': 0.5, 'DD': 0}


def decode(gene):
    if gene < 0.5:
        fenotype = 'C'
    else:
        fenotype = 'D'
    return fenotype


def fitness_table(table, indv_under_test, opponent):

    par = str(decode(indv_under_test)) + str(decode(opponent))

    if par == 'CD':
        fitness = table['CD']
    elif par == 'CC':
        fitness = table['CC']
    elif par == 'DD':
        fitness = table['DD']
    else:
        fitness = table['DC']

    return fitness


def indv_evaluation(table, population, sample):

    for cromossome in population:

        eval_pop = cp.deepcopy(population)
        eval_pop.remove(cromossome)
        pop_size = len(eval_pop)

        fitness = []

        if not sample:

            index = npr.choice(len(eval_pop))
            opponent = eval_pop[index]

            for i in range(len(cromossome.gene)):

                fitness.append(fitness_table(table, cromossome.gene[i], opponent.gene[i]))

        else:

            opponents = rd.sample(eval_pop, int(sample*pop_size))

            for opponent in opponents:

                gene_fitness = []

                for j in range(len(cromossome.gene)):

                    gene_fitness.append(fitness_table(table, cromossome.gene[j], opponent.gene[j]))

                fitness.append(np.mean(gene_fitness))

        cromossome.fitness = np.mean(fitness)

    return population


print('pop final')
fit_pop = indv_evaluation(table_indv, pop, 0)
printPop(pop)

# testes: individual, 10% e 30% da população
tests = [0, 0.1, 0.3]
tables = [table_indv, table_group]


# for i in range(5): as 5 execuções
#   for j in range(len(tables)): funções de avaliação, individual ou grupo
#       for k in range(len(testes)): os 3 tipos de testes avaliados
#           Executar_AG(tables[j], testes[k])
