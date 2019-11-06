import matplotlib.pyplot as plt
import numpy as np

class Cromossomo(object):
    def __init__(self,tamCromossomo=None):
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

    def mutacaoGauss(self,desvpad,probMut):
        for locus in xrange(self.gene.size):
            if np.random.random() < probMut:
                aleloMutado=np.random.normal(self.gene[locus],desvpad)
                if aleloMutado < 0: aleloMutado=0
                elif aleloMutado > 1: aleloMutado=1
                self.gene[locus]=aleloMutado

    def __eq__(self, other):
        return (self.fitness == other.fitness)

    def __lt__(self, other):
        return (self.fitness < other.fitness)

    def __gt__(self, other):
        return (self.fitness > other.fitness)

    def __str__(self):
        return "fit:"+str(self.fitness)+" "+"".join(["{0:.3f} ".format(gene) for gene in self.gene])

class Populacao(list):
    def __init__(self, tamPop=None,tamCromossomo=None):
        listapop=[]
        if tamPop is not None:
            for i in range(tamPop):
                listapop.append(Cromossomo(tamCromossomo))
        super(Populacao, self).__init__(listapop)

#Tabelas

table_indv = {'DC': 3, 'CC': 2, 'DD': 1, 'CD': 0}
table_group = {'CC': 2, 'CD': 1, 'DC': 1, 'DD': 0}

def decode(gene):
        if gene < 0.5:
            fenotype = 'C'
        else:
            fenotype = 'D'
        return fenotype


def tabelaCD(table, gene1, gene2):
    par = str(decode(gene1) + decode(gene2))

    if par == 'CD':
        points = table['CD']
    elif par == 'CC'
        points = table['CC']
    elif par == 'DD':
        points = table['DD']
    else:
        points = table['DC']


def fitness(individual, population, table):
    def normalize(data):
        len_data = len(data)
        normalized = np.zeros(len_data)
        for i in range(len_data):
            normalized[i] = lambda x: (x - min(data)) / (max(data) - min(data))
        return normalized

    def calc_fitness(indv_under_test, opponent, table):
        pass

    fit = 0

    for individual in population:
        undertest = indv
        n_test = len(population) - 1
        for individual in population:
            fit += calc_fitness(under_test, oponnent=individual, table)
        fitness_eval = fit / n_test
