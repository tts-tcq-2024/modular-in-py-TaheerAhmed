# reference_manual.py

from color_seggregation_logic import MAJOR_COLORS, MINOR_COLORS, color_pair_to_string

def generate_reference_manual():
    manual = []
    for i, major in enumerate(MAJOR_COLORS):
        for j, minor in enumerate(MINOR_COLORS):
            pair_number = i * len(MINOR_COLORS) + j + 1
            manual.append(f'{pair_number}: {color_pair_to_string(major, minor)}')
    return '\n'.join(manual)

if __name__ == '__main__':
    print(generate_reference_manual())
