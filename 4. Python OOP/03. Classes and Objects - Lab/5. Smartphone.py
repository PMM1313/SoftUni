class Smartphone:

    def __init__(self, memory):
        self.apps = []
        self.memory = memory
        self.is_on = False

    def power(self):
        self.is_on = not self.is_on

    def install(self, app, app_memory):
        if self.memory >= app_memory and self.is_on:
            self.apps.append(app)
            self.memory -= app_memory
            return f"Installing {app}"
        elif self.memory >= app_memory and not self.is_on:
            return f"Turn on your phone to install {app}"
        else:
            return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"