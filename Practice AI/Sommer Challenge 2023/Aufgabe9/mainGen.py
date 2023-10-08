# https://ide.codingame.com/21609455?id=67159074dfed33eeaec99fa6e7420adaa0162c2


from __future__ import annotations
from typing import TypeVar, Generic, List, Tuple, Callable
from abc import ABC, abstractmethod
from enum import Enum
from random import choices, random, randrange
from heapq import nlargest
from statistics import mean
from copy import deepcopy
import sys,math

T = TypeVar('T', bound='Chromosome') # for returning self
C = TypeVar('C', bound='Chromosome') # type of the chromosomes

# Base class for all chromosomes; all methods must be overridden
class Chromosome(ABC):
    @abstractmethod
    def fitness(self) -> float:
        ...

    @classmethod
    @abstractmethod
    def random_instance(cls: Type[T]) -> T:
        ...

    @abstractmethod
    def crossover(self: T, other: T) -> Tuple[T, T]:
        ...

    @abstractmethod
    def mutate(self) -> None:
        ...


class GeneticAlgorithm(Generic[C]):
    SelectionType = Enum("SelectionType", "ROULETTE TOURNAMENT")

    def __init__(self, initial_population: List[C], threshold: float, max_generations: int = 100, mutation_chance: float = 0.01, crossover_chance: float = 0.7, selection_type: SelectionType = SelectionType.TOURNAMENT) -> None:
        self._population: List[C] = initial_population
        self._threshold: float = threshold
        self._max_generations: int = max_generations
        self._mutation_chance: float = mutation_chance
        self._crossover_chance: float = crossover_chance
        self._selection_type: GeneticAlgorithm.SelectionType = selection_type
        self._fitness_key: Callable = type(self._population[0]).fitness

    # Use the probability distribution wheel to pick 2 parents
    # Note: will not work with negative fitness results
    def _pick_roulette(self, wheel: List[float]) -> Tuple[C, C]:
        return tuple(choices(self._population, weights=wheel, k=2))

    # Choose num_participants at random and take the best 2
    def _pick_tournament(self, num_participants: int) -> Tuple[C, C]:
        participants: List[C] = choices(self._population, k=num_participants)
        return tuple(nlargest(2, participants, key=self._fitness_key))

    # Replace the population with a new generation of individuals
    def _reproduce_and_replace(self) -> None:
        new_population: List[C] = []
        # keep going until we've filled the new generation
        while len(new_population) < len(self._population):
            # pick the 2 parents
            if self._selection_type == GeneticAlgorithm.SelectionType.ROULETTE:
                parents: Tuple[C, C] = self._pick_roulette([x.fitness() for x in self._population])
            else:
                parents = self._pick_tournament(len(self._population) // 2)
            # potentially crossover the 2 parents
            if random() < self._crossover_chance:
                new_population.extend(parents[0].crossover(parents[1]))
            else:
                new_population.extend(parents)
        # if we had an odd number, we'll have 1 extra, so we remove it
        if len(new_population) > len(self._population):
            new_population.pop()
        self._population = new_population # replace reference

    # With _mutation_chance probability mutate each individual
    def _mutate(self) -> None:
        for individual in self._population:
            if random() < self._mutation_chance:
                individual.mutate()

    # Run the genetic algorithm for max_generations iterations
    # and return the best individual found
    def run(self) -> C:
        best: C = max(self._population, key=self._fitness_key)
        for generation in range(self._max_generations):
            # early exit if we beat threshold
            if best.wertFit >= self._threshold:
                return best
            print(f"Generation {generation} Best {best.wertFit} Avg {mean(map(self._fitness_key, self._population))}")
            self._reproduce_and_replace()
            self._mutate()
            highest: C = max(self._population, key=self._fitness_key)
            if highest.wertFit > best.wertFit:
                best = highest # found a new best
        return best # best we found in _max_generations


class SimpleEquation(Chromosome):
    def __init__(self, startList: list, enemyList:list, my: list) -> None:
        self.startList: list = startList
        self.enemy: list = deepcopy(enemy)
        self.my: list = my
        self.runde: int = 0
        self.gefangen: bool = False
        self.wertFit: int = 0
        self.anzEnemy: int = 0

    def defeat(self,zwEnemy):
        newE=[];loeschen=[]
        for i1 in range(len(zwEnemy)-1):
            for i2 in range(1,len(zwEnemy)):
                if zwEnemy[i1] in loeschen or zwEnemy[i2] in loeschen or i1 == i2:
                    a=0
                else:
                    if zwEnemy[i1] == zwEnemy[i2]:
                        if not zwEnemy[i1] in loeschen:
                            loeschen.append(zwEnemy[i1])
                        if not zwEnemy[i2] in loeschen:
                            loeschen.append(zwEnemy[i2])
        for e in zwEnemy:
            if not e in loeschen:
                newE.append(e)
        return newE

    def moveEnemy(self,zwEnemy,zwMy):
        for eny in zwEnemy:
            xdist=eny[0]-zwMy[0]
            ydist=eny[1]-zwMy[1]
            if xdist > 0:
                eny[0] -= 1
            if xdist < 0:
                eny[0] += 1
            if ydist > 0:
                eny[1] -= 1
            if ydist < 0:
                eny[1] += 1            
            if eny == zwMy:
                return True
        return False

    def moveMy(self,zwMy):
        zwMy[0] += self.startList[self.runde][0]
        zwMy[1] += self.startList[self.runde][1]

    def fitness(self) -> float: # anzahl schritte + 50000 - len(enemyList)*500        
        zwEnemy = deepcopy(self.enemy)
        zwMy = deepcopy(self.my)
        for self.runde in range(100):
            zwEnemy = self.defeat(zwEnemy)
            self.gefangen = self.moveEnemy(zwEnemy,zwMy)
            if self.gefangen:
                break            
            if len(zwEnemy) == 0:
                break
            self.moveMy(zwMy)

        self.anzEnemy = len(zwEnemy)
        self.wertFit = -500 if self.gefangen else 0        
        self.wertFit = self.wertFit + 50000 - self.anzEnemy*500 - self.runde 
        return self.wertFit
    
    def printFitness(self) -> float: # anzahl schritte + 50000 - len(enemyList)*500        
        zwEnemy = deepcopy(self.enemy)
        zwMy = deepcopy(self.my)
        for self.runde in range(100):
            zwEnemy = self.defeat(zwEnemy)
            self.gefangen = self.moveEnemy(zwEnemy,zwMy)
            if self.gefangen:
                break            
            if len(zwEnemy) == 0:
                break
            self.moveMy(zwMy)
            print("{} {}  #  {}".format(zwEnemy,zwMy,self.startList[self.runde]),file=sys.stderr)
        self.anzEnemy = len(zwEnemy)
        self.wertFit = -500 if self.gefangen else 0        
        self.wertFit = self.wertFit + 50000 - self.anzEnemy*500 - self.runde 
        a=0


    @classmethod
    def random_instance(self,enemy: list,my: list) -> SimpleEquation:
        mMove=[[0,-1],[0,1],[-1,0],[1,0]]
        startList=[]
        for i in range(300):  # besser 300
            startList.append(mMove[randrange(4)])
        return SimpleEquation(startList,enemy,my)

    def crossover(self, other: SimpleEquation) -> Tuple[SimpleEquation, SimpleEquation]:
        anzahl=int(len(self.startList)/50)        
        for i in range(anzahl):
            pos1 = randrange(len(self.startList))
            pos2 = randrange(len(self.startList))
            if not pos1 == pos2:
                child1: SimpleEquation = deepcopy(self)
                child2: SimpleEquation = deepcopy(other)
                child1.startList[pos1] = other.startList[pos2]
                child2.startList[pos2] = self.startList[pos1]
        return child1, child2

    def mutate(self) -> None:
        for i in range(8):
            pos = randrange(len(self.startList))
            if self.startList[pos][0] == 0:
                self.startList[pos][1] *= -1
            else:
                self.startList[pos][0] *= -1

    def __str__(self) -> str:
        return f"enemy: {self.anzEnemy} runden: {self.runde} Fitness: {self.wertFit} Cached: {self.gefangen}   Weg: {self.startList[:self.runde+2]}"


if __name__ == "__main__":

    s1="37 21 37 27 16 29"  #1
    s2="6 10 16 10 84 35 84 42 11 38"  #2
    s3="-42 191 184 -15 184 -19 185 -19 186 -15 -42 190 92 93" #3
    s4="42 34 33 118 -3 178 151 29 42 59 0 178 106 29 33 65 149 87"
    s5="100 108 114 64 114 63 50 61 74 68 76 68 58 108 50 64 69 92"
    s6="184 -20 184 -22 185 -27 185 -28 158 166 -17 -18 -17 -20 160 154 160 -32 -30 166 93 105"
    s7="-126 -107 -111 249 227 -83 265 260 265 263 235 245 251 233 236 245 227 229 -110 244 251 236 -110 240 -126 257 -111 -99 85 43"
    s8="190 -29 190 165 190 163 80 97"
    s9="193 -26 193 -25 91 125 70 125 193 167 74 131"
    s10="56 111 18 51 106 51 51 95 97 111 18 120 51 59 52 51 51 58 77 88 55 111 75 88 71 79"  #10


    sList=s10.split(" ")
    my=[int(sList[-2]),int(sList[-1])]
    enemy=[]
    for e in range(0,len(sList)-2,2):
        enemy.append([int(sList[e]),int(sList[e+1])])

    initial_population: List[SimpleEquation] = [SimpleEquation.random_instance(enemy,my) for _ in range(20)]
    ga: GeneticAlgorithm[SimpleEquation] = GeneticAlgorithm(initial_population=initial_population, threshold=49701.0, max_generations = 50, mutation_chance = 0.1, crossover_chance = 0.7)
    result: SimpleEquation = ga.run()
    print(result)
    #result.printFitness()