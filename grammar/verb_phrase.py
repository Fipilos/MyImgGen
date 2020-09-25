class VerbPhrase(object):
    def __init__(self, verb, objects, adv_modifiers, particles, adj_complements, attributes):
        self.verb = verb
        self.objects = objects
        self.adv_modifiers = adv_modifiers
        self.particles = particles
        self.adj_complements = adj_complements
        self.attributes = attributes

    def __repr__(self):
        return str(self.__dict__)