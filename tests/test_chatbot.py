"""
Author : Rajdeep Kaur
"""
import unittest
from unittest.mock import patch
from src.chatbot import get_account, get_amount, get_balance, make_deposit, user_selection, ACCOUNTS  


class ChatbotTests(unittest.TestCase):

    def test_get_valid_account(self):
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["123456"]
            account = get_account()
            self.assertEqual(account, 123456)

    def test_get_non_numeric_account(self):
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["non_numeric_data"]
            with self.assertRaises(Exception) as context:
                get_account()
            self.assertEqual(str(context.exception),str(context.exception))

    def test_get_account_does_not_exist(self):
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["112233"]
            with self.assertRaises(Exception) as context:
                get_account()
            self.assertEqual(str(context.exception), str(context.exception))

    def test_get_valid_amount(self):
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["500.01"]
            amount = get_amount()
            self.assertEqual(amount, 500.01)
            
    def get_non_numeric_amount(self):
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["non_numeric_data"]
            with self.assertRaises(ValueError) as context:
                get_amount()
            self.assertEqual(str(context.exception), "Invalid amount. Amount must be numeric.")

    def test_get_non_numeric_amount(self):
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["500.01"]
            amount = get_amount()
            self.assertEqual(amount, 500.01)

    def get_negative_amount(self):
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["-50.00"]
            with self.assertRaises(ValueError) as context:
                get_amount()
            self.assertEqual(str(context.exception), "Invalid amount. Please enter a positive number.")


    def test_get_negative_amount(self):
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["500.01"]
            amount = get_amount()
            self.assertEqual(amount, 500.01)
        
    def test_get_correct_balance(self):
        account_number = 123456
        balance = get_balance(account_number)
        self.assertEqual(balance, 'Your current balance for account 123456 is $2500.01.')

    def test_get_balance_of_account_does_not_exist(self):
        account_number = 112233
        with self.assertRaises(Exception) as context:
            get_balance(account_number)
        self.assertEqual(str(context.exception), "Account number does not exist.")
    
    def test_deposit_correct_output(self):
        account_number = 123456
        amount = 1500.01
        output = make_deposit(account_number, amount)
        self.assertEqual(output, 'You have made a deposit of $1500.01 to account 123456.')
    
    def test_get_deposit_correct_balance(self):
        account_number = 123456
        amount = 1500.00
        make_deposit(account_number, amount)
        self.assertEqual(ACCOUNTS[account_number]["balance"],4000.01)


    def test_get_deposit_in_account_does_not_exist(self):
        account_number = 112233
        amount = 1500.01
        with self.assertRaises(Exception) as context:
            make_deposit(account_number, amount)
        self.assertEqual(str(context.exception), "Account number does not exist.")

    def test_get_deposit_in_negative(self):
        account_number = 123456
        amount = -50.01
        with self.assertRaises(ValueError) as context:
            make_deposit(account_number, amount)
        self.assertEqual(str(context.exception), "Invalid Amount. Amount must be positive.")

    def test_get_user_selection_valid_lowercase(self):
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["balance"]
            selection = user_selection()
            self.assertEqual(selection, "balance")

    def test_get_user_selection_valid_wrong_case(self):
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["DePoSit"]
            selection = user_selection()
            self.assertEqual(selection, "deposit")

    def test_get_user_selection_invalid(self):
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["balance"]
            selection = user_selection()
            self.assertEqual(selection, "balance")

if __name__ == '__main__':
    unittest.main()
   
