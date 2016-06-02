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
    objects = {}

    def __init__(self, name, class_name):
        print('class GameObject called')
        self.name = name
        GameObject.objects[class_name] = self

    def get_desc(self):
        return self.name + " " + self.desc 

class Penny(GameObject):
    def __init__(self, name, class_name):
        print('class Penny called')
        GameObject.__init__(self, name, class_name)
        self.desc = "a beautiful woman"
    
class Sheldon(GameObject):
    def __init__(self, name, class_name):
        print('class Sheldon called')
        GameObject.__init__(self, name, class_name)
        self.desc = "a funny guy"

penny = Penny('Penny Hofstadter', 'penny')
sheldon = Sheldon('Sheldon Cooper', 'sheldon')
