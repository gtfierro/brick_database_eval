def hodify(qstr):
    """
    Strip PREFIX, add ';'
    """
    qstr = qstr.replace('DISTINCT','')
    return qstr+';'
