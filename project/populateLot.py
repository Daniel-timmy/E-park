from models.parking_lot import Space, Lot
from storage.db import db

lt = ['EDU', 'FET', 'LSC', 'PHY', 'LAW',
      'MGT', 'SCS', 'CLS', 'CIS', 'AGR', 'MDS',
      'ENV', 'PHS', 'VET', 'ART']
sp = ['1', '2', '3', '4', '5', '6', '7', '8',
      '9', '10', '11', '12', '13', '14', '15', '16',
      '17', '18', '19', '20', '21', '22', '23', '24',
      '25', '26', '27', '28', '29', '30', '31', '32',
      '33', '34', '35', '36', '37', '38', '39', '40',
      '41', '42', '43', '44', '45', '46', '47', '48',
      '49', '50', '51', '52', '53', '54', '55', '56',
      '57', '58', '59', '60', '61', '62', '63', '64',
      '65', '66', '67', '68', '69', '70', '71', '72',
      '73', '74', '75', '76', '77', '78', '79', '80']
space_list = []

for rlot in lt:
    space_list = []
    for rSpace in sp:
        space = Space(space=rSpace, time_left=0, status='empty')
        space_list.append(space)
    lot = Lot(lot_name=rlot, space=space_list)
    db.insert(lot)

# obj = db.get_lot(id="98aaf16f-ff8b-436b-9345-eba5f3c14644")
# pp = []
# for sp in obj.space:
#     pp.append(sp.space)
# print(pp)

# ldict = {}
# lot = Lot.objects()
#
# separator = ', '
#
# for individual_lot in lot:
#     pSpace = []
#     for individual_space in individual_lot.space:
#         if individual_space.status == 'empty':
#             pSpace.append(individual_space.space)
#     ldict[individual_lot.lot_name] = separator.join(pSpace)
#
# for key, value in ldict.items():
#     print(f'Key: {key}, Value: {value}')

