from toontown.coghq.SpecImports import *
GlobalEntities = {1000: {'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_12/models/bossbotHQ/BossbotFairwayRoom_A',
        'wantDoors': 1},
 1001: {'type': 'editMgr',
        'name': 'EditMgr',
        'parentEntId': 0,
        'insertEntity': None,
        'removeEntity': None,
        'requestNewEntity': {'entType': 'door',
                             'username': 'rurbino',
                             'parentEntId': 110001,
                             'entId': 110002},
        'requestSave': None},
 0: {'type': 'zone',
     'name': 'UberZone',
     'comment': '',
     'parentEntId': 0,
     'scale': 1,
     'description': '',
     'visibility': []},
 110200: {'type': 'battleBlocker',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(70, 0, 0),
          'hpr': Point3(270, 0, 0),
          'scale': Vec3(1, 1, 1),
          'cellId': 0,
          'radius': 10},
 120000: {'type': 'model',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(85.1512, -52.4203, 0.025),
         'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1.0,
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_12/models/bossbotHQ/ttap_m_ara_bhq_cogGolfFlagGreen.bam'},
 10002: {'type': 'goon',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10001,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1.37,
         'attackRadius': 15,
         'crushCellId': None,
         'goonType': 'gg',
         'gridId': None,
         'hFov': 70,
         'strength': 16,
         'velocity': 4.0},
 10004: {'type': 'goon',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10003,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1.37,
         'attackRadius': 15,
         'crushCellId': None,
         'goonType': 'gg',
         'gridId': None,
         'hFov': 70,
         'strength': 16,
         'velocity': 4},
 10006: {'type': 'goon',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10005,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1.37,
         'attackRadius': 15,
         'crushCellId': None,
         'goonType': 'gg',
         'gridId': None,
         'hFov': 70,
         'strength': 16,
         'velocity': 4},
 10009: {'type': 'goon',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10008,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1.37,
         'attackRadius': 15,
         'crushCellId': None,
         'goonType': 'gg',
         'gridId': None,
         'hFov': 70,
         'strength': 16,
         'velocity': 4},
 130009: {'type': 'goon',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 140000,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1.37,
         'attackRadius': 15,
         'crushCellId': None,
         'goonType': 'gg',
         'gridId': None,
         'hFov': 70,
         'strength': 16,
         'velocity': 4},
 131009: {'type': 'goon',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 141000,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1.37,
         'attackRadius': 15,
         'crushCellId': None,
         'goonType': 'gg',
         'gridId': None,
         'hFov': 70,
         'strength': 16,
         'velocity': 4},
 132009: {'type': 'goon',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 142000,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1.37,
         'attackRadius': 15,
         'crushCellId': None,
         'goonType': 'gg',
         'gridId': None,
         'hFov': 70,
         'strength': 16,
         'velocity': 4},
 133009: {'type': 'goon',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 143000,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1.37,
         'attackRadius': 15,
         'crushCellId': None,
         'goonType': 'gg',
         'gridId': None,
         'hFov': 70,
         'strength': 16,
         'velocity': 4},
 10001: {'type': 'path',
         'name': 'nearPace',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(-59.7391967773, 0.0, 0.0),
         'hpr': Point3(90.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'pathIndex': 3,
         'pathScale': 1.0},
 10003: {'type': 'path',
         'name': 'bowtie',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(-40.0336875916, 0.0, 0.0),
         'hpr': Point3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'pathIndex': 2,
         'pathScale': 1.0},
 10005: {'type': 'path',
         'name': 'bridgePace',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(-8.80618190765, -1.5122487545, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'pathIndex': 3,
         'pathScale': 1.0},
 10008: {'type': 'path',
         'name': 'farPace',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(7.5265827179, 7.56240034103, 0.0),
         'hpr': Vec3(90.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'pathIndex': 3,
         'pathScale': 1.0},
 140000: {'type': 'path',
         'name': 'nearPace',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(-30.7391967773, 20.0, 0.0),
         'hpr': Point3(90.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'pathIndex': 3,
         'pathScale': 1.0},
 141000: {'type': 'path',
         'name': 'nearPace',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(30.7391967773, -20.0, 0.0),
         'hpr': Point3(90.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'pathIndex': 3,
         'pathScale': 1.0},
 142000: {'type': 'path',
         'name': 'nearPace',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(50.7391967773, 30.0, 0.0),
         'hpr': Point3(90.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'pathIndex': 3,
         'pathScale': 1.0},
 143000: {'type': 'path',
         'name': 'nearPace',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(-50.7391967773, -30.0, 0.0),
         'hpr': Point3(90.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'pathIndex': 3,
         'pathScale': 1.0},
 110202: {'type': 'door',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 110001,
          'pos': Point3(0, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': 1,
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
          'unlock1Event': 110200,
          'unlock2Event': 0,
          'unlock3Event': 0},
 10002: {'type': 'nodepath',
         'name': 'props',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0, 0, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 110001: {'type': 'nodepath',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(101.07, 0, 0),
          'hpr': Point3(270, 0, 0),
          'scale': Vec3(1, 1, 1)}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities,
 'scenarios': [Scenario0]}
