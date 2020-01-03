import pandas as pd
import itertools

class Node:
    def __init__(self, name, db):
        self.name = name
        self.db = db
        self.rowDb, self.colDb = self.db.shape
        self.phi = {}
        self.listOfParants = []
        self.possibleValues = self.getPossibleValues(self.name)
        self.r = len(self.possibleValues)

    def getPossibleValues(self, name):
        vals = []
        for row in range(0, self.rowDb):
            if self.db[name][row] not in vals:
                vals.append(self.db[name][row])
        return vals

    # def getPssibleInstOfParentsInDBDONTUSE(self):
    #     listOfInst = []
    #     for row in range(0, self.rowDb):
    #         listParents = []
    #         for parent in self.phi:
    #            listParents.append(self.db[parent][row])
    #         str = ','.join(listParents)
    #         if str not in listOfInst:
    #             listOfInst.append(str)




class K2Const:
        DIRECTORY_OF_DB_CSV_PATH = 'db_after_preprosessing.csv'
        U =                         3

class K2:

    def __init__(self):
        self.u = K2Const.U
        self.db = self.getDB(K2Const.DIRECTORY_OF_DB_CSV_PATH)
        self.nodes = self.createNodeList(['song_duration_ms', 'acousticness', 'danceability', 'song_popularity'])
        self.ordering = ['song_duration_ms', 'acousticness', 'danceability', 'song_popularity']

    def getDB(self, pathDBFile):
        db = pd.read_csv(pathDBFile)
        self.rowDb, self.colDb = db.shape
        return db

    def createNodeList(self, nameOfNodes):
        list = []
        for node in nameOfNodes:
            list.append(Node(node, self.db))
        return list

    # def f(self, i):

    def getPssibleInstOfParentsInDB(self, node):
        listOfInst = []
        res = []
        for parent in node.phi:
            listOfInst.append(node.possibleValues(parent))
        for element in itertools.product(listOfInst):
            res.append(element)
        print(res)
        return res




    def k2(self):
        """
        :input: nodes: A set of n nodes
                ordering: An ordering on the nodes
                u:        An upper bound on the number of parents a node may have
                db:       A database D containing m cases
        :return: dependencies: For each node, a printout of the parents of the node
        """
        # for i in range(1, len(self.ordering)+ 1):
            # pOld = f(i, self.nodes.phi)
        # **********************************************************------>>>
        dependencies = {}
        return dependencies



def main():
    k2 = K2()
#    print(k2.db)
    k2.k2()





if __name__ == '__main__':
  main()