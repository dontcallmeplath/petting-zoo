'''Module serving as Index'''
from attractions import Attraction, PettingZoo, SnakePit, WetLands
from animals import Alligator, Gecko, Hognose, Skink, Snork, Axolotl, Catfish, Goldfish, Octopus, Shark, Cougar, Donkey, Goose, Horse, Llama
from movements import slithering, swimming, walking

alfred = Alligator("Alfred", "American alligator", "fish", 123456)
print(alfred)
print(f'{alfred.name} the {alfred.species} is available to view. {alfred.chip_number}')
print(alfred.feed())

martin = Gecko("Martin", "Crested gecko", "crickets", 234567)
print(martin)
print(f'{martin.name} the {martin.species} is available to view.')
print(martin.feed())

baby_cakes = Hognose("Baby Cakes", "Southern Hognose snake", "a feeder mouse", 345678)
print(baby_cakes)
print(f'{baby_cakes.name} the {baby_cakes.species} is available to view.')
print(baby_cakes.feed())

stink = Skink("Stink", "Blue-tongued skink", "leafy greens", 456789)
print(stink)
print(f'{stink.name} the {stink.species} is available to view.')
print(stink.feed())

squish_pls = Snork("Squish", "Ball python", "a rodent", 567890)
print(squish_pls)
print(f'{squish_pls.name} the {squish_pls.species} is available to view.')
print(squish_pls.feed())

marisol = Axolotl("Marisol","Mosaic axolotl", "nightcrawlers", 678901)
print(marisol)
print(f'{marisol.name} the {marisol.species} is available to view.')
print(marisol.feed())

icky_thump = Catfish("Icky Thump", "Armored catfish", "zucchini and squash", 789012)
print(icky_thump)
print(f'{icky_thump.name} the {icky_thump.species} is available to view.')
print(icky_thump.feed())

goldilocks = Goldfish("Goldilocks","Ryukin goldfish", "thawed blood worms", 890123)
print(goldilocks)
print(f'{goldilocks.name} the {goldilocks.species} is available to view.')
print(goldilocks.feed())

ronald = Octopus("Ronald","Umbrella octopus", "frozen razor shell clams", 901234)
print(ronald)
print(f'{ronald.name} the {ronald.species} is available to view.')
print(ronald.feed())

bruce = Shark("Bruce", "Lemon shark", "crabs and lobster", 912345)
print(bruce)
print(f'{bruce.name} the {bruce.species} is available to view.')
print(bruce.feed())

madam_milf = Cougar("Madam","North American cougar", "midday", "venison", 123459)
print(madam_milf)
print(f'{madam_milf.name} the {madam_milf.species} is available to pet during the {madam_milf.shift} shift.')
print(madam_milf.feed())

arsenio = Donkey("Arsenio","regular ol' donkey", "morning", "straw", 234569)
print(arsenio)
print(f'{arsenio.name} the {arsenio.species} is available to pet during the {arsenio.shift} shift.')
print(arsenio.feed())

sir_honk = Goose("Sir Honk", "common goose", "afternoon", "orchard and timothy hay", 345679)
print(sir_honk)
print(f'{sir_honk.name} the {sir_honk.species} is available to pet during the {sir_honk.shift} shift.')
print(sir_honk.feed())
sir_honk.run()
sir_honk.swim()

fusaichi_pegasus = Horse("Fusaichi Pegasus","American Thoroughbred horse", "morning", "timothy and oat hay", 456781)
print(fusaichi_pegasus)
print(f'{fusaichi_pegasus.name} the {fusaichi_pegasus.species} is available to pet during the {fusaichi_pegasus.shift} shift.')
print(fusaichi_pegasus.feed())

miss_fuzz = Llama("Miss Fuzz","domestic llama", "midday", "clover and blackberries", 567819)
# attr = vars(miss_fuzz)
# print(attr)
print(miss_fuzz)
print(f'{miss_fuzz.name} the {miss_fuzz.species} is available to pet during the {miss_fuzz.shift} shift.')
print(miss_fuzz.feed())

fluffy_funhouse = PettingZoo("Fluffy Funhouse", "fluffy good time")
fluffy_funhouse.add_animal(madam_milf)
fluffy_funhouse.add_animal(arsenio)
fluffy_funhouse.add_animal(sir_honk)
fluffy_funhouse.add_animal(fusaichi_pegasus)
fluffy_funhouse.add_animal(miss_fuzz)
print(f"{fluffy_funhouse.attraction_name} is where you'll find the {fluffy_funhouse.description} animals:")
for animal in fluffy_funhouse.animals:
    print(f'- {animal.name} the {animal.species} - {animal.chip_number}')

viper_village = SnakePit("Viper Village", "beings w their bellies on the ground")
viper_village.add_animal(alfred)
viper_village.add_animal(martin)
viper_village.add_animal(baby_cakes)
viper_village.add_animal(stink)
viper_village.add_animal(squish_pls)
print(f"{viper_village.attraction_name} is where {viper_village.description} live:")
for animal in viper_village.animals:
    print(f'- {animal.name} the {animal.species} - {animal.chip_number}')

atchafalaya_swamp = WetLands("Atchafalaya Swamp", "wet + mysterious")
atchafalaya_swamp.add_animal(marisol)
atchafalaya_swamp.add_animal(icky_thump)
atchafalaya_swamp.add_animal(goldilocks)
atchafalaya_swamp.add_animal(ronald)
atchafalaya_swamp.add_animal(bruce)
print(f"{atchafalaya_swamp.attraction_name} is where you'll find {atchafalaya_swamp.description} animals:")
for animal in atchafalaya_swamp.animals:
    print(f'- {animal.name} the {animal.species} - {animal.chip_number}')

print(fluffy_funhouse.last_critter_added)
fluffy_funhouse.add_animal_pythonic(madam_milf)
fluffy_funhouse.add_animal_type_check(madam_milf)
fluffy_funhouse.add_animal_pythonic(alfred)
print(viper_village.last_critter_added)
print(atchafalaya_swamp.last_critter_added)
