from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import ClankWorld


# IDs for each item
LOCATION_NAME_TO_ID = {
    "Artifact Extraction: Bracelet": 1,
    "Artifact Extraction: Anhk": 2,
    "Artifact Extraction: Urn": 3,
    "Artifact Extraction: Golden Banana": 4,
    "Artifact Extraction: Shield": 5,
    "Artifact Extraction: Chestplate": 6,
    "Artifact Extraction: Golden Treasure": 7,
}


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class ClankLocation(Location):
    game =  "Clank!"


# helper method that creates dictionary of all locations and their ID's
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: ClankWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: ClankWorld) -> None:
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



def create_events(world: ClankWorld) -> None:
    pass