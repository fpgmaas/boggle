class HasPrefix(object):
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value[0:len(other.value)] < other.value

class Prefix(object):
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value < other.value[0:len(self.value)]

class AdaptPrefix(object):
    def __init__(self, seq):
        self.seq = seq
    def __getitem__(self, key):
        return HasPrefix(self.seq[key])
    def __len__(self):
        return len(self.seq)