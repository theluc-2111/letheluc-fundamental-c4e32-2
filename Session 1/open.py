# def craw(url='vne.com',limit=10):
#     print(url)
def craw(**kargs):
    print(kargs.get('data'))
craw(data={'k1':'v1'})