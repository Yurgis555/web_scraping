from subpr import by_min, by_max, graph, fibo, transf
from web_scraping import web_sc


web_sc()
cbx = transf(False)
graph(cbx)
# print(by_min(cbx))
min_qv = by_min(cbx)
print('Pagal mažiausiai iškrytusios',)
for i in min_qv:
    print('Kiekis : ', i[0], end=' ')
    print('skaičiai - ', i[1:])
print('_____________________________________________________________')
cbx = transf(False)
# print(by_max(cbx, 15))
max_qv = by_max(cbx, 15)
print('Pagal dažniausiai iškrytusios',)
for i in max_qv:
    print('Kiekis : ', i[0], end=' ')
    print('skaičiai - ', i[1:])

print('_____________________________________________________________')
ff = fibo()
for i in ff:
    print('Tikimibes laipsnis(FIBO) : ', i[0])
    print('skaičiai - ', i[1:])

# graph(bx)
