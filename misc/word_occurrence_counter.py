import cProfile


list_of_words = """
is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever
since the 1500s, when an unknown printer took a galley of type
and scrambled it to make a type specimen book. It has survived
not only five centuries, but also the leap into electronic
typesetting, remaining essentially unchanged. It was popularised
in the 1960s with the release of Letraset sheets containing Lorem
Ipsum passages, and more recently with desktop publishing software
like Aldus PageMaker including versions of Lorem Ipsum
is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever
since the 1500s, when an unknown printer took a galley of type
and scrambled it to make a type specimen book. It has survived
not only five centuries, but also the leap into electronic
typesetting, remaining essentially unchanged. It was popularised
in the 1960s with the release of Letraset sheets containing Lorem
Ipsum passages, and more recently with desktop publishing software
like Aldus PageMaker including versions of Lorem Ipsum
is simply dummy text of the printing and typesetting industry. si
evif ylno ni
"""


def word_counter(text):
    """
    Given a list of words as `text`, count the occurrence of each
    group of characters in any order that they might appear.
    Example: foo, ofo, oof are all counting towards foo = 3
    """
    counter = {}
    delimiters = ['.', ',', '\n']
    for d in delimiters:
        text = text.replace(d, ' ')

    for w in text.split(' '):
        word = w.strip()
        if len(word):
            key = ''.join(sorted(word)).lower()
            record = counter.get(key, None)
            if record is None:
                record = [1, word]
            else:
                record = [record[0]+1, word]
            counter[key] = record

    return counter


def run_test():
    """
    Test function.
    """
    counter = word_counter(list_of_words)
    for c in sorted(counter, key = lambda key: counter[key][0]):
        print counter[c]


if __name__ == "__main__":
    """
    Run the code and profile it.
    """
    cProfile.run('run_test()')

