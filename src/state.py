# -*- coding: utf-8 -*-

from entity import entity
from bank import bank

class state(object):
	def enter(self, e):
		return

	def execute(self, e):
		return

	def exit(self, e):
		return

class mining(state):
	def enter(self, e):
		print("I'm starting to mine")

	def execute(self, e):
		print("I'm mining...")
		e.increaseLoad(1)
		e.increaseThirst(1)
		e.burnStamina(1)
		print("My load is " + str(e.getLoad()))
		print("My thirst is " + str(e.getThirst()))
		print("My stamina is " + str(e.getStamina()))

		if e.getLoad() >= e.getMaxLoad():
			e.sendEvent(entity.full)
		elif e.getThirst() >= e.getMaxThirst():
			e.sendEvent(entity.thirsty)
		elif e.getStamina() <= e.getMinStamina():
			e.sendEvent(entity.tired)

	def exit(self, e):
		print("I'm done mining")

class drinking(state):
	def enter(self, e):
		print("I'm starting to drink")

	def execute(self, e):
		print("I'm drinking a glass of very good whisky")
		e.decreaseThirst(1)
		if e.getThirst() < e.getMinThirst():
			e.sendEvent(entity.not_thirsty)

	def exit(self, e):
		print("I'm done drinking... for now")

class resting(state):
	def enter(self, e):
		print("I'm starting to rest")

	def execute(self, e):
		if e.getStamina() < e.getMaxStamina():
			print("ZzzZZz")
			e.increaseStamina(1)
		else:
			e.sendEvent(entity.rested)

	def exit(self, e):
		print("I'm rested")

class goToBank(state):
	def enter(self, e):
		print("I'm going to the bank")

	def execute(self, e):
		bank.addGold(e.getLoad())
		e.setLoad(0)
		e.sendEvent(entity.resume_state)

	def exit(self, e):
		print("I can resume my work")
