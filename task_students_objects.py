class Students():

    def __init__(self, a_name, a_subject):
        self.name = a_name
        self.subject = a_subject


    def greet(self):
        print(f"Hello, I'm  {self.name}. My favourite subjects are: " f'\n\t{self.subject[0]}\n\t{self.subject[1]}') 


# objects creation
ivan = Students("Ivan Ivanov", ["maths", "phisics"])
alex = Students("Alex Petrov", ["arts", "music"])        
maria = Students('Maria Popova', ['chemistry','biology'])


ivan.greet()
alex.greet()
maria.greet()