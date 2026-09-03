from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import ClankWorld

# init sqlite db
import sqlite3
con = sqlite3.connect("ClankDatabase.db")
cur = con.cursor()


# Id dictionary
LOCATION_NAME_TO_ID = {}


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class ClankLocation(Location):
    game =  "Clank!"


# helper method that creates dictionary of all locations and their ID's
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: ClankWorld) -> None:
    # get all the data from the database
    cur.execute("""
        SELECT l.ID, l.Name, lt.Name FROM locations l
        INNER JOIN locationType lt WHERE lt.ID = l.TypeID
        """)
    locationData = cur.fetchall()

    # add all the data to the location name dictionary
    for i in locationData:
        LOCATION_NAME_TO_ID[i[1]] = i[0]


    create_regular_locations(world, locationData)
    create_events(world, locationData)


def create_regular_locations(world: ClankWorld, locationData) -> None:
    # put all locations into regions

    # grab all the regions as in regions.py
    overall_region = world.get_region("Overall Region")


    # assign locations to regions
    overall_region_locations = get_location_names_with_ids(
        ["Artifact Extraction: Bracelet", "Artifact Extraction: Anhk", "Artifact Extraction: Urn", "Artifact Extraction: Golden Banana",
         "Artifact Extraction: Shield", "Artifact Extraction: Chestplate", "Artifact Extraction: Golden Treasure"]
    )
    overall_region.add_locations(overall_region_locations, ClankLocation)

    # optional locations



def create_events(world: ClankWorld, locationData) -> None:
    pass