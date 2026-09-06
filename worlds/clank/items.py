from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import ClankWorld

import sqlite3
# init SQLite database
con = sqlite3.connect("ClankDatabase.db")
cur = con.cursor()


ITEM_NAME_TO_ID = {}
DEFAULT_ITEM_CLASSIFICATIONS = {}


# add all the items to the relative dictionaries
def init_db():
    # get everything from the database
    cur.execute("""
    SELECT i.ID, i.Name, c.ClassificationName FROM Item i 
    INNER JOIN ItemClassification c ON c.ID = i.Classification
    """)
    itemData = cur.fetchall()

    # add the database data to the dictionaries
    for i in itemData:
        ITEM_NAME_TO_ID[i[1]] = i[0] # add to item dictionary: "name": id
        DEFAULT_ITEM_CLASSIFICATIONS[i[1]] = ItemClassification[i[2]] # add to classification dict: "name": "classification"



# helper function for gaining data from database for option-specific checks
def get_db_data_by_type(typeQuery):
    cur.execute(f"""
        SELECT Name FROM Item WHERE Type IN(
            SELECT ID FROM ItemType WHERE Name = '{typeQuery}')
        """)
    resultData = cur.fetchall()
    return resultData


class ClankItem(Item):
    game = "Clank!"


def get_random_filler_item_name(world: ClankWorld) -> str:
    #if world.random.randint(0, 99) < world.options.Filler_6_Chance:
    return "filler"


def create_item_with_correct_classification(world: ClankWorld, name: str) -> ClankItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return ClankItem(name, classification, ITEM_NAME_TO_ID[name], world.player)
    

def create_all_items(world: ClankWorld) -> None:

    # init db
    init_db()

    # create the pool and items to add lists
    itempool: list[Item] = []
    ITEMS_TO_ADD = []

    # Create all the items needed

    # Artifact Unlocks:
    if world.multiworld.options.artifacts:
        artifactNames = get_db_data_by_type("artifact_unlock")
        startingArtifactDict = world.multiworld.options.starting_artifacts.value
        for i in artifactNames:
            if i not in ["Artifact Unlock: " + x for x, y in startingArtifactDict.items() if y == 1]:
                ITEMS_TO_ADD.append(i)


    # Dungeon Row Unlocks:
    if world.multiworld.options.dungeon_row:
        if world.multiworld.options.row_shuffling_style == "Packs":
            packNames = get_db_data_by_type("dungeon_row_pack")
            for i in packNames:
                ITEMS_TO_ADD.append(i)


    # insert all the items into the pool
    for i in ITEMS_TO_ADD:
        itempool.append(world.create_item(i))


    # get number of required filler items
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    # create the filler items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]


    # add items to the multiworld
    world.multiworld.itempool += itempool