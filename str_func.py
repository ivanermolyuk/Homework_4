'''Пофиксили и улучшили'''
def to_uppercase(string):
    '''Вывод полученной строки в заглавных буквах'''
    return string.upper()

def capitalize_words(string):
    '''Возвращает полученную строку с заглавными первыми буквами'''
    return ' '.join(word.capitalize() for word in string.split())
