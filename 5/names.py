NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    clean_names = [name.title() for name in list(set(names))]
    return clean_names


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names = [s.split() for s in names]
    names.sort(key=lambda element: (element[1], element[0]), reverse=True)
    names = [' '.join(name) for name in names]
    return names


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    # ...
    names = [s.split() for s in names]
    names.sort(key=lambda element: (len(element[0])))
    return names[0][0]
