import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def test_can_start_todo_list(self) -> None:
        # and it navigates to the To-do list app
        self.browser.get("http://localhost:8000")

        # The user can see that it is in the to-do list app by the title
        self.assertIn("To-Do", self.browser.title)


        # The user sees there is a field to add an item
        # The user adds an item "Do the dishes"
        # The app reloads and it shows "1: Do the dishes"
        # The field is still there for more items

        # The user is satisfied and close the app
        self.fail("Finish the tests")

if __name__ == "__main__":
    unittest.main()
