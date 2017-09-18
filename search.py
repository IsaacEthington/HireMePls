from util import Queue, Stack, PriorityQueue

def generalSearch(problem, dataStructure = None, heuristic=None):
#This is a general graph search.
#Basic searches, Breadth-First , Depth-First Search, Universal Cost, and A* can all be easily implemented.
#Other searches can be created via simple modifiation.

'''
Problem         Contains the details of the problem, including goal states, details on successors, etc.
dataStructure   What dataStructure to use, for example Queue, Stack, PriorityQueue
heuristic       What heuristic function to use

This can be easily modified to include other features
for example, to ignore path cost and only focus on heuristic (Best-First Search, or greedy)
'''
    class Node:
        #A basic node. Includes information about self, including costs, and parent, and directions

        def __init__(self):
            self.state = 0;
            self.parent = self
            self.actionFromParent = 0
            self.pathCost =0
            self.distanceToParent = 0
            self.heuristic = 0
    
            
    def solution(n):
        #Returns a list of actions as a solution.
        
        actions = []
        while(n.state != problem.getStartState()):
            actions.insert(0, n.actionFromParent)
            n = n.parent
        return actions
    
    print('Running Search')
    node = Node()
    node.state = problem.getStartState()
    node.pathCost = 0

    frontier = dataStructure()

    #Priority Queue has a priority associated, so must be separated.
    #There is probably a more general way to do this to handle all cases. 
    if(dataStructure == PriorityQueue):
        frontier.push(node, 0)
    else:
        frontier.push (node)    
    
    explored = set()
    while not frontier.isEmpty():        
        node = frontier.pop()
        
        if problem.isGoalState(node.state):
            actions = solution(node)
            return actions

        if node.state not in explored:
            explored.add(node.state)
            
            for successor in problem.getSuccessors(node.state):
                #successor is a tuple of (State,Direction,ActionCost)
                child = Node()
                child.state = successor[0]
                child.parent = node
                child.actionFromParent = successor[1]
                
                if(dataStructure == PriorityQueue):                    
                    child.DistanceToParent = successor[2]
                    child.pathCost = successor[2] + node.pathCost
                    
                    if(heuristic not None):
                        child.heuristic = heuristic(child.state, problem)
                        
                    frontier.update(child, child.pathCost + child.heuristic)
                else:
                    frontier.push(child)
    return False

def depthFirstSearch(problem):
    #Searches deepest node first
    return generalSearch(problem, Stack, None)

def breadthFirstSearch(problem):
    #Searches shallowest node first
    return generalSearch(problem, Queue, None)
def uniformCostSearch(problem):
    #Searches shortest path first
    return generalSearch(problem, PriorityQueue, None)

def aStarSearch(problem, heuristic=nullHeuristic):
    #Searches (shortestPath + heuristic(state) first
    return generalSearch(problem, PriorityQueue, heuristic)

