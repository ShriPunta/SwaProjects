class EachCeleb:
    name = 'PomPom'
    gender = 'u'
    def __init__(self,subLink):
        clean1 = subLink[6:].replace('_',' ').strip()
        self.name = clean1



