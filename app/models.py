class Sources:
    '''
    a class to define the objects instances
    '''

    def __init__(self, id, name, description, url, category, country):
        self.id = id
        self.name = name
        self, description = description
        self.url = url
        self.category = category
        self.country = country


class Articles:
    '''
    class to define new instances of articles
    '''

    def __init__(self, id, author, title, description, url, image, date):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.date = date
