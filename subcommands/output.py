import sys


w = sys.stdout.write


def _rowsep(angles, sep, cols):
    w(angles[0] + (sep * (2 + cols[0])))
    for c in cols[1:]:
        w(angles[1] + (sep * (2 + c)))
    w(angles[2])
    w(u'\n')

def _row(colsep, row, cols):
    for i, c in enumerate(cols):
        w(u'{} {:{}s} '.format(colsep, row[i], c))
    w(colsep)
    w(u'\n')


def printtable(rawdata, headerrows=0):
    data = []
    columns = []
    colsep = u' '
    angles = (
        (u'\u250c', u'\u252c', u'\u2510'),
        (u'\u251c', u'\u253c', u'\u2524'),
        (u'\u2514', u'\u2534', u'\u2518'),
    )
    rowsep = u'\u2500'

    for rrow in rawdata:
        row = []
        for i, rcell in enumerate(rrow):
            cell = unicode(rcell)
            try:
                columns[i] = max(len(cell), columns[i])
            except:
                columns.append(len(cell))
            row.append(cell)
        data.append(row)

    _rowsep(angles[0], rowsep, columns)
    for row in data[:headerrows]:
        _row(colsep, row, columns)
    _rowsep(angles[1], rowsep, columns)
    for row in data[headerrows:]:
        _row(colsep, row, columns)
    _rowsep(angles[2], rowsep, columns)


def printtree(data, indent=0):
    for k in data:
        v = data[k]
        w(' ' * indent + '- ' + k + ':')
        if isinstance(v, basestring):
            w(' ' + v + '\n')
        else:
            w('\n')
            printtree(data[k], indent + 2)
