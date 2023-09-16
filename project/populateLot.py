from models.parking_lot import Space, Lot
from storage.db import db

#
# lt = ['EDU', 'FET', 'LSC', 'PHY', 'LAW', 'MGT', 'SCS', 'CLS', 'CIS', 'AGR', 'MDS']
# sp = ['01', '02', '03', '04', '05', '06', '07', '08',
#       '09', '10', '11', '12', '13', '15', '16', '17',
#       '18', '19', '20', '21', '22', '23', '24', '25']
# space_list = []
#
# for rlot in lt:
#     space_list = []
#     for rSpace in sp:
#         space = Space(space=rSpace, time_left=0, status='empty')
#         space_list.append(space)
#     lot = Lot(lot_name=rlot, space=space_list)
#     db.insert(lot)


obj = db.get_lot(id="98aaf16f-ff8b-436b-9345-eba5f3c14644")
pp = []
# for sp in obj.space:
#     pp.append(sp.space)
# print(pp)

ldict = {}
lot = Lot.objects()

separator = ', '

for individual_lot in lot:
    pSpace = []
    for individual_space in individual_lot.space:
        if individual_space.status == 'empty':
            pSpace.append(individual_space.space)
    ldict[individual_lot.lot_name] = separator.join(pSpace)

for key, value in ldict.items():
    print(f'Key: {key}, Value: {value}')
