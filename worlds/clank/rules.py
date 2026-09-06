from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

# from .options import HardMode

if TYPE_CHECKING:
    from .world import ClankWorld


def set_all_rules(world: ClankWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: ClankWorld) -> None:
    pass


def set_all_location_rules(world: ClankWorld) -> None:
    # set the location specific rules
    
    # artifacts
    world.set_rule(world.get_location("Artifact Extraction: Ankh"), Has("Artifact Unlock: Ankh"))
    world.set_rule(world.get_location("Artifact Extraction: Urn"), Has("Artifact Unlock: Urn"))
    world.set_rule(world.get_location("Artifact Extraction: Golden Banana"), Has("Artifact Unlock: Golden Banana"))
    world.set_rule(world.get_location("Artifact Extraction: Shield"), Has("Artifact Unlock: Shield"))
    world.set_rule(world.get_location("Artifact Extraction: Chestplate"), Has("Artifact Unlock: Chestplate"))
    world.set_rule(world.get_location("Artifact Extraction: Golden Treasure"), Has("Artifact Unlock: Golden Treasure"))

def set_completion_condition(world: ClankWorld) -> None:
    world.set_completion_rule(HasAll(
        "Artifact Extraction: Ankh", "Artifact Extraction: Urn", "Artifact Extraction: Golden Banana", 
        "Artifact Extraction: Shield", "Artifact Extraction: Chestplate", "Artifact Extraction: Golden Treasure"
        ))