def difference(*args):
    return 0 if len(args) == 0 else max(args) - min(args)