def get_input():
    command = input(":").split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unknown verb {}".format(verb_word))
        return

    if len(command)>= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb())

def say(noun):
    return "You said {}".format(noun)

def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return "There is no {} here".format(noun)
                                
class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        print('init class GameObject called')
        self.name = name
        GameObject.objects[self.class_name] = self
        print('self = {}'.format(self))
        print('class name = {}'.format(self.class_name))
        print('Objects = {}'.format(GameObject.objects))

    def get_desc(self):
        return self.name + " " + self.desc 

class Penny(GameObject):
    class_name = 'penny'
    desc = "a beautiful woman"
    
class Sheldon(GameObject):
    class_name = "sheldon"
    desc = "a funny guy"

penny = Penny("Penny Hofstadter")
sheldon = Sheldon("Sheldon Cooper")

verb_dict = {"say":say, "examine":examine,}

while True:
    get_input()
