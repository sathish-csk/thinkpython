if __name__ == '__main__':
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'

    for letter in prefixes:
        if (letter in 'O') or (letter in 'Q'):
            letter = letter + 'u'
        print letter + suffix
    