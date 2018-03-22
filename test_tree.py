import pygame

import time
import random

pygame.init()

display_width=800
display_height=600

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
dark_red=(200,0,0)
brown=(101,67,33)
light_brown=(101,67,66)
orange=(255,140,0)
unknown=(112,0,112)
block_color=brown
light_orange=(255,165,0)
green=(0,200,0)
light_green=(0,240,0)

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('STATS')
clock = pygame.time.Clock()
treeImg=pygame.image.load('tree_2.png')

def tree(x,y):
    gameDisplay.blit(treeImg,(x,y))

def stat():
    font = pygame.font.SysFont(None,48)
    text =font.render('S-t-a-t-s', True ,black)
    gameDisplay.blit(text,(320,5))
    
def dis_height(he_ight):
    font = pygame.font.SysFont(None,25)
    text =font.render('Height'+' '+str(he_ight)+' '+'m', True ,black)
    gameDisplay.blit(text,(0,30))
    


     

def age(t_a):
    dis_age=int(t_a)
    font = pygame.font.SysFont(None,25)
    text =font.render('Age'+' '+str(dis_age)+' '+'Years', True ,black)
    gameDisplay.blit(text,(0,0))

def population(squirrel_pop):
    font = pygame.font.SysFont(None,25)
    text =font.render('Squirels'+' '+str(squirrel_pop)+' ', True ,black)
    gameDisplay.blit(text,(600,0))


def things(thingx,thingy,thingw,thingh,color,age):
    thing_age=int(age)
    
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def things1(thingx1,thingy1,thingw1,thingh1,color,age):
    thing_age=int(age)
    
    pygame.draw.rect(gameDisplay,color,[thingx1,thingy1,thingw1,thingh1])        



def dis_timbre(t_amt,tree_age):
    red=(255,0,0)
    color=red
    
    
    pygame.draw.rect(gameDisplay,color,[700,400,50,t_amt])
    font = pygame.font.SysFont(None,25)
    text =font.render('Timbre',True ,red)
    gameDisplay.blit(text,(670,100))
    

def dis_max_age(maxage):
    
    color=green
    maxage=int(maxage)
    pygame.draw.rect(gameDisplay,color,[100,400,50,maxage])
    font = pygame.font.SysFont(None,25)
    text =font.render('Max-Age', True ,green)
    gameDisplay.blit(text,(96,99))
    


def timbre():
    
    t_change=-1
    
        
    return t_change   
    
    


    
    
def max_age(maxage,change,squirrels):
    sqr=int(squirrels)
    sqr_add=0
    if sqr%20 != 0:
        sqr_add=0.025
    maxage=maxage+change-sqr_add
    return maxage
    

def squirels(age,pop,count):
    
    sqir=int(age)
    tim_change=0
    if count != sqir:
        if sqir%1 == 0:
            addn=random.randrange(30,50)
            pop=pop+addn
            count=sqir
            tim_change=5
            return(pop,count,tim_change)
           
    return (pop,count,tim_change)

def year(age,height):
    
    t=int(time.clock())
   
    if t%20 == 0:
        age=age+0.07
        height=height+random.randrange(0,2)
        
        
        return (age,height)
        
    else:
        return (age,height)

def collision1(thing_startx,thing_width,x,thing_speed,change):
    t_amt=0
    sq_die=0
    sq_list=[2,1,3]
    if (thing_startx + thing_width) > x :
            
            thing_startx=0-thing_width
            thing_starty=545
            t_amt=timbre()
            sq_die=random.choice(sq_list)
            
            if thing_speed >24:
                thing_speed = 12
            change=1
          
            
            
            thing_speed+=1
    return (thing_startx,thing_speed,change,t_amt,sq_die)
    
    
def collision2(thing_startx,thing_width,x_width,thing_speed,change):
    t_amt=0
    sq_die=0
    sq_list=[2,1,3]
    if thing_startx < x_width :
            
            thing_startx=800+thing_width
            thing_starty=545

            t_amt=timbre()    
            sq_die=random.choice(sq_list)
            if thing_speed < -24:
                thing_speed = -12
            change=1
            
            
            
            thing_speed+=-1
    return (thing_startx,thing_speed,change,t_amt,sq_die)

