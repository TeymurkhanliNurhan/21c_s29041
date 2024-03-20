class InvalidRangeError(Exception):
    """"""
class SquareGenerator:

    def generate_squares( self,start, end):

        if end < start:
            raise InvalidRangeError("End value cannot be less than start value")

        squares = [x ** 2 for x in range(start, end + 1)]
        return squares