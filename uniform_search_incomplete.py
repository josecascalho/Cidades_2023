import json
import nodes
import copy

class Uniform_search:

    def __init__(self, initial_city: str,final_city: str) -> None:
        """Initializes the lists and define initial city and goal city"""
        self.frontier_nodes =[]
        self.open_nodes =[]
        self.initial_city = initial_city
        self.final_city = final_city

    def get_smaller_cost(self,nds: list)-> nodes.Node:
    	pass
    	

    def print_nodes(self,description,nds: list):
        print(description)
        print("Name(Parent):Total cost")
        for nd in nds:
            if nd.get_parent() != None:
                print(nd.get_name(),"(",nd.get_parent().get_name(),"):",nd.get_total_cost())
            else:
                print(nd.get_name(),"(---):",nd.get_total_cost())
        print("---------------------------")


    def load_data(self,config_file:str) -> None:
        """Load data from json file"""
        with open(config_file) as cf:
            # Reading the configuration file
            self.data = json.load(cf)
        #print(self.data)
        #print(self.data["connections"])
 
 
 

    def run(self):
        # root tree
        root = nodes.Node(self.initial_city,None,0)
        # openning the root node
        self.open_nodes.append(root)

        for connection in self.data["connections"]:
         if connection["node1"] == self.initial_city:
            new_node = nodes.Node(connection["node2"],root,connection["cost"])
            self.frontier_nodes.append(new_node)
         # Test
        self.print_nodes("Nós fronteira após Lisboa:",self.frontier_nodes)

        #loop until open the target node!
        #node_to_open = self.get_smaller_cost(self.frontier_nodes)
        node_to_open = self.frontier_nodes[0]
        #openning the actual node
        self.open_nodes.append(node_to_open)

        self.print_nodes("Nós abertos:",self.open_nodes)

        for connection in self.data["connections"]:
            if connection["node1"] == node_to_open.get_name():
                new_node = nodes.Node(connection["node2"],node_to_open,connection["cost"])
                self.frontier_nodes.append(new_node)

        self.print_nodes("Nós fronteira:",self.frontier_nodes)

        # Garantir que não há nós abertos na nova fronteira....
        #new_frontier_nodes = []
        #for nd in self.frontier_nodes:
        #    if not in_open_nodes(nd):
        #        new_frontier_nodes.append(nd)
        #self.frontier_nodes = new_frontier_nodes

        # bla bla ...
        # Test





def main():
    uf = Uniform_search("Lisboa","Guarda")
    uf.load_data("./cities2.conf")
    uf.run()
main()
