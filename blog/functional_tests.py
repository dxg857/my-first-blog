from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_login_as_admin_and_add_and_delete_posts(self):
        # Lets open up a tab with the blog about me, Dom, to check out what I've been up to
        self.browser.get('http://localhost:8000')

        # Here we see the title is "Beep Boop Dom", which is a natural indicator of a programmer
        self.assertIn('Beep Boop Dom', self.browser.title)

        # Once we're on the home page, we can see a few posts already made by me but in order to create new posts
        # we actually have to log in as an administrator of the blog
        self.browser.get('http://localhost:8000/admin')
        username_box = self.browser.find_element_by_id('id_username')
        password_box = self.browser.find_element_by_id('id_password')

        # We type in the username and password for the admin account and hit enter to log in
        username_box.send_keys('testAdmin')
        password_box.send_keys('pWVTQdg4pu7sLL2')
        password_box.send_keys(Keys.ENTER)
        time.sleep(1)

        # Just making sure we've successfully logged onto an admin account
        administration = self.browser.find_element_by_id('site-name').text
        self.assertIn('Django administration', administration)

        # After we log in we should go back to the home page of the blog and see the "Add Post" button in the bottom
        # left corner of the screen
        self.browser.get('http://localhost:8000')
        add_post_button = self.browser.find_element_by_id('add_post_button')

        # Lets try adding a new post. First we make sure that the button works as expected and takes us to /post/new
        add_post_button.click()
        time.sleep(1)
        self.assertIn('/post/new', self.browser.current_url)

        # Then we enter the title "Test Post" and some short text ("This will be a post for testing purposes")
        title_box = self.browser.find_element_by_id('id_title')
        text_box = self.browser.find_element_by_id('id_text')

        title_box.send_keys('Test Post')
        text_box.send_keys('This will be a post for testing purposes')

        save_button = self.browser.find_element_by_id('save_btn')
        save_button.click()
        time.sleep(1)

        # We are taken back to the home page and it now shows the latest post that was just created
        post_title = self.browser.find_element_by_id('post_title')
        self.assertIn('Test Post', post_title.text)

        # Lets see if we can delete the post next, so we don't end up spamming the same post with our tests
        # First we'll need to open up the details to the post we just made
        post_title.click()
        time.sleep(1)

        # We make sure that we're looking at the correct post and then search for a delete button
        post_title = self.browser.find_element_by_id('post_title')
        self.assertIn('Test Post', post_title.text)
        delete_button = self.browser.find_element_by_id('delete_btn')

        # After we try and delete the post we should be redirected back to the home page and no longer see our test post
        delete_button.click()
        time.sleep(1)
        self.assertIn('/home', self.browser.current_url)
        post_title = self.browser.find_element_by_id('post_title')
        self.assertNotIn('Test Post', post_title.text)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
