# -*- coding: utf-8 -*-

class state_machine(object):
	def __init__(self):
		self.state = None
		self.oldState = None

	def setState(self, entity, state):
		if self.state is not None:
			self.state.exit(entity)

		self.oldState = self.state
		self.state = state
		self.state.enter(entity)

	def resumeOldState(self, entity):
		self.setState(entity, self.oldState)

	def update(self, entity):
		if self.state is not None:
			self.state.execute(entity)
