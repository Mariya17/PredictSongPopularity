import pandas as pd
import itertools
import math

class Node:
    def __init__(self, name, nodeData, listOfPotentialParents, dataListOfPreviousNodes):
        self.name = name
        self.nodeData = nodeData
        self.rows = len(self.nodeData)
        self.possibleValues = set(self.nodeData)
        self.r = len(self.possibleValues)
        self.listOfParents = []
        self.potentialParents = listOfPotentialParents

    # def getPossibleValues(self):
    #     vals = []
    #     for row in range(0, self.rows):
    #         if self.nodeData[row] not in vals:
    #             vals.append(self.nodeData[row])
    #     return vals

    # def getPossibleInstOfParentsInDBDONTUSE(self):
    #     listOfInst = []
    #     for row in range(0, self.rowDb):
    #         listParents = []
    #         for parent in self.phi:
    #            listParents.append(self.db[parent][row])
    #         str = ','.join(listParents)
    #         if str not in listOfInst:
    #             listOfInst.append(str)




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
    #    self.rowDb, self.colDb = db.shape
        return db

    def createNodeList(self, nameOfNodes):
        listOfNodes = []
        dataListOfPreviousNodes = []
        for node in nameOfNodes:
            listOfNodes.append(Node(node, self.db[node], listOfNodes.copy(), dataListOfPreviousNodes))
            dataListOfPreviousNodes.append(self.db[node])       #TODO[Mariya] think is it nessesary
        return listOfNodes

    def getPssibleInstOfParentsInDB(self, node):
        listOfInst = []
        res = []
        for parent in node.potentialParents:
            listOfInst.append(node.possibleValues(parent))
        for element in itertools.product(listOfInst):
            res.append(element)
        print(res)
        return res
# TODO:[Mariya] add computition also for parents
    def alpha(self, node,  parents =[]):
        res = {}
        for val in node.possibleValues:
            res[val] = 0
        for val in node.nodeData:
            res[val] += 1
        return res

    def getProductOfAlphaFactorials(self, allAlpha):
        res = 1
        for key, val in allAlpha:
            res *= math.factorial(val)
        return res
    def f(self, i, node, parents):
        numerator = 0
        denominator = 1
        res = 0
        if len(parents) == 0:
            allAlpha = self.alpha(node)
            Ni = sum(allAlpha.values())
            productOfAlphaFactorials = self.getProductOfAlphaFactorials(allAlpha)
            numerator = math.factorial(node.r - 1)
            denominator = math.factorial(Ni + node.r - 1)
            res = (numerator/denominator)*productOfAlphaFactorials
        else:
            allAlpha = self.alpha(node, parents)
            Ni = sum(allAlpha.values())
            productOfAlphaFactorials = self.getProductOfAlphaFactorials(allAlpha)
            numerator = math.factorial(node.r - 1)
            denominator = math.factorial(Ni + node.r - 1)
            res = (numerator / denominator) * productOfAlphaFactorials

        return res




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
                tempGroupOfParents = self.nodes[i-1].listOfParents
                for parent_z in self.nodes[i-1].potentialParents:
                    tempGroupOfParents = tempGroupOfParents.append(parent_z)
                    listOfP.append(self.f(i, tempGroupOfParents))
                pNew = max(listOfP)
                if pNew > pOld:
                    pOld = pNew
                    self.nodes[i - 1].listOfParents.append(parent_z)
                else:
                    OKToProceed = False
                return

        # **********************************************************------>>>
        dependencies = {}
        return dependencies



def main():
    k2 = K2()
#    print(k2.db)
    k2.k2()





if __name__ == '__main__':
  main()