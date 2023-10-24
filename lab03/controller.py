from model import MoveDirection

class OptionsParser:
    @staticmethod
    def parse(args):
        parsed_args = []

        for arg in args:
            if arg in MoveDirection.__members__:
                parsed_args.append(MoveDirection[arg].value)

        return parsed_args