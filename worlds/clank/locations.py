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


# init db
def init_db():
    # get all the data from the database
    cur.execute("""
        SELECT l.ID, l.Name, lt.Name FROM locations l
        INNER JOIN locationType lt ON lt.ID = l.TypeID
        """)
    locationData = cur.fetchall()

    # add all the data to the location name dictionary
    for i in locationData:
        LOCATION_NAME_TO_ID[i[1]] = i[0]


# helper function for gaining data from database for option-specific locations
def get_db_data_by_type(typeQuery):
    cur.execute(f"""
        SELECT Name FROM Location WHERE Type IN(
            SELECT ID FROM LocationType WHERE Name = '{typeQuery}')
        """)
    resultData = cur.fetchall()
    return resultData


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class ClankLocation(Location):
    game =  "Clank!"


# helper method that creates dictionary of all locations and their ID's
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: ClankWorld) -> None:

    init_db()

    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: ClankWorld) -> None:
    # put all locations into regions

    # grab all the regions as in regions.py
    overall_region = world.get_region("Overall Region")
    base_board = world.get_region("Base Front")
    advanced_board = world.get_region("Base Back")


    # assign locations to regions
    # seup region lists
    overall_region_locations = []
    base_board_locations = []
    advanced_board_locations = []

    # Artifact Extraction locations
    if world.multiworld.options.artifacts:
        artifactChecks = get_db_data_by_type("artifact_extraction")
        for i in artifactChecks:
            overall_region_locations.append(i)


    overall_region.add_locations(get_location_names_with_ids(overall_region_locations), ClankLocation)
    base_board.add_locations(get_location_names_with_ids(base_board_locations), ClankLocation)
    advanced_board.add_locations(get_location_names_with_ids(advanced_board_locations), ClankLocation)


def create_events(world: ClankWorld) -> None:
    pass