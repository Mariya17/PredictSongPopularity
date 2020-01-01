import pandas as pd
import math
"""
1. procedure K2;
2. {Input: A set of n nodes, an ordering on the nodes, an upper bound u on the
3. number of parents a node may have, and a database D containing m cases.}
4. {Output: For each node, a printout of the parents of the node.}
5. for i:= 1 to n do
6. πi:= ∅;
7. Pold := f(i, πi); {This function is computed using Equation 20.}
8. OKToProceed := true;
9. While OKToProceed and |πi| < u do
10. let z be the node in Pred(xi) - πi that maximizes f(i, πi ∪ {z});
11. Pnew := f(i, πi ∪ {z});
12. if Pnew > Pold then
13. Pold := Pnew;
14. πi:= πi ∪ {z};
15. else OKToProceed := false;
16. end {while};
17. write(’Node: ’, xi, ’ Parent of xi: ’,πi);
18. end {for};
19. end {K2};

K2 algorithm will learn a structure of BN model from given data
"""
def func_f(i, parent, ri,Nij):
    numerator = 0
    denomenator = 1
    for j in range(len(parent)):
        numerator = math.factorial(ri-1)
        denomenator = math.factorial(Nij + ri -1)

        return
def alpha_ijk_func(ri,i, column):
    alpha_i = []
    for k in range(ri):
        alpha_i[k] = sum(m == k for m in column)
    return

def k2Algorithm(header_list):
    # put here a csv file that you want to learn from
    data_frame = pd.read_csv('db_after_preprosessing.csv')
    unique_variables_per_column = data_frame.nunique()
    for i in range(len(header_list)):
        #####parameters preporation
        ri = unique_variables_per_column[header_list[i]]#number of possible values of verticle i
        alpha_ijk = alpha_ijk_func(ri,i,data_frame[header_list[i]])
        Nij =
        ########################
        parent = [] # have no parents
        p_old = func_f(i, parent, ri, Nij)