def colide_m1(thing_startx,thing_starty,thing_speed):
    m_x,m_y=pygame.mouse.get_pos()
    if (((m_x > thing_startx) and m_x < (thing_startx+50)) and (((m_y > thing_starty)and (m_y < thing_starty+50)))):
        print('inside obj')
        thing_startx=-50
        thing_speed+=1
        if thing_speed > 20:
            thing_speed=12
    return (thing_startx,thing_speed)                
                
def colide_m2(thing_startx,thing_starty,thing_speed):
    m_x,m_y=pygame.mouse.get_pos()
    if (((m_x > thing_startx) and m_x < (thing_startx+50)) and (((m_y > thing_starty)and (m_y < thing_starty+50)))):
        print('inside obj')
        thing_startx=850
        thing_speed+=-1
        if thing_speed < -20:
            thing_speed=-12
    return (thing_startx,thing_speed)      


def play(block_x,block_y,play_clor):
    pygame.draw.rect(gameDisplay,play_clor,[block_x,block_y,150,50])
    font = pygame.font.SysFont(None,48)
    text =font.render('play', True ,black)
    gameDisplay.blit(text,(375,255))


def info(block_x,block_y,play_color):
    pygame.draw.rect(gameDisplay,play_color,[block_x,block_y,150,50])
    font = pygame.font.SysFont(None,48)
    text =font.render('info', True ,black)
    gameDisplay.blit(text,(375,315))

def back(block_x,block_y,play_color):
    pygame.draw.rect(gameDisplay,play_color,[block_x,block_y,150,50])
    font = pygame.font.SysFont(None,48)
    text =font.render('back', True ,white)
    gameDisplay.blit(text,(640,20))
    
def abt(block_x,block_y,play_color):
    pygame.draw.rect(gameDisplay,play_color,[block_x,block_y,150,50])
    font = pygame.font.SysFont(None,48)
    text =font.render('about', True ,white)
    gameDisplay.blit(text,(375,375))
    
    
    
    
def info_loop():
    x_back=600
    y_back=10
    back_color=black
    
    gameExit=False
    while not gameExit:
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEMOTION:
                 m_x,m_y=pygame.mouse.get_pos()
                 if ((m_x > x_back) and (m_x < x_back+ 150)) and ((m_y > y_back)and(m_y < y_back + 50)):
                     
                     for_back=pygame.mouse.get_pressed()
                     if for_back[0] != 0:
                         intro_loop()
    
        gameDisplay.fill(light_brown)
        back(x_back,y_back,back_color)
        pygame.display.update()
        clock.tick(60)

def abt_loop():
    x_back=600
    y_back=10
    back_color=black
    
    gameExit=False
    while not gameExit:
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEMOTION:
                 m_x,m_y=pygame.mouse.get_pos()
                 if ((m_x > x_back) and (m_x < x_back+ 150)) and ((m_y > y_back)and(m_y < y_back + 50)):
                     
                     for_back=pygame.mouse.get_pressed()
                     if for_back[0] != 0:
                         intro_loop()
    
        gameDisplay.fill(light_brown)
        back(x_back,y_back,back_color)
        pygame.display.update()
        clock.tick(60)

    
    
def intro_loop():
    
    x_play=330
    y_play=250
    x_info=330
    y_info=310
    x_abt=330
    y_abt=370
    play_color=orange
    info_color=green
    abt_color=dark_red
    gameExit=False
    while not gameExit:
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            m_x,m_y=pygame.mouse.get_pos()
            if ((m_x > x_play) and (m_x < x_play + 150)) and ((m_y > y_play)and(m_y < y_play + 50)):
                play_color=light_orange
                for_play=pygame.mouse.get_pressed()
                print event
                if for_play[0] != 0:
                    game_loop()
                         
            elif ((m_x > x_info) and (m_x < x_info + 150)) and ((m_y > y_info)and(m_y < y_info + 50)):        
                info_color=light_green
                for_info=pygame.mouse.get_pressed()
                print event
                if for_info[0] != 0:
                    info_loop()

            elif ((m_x > x_abt) and (m_x < x_abt + 150)) and ((m_y > y_abt)and(m_y < y_abt + 50)):        
                abt_color=red
                for_abt=pygame.mouse.get_pressed()
                print event
                if for_abt[0] != 0:
                    abt_loop()
                                 
            else:
                play_color=orange
                info_color=green
                abt_color=dark_red
            
                 


            
       
        gameDisplay.fill(light_brown)
        stat()
        play(x_play,y_play,play_color)
        info(x_info,y_info,info_color)
        abt(x_abt,y_abt,abt_color)
        pygame.display.update()
        clock.tick(60)
    

    
