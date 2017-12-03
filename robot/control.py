class Toggle:
    def _init_(self, function):
        """Construct an instance of a Toggle object.

        :type  function: function
        :param function: The function to use as a toggle.
        """
        self.function = function
        self.prevOn = False
        self.prevOff = True

    @property
    def on(self):
        vfunc = self.function()
        if vfunc and !self.prevOn:
            return True
        else:
            return False
        self.prevOn = vfunc

    @property
    def off(self):
        vfunc = self.function()
        if !vfunc and self.prevOff:
            return True
        else:
            return False
        self.prevOff = vfunc


