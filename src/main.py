# -*- coding: utf-8 -*-

import miner
from time import sleep
import sys

def main(argv):
	m = miner.miner()

	while (True):
		m.update()
		sleep(3)

if __name__ == "__main__":
	main(sys.argv[1:])

