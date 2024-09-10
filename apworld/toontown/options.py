from dataclasses import dataclass

from Options import PerGameCommonOptions, StartInventoryPool, Range, Choice, Toggle


class TeamOption(Range):
    """
    Experimental option to set what team you are on. Do not use unless you are admin'ing a race.
    """
    display_name = "Team"
    range_start = 0
    range_end = 20
    default = 0


class StartLaffOption(Range):
    """
    The starting amount of max Laff Points to have when starting a new game.
    """
    display_name = "Starting Laff"
    range_start = 1
    range_end = 80
    default = 20


class MaxLaffOption(Range):
    """
    The max laff you can get from items throughout the run.
    Must be above or equal to the starting_laff.
    """
    display_name = "Max Laff"
    range_start = 1
    range_end = 150
    default = 150


class BaseGlobalGagXPRange(Range):
    """
    The base global gag experience multiplier when starting a new game.
    This multiplier is globally multiplicative on top of in-game boosts.
    """
    display_name = "Base Global Gag XP"
    range_start = 1
    range_end = 10
    default = 2


class MaxGlobalGagXPRange(Range):
    """
    Additional global gag experience that can be obtained from items.
    Stacks additively onto the base value above.
    Must be above or equal to the base_global_gag_xp.
    """
    display_name = "Max Global Gag XP"
    range_start = 0
    range_end = 30
    default = 15


class DamageMultiplierRange(Range):
    """
    The percentage of damage that will be done when battling Cogs.
    50 -> 50%/Half damage, 200 -> 200%/2x damage, etc.
    """
    display_name = "Damage Multiplier"
    range_start = 25
    range_end = 500
    default = 100

class OverflowModRange(Range):
    """
    The percentage multiplier that will given with exp overflow.
    50 -> 50%/Half overflow rate, 200 -> 200%/2x overflow rate, etc.
    """
    display_name = "Overflow Modifier"
    range_start = 25
    range_end = 300
    default = 100


class StartMoneyOption(Range):
    """
    The starting amount of jellybeans to have when starting a new game.
    """
    display_name = "Starting Jellybeans"
    range_start = 0
    range_end = 1000
    default = 1000

class StartingTaskCapacityOption(Range):
    """
    The starting amount of tasks a toon can hold when starting a new game.
    """
    display_name = "Starting Task Capacity"
    range_start = 1
    range_end = 6
    default = 4

class MaxTaskCapacityOption(Range):
    """
    The max amount of tasks a toon can hold.
    """
    display_name = "Max Task Capacity"
    range_start = 1
    range_end = 6
    default = 4
    
class WinCondition(Choice):
    """
    Determines the condition before being able to talk to Flippy to complete the game.
    - cog_bosses (default): Player must defeat a number of cog bosses to complete the game (determined by cog_bosses_required).
    - total_tasks: Player must complete a total number of tasks to complete the game (determined by total_tasks_required).
    - hood_tasks: Player must complete a number of tasks from each neighborhood to complete the game (determined by hood_tasks_required).
    - total_fish_species:  Player must catch a certain amount of fish species to complete the game (determined by fish_species_required).
    - laff_o_lympics: Player must reach a certain amount of laff to complete the game (determined by laff_points_required).
    """
    display_name = "Win Condition"
    option_cog_bosses = 0
    option_total_tasks = 1
    option_hood_tasks = 2
    option_total_gag_tracks = 3
    option_total_fish_species = 4
    option_laff_o_lympics = 5
    default = 0


class SecondWinCondition(Choice):
    """
    NOTE: This condition should NOT be the same as win_condition
    Determines a second condition before being able to talk to Flippy to complete the game.
    - none (default): Disables this option and only one condition is needed to complete the run.
    - cog_bosses: Player must defeat a number of cog bosses to complete the game (determined by cog_bosses_required).
    - total_tasks: Player must complete a total number of tasks to complete the game (determined by total_tasks_required).
    - hood_tasks: Player must complete a number of tasks from each neighborhood to complete the game (determined by hood_tasks_required).
    - total_fish_species:  Player must catch a certain amount of fish species to complete the game (determined by fish_species_required).
    - laff_o_lympics: Player must reach a certain amount of laff to complete the game (determined by laff_points_required).
    """
    display_name = "Second Win Condition"
    option_cog_bosses = 0
    option_total_tasks = 1
    option_hood_tasks = 2
    option_total_gag_tracks = 3
    option_total_fish_species = 4
    option_laff_o_lympics = 5
    option_none = 6
    default = 6


