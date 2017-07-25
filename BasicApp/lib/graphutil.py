import networkx as nx

class GraphUtil():

    @classmethod
    def shortestpath(self,list1,list2,src,des):
        G = nx.Graph()

        addtograph(list1,G)
        addtograph(list2,G)

        return nx.shortest_path(G,source=src,target=des)

def addtograph(list,G):
    for emp in list:
        if(emp.employee_id != None) and (emp.parent_id != None):
            G.add_edge(int(emp.employee_id),int(emp.parent_id))
    return None