class Example:
    name = "Example"

    @staticmethod
    def static():
        print "%s static() called" % Example.name

class Offspring1(Example):
    name = "Offspring1"

class Offspring2(Example):
    name = "Offspring2"

    @staticmethod
    def static():
        print "%s static() called" % Offspring2.name
        
Example.static()
Offspring1.static()
Offspring2.static()