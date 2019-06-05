ds_ke = {'a':['b','c'],'b':['c','d','e'],'c':'d','d':'e'}
from_point = 'a'
end_point = 'e'
ds = []

# hàm liệt kê các đường nối 2 điểm:
def LIST(z):
    y = []
    for m in ds_ke:
        b = [z]
        if z in ds_ke[m]:
            b.insert(0,m)
            y.append(b)
    return y
# hàm kê đường đi
def way(x):
    for i in LIST(x):
        if i[0] != from_point:
            way(i[0])
        else:
            i.append(i[1])
            print(i)

# for i in LIST(end_point):
#     if i[0] != from_point:
#         for j in LIST(i[0]):
#             if j[0] != from_point:
#                 for k in LIST(j[0]):
#                     k.append(j[1])
#                     k.append(i[1])
#                     print(k)
#             else:
#                 j.append(i[1])
#                 print(j)
            
way(end_point)       

# for k in ds_ke:
#     a = list(duong_di)
#     if a[0] in ds_ke[k]:
#         a.insert(0,k)
#         ds.append(a)

# for k in ds:
#     for l in ds_ke:
#         a = list(k)
#         if a[0] in ds_ke[l]:
#             a.insert(0,l)
#             print(a)

