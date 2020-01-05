import pandas as pd
import itertools
import math


class Node:
    def __init__(self, name, nodeData, listOfPotentialParents):
        self.name = name
        self.nodeData = nodeData
        self.rows = len(self.nodeData)
        # self.possibleValues = set(self.nodeData)
        self.possibleValues = self.getPossibleValues()
        self.r = len(self.possibleValues)
        self.listOfParents = []

        self.potentialParents = listOfPotentialParents

    def getPossibleValues(self):
        vals = []
        for row in range(0, self.rows):
            if self.nodeData[row] not in vals:
                vals.append(self.nodeData[row])
        return vals


class K2Const:
        # DIRECTORY_OF_DB_CSV_PATH = 'db_after_preprosessing.csv'
        DIRECTORY_OF_DB_CSV_PATH = 'dbForTest.csv'
        U =                         2

class K2:

    def __init__(self):
        self.u = K2Const.U
        self.db = self.getDB(K2Const.DIRECTORY_OF_DB_CSV_PATH)
        # self.ordering = ['song_duration_ms', 'acousticness', 'danceability', 'song_popularity']
        # self.nodes = self.createNodeList(['song_duration_ms', 'acousticness', 'danceability', 'song_popularity'])
        self.ordering = ['x1', 'x2', 'x3']
        self.nodes = self.createNodeList(self.ordering)

    def getDB(self, pathDBFile):
        db = pd.read_csv(pathDBFile)
        return db

    def createNodeList(self, nameOfNodes):
        listOfNodes = []
        for node in nameOfNodes:
            listOfNodes.append(Node(node, self.db[node], listOfNodes.copy()))
        return listOfNodes

    def getCartesianProduct(self, listOfInst):
        product = list(itertools.product(*listOfInst))
        return product

    def getPossibleInstWithParentsInDB(self, node, parents):
        listOfInst = []
        allPossibleInstantinations = []
        res = {}
        t = ()
        flatten = itertools.chain.from_iterable
        listOfInst.append(node.possibleValues)
        if len(parents) > 0:
            for parent in parents:
                listOfInst.append(parent.possibleValues)
            allPossibleInstantinations = self.getCartesianProduct(listOfInst)
            for instance in allPossibleInstantinations:
                res[instance] = 0
        else:
            listOfInst = flatten(listOfInst)
            for instance in listOfInst:
                t = (instance,)
                res[t] = 0
        return res

    def getInstance(self, row, instansesFromDB):
        instance = ()
        for inst in instansesFromDB:
            instance = instance + (inst[row],)
        return instance

    # This function will summarize all instances and return a dictionary
    # of instance(tuple) as a key and amount of it's appearances as value
    def calculateNumberOfInstances(self, node, parents, possibleInstances):
        instansesFromDB = []
        instansesFromDB.append(node.nodeData)
        for parent in parents:
            instansesFromDB.append(parent.nodeData)
        for row in range(node.rows):
            instance = self.getInstance(row, instansesFromDB)
            possibleInstances[instance] += 1
        return possibleInstances

    def alpha(self, node,  parents =[]):
        res = {}
        res = self.getPossibleInstWithParentsInDB(node, parents)
        res = self.calculateNumberOfInstances(node, parents, res)
        return res


    def getProductOfAlphaFactorials(self, allAlpha):
        res = 1
        for key, val in allAlpha.items():
            res *= math.factorial(val)
        return res

    def getAllNij(self, node, q, r, allAlpha, parents):
        Ni = {}
        i = 0
        listOfInst = []
        listOfInst.append(node.possibleValues)
        for parent in parents:
            listOfInst.append(parent.possibleValues)
        allPossibleInstantinations = self.getCartesianProduct(listOfInst)
        for j in range(q):
            Ni[j] = 0
        for j in range(r):
            for k in range(r):
                Ni[j] += allAlpha[allPossibleInstantinations[i]]
                i += 1
        return Ni

    def getProductOfFirstPartOfEquation(self, r, Nij):
        numerator = math.factorial(r - 1)
        denominator = math.factorial(Nij + r - 1)
        return numerator/denominator

    def f(self, i, node, parents):
        numerator = 0
        denominator = 1
        res = 0
        firstPartProduct = 1
        if len(parents) == 0:
            allAlpha = self.alpha(node)
            Ni = sum(allAlpha.values())
            numerator = math.factorial(node.r - 1)
            denominator = math.factorial(Ni + node.r - 1)
            productOfAlphaFactorials = self.getProductOfAlphaFactorials(allAlpha)
            res = (numerator/denominator)*productOfAlphaFactorials
        else:
            allAlpha = self.alpha(node, parents)
            q = int(len(allAlpha)/node.r)
            Ni = self.getAllNij(node, q, node.r, allAlpha, parents)
            for j in range(q):
                firstPartProduct = firstPartProduct * self.getProductOfFirstPartOfEquation(node.r, Ni[j])
            secondPartProduct = self.getProductOfAlphaFactorials(allAlpha)

            res = firstPartProduct * secondPartProduct

        return res

    # Return max value of fumction f and it's node that suppose to be a new parent
    def getMaximizingParent(self, listOfP):
        max = 0
        node = listOfP[0][1]    # default
        for element in listOfP:
            temp = element[0]
            if temp > max:
                max = temp
                node = element[1]
        return max, node


    def k2(self):
        """
        :input: nodes: A set of n nodes
                ordering: An ordering on the nodes
                u:        An upper bound on the number of parents a node may have
                db:       A database D containing m cases
        :return: dependencies: For each node, a printout of the parents of the node
        """
        for i in range(1, len(self.ordering) + 1):
            tempGroupOfParents = self.nodes[i - 1].listOfParents
            pOld = self.f(i, self.nodes[i-1], tempGroupOfParents)
            OKToProceed = True
            while OKToProceed and (len(self.nodes[i-1].listOfParents) < len(self.nodes[i-1].potentialParents)):
                listOfP = []
                # tempGroupOfParents = self.nodes[i-1].listOfParents.copy()
                for parent_z in self.nodes[i-1].potentialParents:
                    tempGroupOfParents = self.nodes[i - 1].listOfParents.copy()
                    tempGroupOfParents.append(parent_z)
                    listOfP.append([self.f(i, self.nodes[i-1], tempGroupOfParents), parent_z])
                pNew, newParent = self.getMaximizingParent(listOfP)
                if pNew > pOld:
                    pOld = pNew
                    self.nodes[i - 1].listOfParents.append(newParent)
                    self.nodes[i - 1].potentialParents.remove(newParent)
                else:
                    OKToProceed = False

        # **********************************************************------>>>
        dependencies = []
        for node in self.nodes:
            for parent in node.listOfParents:
                dependencies.append((parent.name, node.name))

        print(dependencies)
        return dependencies



def main():
    k2 = K2()
#    print(k2.db)
    k2.k2()





if __name__ == '__main__':
  main()