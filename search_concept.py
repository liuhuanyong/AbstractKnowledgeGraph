# coding = utf-8
import os
import networkx as nx
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class ConceptNet:
    def __init__(self):
        cur = "/".join(os.path.abspath(__file__).split('/')[:-1])
        self.hiearchy_file = os.path.join(cur, "dict/hiearchy.txt")
        self.concept_file = os.path.join(cur, "dict/concept_total.txt")
        return

    '''加载概念边'''
    def load_concept_edges(self, ):
        edges = []
        for line in open(self.hiearchy_file):
            line = line.strip().split(' ')
            if len(line) < 2:
                continue
            from_ = line[0].split('|')[-1]
            to_ = line[1].split('|')[-1]
            edges.append((to_, from_))
        return edges

    '''利用networkx构建有向图'''
    def build_graph(self, edges):
        G = nx.DiGraph()
        G.add_edges_from(edges)
        return G

    '''构造底层概念词典'''
    def build_basic_concept(self):
        concept_dict = {}
        print("loading concept edges")
        edges = self.load_concept_edges()
        print("build grpah")
        graph = self.build_graph(edges)
        path = nx.all_pairs_shortest_path(graph)
        for i in path:
            wd = i[0]
            path_dict = i[1]
            len_dict = {i:len(j) for i,j in path_dict.items()}
            len_dict_ = sorted(len_dict.items(), key=lambda asd:asd[1], reverse=True)
            longest_path = path_dict.get(len_dict_[0][0])
            if not longest_path:
                continue
            concept_dict[wd] = longest_path
        return concept_dict

    '''搜集主函数'''
    def build_all_concepts(self):
        all_dict = {}
        concept_dict = self.build_basic_concept()
        print('building all concepts')
        for line in open(self.concept_file):
            line = line.strip().split('\t')
            wd = line[0]
            concepts = [i.split('|')[-1] for i in line[-1].split(',')]
            concept_path = concept_dict.get(wd, '')
            if not concept_path:
                concept_path = [[wd] + concept_dict.get(c, [c]) for c in concepts]
            all_dict[wd] = concept_path
        return all_dict

    '''层级搜索主函数'''
    def search_hiearchy(self):
        import time
        start_time = time.time()
        all_dict = self.build_all_concepts()
        print(time.time()-start_time)
        while 1:
            wd = input('enter an wd to search:').strip()
            path = all_dict.get(wd, '')
            print(wd, path)

if __name__ == '__main__':
    handler = ConceptNet()
    handler.search_hiearchy()