import pygame, sys, math
import BFS
import blocks

def main():
    
    screen = pygame.display.set_mode((width, height))
    Clock = pygame.time.Clock()
    grid_sprite_list = pygame.sprite.Group()
    
    def find_rect(x,y):
        # Input x,y coordinates x,y in [0, 24]
        # Returns Sprite object in grid group located at x,y in grid
        x_pos = 20*x
        y_pos = 20*y 
        for r in grid_sprite_list:
            if r.rect.x == x_pos and r.rect.y == y_pos:
                return r
        return None

    def mouse_translate(cords):
        # Input raw mouse position
        # Output position in x,y coordniates on the grid, i.e (12, 102) -> (0, 100)
        x = cords[0] + 12 # Coords are offset by half of width of grids beause we meausre from top left corner of the mouse position.
        y = cords[1] + 12

        x = math.trunc(x / 20)
        y = math.trunc(y / 20) 
        
        # Edge cases because we start counting the grid from 0
        if x > 0:
            x -= 1
            
        if y > 0:
            y -= 1
        
        return (x,y)

    # Initiate grid 
    for i in range(int(width/20)):
        for j in range(int(height/20)):
            grid_sprite_list.add(grid(i*20, j*20))

    

    # Game loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # Handle set starter node event
                if event.key == pygame.K_s:
                    x,y = mouse_translate(pygame.mouse.get_pos())
                    r = find_rect(x,y)
                    
                    if r == None: # Catch not found rect
                        break
                    elif r._color == green: # If already starting point set back to normal point
                        r._color = std_block_color
                        r.start = False
                    else:
                        r._color = green
                        r.start = True
                # Handle set end node event
                elif event.key == pygame.K_e:
                    x,y = mouse_translate(pygame.mouse.get_pos())
                    r = find_rect(x,y)
                    
                    if r == None: # Catch not found rect
                        break
                    elif r._color == red: # If already end point set back to normal point
                        r._color = std_block_color
                        r._end = False
                    else:
                        r._color = red
                        r.end = True
                elif event.key == pygame.K_SPACE:
                    start_node = tuple
                    end_node = tuple
                    for r in grid_sprite_list:
                        if r.start:
                            start_node = (r.xpos, r.ypos)
                            
                        elif r.end:
                            end_node = (r.xpos, r.ypos)
                            
                    BFS.search(start_node, end_node, grid_sprite_list)


        # Handle mouse cursour button being hold
        if pygame.mouse.get_pressed()[0] == 1:
            # If mouse pressed the coresponding grid block will become a wall
            # Start and end nodes will be ignored
            x,y = mouse_translate(pygame.mouse.get_pos())
            r = find_rect(x,y)
            if r == None:
                return 0
            elif r.start == True or r.end == True:
                return 0
            
            else:
                r.wall = True
                r._color = wall_block_color
        # Delete walls if shift + mouse pressed. Ignores end and start points walls
        if pygame.mouse.get_pressed()[0] == 1 and pygame.key.get_pressed()[304] == 1:
            x,y = mouse_translate(pygame.mouse.get_pos())
            r = find_rect(x,y)
            if r == None:
                return 0
            elif r.start == True or r.end == True:
                return 0
            
            elif r.wall == True:
                r.wall = False
                r._color = std_block_color
            elif r.wall == False:
                return 0
        screen.fill(main_background)

        grid_sprite_list.draw(screen)
        grid_sprite_list.update()

        

        
        pygame.display.flip()
        
        Clock.tick(30)

if __name__ == '__main__':
    grid = blocks.Grid # Import block class used to create grid 
    # Game settings
    # Dont touch width and height as alot function are staticly defined out of these variables
    width, height = (500, 500)
    green = (127, 255, 0)
    red = (250, 18, 18)
    wall_block_color = (47, 79, 79)
    std_block_color = (211, 211, 211)
    main_background = (255, 255, 255)
    main()