import unittest
import crawler

class CrawlerTester(unittest.TestCase):
    dirs_to_skip = ["Program Files (x86)", "Program Files", "Windows",
                    "Really Long Directory Name to Test For Length Issues"]
    start_dir = "./crawler_test_dir"

    def test_should_skip(self):
        self.assertTrue(crawler.should_skip(r"Windows", self.dirs_to_skip))
        self.assertTrue(crawler.should_skip(r"./crawler/crawler_test_dir\Windows", self.dirs_to_skip))
        self.assertTrue(crawler.should_skip(r"./crawler/crawler_test_dir\Program Files (x86)", self.dirs_to_skip))
        self.assertTrue(crawler.should_skip(r"./crawler/crawler_test_dir\Program Files", self.dirs_to_skip))
        self.assertFalse(crawler.should_skip(r"./crawler/crawler_test_dir\Users\Victim\Videos", self.dirs_to_skip))

    def test_crawl_files(self):
        result = crawler.crawl_files(self.start_dir, self.dirs_to_skip)
        assert result is not None
        assert len(result) > 0
        for file in result:
            assert("dont touch" not in file.path)

if __name__ == '__main__':
    unittest.main()