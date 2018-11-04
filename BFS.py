import queue
from main import *

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
    raw_list = [[x-1,y-1], [x,y-1], [x+1, y-1], [x-1, y], [x+1, y],
                [x-1, y+1], [x, y+1], [x+1, y+1]]
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

    for r in mod_list:
        Find_rect(r, sprite_group)._color = (255, 0, 255)
    
    neighbor_list = tuple((tuple(t) for t in mod_list))
    return neighbor_list

def search(start_node: tuple, end_node: tuple, sprite_group):
    #print(start_node, end_node)
    start_node = translate_cords(start_node)
    end_node = translate_cords(end_node)

    
