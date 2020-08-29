from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


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

        # Once we're on the home page, we can see a few posts already made by me, with the latest
        # one being titled "Working with Django"
        post_title = self.browser.find_element_by_id('post_title').text
        self.assertIn('Working with Django', post_title)

        # We actually have to log in as an administrator of the blog in order to create new posts
        self.browser.get('http://localhost:8000/admin')
        username_box = self.browser.find_element_by_id('id_username')
        password_box = self.browser.find_element_by_id('id_password')

        # We type in the username and password for the admin account and hit enter to log in
        username_box.send_keys('Rummeris')
        password_box.send_keys('vdddnknv')
        password_box.send_keys(Keys.ENTER)
        time.sleep(1)

        # Just making sure we've successfully logged onto an admin account
        administration = self.browser.find_element_by_id('site-name').text
        self.assertIn('Django administration', administration)

        # After we log in we should go back to the home page of the blog and see the "Add Post" button in the bottom
        # left corner of the screen
        self.browser.get('http://localhost:8000')
        add_post_button = self.browser.find_element_by_id('add_post_button')

        # We try adding a new post with the title "Test Post" and a randomly generated sha-256 hash
        # as its text

        # We are taken back to the home page and it now shows the latest post that was just created


if __name__ == '__main__':
    unittest.main(warnings='ignore')
