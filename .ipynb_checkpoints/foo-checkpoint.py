def foo(object):
    count = 0
    for i in object:
        print(object[1])
        count += 1
    return 'Final count:', count