from django.test import TestCase
from django.urls import resolve
from blog.views import home_page
# from blog.models import Post
# from django.contrib.auth import authenticate


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'devBlog/home.html')


# class ItemModelTest(TestCase):
#
#     def test_saving_and_retrieving_items(self):
#         user = authenticate(username='testAdmin', password='pWVTQdg4pu7sLL2')
#
#         first_post = Post()
#         first_post.title = "The first post's title"
#         first_post.text = 'The first list post'
#         first_post.author = user
#         first_post.publish()
#
#         second_post = Post()
#         second_post.title = "The second post's title"
#         second_post.text = 'The second post'
#         second_post.author = user
#         second_post.publish()
#
#         saved_posts = Post.objects.all()
#         self.assertEqual(saved_posts.count(), 2)
#
#         first_saved_post = saved_posts[0]
#         second_saved_post = saved_posts[1]
#         self.assertEqual(first_saved_post.text, 'The first list post')
#         self.assertEqual(second_saved_post.text, 'The second post')
