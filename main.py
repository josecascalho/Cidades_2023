import json
import nodes

import stack
#import queue

def print_nodes(dsc:str,ns:list):
	print(dsc,":")
	for n in ns:
		n.print()


def print_path(last:nodes.Node ):
	"""
	Print the sequence of steps (with increasing cost) from root to goal node
	:return:
	"""
	node = last
	path = []
	while (not (node is None)):
		if node.get_parent() is None:
			path.insert(0, [node.get_name(),node.get_total_cost(),"(root)"])
		else:
			path.insert(0, [node.get_name(),node.get_total_cost(),node.get_parent().get_name()])

		node = node.get_parent()
	for step in path:
		print(step[2],"-",step[1],"->",step[0])

def in_nodes_list(nm:str, nodes:list) -> bool:
	names_list = []
	for n in nodes:
		names_list.append(n.get_name())
	# Test
	#print("in_nodes_list:",names_list)
	if nm in names_list:
		return True
	else:
		return False



# Example of Search using cities
def read_file(cities:str) -> list:
	with open(cities) as config_file:
		# Reading the configuration file
		lst = json.load(config_file)
		# Test: printing config file
		print("Configuração:",lst)
	return lst

def main():
	# data structure
	#cities = read_file("./cities.conf")
	# root
	#root = nodes.Node("Lisboa",None,0)

	# First test:
	# Get all connections from Lisboa
	#frontier_nodes =stack.Stack()
	#frontier_nodes.put(root)
	#visited_nodes = []
	#frontier_nodes.pop()
	#for cn in cities["connections"]:
	#	if cn["from"] == "Lisboa":
	#		new_node = nodes.Node(cn["to"],root,cn["cost"])
	#		frontier_nodes.put(new_node)
	#visited_nodes.append(root)
	#frontier_nodes.print_stack("Frontier nodes")
	#print_nodes("Opened nodes",opened_nodes)


	# Deep First Seach from Lisboa to Faro
	cities = read_file("./cities.conf")
	# root
	root = nodes.Node("Leiria",None,0)
	# Initializing stack to keep in frontier
	frontier_nodes = stack.Stack()
	visited_nodes = []
	end = False
	solution = False
	last_node = None
	goal_node_name = "Faro"
	frontier_nodes.push(root)
	while end== False:
		print("Size of frontiers nodes:",frontier_nodes.get_size())
		if frontier_nodes.empty():
			end = True
			print("Solution not found!")
		else:
			node = frontier_nodes.pop()
			visited_nodes.append(node)
			if node.get_name() == goal_node_name:
				end = True
				solution = True
				last_node = node
				print("Solution found!")
			else:
				for cn in cities["connections"]:
					if node.get_name() ==  cn["from"]:
						# if not in frontier nor in *visited nodes*
						# Test
						#print("New node:",new_node.get_name())
						if not in_nodes_list(cn["to"],frontier_nodes.get_list()):
							if not in_nodes_list(cn["to"],visited_nodes):
								new_node = nodes.Node(cn["to"],node,cn["cost"])

								# Test
								#print("New node not in the frontiers and not visited!")
								frontier_nodes.push(new_node)
								# Test
								frontier_nodes.print_stack("Stack")

	if solution == True:
		print("Last node:",last_node.get_name())
		print("Root node:",root.get_name())
		print_path(last_node)
main()





