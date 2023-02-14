class UnoCard:

    COLOR_SUITS: tuple[str,...] = ('Red', 'Yellow', 'Green', 'Blue')
    WILD_SUIT: tuple[str] = ( 'Wild' ,) # Comma at the end tells Python this is a tuple
    SUITS: tuple[str,...] = COLOR_SUITS + WILD_SUIT

    COLOR_RANK_NAMES: tuple[str, ...] = ('0', '1', '2', '3', '4', 
                                         '5', '6', '7', '8', '9', 
                                         'Skip', 'Reverse', 'Draw 2')
    WILD_RANK_NAMES: tuple[str, ...] = ('', 'Draw 4')
    RANK_NAMES: tuple[str, ...] = COLOR_RANK_NAMES + WILD_RANK_NAMES
    _BOTTOM_RANK: int = 0
    _TOP_COLOR_RANK: int = len(COLOR_RANK_NAMES) - 1
    _TOP_RANK: int = len(RANK_NAMES) - 1
    _COLOR_RANKS: tuple[int, ...] = tuple(range(_TOP_COLOR_RANK + 1))
    _WILD_RANKS: tuple[int, ...] = tuple(range(_TOP_COLOR_RANK + 1, _TOP_RANK + 1))
    _RANKS: tuple[int, ...] = _COLOR_RANKS + _WILD_RANKS

