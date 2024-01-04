import unittest
from unittest.mock import patch
import race
from arcade import key

class TestRaceGameRegression(unittest.TestCase):

    def setUp(self):
        self.game = race.Mygame()
        self.game.setup()

    def test_initialization(self):
        """Test that all game elements are correctly initialized."""
        self.assertIsNotNone(self.game.car_list, "Car list should be initialized")
        self.assertIsNotNone(self.game.fuel_list, "Fuel list should be initialized")
        self.assertIsNotNone(self.game.road_list, "Road list should be initialized")
        self.assertIsNotNone(self.game.obstacle_list, "Obstacle list should be initialized")
        self.assertEqual(self.game.lives, 3, "Initial lives should be 3")
        self.assertEqual(self.game.fuel_left, 10, "Initial fuel should be 10")

    @patch('race.arcade')
    def test_user_input_handling(self, mock_arcade):
        """Test response to key presses."""
        self.game.on_key_press(key.LEFT, None)
        self.assertEqual(self.game.car_sprite.change_x, -6, "Car should move left on pressing LEFT key")

        self.game.on_key_press(key.RIGHT, None)
        self.assertEqual(self.game.car_sprite.change_x, 6, "Car should move right on pressing RIGHT key")

        self.game.on_key_release(key.LEFT, None)
        self.game.on_key_release(key.RIGHT, None)
        self.assertEqual(self.game.car_sprite.change_x, 0, "Car should stop moving on key release")

    def test_update_logic(self):
        """Test the update logic of the game."""
        initial_distance = self.game.distance
        initial_fuel_left = self.game.fuel_left

        self.game.on_update(1)  # Simulating a frame update
        self.assertTrue(self.game.distance > initial_distance, "Distance should increase over time")
        self.assertTrue(self.game.fuel_left <= initial_fuel_left, "Fuel should decrease over time")

    def test_collision_detection_with_fuel(self):
        """Test collision detection logic with fuel."""
        mock_fuel = race.arcade.Sprite(":resources:images/items/coinGold.png", 0.5)
        mock_fuel.center_x = self.game.car_sprite.center_x
        mock_fuel.center_y = self.game.car_sprite.center_y

        self.game.fuel_list.append(mock_fuel)
        self.game.on_update(1)

        self.assertTrue(self.game.fuel_left > 10, "Fuel should increase on collecting fuel")

    def test_collision_detection_with_obstacle(self):
        """Test collision detection logic with obstacle."""
        mock_obstacle = race.arcade.Sprite(":resources:images/tiles/boxCrate_double.png", 0.5)
        mock_obstacle.center_x = self.game.car_sprite.center_x
        mock_obstacle.center_y = self.game.car_sprite.center_y

        self.game.obstacle_list.append(mock_obstacle)
        self.game.on_update(1)

        self.assertTrue(self.game.lives < 3, "Lives should decrease on hitting an obstacle")

    def test_boundary_conditions(self):
        """Test the boundary conditions for the car sprite."""
        self.game.car_sprite.center_x = -10
        self.game.on_update(1)
        self.assertGreaterEqual(self.game.car_sprite.center_x, 0, "Car should not go beyond left boundary")

        self.game.car_sprite.center_x = race.SCREEN_WIDTH + 10
        self.game.on_update(1)
        self.assertLessEqual(self.game.car_sprite.center_x, race.SCREEN_WIDTH, "Car should not go beyond right boundary")

if __name__ == '__main__':
    unittest.main()
