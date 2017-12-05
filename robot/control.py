class Toggle:
    def __init__(self, function):
        """Construct an instance of a Toggle object.

        :type  function: function
        :param function: The function to use as a toggle.
        """
        self.function = function
        self.prevOn = False
        self.prevOff = True

    def check(self):
        return self.function()

    @property
    def on(self):
        vfunc = self.function()
        if vfunc and not self.prevOn:
            self.prevOn = vfunc
            return True
        else:
            self.prevOn = vfunc
            return False

    @property
    def off(self):
        vfunc = self.function()
        if not vfunc and self.prevOff:
            self.prevOff = vfunc
            return True
        else:
            self.prevOff = vfunc
            return False

    __bool__ = check


