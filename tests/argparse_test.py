import unittest
import sys
from toml_argparse import ExperimentParser

class ParserTest(unittest.TestCase):
    def _create_parser(self):
        parser = ExperimentParser()
        parser.add_argument("--path", type=str, default="./test")
        parser.add_argument("--number", type=int, default=10)
        return parser
    
    def test_defaults(self):
        sys.argv = ["experiment_parser.py"]
        parser = self._create_parser()
        args = parser.parse_args()
        self.assertEqual(args.path, "./test")
        self.assertEqual(args.number, 10)

    def test_config(self):
        """ This takes the default value from the .toml file and ignores sections"""
        sys.argv = ["experiment_parser.py", "--config", "config.toml"]
        parser = self._create_parser()
        args = parser.parse_args()    
        self.assertEqual(args.path, "./test")
        self.assertEqual(args.number, 0)

    def test_section(self):
        """ This takes the default value from the .toml file and ignores sections"""
        sys.argv = ["experiment_parser.py", "--config", "config.toml", "--section", "experiment_1"]
        parser = self._create_parser()
        args = parser.parse_args()
        self.assertEqual(args.path, "./path_1")
        self.assertEqual(args.number, 20)

    def test_section_2(self):
        """ This takes the default value from the .toml file and ignores sections"""
        sys.argv = ["experiment_parser.py", "--config", "config.toml", "--section", "experiment_1", "--number", "30"]
        parser = self._create_parser()
        args = parser.parse_args()
        self.assertEqual(args.path, "./path_1")
        self.assertEqual(args.number, 30)