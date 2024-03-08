# Pytest for main module

import unittest
from unittest.mock import patch, MagicMock
import main

class TestMenu(unittest.TestCase):
    """
    Unit tests for the main menu functionality of the AQUA (Air Quality Analytics) application.

    These tests verify that the main menu and its related functionalities behave as expected.
    """

    @patch('builtins.input', side_effect=['R', 'Q'])
    @patch('main.clear_screen')
    @patch('main.reporting_menu')
    @patch('main.quit')
    def test_main_menu(self, mock_quit, mock_reporting_menu, mock_clear_screen, mock_input):
        """
        Test the main_menu function.

        This test verifies that the main_menu function correctly calls the reporting_menu
        and quit functions based on user input.

        Args:
            mock_quit (MagicMock): Mock object for the quit function.
            mock_reporting_menu (MagicMock): Mock object for the reporting_menu function.
            mock_clear_screen (MagicMock): Mock object for the clear_screen function.
            mock_input (MagicMock): Mock object for the input function.
        """

        # test initial call to clear_screen
        mock_clear_screen.assert_called_once()

        # test input 'R' calls reporting_menu
        mock_reporting_menu.assert_called_once()

        # test input 'Q' calls quit
        mock_quit.assert_called_once()

    # Additional test cases for other menu functions can be added here

if __name__ == "__main__":
    unittest.main()

