

import pygame
pygame.init()

class Sprite:
    
    #Constructor (Entering file location, x position, y position, screen surface)
    def __init__(self,img,x,y,screen,x_width=0,y_width=0,x_spam=0,y_spam=0):

        self.__img=img
        self.__x=x
        self.__y=y
        
        self.__sprite=pygame.image.load(self.__img)
        self.__screen=screen

        self.__animation_rate=30
        
        #Set Rect parameters to 0 by default
        if (x_width is None) or (y_width is None) or (x_spam is None) or (y_spam is None):
            self.__x_width=0
            self.__y_width=0
            self.__x_spam=0
            self.__y_spam=0
        else:
            self.__x_width=x_width
            self.__y_width=y_width
            self.__x_spam=x_spam
            self.__y_spam=y_spam
              
        self.__x_num=0
        self.__y_num=0
          
    #Flip sprite, Enter True on x to flip horizontally; Enter True on y to flip vertically
    def flip(self,x_flip,y_flip):
        if x_flip:
            self.__sprite=pygame.transform.flip(self.__sprite,True,False)
        elif y_flip:
            self.__sprite=pygame.transform.flip(self.__sprite,False,True)
        else:
            self.__sprite=pygame.transform.flip(self.__sprite,True,True)
            
    #Change scale of the sprite, enter the width of x and width of y
    def scale(self,x_scale,y_scale):
        self.__sprite=pygame.transform.scale(self.__sprite,(x_scale,y_scale))
        self.__x_width=int(x_scale/self.__x_spam)
        self.__y_width=int(y_scale/self.__y_spam)

        
    #Draw function, draw sprite using blit function
    def draw(self):
        self.__screen.blit(self.__sprite,(self.__x,self.__y))
                
    #Change image function, enter new image location
    def image(self,image):
        self.__sprite=pygame.image.load(image)
          
    #Change x_position
    @property
    def x_position(self):
        return self.__x
    @x_position.setter
    def x_position(self,new_x):
        self.__x=new_x

    #Change y_position
    @property
    def y_position(self):
        return self.__y
    @y_position.setter
    def y_position(self,new_y):
        self.__y=new_y

    #Change animation rate
    @property
    def rate(self):
        return self.__animation_rate
    @rate.setter
    def rate(self,new_rate):
        self.__animation_rate=new_rate
        
    #Draw sprite sheet
    def draw_sheet(self):
        self.__screen.blit(self.__sprite,(self.__x,self.__y),(self.__x_num*self.__x_width,self.__y_num*self.__y_width,self.__x_width,self.__y_width))
                
    #Update position
    def update(self):
        if self.__animation_rate!=0:
            delay=1/self.__animation_rate
            pygame.time.wait(int(delay*1000))
            
            if self.__x_num<self.__x_spam-1:
                self.__x_num+=1

            else:
                self.__x_num=0
                if self.__y_num<self.__y_spam-1:
                    self.__y_num+=1
                else:
                    self.__y_num=0
              
import pygame
import sprite

w = pygame.display.set_mode([1000,667])

background = sprite.Sprite("StreetLight.jpg", 0, 0)
car = sprite.Sprite("Car.png", 400, 100)
drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
    background.draw()
    car.draw()
    pygame.display.flip()
            

