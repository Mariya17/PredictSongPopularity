import pandas as pd
import itertools
import math
from decimal import Decimal


class Node:
    def __init__(self, name, nodeData, listOfPotentialParents):
        self.name = name
        self.nodeData = nodeData
        self.rows = len(self.nodeData)
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
        U =                         13

class K2:

    def __init__(self, ordered_list, db_file_name):
        self.u = K2Const.U
        self.db = self.getDB(db_file_name)
        self.ordering = ordered_list
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
        return sorted(product)

    def getListOfInst(self, node, parents):
        listOfInst = []
        for parentNode in self.nodes:
            if (parentNode in parents) or (parentNode is node):
                listOfInst.append(parentNode.possibleValues)
        return listOfInst

    def getPossibleInstWithParentsInDB(self, node, parents):
        listOfInst = []
        allPossibleInstantinations = []
        res = {}
        t = ()
        flatten = itertools.chain.from_iterable
        if len(parents) > 0:
            listOfInst = self.getListOfInst(node, parents)
            allPossibleInstantinations = self.getCartesianProduct(listOfInst)
            for instance in allPossibleInstantinations:
                res[instance] = 0
        else:
            listOfInst.append(node.possibleValues)
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
        for parentNode in self.nodes:
            if (parentNode in parents) or (parentNode is node):
                instansesFromDB.append(parentNode.nodeData)
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
            res *= Decimal(math.factorial(val))
        return res

    def getAllNij(self, node, q, r, allAlpha, parents):
        Ni = {}
        i = 0
        listOfInst = self.getListOfInst(node, parents)
        allPossibleInstantinations = self.getCartesianProduct(listOfInst)
        for j in range(q):
            Ni[j] = 0
        for j in range(q):
            for k in range(r):
                Ni[j] += allAlpha[allPossibleInstantinations[i]]
                i += 1
        return Ni

    def getProductOfFirstPartOfEquation(self, r, Nij):
        numerator = math.factorial(r - 1)
        denominator = Decimal(math.factorial(Nij + r - 1))
        return numerator/denominator

    def f(self, node, parents):
        numerator = 0
        denominator = 1
        res = 0
        firstPartProduct = 1
        if len(parents) == 0:
            allAlpha = self.alpha(node)
            Ni = sum(allAlpha.values())
            numerator = math.factorial(node.r - 1)
            denominator = Decimal(math.factorial(Ni + node.r - 1))
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
        node = self.nodes[0]   # default
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
        for i in range(len(self.ordering)):
            pNew = 0
            tempGroupOfParents = self.nodes[i - 1].listOfParents
            pOld = self.f(self.nodes[i-1], tempGroupOfParents)
            OKToProceed = True
            while OKToProceed and (len(self.nodes[i].listOfParents) < self.u):
                listOfP = []
                for parent_z in self.nodes[i].potentialParents:
                    tempGroupOfParents = self.nodes[i].listOfParents.copy()
                    tempGroupOfParents.append(parent_z)
                    listOfP.append([self.f(self.nodes[i], tempGroupOfParents), parent_z])
                pNew, newParent = self.getMaximizingParent(listOfP)
                if pNew > pOld:
                    pOld = pNew
                    self.nodes[i].listOfParents.append(newParent)
                    self.nodes[i].potentialParents.remove(newParent)
                else:
                    OKToProceed = False

        # **********************************************************------>>>
        dependencies = []
        for node in self.nodes:
            for parent in node.listOfParents:
                dependencies.append((parent.name, node.name))

        print(dependencies)
        return dependencies
