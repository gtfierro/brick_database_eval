def hodify(qstr):
    """
    Strip PREFIX, add ';'
    """
    qstr = qstr.replace('DISTINCT','')
    lines = qstr.split('\n')
    res = []
    for l in lines:
        if l.strip().startswith('PREFIX'): continue
        res.append(l)
    return '\n'.join(res)+';'
