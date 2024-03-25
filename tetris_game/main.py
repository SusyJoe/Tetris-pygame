import pygame
import sys
import random
pygame.init()

#Constant variable
WIDTH, HEIGHT = 300,500
FPS = 60
CELLSIZE = 0
ROW = 0
COL = 0

#Game Settings
screen = pygame.display.setmode((WIDTH,HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
BLACK = (0,0,0)
WHITE = (255, 255, 255)
ORANGE = (255, 90, 20)
PURPLE = (255, 0, 255)

# Load Images
images = {1:pygame.image.load("Assets/Tert1.png"), 2:pygame.image.load("Assets/tet2.png", 3:pygame.image.load("Assets/tret3.png")), 1:pygame.image.load("Assets/tretr4.png")} 
font1 = pygame.font.Font(None, 40)
font2 = pygame.font.SysFont("comic sans", 40)

# Store images in dictionary


# Load fonts


# Define Tetramino (shape) class
class Tetramino:
    FIGURES = {
        'I': [[1, 5, 9, 13], [4, 5, 6, 7]],
        'Z': [[4, 5, 9, 10], [2, 6, 5, 9]],
        'S': [[6, 7, 9, 10], [1, 5, 6, 10]],
        'L': [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        'J': [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        'T': [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        'O': [[1, 2, 5, 6]]
    }
    TYPES = ['I', 'Z', 'S', 'L', 'J', 'T', 'O']

    # Constructor ~ x, y, type, shape, color, rotation
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.choice(self.TYPES)
        self.shape = self.FIGURES(self.type)
        self.color = random.randint(1,4)
        self.rotation = 0
    
    # Provide the current shape 
    def image(self):
        return self.shape[self.rotation]

    # Rotate the shape
    def rotate(self):
    self.rotation = (self.rotation+1)%len(self.shape)
    
    
    

# Define Tetris class
    # Constructor ~ rows, cols, score, level, game_board
    

    # Draw a Tetris Grid
    

    # Create a new figure
    


# Main function
def main():
    run = True
    while run:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
        clock.tick(FPS)
        pygame.display.update()