import queue
from main import *
import time

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

    # for r in mod_list:
    #     Find_rect(r, sprite_group)._color = (255, 0, 255)
    
    neighbor_list = tuple((tuple(t) for t in mod_list))
    return neighbor_list

# Does not work!
def construct_path(meta, end):
    action_list = list()
    direction = end
    i = 1
    while meta[direction] is not None:
        i+= 1
        direction = meta[direction]
        print('dir: ', direction, 'i: ', i)
        action_list.append(direction)
        
    print(action_list.reverse())
    return action_list.reverse()


def search(start_node: tuple, end_node: tuple, sprite_group):
    #print(start_node, end_node)
    start_node = translate_cords(start_node)
    end_node = translate_cords(end_node)
    
    open_set = queue.Queue()
    closed_set = set()
    meta = dict()
    meta[start_node] = (None)

    open_set.put(start_node)
    last_key = tuple
    while not open_set.empty():
        subtree_open = open_set.get()

        if end_node == subtree_open:
            print('Path found to end node!')
            meta[end_node] = (subtree_open)
            break

        for nb in get_neighbors(subtree_open, sprite_group):
            
            if nb in closed_set:
                continue
            if nb not in open_set.queue:
                Find_rect(nb, sprite_group)._color = (255, 0, 255)
                #print('Added to queue: ', nb)
                meta[nb] = (subtree_open)
                open_set.put(nb)
        last_key = subtree_open
        
        closed_set.add(subtree_open)


    return 0
