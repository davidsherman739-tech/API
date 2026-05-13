class Task:

    def _init_(self, title, done=False):
        self.title = title
        self.done = done

    def complete(self):
        self.done = True

    def show(self):
        print(f"Úkol: {self.title}, hotovo: {self.done}")


ukol1 = Task("Napsat domácí úkol")

ukol1.show()

ukol1.complete()

ukol1.show()
