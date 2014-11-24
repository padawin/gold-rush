# -*- coding: utf-8 -*-

class bank(object):
	gold = 0
	@staticmethod
	def addGold(value):
		bank.gold = bank.gold + int(value)
