
def m_to_mm():
    m = float(input("How many m?"))
    result = m * 1000
    sentence = '{} m is equal to {} mm.'.format(m, result)
    print(sentence)

def cm_to_m():
    cm = float(input("How many cm?"))
    result = cm / 100
    sentence = '{} cm is equal to {} m.'.format(cm, result)
    print(sentence)

m_to_mm()
cm_to_m()