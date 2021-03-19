def validate_coordinates(*coordinates):
    for coor in coordinates:
        for num in coor:
            if not isinstance(num, int):
                raise Exception(f'Coordinates must be integers: {coor}')
        if len(coor) != 2:
            raise Exception(f'Unexpected coordinates: {coor}')
        if max(coor) > 8 or min(coor) < 1:
            raise Exception(
                f'Coordinates cant be greater 8 and less than 1: {coor}')


def knight_beats_pawn(knight, pawn):
    """Function calculate can knight beat pawn from coordinates.

    Args:

        knight (tuple): Coordinates of knight.
        pawn (tuple): Coordinates of pawn.

    Returns:
        bool: True if knight beat pawn.

    """

    validate_coordinates(knight, pawn)
    dx = abs(pawn[0] - knight[0])
    dy = abs(pawn[1] - knight[1])
    return dx + dy == 3 and all((dx, dy))
