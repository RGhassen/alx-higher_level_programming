def magic_string():
    setattr(magic_string, 'count', getattr(magic_string, 'count', -1) + 1)
    return "BestSchool" + ", BestSchool" * magic_string.count
