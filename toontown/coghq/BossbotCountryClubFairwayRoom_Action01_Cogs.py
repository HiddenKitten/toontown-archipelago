from .SpecImports import *
from toontown.toonbase import ToontownGlobals
CogParent = 110200
BattleCellId = 0
BattleCells = {BattleCellId: {'parentEntId': CogParent,
                'pos': Point3(0, 0, 0)}}
CogData = [{'parentEntId': CogParent,
  'boss': 0,
  'level': ToontownGlobals.BossbotCountryClubCogLevel - 2,
  'battleCell': BattleCellId,
  'pos': Point3(0, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': ToontownGlobals.BossbotCountryClubCogLevel - 2,
  'battleCell': BattleCellId,
  'pos': Point3(-4, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': ToontownGlobals.BossbotCountryClubCogLevel,
  'battleCell': BattleCellId,
  'pos': Point3(4, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0}]
ReserveCogData = []
