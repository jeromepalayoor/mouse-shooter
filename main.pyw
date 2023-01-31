import pygame

width,height = 1000,600
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Mouse Shooter")

info = []

count = 0
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(20)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
    win.fill((255,255,255))

    count += 1

    pos = pygame.mouse.get_pos()
    if (pos[0] != width//2 and pos[1] != height//2):
        if count >= 7:
            x_vel = ((pos[0]-(width//2))/30)*2
            y_vel = ((pos[1]-(height//2))/30)*2
            info.append([width//2,height//2,x_vel,y_vel])

    if count == 7:
        count = 0
    
    pygame.draw.circle(win,(255,0,0),(width//2,height//2),20)
    
    for i,point in enumerate(info):
        pygame.draw.circle(win,(0,0,0),(point[0],point[1]),10)
        info[i][0] += point[2]
        info[i][1] += point[3]
        if point[0] < 0 or point[0] > width or point[1] < 0 or point[1] > height:
            info.remove(point)
    
    pygame.display.update()

pygame.quit()
exit()