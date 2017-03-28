import unittest
import crawler

class CrawlerTester(unittest.TestCase):

    def test_should_skip(self):
        dirs_to_skip = ["Program Files (x86)", "Program Files", "Windows", "Really Long Directory Name to Test Index Out of Bounds"]
        self.assertTrue(crawler.should_skip(r"Windows", dirs_to_skip))
        self.assertTrue(crawler.should_skip(r"./crawler/crawler_test_dir\Windows", dirs_to_skip))
        self.assertTrue(crawler.should_skip(r"./crawler/crawler_test_dir\Program Files (x86)", dirs_to_skip))
        self.assertTrue(crawler.should_skip(r"./crawler/crawler_test_dir\Program Files", dirs_to_skip))
        self.assertFalse(crawler.should_skip(r"./crawler/crawler_test_dir\Users\Victim\Videos", dirs_to_skip))

if __name__ == '__main__':
    unittest.main()