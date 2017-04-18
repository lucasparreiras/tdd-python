import unittest
from app import meu_web_app


class TestHome(unittest.TestCase):

    def setUp(self):
        app = meu_web_app.test_client()
        self.response = app.get('/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)

    def test_content(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('<title>Lucas Parreiras</title>', str(response_str))
        self.assertIn('<h1>Lucas Parreiras</h1>', str(response_str))
        self.assertIn('<p>Programador', str(response_str))


if __name__ == '__main__':
    unittest.main()
