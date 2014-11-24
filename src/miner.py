# -*- coding: utf-8 -*-

from entity import entity
import state
import state_machine

class miner(entity):
	def __init__(self):
		super(miner, self).__init__(state.resting())
		self.stamina = self.getMaxStamina()
		self.setLoad(0)
		self.setThirst(0)

	def getMinStamina(self):
		return 0

	def getStamina(self):
		return self.stamina

	def increaseStamina(self, inc):
		self.stamina = self.stamina + int(inc)

	def burnStamina(self, inc):
		self.stamina = self.stamina - int(inc)

	def getMaxStamina(self):
		return 11

	def increaseLoad(self, inc):
		self.load = self.load + int(inc)

	def setLoad(self, value):
		self.load = int(value)

	def getMaxLoad(self):
		return 7

	def getLoad(self):
		return self.load

	def increaseThirst(self, inc):
		self.thirst = self.thirst + int(inc)

	def decreaseThirst(self, inc):
		self.thirst = self.thirst - int(inc)

	def setThirst(self, value):
		self.thirst = int(value)

	def getThirst(self):
		return self.thirst

	def getMaxThirst(self):
		return 6

	def getMinThirst(self):
		return 0

	def sendEvent(self, event):
		if event == entity.rested:
			self.state_machine.setState(self, state.mining())
		elif event == entity.thirsty:
			self.state_machine.setState(self, state.drinking())
		elif event == entity.tired:
			self.state_machine.setState(self, state.resting())
		elif event == entity.full:
			self.state_machine.setState(self, state.goToBank())
		elif event == entity.not_thirsty:
			self.state_machine.setState(self, state.mining())
		elif event == entity.resume_state:
			self.state_machine.resumeOldState(self)
