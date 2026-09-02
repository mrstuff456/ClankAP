from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle


class TestToggle(Toggle):
    """
    This is a test toggle
    """
    display_name = "Test Toggle"


class TestRange(Range):
    """
    this is a test range    
    """
    display_name = "Test Range"
    range_start = 0
    range_end = 100
    default = 50


class TestChoice(Choice):
    """
    this is a test choice
    """
    display_name = "Test Choice"

    option_one = 0
    option_two = 1
    option_three = 2


@dataclass
class ClankOptions(PerGameCommonOptions):
    test_toggle: TestToggle
    test_range: TestRange
    test_choice: TestChoice