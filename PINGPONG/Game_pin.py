import arcade
SCREEN_WIDTH=1450
SCREEN_HEIGHT=800

d2=1
d1=2
print(d1,d2)

class Window(arcade.Window):

    speed=-20
    speedy=20
    pip=0
    pit=0
    a1=0
    a2=0
    a3=1
    def on_draw(self):
        self.clear((200,4,80))
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,arcade.load_texture("стол.png"))
        self.sprite.draw()
        self.poc.draw()
        self.pos.draw()
        arcade.draw_text(f"{self.a1}:{self.a2}",650,700,arcade.color.RED,100)

    def __init__(self,width,height):
        super().__init__(width,height)
        self.sprite=arcade.Sprite("мячч.png",scale=0.2)
        self.sprite.center_x=960                                   
        self.sprite.center_y=540
        self.poc=arcade.Sprite("ракетка (2).png",scale=0.4)
        self.poc.center_x=50                                   
        self.poc.center_y=540
        self.pos=arcade.Sprite("ракетка чер (2).png",scale=0.4)
        self.pos.center_x=1400                                   
        self.pos.center_y=540
        

    def update(self,delta_time):
        self.sprite.center_x+=self.speed
        if self.sprite.left<=0:
            self.sprite.center_x=SCREEN_WIDTH/2
            self.sprite.center_y=SCREEN_HEIGHT/2
            self.speed=5
        elif self.sprite.right>=SCREEN_WIDTH:
            self.sprite.center_x=SCREEN_WIDTH/2
            self.sprite.center_y=SCREEN_HEIGHT/2   
            self.speed=-5
        self.sprite.center_y+=self.speedy
        if self.sprite.top>=SCREEN_HEIGHT:
            self.speedy=-5
        elif self.sprite.bottom<=0:
            self.speedy=5
        self.poc.center_y+=self.pip
        self.pos.center_y+=self.pit
        osoe=arcade.check_for_collision(self.sprite,self.poc)
        if osoe:
            self.sprite.left=self.poc.right
            self.speed=5
            self.a1 +=1
        swe=arcade.check_for_collision(self.sprite,self.pos)
        if swe:
            self.sprite.right=self.poc.left
            self.speed=-5
            self.a2 +=1
        



    def on_key_press(self, symbol: int, modifiers: int):
        print(symbol)
        if symbol == arcade.key.W:
            self.pip=10
        if symbol == arcade.key.S:
            self.pip=-10
        if symbol == arcade.key.UP:
            self.pit=10
        if symbol == arcade.key.DOWN:
            self.pit=-10
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W:
           self.pip=0
        if symbol == arcade.key.S:
           self.pip=0
        if symbol == arcade.key.UP:
           self.pit=0
        if symbol == arcade.key.DOWN:
           self.pit=-0


w=Window(width = SCREEN_WIDTH,height = SCREEN_HEIGHT)
arcade.run()