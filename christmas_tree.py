import argparse
import random

#
# Print you Python Xmas tree :)
#
# python christmas_tree(10)
#
#      *
#     *@*
#    @*@**
#   **@@***
#  *@@***@@*
# @*@@*@*****
#      #
#
def print_christmas_tree(tree_base_size: int) -> None:

    tree_base_size = tree_base_size + 1 if tree_base_size % 2 == 0 else tree_base_size
    steps = 1
    whites = tree_base_size // 2

    while steps <= tree_base_size:
        decoration = [char for char in ('*' * steps)]
        for i in range(len(decoration) // 2):
            decoration[int(random.random() * len(decoration))] = '\033[31m@\033[0;0m'

        print(' ' * whites + ''.join(decoration))
        steps = steps + 2
        whites = whites - 1

    print(' ' * (tree_base_size // 2) + '\033[33m#\033[0;0m')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print an ASCII Christmas Tree')
    parser.add_argument("tree_base_size", metavar='N', type=int, help="size of tree base")
    args = parser.parse_args()

    print_christmas_tree(args.tree_base_size)
