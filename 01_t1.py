class FirstAuthors:
    def __init__(self, summaries):
        self.summaries = summaries
        self.authors_at_year = {}

    def _populate_authors(self):
        if not self.authors_at_year:
            for paper in self.summaries.values():
                if paper.authors:
                    first_author = paper.authors[0]
                    if paper.year not in self.authors_at_year:
                        self.authors_at_year[paper.year] = set()
                    self.authors_at_year[paper.year].add(first_author)

    def get_first_authors(self, year):
        self._populate_authors()
        return self.authors_at_year.get(year, set())
    
first_authors = FirstAuthors(Summaries)
first_authors_1965_method = first_authors.get_first_authors(1965)
print(f"First authors for the year 1965 (method): {first_authors_1965_method}")




from collections import defaultdict

first_authors_at_year = defaultdict(set)

for paper in Summaries.values():
    if paper.authors:
        first_author = paper.authors[0]
        first_authors_at_year[paper.year].add(first_author)

first_authors_1965 = first_authors_at_year[1965]
print(f"First authors for the year 1965: {first_authors_1965}")