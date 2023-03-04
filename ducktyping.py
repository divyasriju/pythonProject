class duck:
    def walk(self):
        print("this duck is walking")

    def talk(self):
        print("this duck is talking")
class chicken:
    def walk(self):
        print("this chicken is walking")

    def talk(self):
        print("this chicken  talking")


class person:
    def catch(self,chicken):

        print("you caught the critter")

duck=duck()
chicken=chicken()
person=person()
person.catch(duck)
person.catch(chicken)