def game_loop():
    
    x =(display_width * 0.25) #tree position
    y= (display_height * 0.43) #tree pos
    x_width=x+360
    tree_age=1
    pop=20
    count=0
    height=5
    change=0
    maxage=-280
    t_amt=-20
    
    thing_startx = -300# first collision object
    thing_starty= 545
    thing_speed= 4
    thing_width=50
    thing_height=50

    thing_startx1 = 900# second collision object
    thing_starty1= 545
    thing_speed1= -4
    thing_width1=50
    thing_height1=50
    
    gameExit=False
   
        

    while not gameExit:
        
        req_tup0=year(tree_age,height)
        tree_age=req_tup0[0]
        height=req_tup0[1]
        req_tup=squirels(tree_age,pop,count)
        pop=req_tup[0]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
               
            if event.type == pygame.MOUSEMOTION:
                col_m1=colide_m1(thing_startx,thing_starty,thing_speed)
                col_m2=colide_m2(thing_startx1,thing_starty1,thing_speed1)
                thing_startx=col_m1[0]
                thing_speed=col_m1[1]
                thing_startx1=col_m2[0]
                thing_speed1=col_m2[1]
                
                
           
            

            
                 

            print(event)

        
        gameDisplay.fill(white)

        #things(thingx,thingY,thingw,thingh,color)
        
        things(thing_startx,thing_starty,thing_width,thing_height,block_color,tree_age)
        thing_startx+=thing_speed
        things1(thing_startx1,thing_starty1,thing_width1,thing_height1,block_color,tree_age)
        thing_startx1+=thing_speed1
        

    
        col_take=collision1(thing_startx,thing_width,x,thing_speed,change)
        col_take1=collision2(thing_startx1,thing_width1,x_width,thing_speed1,change)
        thing_startx=col_take[0]
        thing_speed=col_take[1]
        
        
        thing_startx1=col_take1[0]
        thing_speed1=col_take1[1]
        chang_e=col_take[2]+col_take1[2]
        maxage=max_age(maxage,chang_e,pop)                   
        t_change= col_take[3]+col_take1[3]    
        
        t_amt=t_amt+t_change    
        pop=pop -(col_take[4]+col_take1[4])
        if (t_amt == -250):
            t_amt=t_amt+230
        
        t_amt+=req_tup[2]
            
            
        
        tree(x,y)
        
        
        
        age(tree_age)
        population(pop)
        count=req_tup[1]
        dis_height(height)
        dis_max_age(maxage)
        dis_timbre(t_amt,tree_age)
        stat()
        
        if (t_amt == 0) or (maxage >= 0) or (pop <=0):

            font = pygame.font.SysFont(None,132)
            text =font.render('GAME'+' '+ 'OVER ', True ,brown)

            if t_amt ==0:
                font = pygame.font.SysFont(None,96)
                text=font.render('Forrest Gump'+' '+ ' ', True ,brown)
            elif maxage >=0:
                font = pygame.font.SysFont(None,96)
                text=font.render('The City Man'+' '+ ' ', True ,brown)
            
            elif pop <=0:
                font = pygame.font.SysFont(None,72)
                text=font.render('Squirrels are'+'Neccessary too', True ,brown)
            
                
            
            
            time.sleep(2)
            gameDisplay.fill(white)
            gameDisplay.blit(text,(10,300))
            pygame.display.update()
            time.sleep(2)
            intro_loop()
            
            

        
            
        
        pygame.display.update()
        clock.tick(60)
intro_loop()
pygame.quit()
quit()
t=raw_input(" ")
