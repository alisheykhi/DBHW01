from flask_table import Table, Col

class ItemTable(Table):
    id = Col ('Student Number')
    name = Col('Name')
    family = Col ('Family')
    major = Col ('Major')


class Item(object):
    def __init__(self, id, name, family, major):
        self.id = id
        self.name = name
        self.family = family
        self.major = major