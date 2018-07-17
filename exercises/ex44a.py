class Parent(object):

	def implicit(self):
		print "Hello there i'm the Parent"

class Child(Parent):
	pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()