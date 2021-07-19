# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Define the static list of units for SC2. Generated by bin/gen_data.py."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import enum


# pylint: disable=invalid-name
class Neutral(enum.IntEnum):
    """Neutral units."""
    NoUnit = 0  # add this to simplify embedding a 'pad' unit
    BattleStationMineralField = 886
    BattleStationMineralField750 = 887
    CarrionBird = 322
    CleaningBot = 612
    CollapsibleRockTower = 609
    CollapsibleRockTowerDebris = 490
    CollapsibleRockTowerDebrisRampLeft = 518
    CollapsibleRockTowerDebrisRampRight = 517
    CollapsibleRockTowerDiagonal = 588
    CollapsibleRockTowerPushUnit = 561
    CollapsibleRockTowerPushUnitRampLeft = 564
    CollapsibleRockTowerPushUnitRampRight = 563
    CollapsibleRockTowerRampLeft = 664
    CollapsibleRockTowerRampRight = 663
    CollapsibleTerranTower = 610
    CollapsibleTerranTowerDebris = 485
    CollapsibleTerranTowerDiagonal = 589
    CollapsibleTerranTowerPushUnit = 562
    CollapsibleTerranTowerPushUnitRampLeft = 559
    CollapsibleTerranTowerPushUnitRampRight = 560
    CollapsibleTerranTowerRampLeft = 590
    CollapsibleTerranTowerRampRight = 591
    Crabeetle = 662
    Debris2x2NonConjoined = 475
    DebrisRampLeft = 486
    DebrisRampRight = 487
    DestructibleBillboardTall = 350
    DestructibleCityDebris4x4 = 628
    DestructibleCityDebris6x6 = 629
    DestructibleCityDebrisHugeDiagonalBLUR = 630
    DestructibleDebris4x4 = 364
    DestructibleDebris6x6 = 365
    DestructibleDebrisRampDiagonalHugeBLUR = 377
    DestructibleDebrisRampDiagonalHugeULBR = 376
    DestructibleIce4x4 = 648
    DestructibleIce6x6 = 649
    DestructibleIceDiagonalHugeBLUR = 651
    DestructibleRampDiagonalHugeBLUR = 373
    DestructibleRampDiagonalHugeULBR = 372
    DestructibleRock6x6 = 371
    DestructibleRockEx14x4 = 638
    DestructibleRockEx16x6 = 639
    DestructibleRockEx1DiagonalHugeBLUR = 641
    DestructibleRockEx1DiagonalHugeULBR = 640
    DestructibleRockEx1HorizontalHuge = 643
    DestructibleRockEx1VerticalHuge = 642
    Dog = 336
    InhibitorZoneMedium = 1958
    InhibitorZoneSmall = 1957
    KarakFemale = 324
    LabBot = 661
    LabMineralField = 665
    LabMineralField750 = 666
    Lyote = 321
    MineralField = 341
    MineralField450 = 1961
    MineralField750 = 483
    ProtossVespeneGeyser = 608
    PurifierMineralField = 884
    PurifierMineralField750 = 885
    PurifierRichMineralField = 796
    PurifierRichMineralField750 = 797
    PurifierVespeneGeyser = 880
    ReptileCrate = 877
    RichMineralField = 146
    RichMineralField750 = 147
    RichVespeneGeyser = 344
    Scantipede = 335
    ShakurasVespeneGeyser = 881
    SpacePlatformGeyser = 343
    UnbuildableBricksDestructible = 473
    UnbuildablePlatesDestructible = 474
    UnbuildableRocksDestructible = 472
    UtilityBot = 330
    VespeneGeyser = 342
    XelNagaDestructibleBlocker8NE = 1904
    XelNagaDestructibleBlocker8SW = 1908
    XelNagaTower = 149
    FloatingMineralPickup = 1680


class Protoss(enum.IntEnum):
    """Protoss units."""
    Adept = 311
    AdeptPhaseShift = 801
    Archon = 141
    Assimilator = 61
    AssimilatorRich = 1955
    Carrier = 79
    Colossus = 4
    CyberneticsCore = 72
    DarkShrine = 69
    DarkTemplar = 76
    Disruptor = 694
    DisruptorPhased = 733
    FleetBeacon = 64
    ForceField = 135
    Forge = 63
    Gateway = 62
    HighTemplar = 75
    Immortal = 83
    Interceptor = 85
    Mothership = 10
    MothershipCore = 488
    Nexus = 59
    Observer = 82
    ObserverSurveillanceMode = 1911
    Oracle = 495
    Phoenix = 78
    PhotonCannon = 66
    Probe = 84
    Pylon = 60
    PylonOvercharged = 894
    RoboticsBay = 70
    RoboticsFacility = 71
    Sentry = 77
    ShieldBattery = 1910
    Stalker = 74
    Stargate = 67
    StasisTrap = 732
    Tempest = 496
    TemplarArchive = 68
    TwilightCouncil = 65
    VoidRay = 80
    WarpGate = 133
    WarpPrism = 81
    WarpPrismPhasing = 136
    Zealot = 73


