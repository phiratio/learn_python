class Silly:
    def __setattr__(self, attr, value):
        if attr == "silly" and value == 7:
            raise AttributeError("you shall not set 7 for silly")
        super().__setattr__(attr, value)

    def __getattribute__(self, attr):
        if attr == "silly":
            return "Just Try and Change Me!"
        return super().__getattribute__(attr)

    @property
    def silly(self):
        "This is a silly property"
        print("You are getting silly")
        return self._silly

    @silly.setter
    def silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value

    @silly.deleter
    def silly(self):
        print("Whoa, you killed silly!")
        del self._silly


s = Silly()
s.silly = 4  # setter
print(s.silly)  # getter
