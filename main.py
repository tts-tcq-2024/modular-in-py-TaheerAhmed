# main.py

from tests import test_number_to_pair, test_pair_to_number
from color_reference_manual import generate_reference_manual

if __name__ == '__main__':
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    print('All tests passed!')
    print('Reference Manual:')
    print(generate_reference_manual())
