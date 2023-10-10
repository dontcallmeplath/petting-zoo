'''Module serving as Index'''
from attractions import Attraction, PettingZoo
from slithering import Alligator, Gecko, Hognose, Skink, Snork
from swimming import Axolotl, Catfish, Goldfish, Octopus, Shark
from walking import Cougar, Donkey, Goose, Horse, Llama

alfred = Alligator("Alfred", "American alligator", "afternoon", "fish")
print(alfred)
print(f'{alfred.name} the {alfred.species} is available to pet during the {alfred.shift} shift.')
print(alfred.feed())

martin = Gecko("Martin", "Crested gecko", "morning", "crickets")
print(martin)
print(f'{martin.name} the {martin.species} is available to pet during the {martin.shift} shift.')
print(martin.feed())

baby_cakes = Hognose("Baby Cakes", "Southern Hognose snake", "midday", "a feeder mouse")
print(baby_cakes)
print(f'{baby_cakes.name} the {baby_cakes.species} is available to pet during the {baby_cakes.shift} shift.')
print(baby_cakes.feed())

stink = Skink("Stink", "Blue-tongued skink", "morning", "leafy greens")
print(stink)
print(f'{stink.name} the {stink.species} is available to pet during the {stink.shift} shift.')
print(stink.feed())

squish_pls = Snork("Squish", "Ball python", "afternoon", "a rodent")
print(squish_pls)
print(f'{squish_pls.name} the {squish_pls.species} is available to pet during the {squish_pls.shift} shift.')
print(squish_pls.feed())

marisol = Axolotl("Marisol","Mosaic axolotl", "morning", "nightcrawlers")
print(marisol)
print(f'{marisol.name} the {marisol.species} is available to view during the {marisol.shift} shift.')
print(marisol.feed())

icky_thump = Catfish("Icky Thump", "Armored catfish", "midday", "zucchini and squash")
print(icky_thump)
print(f'{icky_thump.name} the {icky_thump.species} is available to pet during the {icky_thump.shift} shift.')
print(icky_thump.feed())

goldilocks = Goldfish("Goldilocks","Ryukin goldfish", "midday", "thawed blood worms")
print(goldilocks)
print(f'{goldilocks.name} the {goldilocks.species} is available to pet during the {goldilocks.shift} shift.')
print(goldilocks.feed())

ronald = Octopus("Ronald","Umbrella octopus", "afternoon", "frozen razor shell clams")
print(ronald)
print(f'{ronald.name} the {ronald.species} is available to pet during the {ronald.shift} shift.')
print(ronald.feed())

bruce = Shark("Bruce", "Lemon shark", "morning", "crabs and lobster")
print(bruce)
print(f'{bruce.name} the {bruce.species} is available to pet during the {bruce.shift} shift.')
print(bruce.feed())

madam_milf = Cougar("Madam","North American cougar", "midday", "venison")
print(madam_milf)
print(f'{madam_milf.name} the {madam_milf.species} is available to pet during the {madam_milf.shift} shift.')
print(madam_milf.feed())

arsenio = Donkey("Arsenio","regular ol' donkey", "morning", "straw")
print(arsenio)
print(f'{arsenio.name} the {arsenio.species} is available to pet during the {arsenio.shift} shift.')
print(arsenio.feed())

sir_honk = Goose("Sir Honk", "common goose", "afternoon", "orchard and timothy hay")
print(sir_honk)
print(f'{sir_honk.name} the {sir_honk.species} is available to pet during the {sir_honk.shift} shift.')
print(sir_honk.feed())

fusaichi_pegasus = Horse("Fusaichi Pegasus","American Thoroughbred horse", "morning", "timothy and oat hay")
print(fusaichi_pegasus)
print(f'{fusaichi_pegasus.name} the {fusaichi_pegasus.species} is available to pet during the {fusaichi_pegasus.shift} shift.')
print(fusaichi_pegasus.feed())

miss_fuzz = Llama("Miss Fuzz","domestic llama", "midday", "clover and blackberries")
# attr = vars(miss_fuzz)
# print(attr)
print(miss_fuzz)
print(f'{miss_fuzz.name} the {miss_fuzz.species} is available to pet during the {miss_fuzz.shift} shift.')
print(miss_fuzz.feed())

fluffy_funhouse = PettingZoo("Fluffy Funhouse")
fluffy_funhouse.animals.append(madam_milf)
fluffy_funhouse.animals.append(arsenio)
fluffy_funhouse.animals.append(sir_honk)
fluffy_funhouse.animals.append(fusaichi_pegasus)
fluffy_funhouse.animals.append(miss_fuzz)
print(f"{fluffy_funhouse.attraction_name} is where you'll find the {fluffy_funhouse.description} animals:")
for animal in fluffy_funhouse.animals:
    print(f'{animal.name}')

    