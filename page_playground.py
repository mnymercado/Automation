class Page:
    def __init__(self):
        self.url = 'www.amazon.com'

    def open_url(self):
        print('Opening url: ', self.url)

    def close(self):
        print('Closing url: ', self.url)


p = Page()
p.open_url()
p.close()

