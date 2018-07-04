class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """

    def __init__(self, center_loc, tent_loc=Location(0, 0)):
        """ Assumes center_loc and tent_loc are Location objects
        Initializes a new Campus centered at location center_loc
        with a tent at location tent_loc """
        self.center_loc = center_loc
        self.tent_loc = tent_loc
        self.all_locals = [tent_loc]

    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        if new_tent_loc in self.all_locals:
            return False
        if new_tent_loc not in self.all_locals:
            self.all_locals.append(new_tent_loc)
        for i in self.all_locals:
            for x in self.all_locals:
                if i is x:
                    continue
                if Location.dist_from(i, x) >= 0.5:
                    continue
                else:
                    return False
        return True

    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus.
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        self.all_locals.remove(tent_loc)

    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain
        the string representation of the Location of a tent. The list should
        be sorted by the x coordinate of the location. """
        all_tents = []
        for x in self.all_locals:
            all_tents.append(str(x))
        return sorted(all_tents)