class Terran(enum.IntEnum):
    """Terran units."""
    Armory = 29
    AutoTurret = 31
    Banshee = 55
    Barracks = 21
    BarracksFlying = 46
    BarracksReactor = 38
    BarracksTechLab = 37
    Battlecruiser = 57
    Bunker = 24
    CommandCenter = 18
    CommandCenterFlying = 36
    Cyclone = 692
    EngineeringBay = 22
    Factory = 27
    FactoryFlying = 43
    FactoryReactor = 40
    FactoryTechLab = 39
    FusionCore = 30
    Ghost = 50
    GhostAcademy = 26
    GhostAlternate = 144
    GhostNova = 145
    Hellion = 53
    Hellbat = 484
    KD8Charge = 830
    Liberator = 689
    LiberatorAG = 734
    MULE = 268
    Marauder = 51
    Marine = 48
    Medivac = 54
    MissileTurret = 23
    Nuke = 58
    OrbitalCommand = 132
    OrbitalCommandFlying = 134
    PlanetaryFortress = 130
    PointDefenseDrone = 11
    Raven = 56
    Reactor = 6
    Reaper = 49
    Refinery = 20
    RefineryRich = 1960
    RepairDrone = 1913
    SCV = 45
    SensorTower = 25
    SiegeTank = 33
    SiegeTankSieged = 32
    Starport = 28
    StarportFlying = 44
    StarportReactor = 42
    StarportTechLab = 41
    SupplyDepot = 19
    SupplyDepotLowered = 47
    TechLab = 5
    Thor = 52
    ThorHighImpactMode = 691
    VikingAssault = 34
    VikingFighter = 35
    WidowMine = 498
    WidowMineBurrowed = 500


class Zerg(enum.IntEnum):
    """Zerg units."""
    Baneling = 9
    BanelingBurrowed = 115
    BanelingCocoon = 8
    BanelingNest = 96
    BroodLord = 114
    BroodLordCocoon = 113
    Broodling = 289
    BroodlingEscort = 143
    Changeling = 12
    ChangelingMarine = 15
    ChangelingMarineShield = 14
    ChangelingZealot = 13
    ChangelingZergling = 17
    ChangelingZerglingWings = 16
    Cocoon = 103
    Corruptor = 112
    CreepTumor = 87
    CreepTumorBurrowed = 137
    CreepTumorQueen = 138
    Drone = 104
    DroneBurrowed = 116
    EvolutionChamber = 90
    Extractor = 88
    ExtractorRich = 1956
    GreaterSpire = 102
    Hatchery = 86
    Hive = 101
    Hydralisk = 107
    HydraliskBurrowed = 117
    HydraliskDen = 91
    InfestationPit = 94
    InfestedTerran = 7
    InfestedTerranBurrowed = 120
    InfestedTerranCocoon = 150
    Infestor = 111
    InfestorBurrowed = 127
    Lair = 100
    Larva = 151
    Locust = 489
    LocustFlying = 693
    Lurker = 502
    LurkerBurrowed = 503
    LurkerDen = 504
    LurkerCocoon = 501
    Mutalisk = 108
    NydusCanal = 142
    NydusNetwork = 95
    Overlord = 106
    OverlordTransport = 893
    OverlordTransportCocoon = 892
    Overseer = 129
    OverseerCocoon = 128
    OverseerOversightMode = 1912
    ParasiticBombDummy = 824
    Queen = 126
    QueenBurrowed = 125
    Ravager = 688
    RavagerBurrowed = 690
    RavagerCocoon = 687
    Roach = 110
    RoachBurrowed = 118
    RoachWarren = 97
    SpawningPool = 89
    SpineCrawler = 98
    SpineCrawlerUprooted = 139
    Spire = 92
    SporeCrawler = 99
    SporeCrawlerUprooted = 140
    SwarmHost = 494
    SwarmHostBurrowed = 493
    Ultralisk = 109
    UltraliskBurrowed = 131
    UltraliskCavern = 93
    Viper = 499
    Zergling = 105
    ZerglingBurrowed = 119


def get_unit_type(unit_id):
    for race in (Neutral, Protoss, Terran, Zerg):
        try:
            return race(unit_id)
        except ValueError:
            pass  # Wrong race.


# convert the unit_ids to a dense list so that we dont waste a
# heap of memory creating embeddings for units that dont exist
def get_unit_embed_lookup():
    lookup = {}
    embed_index = 0

    for race in (Neutral, Protoss, Terran, Zerg):
        for unit_id in list(map(int, race)):
            lookup[unit_id] = embed_index
            embed_index += 1

    return lookup
