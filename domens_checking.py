import socket
import string


class DomenSearch:

    def __init__(self, key_word):
        self.list_of_domens = ['com', 'ru', 'net', 'org', 'info', 'cn', 'es', 'top', 'au', 'pl', 'it', 'uk', 'tk', 'ml',
                               'ga', 'cf', 'us', 'xyz', 'top', 'site', 'win', 'bid']
        self.all_variations = []
        self.key_word = key_word

    def create_variations(self):
        for char in string.ascii_lowercase:
            website = self.key_word + char
            self.all_variations.append(website)

        _string = list(self.key_word)
        for chars in _string:
            new_k = self.key_word.replace(chars, "")
            self.all_variations.append(new_k)

        for index in range(len(_string) + 1):
            new_dom = self.key_word[:index] + '.' + self.key_word[index:]
            self.all_variations.append(new_dom)

        return self.all_variations

    def check_domens(self, host):
        for dom in self.list_of_domens:
            web = host + '.' + dom
            try:
                res = socket.gethostbyname(web)
                print(web, res)
            except:
                pass


if __name__ == '__main__':
    key_word = input(str('Введите интересующее вас слово: '))
    fishing_checking = DomenSearch(key_word=key_word)
    list_of_hosts = fishing_checking.create_variations()
    for host in list_of_hosts:
        fishing_checking.check_domens(host=host)
