def read_next(*collections):
    for collection in collections:
        yield from collection