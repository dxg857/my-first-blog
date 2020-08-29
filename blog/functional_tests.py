from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_blog(self):
        # Lets open up a tab with the blog about me, Dom, to check out what I've been up to
        self.browser.get('http://localhost:8000')

        # Here we see the title is "Beep Boop Dom", which is a natural indicator of a programmer
        self.assertIn('Beep Boop Dom', self.browser.title)
        self.fail('Finish the test!')

        # Once we're on the home page, we can see a few posts already made by me, with the latest
        # one being titled "Working with Django"

        # We actually have to log in as an administrator of the blog in order to create new posts
        # And once we do we should see the "Add Post" button in the bottom left corner of the screen

        # We try adding a new post with the title "Test Post" and a randomly generated sha-256 hash
        # as its text

        # We are taken back to the home page and it now shows the latest post that was just created


if __name__ == '__main__':
    unittest.main(warnings='ignore')
