from toontown.coghq.SpecImports import *
GlobalEntities = {1000: {'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_10/models/cashbotHQ/ZONE08a',
        'wantDoors': 1},
 1001: {'type': 'editMgr',
        'name': 'EditMgr',
        'parentEntId': 0,
        'insertEntity': None,
        'removeEntity': None,
        'requestNewEntity': None,
        'requestSave': None},
 0: {'type': 'zone',
     'name': 'UberZone',
     'comment': '',
     'parentEntId': 0,
     'scale': 1,
     'description': '',
     'visibility': []},
 140050051: {'type': 'button',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(6.53053, -39.3021, 11.0133),
         'hpr': Vec3(0, 0, 0),
         'scale': Point3(4, 4, 4),
         'color': Vec4(1, 0, 0, 1),
         'isOn': 0,
         'isOnEvent': 0,
         'secondsOn': -1.0},
 140000051: {'type': 'door',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-1.05295, 49.1, 5.6),
          'hpr': Vec3(0, 0, 0),
          'scale': 0.80,
          'color': Vec4(1, 1, 1, 1),
          'isLock0Unlocked': 1,
          'isLock1Unlocked': 0,
          'isLock2Unlocked': 1,
          'isLock3Unlocked': 1,
          'isOpen': 0,
          'isOpenEvent': 0,
          'isVisBlocker': 0,
          'secondsOpen': 1,
          'unlock0Event': 0,
          'unlock1Event': 140050051,
          'unlock2Event': 0,
          'unlock3Event': 0},
 700556000: {'type': 'goon',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 7005596000,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1.2,
         'attackRadius': 12,
         'crushCellId': None,
         'goonType': 'pg',
         'gridId': None,
         'hFov': 70,
         'strength': 12,
         'velocity': 3.2},
 7005596000: {'type': 'path',
         'name': 'nearPace',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0, 0.0, 0.0),
         'hpr': Point3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'pathIndex': 110,
         'pathScale': 1.0},
 700656000: {'type': 'goon',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 7006596000,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1.8,
         'attackRadius': 10,
         'crushCellId': None,
         'goonType': 'pg',
         'gridId': None,
         'hFov': 90,
         'strength': 20,
         'velocity': 3.2},
 7006596000: {'type': 'path',
         'name': 'nearPace',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0, 0.0, 0.0),
         'hpr': Point3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'pathIndex': 111,
         'pathScale': 1.0},
 70010049: {'type': 'stomper',
         'name': 'first',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(58.7457, -0.804199, 0.0247555),
         'hpr': Point3(0.0, 0.0, 0.0),
         'scale': Vec3(1.1, 1.1, 1.0),
         'animateShadow': 1,
         'crushCellId': None,
         'damage': 10,
         'headScale': Point3(5, 6, 6.25),
         'modelPath': 0,
         'motion': 3,
         'period': 2.5,
         'phaseShift': 0.34,
         'range': 7.0,
         'removeCamBarrierCollisions': 0,
         'removeHeadFloor': 1,
         'shaftScale': Point3(1, 10, 1),
         'soundLen': 0,
         'soundOn': 1,
         'soundPath': 1,
         'style': 'vertical',
         'switchId': 0,
         'wantShadow': 1,
         'wantSmoke': 1,
         'zOffset': 0},
 70020049: {'type': 'stomper',
         'name': 'second',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(25.2436, -22.8007, 0.0247555),
         'hpr': Point3(0.0, 0.0, 0.0),
         'scale': Vec3(1.3, 1.3, 1.0),
         'animateShadow': 1,
         'crushCellId': None,
         'damage': 10,
         'headScale': Point3(5, 6, 6.25),
         'modelPath': 0,
         'motion': 3,
         'period': 2.0,
         'phaseShift': 0.34,
         'range': 7.0,
         'removeCamBarrierCollisions': 0,
         'removeHeadFloor': 1,
         'shaftScale': Point3(1, 10, 1),
         'soundLen': 0,
         'soundOn': 1,
         'soundPath': 1,
         'style': 'vertical',
         'switchId': 0,
         'wantShadow': 1,
         'wantSmoke': 1,
         'zOffset': 0},
 70030049: {'type': 'stomper',
         'name': 'third',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(-14.2493, -34.7397, 0.0247555),
         'hpr': Point3(0.0, 0.0, 0.0),
         'scale': Vec3(1.3, 1.3, 1.0),
         'animateShadow': 1,
         'crushCellId': None,
         'damage': 10,
         'headScale': Point3(5, 6, 6.25),
         'modelPath': 0,
         'motion': 3,
         'period': 1.0,
         'phaseShift': 0.34,
         'range': 7.0,
         'removeCamBarrierCollisions': 0,
         'removeHeadFloor': 1,
         'shaftScale': Point3(1, 10, 1),
         'soundLen': 0,
         'soundOn': 1,
         'soundPath': 1,
         'style': 'vertical',
         'switchId': 0,
         'wantShadow': 1,
         'wantSmoke': 1,
         'zOffset': 0},
 70040049: {'type': 'stomper',
         'name': 'fourth',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(-61.652, -15.3327, 0.0247555),
         'hpr': Point3(0.0, 0.0, 0.0),
         'scale': Vec3(1.3, 1.3, 1.0),
         'animateShadow': 1,
         'crushCellId': None,
         'damage': 10,
         'headScale': Point3(5, 6, 6.25),
         'modelPath': 0,
         'motion': 3,
         'period': 1.3,
         'phaseShift': 0.34,
         'range': 7.0,
         'removeCamBarrierCollisions': 0,
         'removeHeadFloor': 1,
         'shaftScale': Point3(1, 10, 1),
         'soundLen': 0,
         'soundOn': 1,
         'soundPath': 1,
         'style': 'vertical',
         'switchId': 0,
         'wantShadow': 1,
         'wantSmoke': 1,
         'zOffset': 0},
 70050049: {'type': 'stomper',
         'name': 'fifth',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(-23.6454, 30.3258, 0.0249996),
         'hpr': Point3(0.0, 0.0, 0.0),
         'scale': Vec3(1.3, 1.3, 1.0),
         'animateShadow': 1,
         'crushCellId': None,
         'damage': 10,
         'headScale': Point3(5, 6, 6.25),
         'modelPath': 0,
         'motion': 3,
         'period': 1.06,
         'phaseShift': 0.34,
         'range': 7.0,
         'removeCamBarrierCollisions': 0,
         'removeHeadFloor': 1,
         'shaftScale': Point3(1, 10, 1),
         'soundLen': 0,
         'soundOn': 1,
         'soundPath': 1,
         'style': 'vertical',
         'switchId': 0,
         'wantShadow': 1,
         'wantSmoke': 1,
         'zOffset': 0},
 10041: {'type': 'apBarrel',
         'name': 'archi',
         'comment': '',
         'parentEntId': 10033,
         'pos': Point3(5.40611028671, 0.0, 0.0),
         'hpr': Vec3(199.440032959, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'apRewardIndex': 0,
         'rewardPerGrab': 6,
         'rewardPerGrabMax': 8},
 10034: {'type': 'healBarrel',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10033,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(163.300750732, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'rewardPerGrab': 20,
         'rewardPerGrabMax': 20},
 10015: {'type': 'mintProductPallet',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10014,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1,
         'mintId': 12500},
 10016: {'type': 'mintProductPallet',
         'name': 'copy of <unnamed>',
         'comment': '',
         'parentEntId': 10014,
         'pos': Point3(0.0, 13.6865262985, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'mintId': 12700},
 10017: {'type': 'mintProductPallet',
         'name': 'copy of <unnamed> (2)',
         'comment': '',
         'parentEntId': 10014,
         'pos': Point3(0.0, 27.3799991608, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'mintId': 12600},
 10018: {'type': 'mintProductPallet',
         'name': 'copy of <unnamed> (3)',
         'comment': '',
         'parentEntId': 10014,
         'pos': Point3(0.0, 41.0699996948, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'mintId': 12700},
 10019: {'type': 'mintProductPallet',
         'name': 'copy of <unnamed> (4)',
         'comment': '',
         'parentEntId': 10014,
         'pos': Point3(0.0, 54.7599983215, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'mintId': 12700},
 10020: {'type': 'mintProductPallet',
         'name': 'copy of <unnamed> (5)',
         'comment': '',
         'parentEntId': 10014,
         'pos': Point3(0.0, 68.4499969482, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'mintId': 12500},
 10022: {'type': 'mintProductPallet',
         'name': 'copy of <unnamed>',
         'comment': '',
         'parentEntId': 10021,
         'pos': Point3(0.0, 11.766998291, 0.0),
         'hpr': Point3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'mintId': 12700},
 10025: {'type': 'mintProductPallet',
         'name': 'copy of <unnamed> (4)',
         'comment': '',
         'parentEntId': 10045,
         'pos': Point3(0.0, 54.7599983215, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'mintId': 12700},
 10026: {'type': 'mintProductPallet',
         'name': 'copy of <unnamed> (5)',
         'comment': '',
         'parentEntId': 10045,
         'pos': Point3(0.0, 68.4499969482, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'mintId': 12500},
 10036: {'type': 'mintProductPallet',
         'name': 'copy of <unnamed>',
         'comment': '',
         'parentEntId': 10035,
         'pos': Point3(0.0, 13.6865262985, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'mintId': 12700},
 10037: {'type': 'mintProductPallet',
         'name': 'copy of <unnamed> (2)',
         'comment': '',
         'parentEntId': 10035,
         'pos': Point3(0.0, 27.3799991608, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'mintId': 12600},
 10038: {'type': 'mintProductPallet',
         'name': 'copy of <unnamed> (3)',
         'comment': '',
         'parentEntId': 10035,
         'pos': Point3(0.0, 41.0699996948, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'mintId': 12700},
 10043: {'type': 'mintProductPallet',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10007,
         'pos': Point3(-36.662399292, -39.0314712524, 0.0),
         'hpr': Point3(90.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'mintId': 12500},
 10044: {'type': 'mintProductPallet',
         'name': 'copy of <unnamed> (2)',
         'comment': '',
         'parentEntId': 10021,
         'pos': Point3(0.0, 25.4739685059, 0.0),
         'hpr': Point3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'mintId': 12600},
 10004: {'type': 'model',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10021,
         'pos': Point3(0.0, -1.09804749489, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(2.0, 2.0, 2.0),
         'collisionsOnly': 0,
         'flattenType': 'strong',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'},
 10009: {'type': 'model',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10008,
         'pos': Point3(-3.9962117672, 0.695078849792, 0.0113303475082),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.20000004768, 1.20000004768, 1.20000004768),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/crates_E.bam'},
 10010: {'type': 'model',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10008,
         'pos': Point3(48.0530014038, -0.531660735607, -0.327078670263),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/crates_C1.bam'},
 10012: {'type': 'model',
         'name': 'rightCrates',
         'comment': '',
         'parentEntId': 10007,
         'pos': Point3(36.0373382568, 71.3546981812, 9.99835586548),
         'hpr': Vec3(315.0, 0.0, 0.0),
         'scale': Vec3(1.5, 1.5, 1.5),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/crates_E.bam'},
 10024: {'type': 'model',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10028,
         'pos': Point3(-3.7328555584, 27.1218452454, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Point3(2.0, 2.0, 2.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'},
 10027: {'type': 'model',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10028,
         'pos': Point3(-11.9349050522, 38.9528312683, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Point3(2.0, 2.0, 2.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'},
 10029: {'type': 'model',
         'name': 'crate',
         'comment': '',
         'parentEntId': 10035,
         'pos': Point3(0.0, 0.863602340221, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(2.0, 2.0, 2.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'},
 10030: {'type': 'model',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10023,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1,
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'},
 10031: {'type': 'model',
         'name': 'copy of crate',
         'comment': '',
         'parentEntId': 10029,
         'pos': Point3(0.0, 0.0, 5.46999979019),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Point3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'},
 10032: {'type': 'model',
         'name': 'copy of <unnamed>',
         'comment': '',
         'parentEntId': 10023,
         'pos': Point3(0.0, -5.92218112946, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'},
 10039: {'type': 'model',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10010,
         'pos': Point3(-9.23663234711, 0.821143984795, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.5, 1.5, 1.5),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/crates_F1.bam'},
 10042: {'type': 'model',
         'name': 'copy of <unnamed> (2)',
         'comment': '',
         'parentEntId': 10023,
         'pos': Point3(3.0, -11.8400001526, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'},
 10048: {'type': 'model',
         'name': 'cratesAgainstWall',
         'comment': '',
         'parentEntId': 10007,
         'pos': Point3(-37.0983123779, 70.2133865356, 10.0),
         'hpr': Vec3(225.0, 0.0, 0.0),
         'scale': Vec3(1.5, 1.5, 1.5),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/crates_E.bam'},
 10000: {'type': 'nodepath',
         'name': 'cogs',
         'comment': '',
         'parentEntId': 10011,
         'pos': Point3(0.0, 66.1200027466, 10.1833248138),
         'hpr': Point3(270.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0)},
 10002: {'type': 'nodepath',
         'name': 'battle',
         'comment': '',
         'parentEntId': 10000,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Point3(90.0, 0.0, 0.0),
         'scale': 1},
 10003: {'type': 'nodepath',
         'name': 'cogs2',
         'comment': '',
         'parentEntId': 10011,
         'pos': Point3(-53.9246749878, -22.7616195679, 0.0),
         'hpr': Point3(45.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0)},
 10005: {'type': 'nodepath',
         'name': 'battle',
         'comment': '',
         'parentEntId': 10003,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1},
 10007: {'type': 'nodepath',
         'name': 'props',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1},
 10008: {'type': 'nodepath',
         'name': 'topWall',
         'comment': '',
         'parentEntId': 10007,
         'pos': Point3(0.0, 48.0299987793, 10.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1},
 10011: {'type': 'nodepath',
         'name': 'cogs',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1},
 10013: {'type': 'nodepath',
         'name': 'frontCogs',
         'comment': '',
         'parentEntId': 10011,
         'pos': Point3(25.3957309723, -12.3005743027, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0)},
 10014: {'type': 'nodepath',
         'name': 'frontPalletWall',
         'comment': '',
         'parentEntId': 10007,
         'pos': Point3(45.5494384766, 38.2237281799, 0.0),
         'hpr': Point3(180.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0)},
 10021: {'type': 'nodepath',
         'name': 'middlePalletWallLeft',
         'comment': '',
         'parentEntId': 10046,
         'pos': Point3(6.0, -37.9928665161, 0.0),
         'hpr': Point3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0)},
 10023: {'type': 'nodepath',
         'name': 'crateIsland',
         'comment': '',
         'parentEntId': 10007,
         'pos': Point3(-23.1813278198, 7.08758449554, 0.00999999977648),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(2.0, 2.0, 2.0)},
 10028: {'type': 'nodepath',
         'name': 'rewardCulDeSac',
         'comment': '',
         'parentEntId': 10045,
         'pos': Point3(-8.26172065735, 38.377407074, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0)},
 10033: {'type': 'nodepath',
         'name': 'barrels',
         'comment': '',
         'parentEntId': 10028,
         'pos': Point3(-4.75077962875, 34.1425209045, 0.0),
         'hpr': Point3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0)},
 10035: {'type': 'nodepath',
         'name': 'backPalletWall',
         'comment': '',
         'parentEntId': 10007,
         'pos': Point3(-47.6501731873, 40.006893158, 0.0),
         'hpr': Point3(180.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0)},
 10040: {'type': 'nodepath',
         'name': 'centerCogs',
         'comment': '',
         'parentEntId': 10011,
         'pos': Point3(-23.9375743866, 28.353269577, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0)},
 10045: {'type': 'nodepath',
         'name': 'middlePalletWallRight',
         'comment': '',
         'parentEntId': 10046,
         'pos': Point3(17.4200000763, -38.2999992371, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1},
 10046: {'type': 'nodepath',
         'name': 'middlePalletWall',
         'comment': '',
         'parentEntId': 10007,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities,
 'scenarios': [Scenario0]}
