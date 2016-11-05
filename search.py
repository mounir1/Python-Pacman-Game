# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
# implemented by Mounir Abderrahmani


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #print "", problem
    #print "-Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "-Start's successors:", problem.getSuccessors(problem.getStartState())
    print "---------------------------------------------------------------------"
    #print "-Start:", problem.getStartState()
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH

    Mystack = util.Stack()
    Mystack.push( (problem.getStartState(), [], []) )
    while not Mystack.isEmpty():
        node, actions, visited = Mystack.pop()
        
        for i, direction, dots in problem.getSuccessors(node):
            #print "-node's successors:", problem.getSuccessors(i)
            #print "current i : ", i , "node :",node
            #print " successors : ",problem.getSuccessors(node)
            if i in visited:
                continue
                #print "-Is the  goal?", problem.isGoalState(i)
            elif problem.isGoalState(i):
                return actions + [direction]
            Mystack.push((i, actions + [direction], visited + [node] ))

        
        #print "- actions ", actions 
        #print "- direction :",direction
        #print "- node visited :", visited 
        #print "- nodes :", [node]
    return [] #path never found !




    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first..
    divides the graph to many possible paths and choose using the priority queue the best cost "least actions" 
"""
    print "---------------------------------------------------------------------"
    Myqueue = util.PriorityQueue()
    #state, action, action cost for priority queue  
    Myqueue.push( (problem.getStartState(), []), 0)
    visited = []
    while not Myqueue.isEmpty():
        node, actions = Myqueue.pop()
        #print "old actions : ", actions
        if problem.isGoalState(node):
            return actions

        visited.append(node)
        #print " - successors : ",problem.getSuccessors(node)
        for i, direction, dots in problem.getSuccessors(node):
            if i in visited:  #don't go back !
                continue
            else :    
                new_actions = actions + [direction]
                Myqueue.push((i, new_actions), problem.getCostOfActions(new_actions))
                #print "the action : ",new_actions
                #print " problem.getCostOfActions(new_actions) :",problem.getCostOfActions(new_actions)
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    Myqueue = util.PriorityQueue()
    start = problem.getStartState()
    Myqueue.push( (start, []), 0)
    visited = []

    while not Myqueue.isEmpty():
        node, actions = Myqueue.pop()

        if problem.isGoalState(node):
            return actions

        visited.append(node)
        successors = problem.getSuccessors(node)
        for i, direction, dots in successors:
            if i in visited:
                continue
            else:    
                new_actions = actions + [direction]
                Myqueue.push((i, new_actions), problem.getCostOfActions(new_actions))

    return []
    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
   
    Myqueue = util.PriorityQueue()
    start = problem.getStartState()
    Myqueue.push( (start, []), heuristic(start, problem))
    visited = []
    while not Myqueue.isEmpty():
        node, actions = Myqueue.pop()

        if problem.isGoalState(node): #we are done!
            return actions

        visited.append(node)

        for i, direction, cost in problem.getSuccessors(node):
            if not i in visited:
                new_actions = actions + [direction]
                score = problem.getCostOfActions(new_actions) + heuristic(i, problem)
                Myqueue.push( (i, new_actions), score)

    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
