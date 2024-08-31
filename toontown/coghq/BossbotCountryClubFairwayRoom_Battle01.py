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
        'requestNewEntity': None,
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
          'pos': Point3(0, 40, 0),
          'hpr': Point3(270, 0, 0),
          'scale': Vec3(1, 1, 1),
          'cellId': 0,
          'radius': 20},
 120200: {'type': 'battleBlocker',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(0, -40, 0),
          'hpr': Point3(270, 0, 0),
          'scale': Vec3(1, 1, 1),
          'cellId': 1,
          'radius': 20},
 120000: {'type': 'model',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 2.5,
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_12/models/bossbotHQ/ttap_m_ara_bhq_cogGolfRoofTower.bam'},
 1202000: {'type': 'model',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(85.1512, -52.4203, 0.025),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1.0,
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_12/models/bossbotHQ/ttap_m_ara_bhq_cogGolfFlagBlue.bam'},
 10002: {'type': 'nodepath',
         'name': 'props',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0, 0, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 10003:  {'type': 'apBarrel', # ARCHI BARREL PLACEMENT
          'name': 'archi',
          'comment': '',
          'parentEntId': 10002,
          'pos': Point3(31.42, -72.9, 0.025),
          'hpr': Vec3(-140, 0, 0),
          'scale': Vec3(1, 1, 1),
          'apRewardIndex': 0,
          'rewardPerGrab': 15,
          'rewardPerGrabMax': 0},
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