class CogBossesRequired(Range):
    """
    How many cog bosses must be defeated before being able to talk to Flippy to complete the game.
    Unused if win_condition is not cog_bosses.
    """
    display_name = "Cog Bosses Required"
    range_start = 0
    range_end = 4
    default = 4


class TotalTasksRequired(Range):
    """
    How many total tasks must be finished before being able to talk to Flippy to complete the game.
    Must be less than total tasks in game (6 zones times logical_tasks_per_playground tasks).
    Unused if win_condition is not total_tasks.
    """
    display_name = "Total Tasks Required"
    range_start = 0
    range_end = 72
    default = 48


class HoodTasksRequired(Range):
    """
    How many tasks must be finished in each neighborhood before being able to talk to Flippy to complete the game.
    Must be less than logical_tasks_per_playground.
    Unused if win_condition is not hood_tasks.
    """
    display_name = "Hood Tasks Required"
    range_start = 0
    range_end = 12
    default = 8


class GagTracksRequired(Range):
    """
    How many gag tracks must be maxxed before being able to talk to Flippy to complete the game.
    Must be less than or equal to total number of gag tracks a toon can obtain.
    Unused if win_condition is not total_gag_tracks
    """
    display_name = "Gag Tracks Required"
    range_start = 0
    range_end = 7
    default = 5


class FishSpeciesRequired(Range):
    """
    How many fish species must be caught before being able to talk to Flippy to complete the game.
    Must be less than or equal to total number of fish species a toon can obtain.
    Unused if win_condition is not total_fish_species
    """
    display_name = "Fish Species Required"
    range_start = 0
    range_end = 70
    default = 70


class LaffPointsRequired(Range):
    """
    How many laff points we must have before being able to talk to Flippy to complete the game.
    Setting must be below or equal to max_laff setting
    Unused if win_condition is not laff_o_lympics
    """
    display_name = "Laff Points Required"
    range_start = 0
    range_end = 150
    default = 120

    
class TPSanity(Choice):
    """
    Determines how Teleport Access is shuffled in the Item Pool for all Playgrounds/HQs.
    - keys: Playgrounds and HQs are locked until their respective Teleport Access is found.
    - treasure: All areas are accessible. Teleport Access items are guaranteed to spawn in their area treasure.
    - shuffle: All areas are accessible. Teleport Access items are shuffled in the pool.
    - none: All areas are accessible. You start with global teleport access.
    """
    display_name = "tpsanity"
    option_keys = 0
    option_treasure = 1
    option_shuffle = 2
    option_none = 3
    default = 0


class TreasuresPerLocation(Range):
    """
    The amount of archipelago treasures that'll have items in each location
    """
    display_name = "AP Treasures Per Location"
    range_start = 0
    range_end = 6
    default = 4


class ChecksPerBoss(Range):
    """
    How many checks you will receive from a cog boss upon completion.
    """
    display_name = "Checks Per Boss"
    range_start = 0
    range_end = 5
    default = 4


class GagTrainingCheckBehavior(Choice):
    """
    Behavior of how gag experience check locations are handled.

    unlock: When unlocking a new gag, you get its respective check.
    trained: When earning all available experience for a specific gag level, you get its respective check.
    disabled: Does not give checks for gags.
    """
    option_unlock = 0
    option_trained = 1
    option_disabled = 2
    default = 1

    display_name = "Gag Training Check Behavior"


class GagTrainingFrameBehavior(Choice):
    """
    Behavior of how gag frame items are handled

    vanilla: unlocks the gag when you get the exp required.
    unlock: unlocks the gag immediately, giving you the required exp directly.
    trained: maxes your experience in the track immediately, effectively disabling exp entirely until overcapped.
    """

    option_vanilla = 0
    option_unlock = 1
    option_trained = 2
    default = 0

    display_name = "Gag Frame Item Behavior"

class LogicalTasksPerPlayground(Range):
    """
    Determines the amount of tasks per playground that are in logic.
    """
    display_name = "Logical Tasks Per Playground"
    range_start = 0
    range_end = 12
    default = 12


