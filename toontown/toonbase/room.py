from panda3d.core import *
from . import TTLocalizer
import random
GlobalEntities = {1000: {'type': 'levelMgr', 'name': 'UberZone', 'comment': '', 'parentEntId': 0, 'cogLevel': 0, 'farPlaneDistance': 1500, 'modelFilename': 'phase_11/models/lawbotHQ/LB_Zone04a', 'wantDoors': 1}, 1001: {'type': 'editMgr', 'name': 'EditMgr', 'parentEntId': 0, 'insertEntity': None, 'removeEntity': None, 'requestNewEntity': None, 'requestSave': None}, 0: {'type': 'zone', 'name': 'UberZone', 'comment': '', 'parentEntId': 0, 'scale': LVecBase3f(1, 1, 1), 'description': '', 'visibility': []}, 10001: {'type': 'battleBlocker', 'name': 'exitBlocker', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(0, 76.2264, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'cellId': 0, 'radius': 10.0}, 10021: {'type': 'battleBlocker', 'name': 'middleBlocker', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(9.79564, 7.17855, 0), 'hpr': LVecBase3f(90, 0, 0), 'scale': LVecBase3f(1.61347, 0.225867, 1.99823), 'cellId': 1, 'radius': 10.0}, 10061: {'type': 'battleBlocker', 'name': 'frontBlocker', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(-45.6075, -22.7538, 0), 'hpr': LVecBase3f(45, 0, 0), 'scale': LVecBase3f(1.61347, 0.225867, 1.99823), 'cellId': 2, 'radius': 10.0}, 10025: {'type': 'mintProductPallet', 'name': '<unnamed>', 'comment': '', 'parentEntId': 10024, 'pos': LPoint3f(0, 7.96, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'mintId': 12500}, 10031: {'type': 'mintProductPallet', 'name': '<unnamed>', 'comment': '', 'parentEntId': 10024, 'pos': LPoint3f(-36.1348, -12.7274, 0), 'hpr': LVecBase3f(45, 0, 0), 'scale': LVecBase3f(0.7, 0.7, 0.7), 'mintId': 12500}, 10032: {'type': 'mintProductPallet', 'name': '<unnamed>', 'comment': '', 'parentEntId': 10028, 'pos': LPoint3f(-25, 9.05, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'mintId': 12500}, 10033: {'type': 'mintProductPallet', 'name': '<unnamed>', 'comment': '', 'parentEntId': 10028, 'pos': LPoint3f(26.84, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'mintId': 12500}, 10003: {'type': 'mintShelf', 'name': 'bookshelf', 'comment': '', 'parentEntId': 10002, 'pos': LPoint3f(-60.84, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1.5, 1.15, 1.5), 'mintId': 12500}, 10004: {'type': 'mintShelf', 'name': 'copy of bookshelf', 'comment': '', 'parentEntId': 10003, 'pos': LPoint3f(0.18, 6.85808, 0), 'hpr': LVecBase3f(180, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'mintId': 12500}, 10005: {'type': 'mintShelf', 'name': 'bookshelf', 'comment': '', 'parentEntId': 10002, 'pos': LPoint3f(-47.4124, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1.5, 1.15, 1.5), 'mintId': 12500}, 10006: {'type': 'mintShelf', 'name': 'copy of bookshelf', 'comment': '', 'parentEntId': 10005, 'pos': LPoint3f(0.18, 6.85808, 0), 'hpr': LVecBase3f(180, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'mintId': 12500}, 10007: {'type': 'mintShelf', 'name': 'bookshelf', 'comment': '', 'parentEntId': 10002, 'pos': LPoint3f(-33.9436, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1.5, 1.15, 1.5), 'mintId': 12500}, 10008: {'type': 'mintShelf', 'name': 'copy of bookshelf', 'comment': '', 'parentEntId': 10007, 'pos': LPoint3f(0.18, 6.85808, 0), 'hpr': LVecBase3f(180, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'mintId': 12500}, 10009: {'type': 'mintShelf', 'name': 'bookshelf', 'comment': '', 'parentEntId': 10002, 'pos': LPoint3f(-20.4899, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1.5, 1.15, 1.5), 'mintId': 12500}, 10010: {'type': 'mintShelf', 'name': 'copy of bookshelf', 'comment': '', 'parentEntId': 10009, 'pos': LPoint3f(0.18, 6.85808, 0), 'hpr': LVecBase3f(180, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'mintId': 12500}, 10011: {'type': 'mintShelf', 'name': 'bookshelf', 'comment': '', 'parentEntId': 10002, 'pos': LPoint3f(60.7196, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1.5, 1.15, 1.5), 'mintId': 12500}, 10012: {'type': 'mintShelf', 'name': 'copy of bookshelf', 'comment': '', 'parentEntId': 10011, 'pos': LPoint3f(0.18, 6.85808, 0), 'hpr': LVecBase3f(180, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'mintId': 12500}, 10013: {'type': 'mintShelf', 'name': 'bookshelf', 'comment': '', 'parentEntId': 10002, 'pos': LPoint3f(33.2061, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1.5, 1.15, 1.5), 'mintId': 12500}, 10014: {'type': 'mintShelf', 'name': 'copy of bookshelf', 'comment': '', 'parentEntId': 10013, 'pos': LPoint3f(0.18, 6.85808, 0), 'hpr': LVecBase3f(180, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'mintId': 12500}, 10015: {'type': 'mintShelf', 'name': 'bookshelf', 'comment': '', 'parentEntId': 10002, 'pos': LPoint3f(19.7814, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1.5, 1.15, 1.5), 'mintId': 12500}, 10016: {'type': 'mintShelf', 'name': 'copy of bookshelf', 'comment': '', 'parentEntId': 10015, 'pos': LPoint3f(0.18, 6.85808, 0), 'hpr': LVecBase3f(180, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'mintId': 12500}, 10017: {'type': 'mintShelf', 'name': 'bookshelf', 'comment': '', 'parentEntId': 10002, 'pos': LPoint3f(-7.05516, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1.5, 1.15, 1.5), 'mintId': 12500}, 10018: {'type': 'mintShelf', 'name': 'copy of bookshelf', 'comment': '', 'parentEntId': 10017, 'pos': LPoint3f(0.18, 6.85808, 0), 'hpr': LVecBase3f(180, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'mintId': 12500}, 10019: {'type': 'mintShelf', 'name': 'bookshelf', 'comment': '', 'parentEntId': 10002, 'pos': LPoint3f(6.35371, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1.5, 1.15, 1.5), 'mintId': 12500}, 10020: {'type': 'mintShelf', 'name': 'copy of bookshelf', 'comment': '', 'parentEntId': 10019, 'pos': LPoint3f(0.18, 6.85808, 0), 'hpr': LVecBase3f(180, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'mintId': 12500}, 10042: {'type': 'mintShelf', 'name': 'bookshelf', 'comment': '', 'parentEntId': 10041, 'pos': LPoint3f(-7.05516, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1.4, 1.4, 1.4), 'mintId': 12500}, 10043: {'type': 'mintShelf', 'name': 'bookshelf', 'comment': '', 'parentEntId': 10041, 'pos': LPoint3f(-60.84, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1.5, 1.15, 1.5), 'mintId': 12500}, 10044: {'type': 'mintShelf', 'name': 'bookshelf', 'comment': '', 'parentEntId': 10041, 'pos': LPoint3f(6.35371, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1.5, 1.15, 1.5), 'mintId': 12500}, 10045: {'type': 'mintShelf', 'name': 'bookshelf', 'comment': '', 'parentEntId': 10041, 'pos': LPoint3f(-47.4124, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1.5, 1.15, 1.5), 'mintId': 12500}, 10046: {'type': 'mintShelf', 'name': 'bookshelf', 'comment': '', 'parentEntId': 10041, 'pos': LPoint3f(-33.9436, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1.5, 1.15, 1.5), 'mintId': 12500}, 10047: {'type': 'mintShelf', 'name': 'bookshelf', 'comment': '', 'parentEntId': 10041, 'pos': LPoint3f(-20.4899, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1.5, 1.15, 1.5), 'mintId': 12500}, 10048: {'type': 'mintShelf', 'name': 'bookshelf', 'comment': '', 'parentEntId': 10041, 'pos': LPoint3f(60.7196, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1.5, 1.15, 1.5), 'mintId': 12500}, 10049: {'type': 'mintShelf', 'name': 'bookshelf', 'comment': '', 'parentEntId': 10041, 'pos': LPoint3f(33.2061, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1.5, 1.15, 1.5), 'mintId': 12500}, 10050: {'type': 'mintShelf', 'name': 'bookshelf', 'comment': '', 'parentEntId': 10041, 'pos': LPoint3f(19.7814, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1.5, 1.15, 1.5), 'mintId': 12500}, 10051: {'type': 'mintShelf', 'name': 'copy of bookshelf', 'comment': '', 'parentEntId': 10042, 'pos': LPoint3f(0.18, 6.85808, 0), 'hpr': LVecBase3f(180, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'mintId': 12500}, 10052: {'type': 'mintShelf', 'name': 'copy of bookshelf', 'comment': '', 'parentEntId': 10043, 'pos': LPoint3f(0.18, 6.85808, 0), 'hpr': LVecBase3f(180, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'mintId': 12500}, 10053: {'type': 'mintShelf', 'name': 'copy of bookshelf', 'comment': '', 'parentEntId': 10044, 'pos': LPoint3f(0.18, 6.85808, 0), 'hpr': LVecBase3f(180, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'mintId': 12500}, 10054: {'type': 'mintShelf', 'name': 'copy of bookshelf', 'comment': '', 'parentEntId': 10045, 'pos': LPoint3f(0.18, 6.85808, 0), 'hpr': LVecBase3f(180, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'mintId': 12500}, 10055: {'type': 'mintShelf', 'name': 'copy of bookshelf', 'comment': '', 'parentEntId': 10046, 'pos': LPoint3f(0.18, 6.85808, 0), 'hpr': LVecBase3f(180, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'mintId': 12500}, 10056: {'type': 'mintShelf', 'name': 'copy of bookshelf', 'comment': '', 'parentEntId': 10047, 'pos': LPoint3f(0.18, 6.85808, 0), 'hpr': LVecBase3f(180, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'mintId': 12500}, 10057: {'type': 'mintShelf', 'name': 'copy of bookshelf', 'comment': '', 'parentEntId': 10048, 'pos': LPoint3f(0.18, 6.85808, 0), 'hpr': LVecBase3f(180, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'mintId': 12500}, 10058: {'type': 'mintShelf', 'name': 'copy of bookshelf', 'comment': '', 'parentEntId': 10049, 'pos': LPoint3f(0.18, 6.85808, 0), 'hpr': LVecBase3f(180, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'mintId': 12500}, 10059: {'type': 'mintShelf', 'name': 'copy of bookshelf', 'comment': '', 'parentEntId': 10050, 'pos': LPoint3f(0.18, 6.85808, 0), 'hpr': LVecBase3f(180, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'mintId': 12500}, 10000: {'type': 'nodepath', 'name': 'cogs', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(0, 58.7971, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1, 1, 1)}, 10002: {'type': 'nodepath', 'name': 'backWall', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(0, 22.0885, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1, 1, 1)}, 10022: {'type': 'nodepath', 'name': 'middleCogs', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(0, 7.57602, 0), 'hpr': LVecBase3f(270, 0, 0), 'scale': LVecBase3f(1, 1, 1)}, 10023: {'type': 'nodepath', 'name': 'props', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(0, 0, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1, 1, 1)}, 10024: {'type': 'nodepath', 'name': 'frontMoney', 'comment': '', 'parentEntId': 10023, 'pos': LPoint3f(22.4126, -39.3388, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1, 1, 1)}, 10028: {'type': 'nodepath', 'name': 'backMoney', 'comment': '', 'parentEntId': 10023, 'pos': LPoint3f(0, 48.4982, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1, 1, 1)}, 10041: {'type': 'nodepath', 'name': 'backWall', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(0, -6.69598, 0), 'hpr': LVecBase3f(180, 0, 0), 'scale': LVecBase3f(1, 1, 1)}, 10060: {'type': 'nodepath', 'name': 'frontCogs', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(-28.8659, -31.1732, 0), 'hpr': LVecBase3f(51.3402, 0, 0), 'scale': LVecBase3f(1, 1, 1)}, 16000: {'type': 'model', 'name': 'middle', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(-37.5243, -38.3105, 0), 'hpr': LVecBase3f(140, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_11/models/lawbotHQ/LB_couchA.bam'}, 16001: {'type': 'model', 'name': 'middle', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(0, 18.9066, 0.0241111), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1.00897, 1.00897, 1.00897), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_11/models/lawbotHQ/LB_couchA.bam'}, 16002: {'type': 'model', 'name': 'middle', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(-46.8285, -31.8275, 0), 'hpr': LVecBase3f(128.674, 0, 0), 'scale': LVecBase3f(30, 30, 30), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cab.bam'}, 16003: {'type': 'model', 'name': 'middle', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(-49.9481, -28.1406, 0), 'hpr': LVecBase3f(128.67, 0, 0), 'scale': LVecBase3f(30, 30, 30), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cab.bam'}, 16004: {'type': 'model', 'name': 'middle', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(-8.5618, 18.462, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_11/models/lawbotHQ/LB_torch_lampB.bam'}, 16005: {'type': 'model', 'name': 'middle', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(-31.262, -44.071, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_11/models/lawbotHQ/LB_torch_lampB.bam'}, 16006: {'type': 'model', 'name': 'middle', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(-14.324, 36.5287, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_11/models/lawbotHQ/LB_torch_lampB.bam'}, 16007: {'type': 'model', 'name': 'middle', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(8.33687, 19.0271, 0), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(8, 8, 8), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_11/models/lawbotHQ/LB_pottedplantA.bam'}, 16008: {'type': 'model', 'name': 'middle', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(-22.9487, 36.6941, 0.0959283), 'hpr': LVecBase3f(0, 0, 0), 'scale': LVecBase3f(1, 1, 1), 'collisionsOnly': 0, 'flattenType': 'light', 'loadType': 'loadModelCopy', 'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox.bam'}, 180000: {'type': 'healBarrel', 'name': 'healBuddy', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(63.0589, -11.7714, 0), 'hpr': LVecBase3f(277.896, 0, 0), 'scale': 1, 'rewardPerGrab': 16, 'rewardPerGrabMax': 16}, 180001: {'type': 'healBarrel', 'name': 'healBuddy', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(-28.038, 35.557, 0), 'hpr': LVecBase3f(211.908, 0, 0), 'scale': 1, 'rewardPerGrab': 16, 'rewardPerGrabMax': 16}, 180002: {'type': 'healBarrel', 'name': 'healBuddy', 'comment': '', 'parentEntId': 0, 'pos': LPoint3f(-59.7889, 26.9639, 0), 'hpr': LVecBase3f(92.533, 0, 0), 'scale': 1, 'rewardPerGrab': 16, 'rewardPerGrabMax': 16}}

"""
GlobalEntities[180000] = {'type': 'healBarrel',
          'name': 'healBuddy',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(0, 0, 0.0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'rewardPerGrab': 16,
          'rewardPerGrabMax': 16}

GlobalEntities[180001] = {'type': 'healBarrel',
          'name': 'healBuddy',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(0, 0, 0.0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'rewardPerGrab': 16,
          'rewardPerGrabMax': 16}

GlobalEntities[180002] = {'type': 'healBarrel',
          'name': 'healBuddy',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(0, 0, 0.0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'rewardPerGrab': 16,
          'rewardPerGrabMax': 16}


GlobalEntities[16000] = {'type': 'model',
         'name': 'middle',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1,
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_11/models/lawbotHQ/LB_couchA.bam'}

GlobalEntities[16001] = {'type': 'model',
         'name': 'middle',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1,
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_11/models/lawbotHQ/LB_couchA.bam'}

GlobalEntities[16002] = {'type': 'model',
         'name': 'middle',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1,
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cab.bam'}

GlobalEntities[16003] = {'type': 'model',
         'name': 'middle',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1,
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cab.bam'}

GlobalEntities[16004] = {'type': 'model',
         'name': 'middle',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1,
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_11/models/lawbotHQ/LB_endtableA.bam'}

GlobalEntities[16005] = {'type': 'model',
         'name': 'middle',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1,
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_11/models/lawbotHQ/LB_torch_lampA.bam'}

GlobalEntities[16006] = {'type': 'model',
         'name': 'middle',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1,
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_11/models/lawbotHQ/LB_torch_lampA.bam'}

GlobalEntities[16007] = {'type': 'model',
         'name': 'middle',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1,
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_11/models/lawbotHQ/LB_pottedplantA.bam'}

GlobalEntities[16008] = {'type': 'model',
         'name': 'middle',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1,
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox.bam'}




GlobalEntities[180010] = {'type': 'healBarrel',
          'name': 'archi',
          'comment': '',
          'parentEntId': 1000,
          'pos': Point3(0, 0, 0.0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'rewardPerGrab': 10,
          'rewardPerGrabMax': 10}

"""