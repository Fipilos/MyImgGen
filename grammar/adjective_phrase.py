class AdjectivePhrase(object):
    def __init__(self, token):
        self.root = token

    def __repr__(self):
        return self.root.text

    """
    todo expand
    """