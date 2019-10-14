#!/usr/bin/env python3
import sys
from pathlib import Path
from collections import OrderedDict
import unittest

thisFile = Path(__file__).absolute()
thisDir = thisFile.parent.absolute()
repoMainDir = thisDir.parent.absolute()
sys.path.insert(0, str(repoMainDir))

dict = OrderedDict

from ClassDictMeta import ClassDictMeta


class SimpleTests(unittest.TestCase):
	def testOperation1(self):
		class a(metaclass=ClassDictMeta):
			a = "b"
			c = 0xD

		self.assertEqual(a["a"], "b")
		self.assertEqual(a["c"], 0xD)


if __name__ == "__main__":
	unittest.main()
