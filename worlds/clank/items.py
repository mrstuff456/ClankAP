from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import ClankWorld


ITEM_NAME_TO_ID = {
    #"Artifact Unlock: Bracelet": 1,
    "Artifact Unlock: Anhk": 2,
    "Artifact Unlock: Urn": 3,
    "Artifact Unlock: Golden Banana": 4,
    "Artifact Unlock: Shield": 5,
    "Artifact Unlock: Chestplate": 6,
    "Artifact Unlock: Golden Treasure": 7,
    "filler": 8,
}


DEFAULT_ITEM_CLASSIFICATIONS = {
    #"Artifact Unlock: Bracelet": ItemClassification.progression,
    "Artifact Unlock: Anhk": ItemClassification.progression,
    "Artifact Unlock: Urn": ItemClassification.progression,
    "Artifact Unlock: Golden Banana": ItemClassification.progression,
    "Artifact Unlock: Shield": ItemClassification.progression,
    "Artifact Unlock: Chestplate": ItemClassification.progression,
    "Artifact Unlock: Golden Treasure": ItemClassification.progression,
    "filler": ItemClassification.filler,
}


class ClankItem(Item):
    game = "Clank!"


def get_random_filler_item_name(world: ClankWorld) -> str:
    #if world.random.randint(0, 99) < world.options.Filler_6_Chance:
    return "filler"


def create_item_with_correct_classification(world: ClankWorld, name: str) -> ClankItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return ClankItem(name, classification, ITEM_NAME_TO_ID[name], world.player)
    

def create_all_items(world: ClankWorld) -> None:

    # create the pool containing all the items
    itempool: list[Item] = [
        world.create_item("Artifact Unlock: Anhk"),
        world.create_item("Artifact Unlock: Urn"),
        world.create_item("Artifact Unlock: Golden Banana"),
        world.create_item("Artifact Unlock: Shield"),
        world.create_item("Artifact Unlock: Chestplate"),
        world.create_item("Artifact Unlock: Golden Treasure"),
    ]


    # get number of required filler items
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    # create the filler items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]


    # add items to the multiworld
    world.multiworld.itempool += itempool