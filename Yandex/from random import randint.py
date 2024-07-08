from random import randint


class MarsURLEncoder:

    def __init__(self):
        self.dict = {}

    def random(self):
        return randint(1, 1)

    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        key = str(self.random())
        while key in self.dict:
            key = str(self.random())
        self.dict[key] = str(long_url)
        short_url = 'https://ma.rs/' + key
        return short_url

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        for key, value in self.dict.items():
            if key in short_url:
                return self.dict[key]


url = MarsURLEncoder()
print(url.encode('https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html'))
print(url.dict)
print(url.decode('https://ma.rs/1'))
