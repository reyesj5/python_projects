class Parent(object):
	def altered(self):
		print "check inheritance: this is Parent"

class Child(Parent):
	def altered(self):
		print "child modified function"
		super(Child, self). altered()
		print "Child after calling Parent function"

dad = Parent()
son = Child()

dad.altered()
son.altered()