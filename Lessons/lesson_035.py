def mystery(ls1, ls2):
    output = []
    for k,v in zip(ls1, ls2):
        if k == v:
            output.append(k)
    return output