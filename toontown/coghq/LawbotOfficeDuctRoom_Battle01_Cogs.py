from .SpecImports import *
from toontown.toonbase import ToontownGlobals
import random
CogParent = 10000
CogParent2 = 11000
BattleCellId = 0
BattleCell2Id = 1
BattleCells = {BattleCellId: {'parentEntId': CogParent,
                'pos': Point3(0, 0, 0)},
                BattleCell2Id: {'parentEntId': CogParent2,
                                'pos': Point3(0, 0, 0)}}
CogData = [{'parentEntId': CogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel+1,
  'battleCell': BattleCellId,
  'pos': Point3(-4, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintSkelecogLevel+1,
  'battleCell': BattleCellId,
  'pos': Point3(0, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': random.choice([0, 0, 1])},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintSkelecogLevel-2,
  'battleCell': BattleCellId,
  'pos': Point3(4, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': random.choice([0, 0, 1])},
  {'parentEntId': CogParent2,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel+2,
  'battleCell': BattleCell2Id,
  'pos': Point3(-6, 0, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent2,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintSkelecogLevel+1,
  'battleCell': BattleCell2Id,
  'pos': Point3(2, 0, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': random.choice([0, 0, 1])},
 {'parentEntId': CogParent2,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintSkelecogLevel+1,
  'battleCell': BattleCell2Id,
  'pos': Point3(-2, 0, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': random.choice([0, 0, 1])},
 {'parentEntId': CogParent2,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintSkelecogLevel-2,
  'battleCell': BattleCell2Id,
  'pos': Point3(6, 0, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': random.choice([0, 0, 1])}]
ReserveCogData = []
