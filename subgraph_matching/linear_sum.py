import numpy as np
import argparse
import pickle
import networkx as nx
from scipy.optimize import linear_sum_assignment



def main():

    parser = argparse.ArgumentParser(description='Alignment arguments')
    parser.add_argument('--matrix_path', type=str, help='path of matrix',
        default="")
    parser.add_argument('--query_path', type=str, help='path of query graph',
        default="")
    parser.add_argument('--target_path', type=str, help='path of target graph',
        default="")
    args = parser.parse_args()
    args.test = True
    
    
    with open(args.matrix_path, "rb") as f:
        matrix = np.load(f)

    
    with open(args.query_path, "rb") as f:
        query = pickle.load(f)

    with open(args.target_path, "rb") as f:
        target = pickle.load(f)
    
    #Using scipy
    row_ind, col_ind = linear_sum_assignment(matrix, maximize=True)
    print(col_ind)
    print(matrix[row_ind, col_ind].sum())
    
        
    target_nodes = [i for i in enumerate(target.nodes)]
    print(len(target_nodes))

    nodes =[]
    for node in col_ind:
        nodes.append(target_nodes[node][1])
    
    print(nodes)
    subgraph = target.subgraph(nodes)
    print(subgraph)
 
 
    
if __name__ == "__main__":
    main()