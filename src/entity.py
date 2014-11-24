# -*- coding: utf-8 -*-

import state_machine

class entity(object):
	rested = 'RESTED'
	tired = 'TIRED'
	full = 'FULL'
	thirsty = 'THIRSTY'
	resume_state = 'RESUME_STATE'
	not_thirsty = 'NOT_THIRSTY'

	def __init__(self, initState):
		self.state_machine = state_machine.state_machine()
		self.state_machine.setState(self, initState)

	def update(self):
		self.state_machine.update(self)

	def sendEvent(self, event):
		pass
