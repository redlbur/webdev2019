def swap_case(s):
    return
print ''.join([i.lower() if i.isupper() else i.upper() for i in raw_input()])

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result