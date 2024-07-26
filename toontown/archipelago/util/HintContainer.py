from dataclasses import dataclass
from typing import List

from toontown.archipelago.util.net_utils import NetworkItem


@dataclass
class HintedItem:
    destination: int    # The player that is receiving this item
    item: NetworkItem   # AP protocol definition of the item
    player_name: str    # Display name of the player who needs to check the location
    location_name: str  # Display name to show to the user for the location of the item
    found: bool         # If this item was found or not

    def __str__(self):
        return f"HintedItem<destination={self.destination}, item={self.item}, player_name={self.player_name}, location_name={self.location_name}, found={self.found}>"

    def similar(self, other: "HintedItem") -> bool:
        return (self.destination == other.destination and
                self.item.item == other.item.item and
                self.item.location == other.item.location and
                self.item.player == other.item.player)

    def to_struct(self):
        return [self.destination, list(self.item), self.player_name, self.location_name, self.found]

    @classmethod
    def from_struct(cls, struct):
        return HintedItem(struct[0], NetworkItem(*struct[1]), *struct[2:])


class HintContainer:

    def __init__(self, avId):
        self.avId = avId
        self.hints: list[HintedItem] = []

    def contains(self, other: HintedItem) -> bool:
        """
        Checks if a hint is too similar to another hint to be stored as a duplicate
        """
        return any(hint.similar(other) for hint in self.hints)

    def addHint(self, hint: HintedItem) -> bool:
        """
        Adds a new hint to the hint container
        Returns true if the hint was added, false otherwise
        """

        # If we already have this hint don't store it
        if self.contains(hint):
            return False

        self.hints.append(hint)
        return True

    def getHints(self) -> List[HintedItem]:
        return self.hints

    def getHintsForSlot(self, slot: int) -> List[HintedItem]:
        """
        Returns a list of hints that strictly only apply to a certain slot number
        """
        hints = []
        for hint in self.hints:
            # If the player this hint is for matches the slot, it is a valid hint
            if hint.destination == slot:
                hints.append(hint)
        return hints

    def getHintsForItem(self, item_id) -> List[HintedItem]:
        """
        Returns a list of hints that strictly only apply to a certain item ID
        """
        hints = []
        for hint in self.hints:
            if hint.item.item == item_id:
                hints.append(hint)
        return hints

    def getHintsForItemAndSlot(self, item_id: int, slot: int) -> List[HintedItem]:
        """
        A combination of getHintsForSlot and getHintsForItem
        """
        hints = []
        for hint in self.hints:
            if hint.item.item == item_id and hint.destination == slot:
                hints.append(hint)
        return hints

    def __str__(self):
        return f"HintContainer<avId={self.avId}, hints=[{self.hints}]>"

    def to_struct(self):
        """
        Returns a primitive version of this instance that is safe to send over astron
        """
        return [hint.to_struct() for hint in self.hints]

    @classmethod
    def from_struct(cls, avId, primitive_hints):
        """
        Returns a new instance of HintContainer given primitive version of an instance
        """
        container = cls(avId)
        for hint in primitive_hints:
            container.addHint(HintedItem.from_struct(hint))
        return container

