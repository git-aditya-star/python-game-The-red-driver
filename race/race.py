import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
SCREEN_height = [700,350]
SCREEN_TITLE="The Red Driver"

class Mygame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)

        self.car_list =None
        self.car_sprite=None
        self.fuel_list=None
        self.road_list=None
        self.obstacle_list=None
        self.start_frame=0
        self.distance=0
        self.fuel_left=10
        self.road_change=4
        self.set_mouse_visible(False)
        self.paused = False
        self.lives=3
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        self.paused=False
        self.lives=3
        self.distance=0
        self.fuel_left=10
        self.car_list=arcade.SpriteList()
        self.fuel_list=arcade.SpriteList()
        self.road_list=arcade.SpriteList()
        self.obstacle_list=arcade.SpriteList()
        for i in range(2):
            road=arcade.Sprite("images/road.png",0.8)
            road.center_x=SCREEN_WIDTH/2
            road.center_y=SCREEN_height[i]
            road.change_y=-8
            self.road_list.append(road)
        self.car_sprite=arcade.Sprite("images/car1.png",0.3)
        self.car_sprite.angle=-90
        self.car_sprite.center_x=SCREEN_WIDTH/2
        self.car_sprite.center_y=100
        self.car_sprite.change_x=0
        self.car_list.append(self.car_sprite)



    def on_draw(self):
        arcade.start_render()
        self.road_list.draw()
        self.car_list.draw()
        self.fuel_list.draw()
        self.obstacle_list.draw()
        output=f"Distance travelled : {self.distance}"
        output1=f"Fuel Left : {self.fuel_left}"
        output2=f"Lives Left : {self.lives}"
        arcade.draw_text(output1,10,40,arcade.color.WHITE,14)
        arcade.draw_text(output,10,20,arcade.color.WHITE,14)
        arcade.draw_text(output2,10,60,arcade.color.WHITE,14)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT :
            self.car_sprite.change_x=-6

        elif key == arcade.key.RIGHT :
            self.car_sprite.change_x=6


    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT :
            self.car_sprite.change_x=0

    def on_update(self, delta_time):
        if not self.paused :
            self.start_frame+=1
            if self.start_frame % 240 == 0 :
                fuel=arcade.Sprite("images/coin.png",0.2)
                fuel.center_x = random.randrange(SCREEN_WIDTH)
                fuel.center_y = SCREEN_HEIGHT
                fuel.change_y = -6
                self.fuel_list.append(fuel)
            self.fuel_list.update()
            for coin in self.fuel_list:
                if coin.center_y <0 :
                    coin.remove_from_sprite_lists()

            if self.start_frame % 30 ==0 :
                self.distance +=1
            if self.start_frame %120 == 0:
                self.fuel_left -=1
            if self.car_sprite.center_x < 40 :
                self.car_sprite.change_x =0
                self.car_sprite.center_x+=1
            if self.car_sprite.center_x > SCREEN_WIDTH - 40:
                self.car_sprite.change_x=0
                self.car_sprite.center_x-=1
            if self.start_frame % 60 == 0 :
                for road in  self.road_list :
                    road.change_y-=0.2
                for fuel in self.fuel_list :
                    fuel.change_y-=0.1



            self.car_list.update()
            self.road_list.update()
            for road in self.road_list:
                if road.center_y <0:
                    road.center_y=SCREEN_HEIGHT
            if self.fuel_left <= 0 or self.lives <=0:
                self.paused = True

            hit_list=arcade.check_for_collision_with_list(self.car_sprite,self.fuel_list)
            for i in hit_list :
                self.fuel_left+=5
                i.remove_from_sprite_lists()
            if random.randrange(100) == 0 :
                rock=arcade.Sprite("images/Layered Rock.png",0.3)
                rock.center_x = random.randrange(SCREEN_WIDTH)
                rock.center_y = SCREEN_HEIGHT
                rock.change_y = -10
                self.obstacle_list.append(rock)
            self.obstacle_list.update()
            if self.start_frame % 60 == 0:
                for rock in self.obstacle_list:
                    rock.change_y-=0.1
            for rock in self.obstacle_list:
                if rock.center_y <0 :
                    rock.remove_from_sprite_lists()
            hit_list1=arcade.check_for_collision_with_list(self.car_sprite,self.obstacle_list)
            for i in hit_list1:
                i.remove_from_sprite_lists()
                self.lives -=1




def main():
    window=Mygame()
    window.setup()
    arcade.run()
if __name__ == "__main__" :
    main()