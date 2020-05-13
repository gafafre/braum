# from django.test import TestCase, Client
# from articles.models import Article
# from writers.models import Writer
# from django.contrib.auth.models import User


# class TestModels(TestCase):

#     print('\nTesting Articles Models ...\n')

#     def setUp(self):
#         self.client = Client()

#         # Creating a temporary Article for tests
#         self.test_user = User.objects.create_user('tester', 'tester@test.com', 'testerpassword')
#         self.test_writer = Writer.objects.create(user=self.test_user)
#         self.article1 = Article.objects.create(
#             writer_id=self.test_writer,
#             title='test title 1',
#             subtitle='test subtitle',
#         )

#     def test_article_slug(self):
#         self.assertEquals(self.article1.slug, 'test-title-1')
