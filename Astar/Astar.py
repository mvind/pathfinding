import queue
from main import *
import math

def translate_cords(cords):
    # Input coords (300, 420) -> (14, 20)
    # This function is used to translate between screens coordinates and the 24x24 grid
    return (cords[0]/20, cords[1]/20)

def Find_rect(cords, sprite_group):
    for r in sprite_group:
        if r.xpos == cords[0]*20 and r.ypos == cords[1]*20:
            return r
    return 0

def get_neighbors(cords, sprite_group):
    # Input coords (3, 4)
    # Returns a set of coordniates of neighbors to the input coordinate
    # If a neighbor is wall the coordinate is not returned 
    x = cords[0]
    y = cords[1]
    #print(x,y)
    # Catch if coordinates doenst make sense 
    if x > 24 or x < 0:
        return 0
    elif y > 24 or y <0:
        return 0

    # This is just a list of neightbors
    raw_list = [ [x,y-1], [x-1, y], [x+1, y],
                [x, y+1]]
    mod_list = []

    for i, li in enumerate(raw_list):
        # Li = set 
        # i = index in rawlist
        # First we delete out of bounds coordinates
        fail = False
        if li[0] < 0 or li[0] > 24:
            fail = True
        elif li[1] < 0 or li[1] > 24:
            fail = True

        # Delete cordinates which coresponds to rect which is wall
        if Find_rect(li, sprite_group) == 0:
            fail = True

        elif not Find_rect(li, sprite_group).wall: # If wall delete coordinate
            if not fail:
                mod_list.append(li)

   
    
    neighbor_list = tuple((tuple(t) for t in mod_list))
    return neighbor_list

def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.append(current)
    #print(total_path)
    return total_path
    

def search(start_node: tuple, end_node: tuple, sprite_group):
    #print(start_node, end_node)
    start_node = translate_cords(start_node)
    end_node = translate_cords(end_node)

    gs = dict()
    fs = dict()
    came_from = dict()

    closed_set = set()
    open_set = set()
    open_set.add(start_node)
    print(open_set)
    def gScore(cords):
        x = cords[0]
        y = cords[1]

        return abs(start_node[0]-x) + abs(start_node[1]-y)

    def fScore(cords):
        x = cords[0]
        y = cords[1]
        return abs(end_node[0]-x) + abs(end_node[1]-y)
        # return math.sqrt(abs(end_node[0]-x)**2 + abs(end_node[1]-y)**2)

    while len(open_set) != 0:
        current = [None, None]
        for e in open_set:
            if current[0] == None:
                current[0] = fScore(e)
                current[1] = e
            elif fScore(e) < current[0]:
                current[0] = fScore(e)
                current[1] = e
        
        if current[1] == end_node:
            print('Found path!')
            return reconstruct_path(came_from, current[1])

        open_set.remove(current[1])
        closed_set.add(current[1])

        nbs = get_neighbors(current[1], sprite_group)
        for nb in nbs:

            if nb in closed_set:
                continue

            tentative_gScore = gScore(current[1]) + abs(nb[0]-current[1][0]) + abs(nb[1]-current[1][1])

            if nb not in open_set:
                open_set.add(nb)
            elif tentative_gScore >= gScore(nb):
                continue
            

            came_from[nb] = current[1]
            gs[nb] = tentative_gScore
            fs[nb] = gScore(nb) + fScore(nb)
    
    