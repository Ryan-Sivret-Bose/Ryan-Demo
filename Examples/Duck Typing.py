class VisualStudioCode:

    def execute(self):
        print('Compiling')
        print('Running')

class myEditor:

    def execute(self):
        print('Spell Check')
        print('Convention Check')
        print('Compiling')
        print('Running')


class Laptop:

    def code(self,ide):
       ide.execute() 

ide = myEditor()

lap1 = Laptop()

lap1.code(ide)
