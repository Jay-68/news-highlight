import unittest
from app.models import Sources, Articles


class SourcesTest(unittest.TestCase):
    '''
    Test class for the sources
    '''

    def setUp(self):
        '''
        set up function to run before each test
        '''
        self.new_source = Sources(
            50342, 'How I met your Mother', 'A funny comedy series', '/mother', 'general', 'USA')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Sources))

      def test_instance_variables(self):
        self.assertEqual(self.new_source.id, 50342)
        self.assertEqual(self.new_source.name, 'How I met your Mother')
        self.assertEqual(self.new_source.description, 'A funny comedy series')
        self.assertEqual(self.new_source.url, '/mother')
        self.assertEqual(self.new_source.category, 'general')
        self.assertEqual(self.new_source.country, 'USA')

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('CNN','Peter Polle','The tech scene in Africa-Is it the next big thing?','A look at various tech hubs in Africa and the impact they have on the worlds economy','techie.com','techie.com/7643t94.jpg','2018-04-11T07:57:16Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'CNN')
        self.assertEquals(self.new_article.author,'Peter Polle')
        self.assertEquals(self.new_article.title,'The tech scene in Africa-Is it the next big thing?')
        self.assertEquals(self.new_article.description,'A look at various tech hubs in Africa and the impact they have on the worlds economy')
        self.assertEquals(self.new_article.url,'techie.com')
        self.assertEquals(self.new_article.image,'techie.com/7643t94.jpg')
        self.assertEquals(self.new_article.date,'2019-09-14')
