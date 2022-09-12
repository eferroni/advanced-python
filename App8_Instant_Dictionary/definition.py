import pandas


class Definition:

    def __init__(self, term: str) -> None:
        self.term = term.lower()

    def get(self):
        df = pandas.read_csv('data.csv')
        return tuple(df.loc[df['word'] == self.term]['definition'])


if __name__ == '__main__':
    d = Definition(term='sun')
    print(d.get())
