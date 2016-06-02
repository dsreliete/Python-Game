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
    def __init__(self, name):
        self.class_name = 'penny'
        self.internet = 0
        self.desc = "a beautiful woman"
        super().__init__(name)

    @property
    def desc(self):
        if self.internet == 0:
            return self.internet
        elif self.internet == 1:
            use = 'get your own Wi-Fi'
        elif self.internet == 2:
            use = 'already eats our food so you can pay for Wi-Fi'
        elif self.internet > 2:
            use = 'goes work to pay your own Wi-Fi'
        return self.desc + ' ' + use

    @desc.setter
    def desc(self, value):
        self.desc = value
        
    def use_internet(noun):
        if noun in GameObject.objects:
            thing = GameObject.objects[noun]
            if type(thing) == Penny:
                thing.internet += 1
                if thing.internet >= 1:
                    msg = 'I got your Wi-Fi password'
                else:
                    msg = '{}, I am trying to discover your Wi-Fi passoword'.format(thing.class_name)
            else:
                msg = "There is no {} here".format(noun)
            return msg

        
penny = Penny("Penny Hofstadter")

verb_dict = {"say":say, "examine":examine, "internet":internet}

while True:
    get_input()