class StartingTaskOption(Choice):
    """
    Determines the starting tasking PG of a player
    """
    display_name = "Starting Task Playground"
    option_ttc = 0
    option_dd = 1
    option_dg = 2
    option_mml = 3
    option_tb = 4
    option_ddl = 5
    option_randomized = 6
    default = 0


class LogicalMaxedCogGallery(Toggle):
    """
    Enable to make Cog Gallery Maxed checks be in logic.
    """
    display_name = "Logical Maxed Cog Gallery"
    default = True


class MaxedCogGalleryQuota(Range):
    """
    The amount of Cogs required to reach its maxed Cog Gallery.
    """
    display_name = "Maxed Cog Gallery Quota"
    range_start = 0
    range_end = 10
    default = 3


class FacilityLocking(Choice):
    """
    Determines how facilities are locked within a run.
    - keys: Default, each facility has its own key.
    - access: Adds a second area access key for each cog HQ to the pool that unlocks all facilities within.
    - unlocked: Facilities are unlocked from the start of the run.
    """
    display_name = "Facility Locking"
    option_keys = 0
    option_access = 1
    option_unlocked = 2
    default = 0


class FishLocations(Choice):
    """
    Determines where fish can spawn.
    - playgrounds: Fish spawn in their vanilla locations. Street-exclusive fish can be found anywhere in their playgrounds.
    - vanilla: Fish spawn in their vanilla locations. Street-exclusive fish remain in their vanilla locations.
    - global: Fish can spawn anywhere.
    """
    display_name = "fish_locations"
    option_playgrounds = 0
    option_vanilla = 1
    option_global = 2
    default = 0


class FishChecks(Choice):
    """
    Determines the amount of items that can be found from fishing.
    - all_species: All 70 species will have an item.
    - all_gallery_and_genus: Every 10 species and unique genus will have an item.
    - all_gallery: Every 10 species will have an item.
    - none: There are no items in fishing.
    """
    display_name = "fish_checks"
    option_all_species = 0
    option_all_gallery_and_genus = 1
    option_all_gallery = 2
    option_none = 3
    default = 1


class FishProgression(Choice):
    """
    Determines the progression for fishing.
    - licenses_and_rods: Both 'licenses' and 'rods' progression are active.
    - licenses: Playground fishing is restricted until their respective Fishing License is obtained. The player starts with a Gold Rod.
    - rods: Progressive fishing rod items are added to the pool.
    - none: All fishing areas are available. The player starts with a Gold Rod.
    """
    display_name = "fish_progression"
    option_licenses_and_rods = 0
    option_licenses = 1
    option_rods = 2
    option_none = 3
    default = 2


class RacingOption(Toggle):
    """
    Enable to turn on racing checks.
    """

    display_name = "Racing Logic"
    default = False


class GolfingOption(Toggle):
    """
    Enable to turn on the minigolf checks.
    """

    display_name = "Golfing Logic"
    default = False


class SyncJellybeans(Toggle):
    """
    Enable to sync Jellybeans between toons on the same slot.
    Even if you aren't using multiple toons,
    leaving this on will retain your jellybeans if you need to make a new toon to reconnect.
    If this is 'false', the data will still be sent, but your toon will not sync with it.
    """
    display_name = "Sync Jellybeans"
    default = True


class SyncGagExp(Toggle):
    """
    Enable to sync Gag Experience between toons on the same slot.
    Even if you aren't using multiple toons,
    leaving this on will retain your gag experience if you need to make a new toon to reconnect.
    If this is 'false', the data will still be sent, but your toon will not sync with it.
    """
    display_name = "Sync Gag Experience"
    default = True


class SeedGenerationTypeOption(Choice):
    """
    Type of seeding to use when RNG checks happen in game.

    Global: RNG elements are determined solely by the AP seed
    Per Slot: RNG elements are determined by AP seed and Slot Name
    Per Toon: RNG elements are determined by AP seed and internal toon ID
    Wild: RNG elements are completely random and will shuffle upon relogging
    """
    option_global = 0
    option_slot_name = 1
    option_unique = 2
    option_wild = 3

    display_name = "Seed Generation Type"


