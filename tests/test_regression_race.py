import pytest
from unittest.mock import patch
import race
#from arcade import key
import arcade

@pytest.fixture
def game_setup():
   game = race.Mygame()
   game.setup()
   return game

def test_initialization(game):
    """Test that all game elements are correctly initialized."""
    assert game.car_list is not None, "Car list should be initialized"
    assert game.fuel_list is not None, "Fuel list should be initialized"
    assert game.road_list is not None, "Road list should be initialized"
    assert game.obstacle_list is not None, "Obstacle list should be initialized"
    assert game.lives == 3, "Initial lives should be 3"
    assert game.fuel_left == 10, "Initial fuel should be 10"

@patch('race.arcade')
def test_user_input_handling(game, mock_arcade):
    """Test response to key presses."""
    game.on_key_press(key.LEFT, None)
    assert game.car_sprite.change_x == -6, "Car should move left on pressing LEFT key"

    game.on_key_press(key.RIGHT, None)
    assert game.car_sprite.change_x == 6, "Car should move right on pressing RIGHT key"
 
    game.on_key_release(key.LEFT, None)
    game.on_key_release(key.RIGHT, None)
    assert game.car_sprite.change_x == 0, "Car should stop moving on key release"

def test_update_logic(game):
    """Test the update logic of the game."""
    initial_distance = game.distance
    initial_fuel_left = game.fuel_left

    game.on_update(1)  # Simulating a frame update
    assert game.distance > initial_distance, "Distance should increase over time"
    assert game.fuel_left <= initial_fuel_left, "Fuel should decrease over time"


def test_collision_detection_with_fuel(game):
    """Test collision detection logic with fuel."""
    mock_fuel = race.arcade.Sprite(":resources:images/items/coinGold.png", 0.5)
    mock_fuel.center_x = game.car_sprite.center_x
    mock_fuel.center_y = game.car_sprite.center_y

    game.fuel_list.append(mock_fuel)
    game.on_update(1)

    assert game.fuel_left > 10, "Fuel should increase on collecting fuel"


def test_collision_detection_with_obstacle(game):
    """Test collision detection logic with obstacle."""
    mock_obstacle = race.arcade.Sprite(":resources:images/tiles/boxCrate_double.png", 0.5)
    mock_obstacle.center_x = game.car_sprite.center_x
    mock_obstacle.center_y = game.car_sprite.center_y

    game.obstacle_list.append(mock_obstacle)
    game.on_update(1)

    assert game.lives < 3, "Lives should decrease on hitting an obstacle"


def test_boundary_conditions(game):
    """Test the boundary conditions for the car sprite."""
    game.car_sprite.center_x = -10
    game.on_update(1)
    assert game.car_sprite.center_x >= 0, "Car should not go beyond left boundary"

    game.car_sprite.center_x = race.SCREEN_WIDTH + 10
    game.on_update(1)
    assert self.game.car_sprite.center_x <= race.SCREEN_WIDTH, "Car should not go beyond right boundary"
