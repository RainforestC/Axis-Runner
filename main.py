import pygame
from pygame.locals import * 

from Model import *
from View import * 
from GlobalData import *
from Status import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    GlobalData.screen = screen
    pygame.display.set_caption('Test')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    clock = pygame.time.Clock()
    GlobalData.clock = clock

    view1,view2 = TextView(),TextView((0,200,0))
    model1,model2 = CounterModel(view1,114514),TimerModel(view2)
    GlobalData.statusList = [CounterStatus(model1,view1),TimerStatus(model2,view2)]
    GlobalData.changeStatus(0)

    while 1:
        clock.tick(60) #<=60

        status = GlobalData.getStatus()
        status.timeElapse()
        for event in pygame.event.get():
            status.handle(event)

if __name__ == '__main__': main()