class TrapPercentOption(Range):
    """
    Percentage of junk items to be replaced with traps
    """

    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 20


class UberWeightOption(Range):
    """
    Weight of uber traps in the trap pool.
    """

    display_name = "Uber Trap Weight"
    range_start = 0
    range_end = 100
    default = 100


class DripWeightOption(Range):
    """
    Weight of drip traps in the trap pool.
    """

    display_name = "Drip Trap Weight"
    range_start = 0
    range_end = 100
    default = 50


class TaxWeightOption(Range):
    """
    Weight of bean taxes in the trap pool.
    """

    display_name = "Bean Tax Weight"
    range_start = 0
    range_end = 100
    default = 36


class ShuffleWeightOption(Range):
    """
    Weight of gag shuffles in the trap pool.
    """

    display_name = "Gag Shuffle Weight"
    range_start = 0
    range_end = 100
    default = 100


class BeanWeightOption(Range):
    """
    Weight of bean items in the junk pool.
    """

    display_name = "Bean Junk Weight"
    range_start = 0
    range_end = 100
    default = 100


class GagExpWeightOption(Range):
    """
    Weight of gag exp items in the junk pool.
    """

    display_name = "Exp Bundle Weight"
    range_start = 0
    range_end = 100
    default = 100


class SOSWeightOption(Range):
    """
    Weight of SOS card items in the junk pool.
    """

    display_name = "SOS Card Weight"
    range_start = 0
    range_end = 100
    default = 65


class UniteWeightOption(Range):
    """
    Weight of unite items in the junk pool.
    """

    display_name = "Unite Weight"
    range_start = 0
    range_end = 100
    default = 65


class FireWeightOption(Range):
    """
    Weight of Pink Slip items in the junk pool.
    """

    display_name = "Pink Slip Weight"
    range_start = 0
    range_end = 100
    default = 65


class DeathLinkOption(Toggle):
    """
    Enable to turn on the "DeathLink" mechanic in Archipelago.
    """

    display_name = "Death Link"
    default = False


@dataclass
class ToontownOptions(PerGameCommonOptions):
    team: TeamOption
    max_laff: MaxLaffOption
    starting_laff: StartLaffOption
    base_global_gag_xp: BaseGlobalGagXPRange
    max_global_gag_xp: MaxGlobalGagXPRange
    damage_multiplier: DamageMultiplierRange
    overflow_mod: OverflowModRange
    starting_money: StartMoneyOption
    starting_task_capacity: StartingTaskCapacityOption
    max_task_capacity: MaxTaskCapacityOption
    win_condition: WinCondition
    second_win_condition: SecondWinCondition
    cog_bosses_required: CogBossesRequired
    total_tasks_required: TotalTasksRequired
    hood_tasks_required: HoodTasksRequired
    gag_tracks_required: GagTracksRequired
    fish_species_required: FishSpeciesRequired
    laff_points_required: LaffPointsRequired
    tpsanity: TPSanity
    treasures_per_location: TreasuresPerLocation
    checks_per_boss: ChecksPerBoss
    gag_training_check_behavior: GagTrainingCheckBehavior
    gag_frame_item_behavior: GagTrainingFrameBehavior
    logical_tasks_per_playground: LogicalTasksPerPlayground
    starting_task_playground: StartingTaskOption
    logical_maxed_cog_gallery: LogicalMaxedCogGallery
    maxed_cog_gallery_quota: MaxedCogGalleryQuota
    facility_locking: FacilityLocking
    fish_locations: FishLocations
    fish_checks: FishChecks
    fish_progression: FishProgression
    slot_sync_jellybeans: SyncJellybeans
    slot_sync_gag_experience: SyncGagExp
    racing_logic: RacingOption
    minigolf_logic: GolfingOption
    seed_generation_type: SeedGenerationTypeOption
    trap_percent: TrapPercentOption
    uber_trap_weight: UberWeightOption
    drip_trap_weight: DripWeightOption
    bean_tax_weight: TaxWeightOption
    gag_shuffle_weight: ShuffleWeightOption
    bean_weight: BeanWeightOption
    exp_weight: GagExpWeightOption
    sos_weight: SOSWeightOption
    unite_weight: UniteWeightOption
    fire_weight: FireWeightOption
    death_link: DeathLinkOption
