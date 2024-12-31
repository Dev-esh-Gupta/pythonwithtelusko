class PyCharm:
    def execute(self):
        print('Compiling')
        print('Running')


# Both having save function that is both acting as duck
class MyEditor:
    def execute(self):
        print('Spell Check')
        print('Convention Check')
        print('Compiling')
        print('Running')


class Laptop:
    def code(self, ide):
        ide.execute()


ide = PyCharm()
ide2 = MyEditor()

lap1 = Laptop()
lap1.code(ide)
print()
lap1.code(ide2)
