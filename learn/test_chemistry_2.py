# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

from chemistry import make_periodic_table, compute_molar_mass
from formula import parse_formula, FormulaError
from pytest import approx
import pytest

# These are the indexes of the elements in the periodic table.
ATOMIC_NUMBER_INDEX = 0
NAME_INDEX = 1
ATOMIC_MASS_INDEX = 2

def test_make_periodic_table():
    """Verify that the make_periodic_table function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the make_periodic_table function and store the returned
    # dictionary in a variable named periodic_table_dict.
    periodic_table_dict = make_periodic_table()

    # Verify that the make_periodic_table function returns a dictionary.
    assert isinstance(periodic_table_dict, dict), \
        "make_periodic_table function must return a dictionary: " \
        f" expected a dictionary but found a {type(periodic_table_dict)}"

    # Check each item in the periodic table dictionary.
    check_element(periodic_table_dict, "Ac", [89, "Actinium", 227])
    check_element(periodic_table_dict, "Ag", [47, "Silver", 107.8682])
    check_element(periodic_table_dict, "Al", [13, "Aluminum", 26.9815386])
    check_element(periodic_table_dict, "Ar", [18, "Argon", 39.948])
    check_element(periodic_table_dict, "As", [33, "Arsenic", 74.9216])
    check_element(periodic_table_dict, "At", [85, "Astatine", 210])
    check_element(periodic_table_dict, "Au", [79, "Gold", 196.966569])
    check_element(periodic_table_dict, "B", [5, "Boron", 10.811])
    check_element(periodic_table_dict, "Ba", [56, "Barium", 137.327])
    check_element(periodic_table_dict, "Be", [4, "Beryllium", 9.012182])
    check_element(periodic_table_dict, "Bi", [83, "Bismuth", 208.9804])
    check_element(periodic_table_dict, "Br", [35, "Bromine", 79.904])
    check_element(periodic_table_dict, "C", [6, "Carbon", 12.0107])
    check_element(periodic_table_dict, "Ca", [20, "Calcium", 40.078])
    check_element(periodic_table_dict, "Cd", [48, "Cadmium", 112.411])
    check_element(periodic_table_dict, "Ce", [58, "Cerium", 140.116])
    check_element(periodic_table_dict, "Cl", [17, "Chlorine", 35.453])
    check_element(periodic_table_dict, "Co", [27, "Cobalt", 58.933195])
    check_element(periodic_table_dict, "Cr", [24, "Chromium", 51.9961])
    check_element(periodic_table_dict, "Cs", [55, "Cesium", 132.9054519])
    check_element(periodic_table_dict, "Cu", [29, "Copper", 63.546])
    check_element(periodic_table_dict, "Dy", [66, "Dysprosium", 162.5])
    check_element(periodic_table_dict, "Er", [68, "Erbium", 167.259])
    check_element(periodic_table_dict, "Eu", [63, "Europium", 151.964])
    check_element(periodic_table_dict, "F", [9, "Fluorine", 18.9984032])
    check_element(periodic_table_dict, "Fe", [26, "Iron", 55.845])
    check_element(periodic_table_dict, "Fr", [87, "Francium", 223])
    check_element(periodic_table_dict, "Ga", [31, "Gallium", 69.723])
    check_element(periodic_table_dict, "Gd", [64, "Gadolinium", 157.25])
    check_element(periodic_table_dict, "Ge", [32, "Germanium", 72.64])
    check_element(periodic_table_dict, "H", [1, "Hydrogen", 1.00794])
    check_element(periodic_table_dict, "He", [2, "Helium", 4.002602])
    check_element(periodic_table_dict, "Hf", [72, "Hafnium", 178.49])
    check_element(periodic_table_dict, "Hg", [80, "Mercury", 200.59])
    check_element(periodic_table_dict, "Ho", [67, "Holmium", 164.93032])
    check_element(periodic_table_dict, "I", [53, "Iodine", 126.90447])
    check_element(periodic_table_dict, "In", [49, "Indium", 114.818])
    check_element(periodic_table_dict, "Ir", [77, "Iridium", 192.217])
    check_element(periodic_table_dict, "K", [19, "Potassium", 39.0983])
    check_element(periodic_table_dict, "Kr", [36, "Krypton", 83.798])
    check_element(periodic_table_dict, "La", [57, "Lanthanum", 138.90547])
    check_element(periodic_table_dict, "Li", [3, "Lithium", 6.941])
    check_element(periodic_table_dict, "Lu", [71, "Lutetium", 174.9668])
    check_element(periodic_table_dict, "Mg", [12, "Magnesium", 24.305])
    check_element(periodic_table_dict, "Mn", [25, "Manganese", 54.938045])
    check_element(periodic_table_dict, "Mo", [42, "Molybdenum", 95.96])
    check_element(periodic_table_dict, "N", [7, "Nitrogen", 14.0067])
    check_element(periodic_table_dict, "Na", [11, "Sodium", 22.98976928])
    check_element(periodic_table_dict, "Nb", [41, "Niobium", 92.90638])
    check_element(periodic_table_dict, "Nd", [60, "Neodymium", 144.242])
    check_element(periodic_table_dict, "Ne", [10, "Neon", 20.1797])
    check_element(periodic_table_dict, "Ni", [28, "Nickel", 58.6934])
    check_element(periodic_table_dict, "Np", [93, "Neptunium", 237])
    check_element(periodic_table_dict, "O", [8, "Oxygen", 15.9994])
    check_element(periodic_table_dict, "Os", [76, "Osmium", 190.23])
    check_element(periodic_table_dict, "P", [15, "Phosphorus", 30.973762])
    check_element(periodic_table_dict, "Pa", [91, "Protactinium", 231.03588])
    check_element(periodic_table_dict, "Pb", [82, "Lead", 207.2])
    check_element(periodic_table_dict, "Pd", [46, "Palladium", 106.42])
    check_element(periodic_table_dict, "Pm", [61, "Promethium", 145])
    check_element(periodic_table_dict, "Po", [84, "Polonium", 209])
    check_element(periodic_table_dict, "Pr", [59, "Praseodymium", 140.90765])
    check_element(periodic_table_dict, "Pt", [78, "Platinum", 195.084])
    check_element(periodic_table_dict, "Pu", [94, "Plutonium", 244])
    check_element(periodic_table_dict, "Ra", [88, "Radium", 226])
    check_element(periodic_table_dict, "Rb", [37, "Rubidium", 85.4678])
    check_element(periodic_table_dict, "Re", [75, "Rhenium", 186.207])
    check_element(periodic_table_dict, "Rh", [45, "Rhodium", 102.9055])
    check_element(periodic_table_dict, "Rn", [86, "Radon", 222])
    check_element(periodic_table_dict, "Ru", [44, "Ruthenium", 101.07])
    check_element(periodic_table_dict, "S", [16, "Sulfur", 32.065])
    check_element(periodic_table_dict, "Sb", [51, "Antimony", 121.76])
    check_element(periodic_table_dict, "Sc", [21, "Scandium", 44.955912])
    check_element(periodic_table_dict, "Se", [34, "Selenium", 78.96])
    check_element(periodic_table_dict, "Si", [14, "Silicon", 28.0855])
    check_element(periodic_table_dict, "Sm", [62, "Samarium", 150.36])
    check_element(periodic_table_dict, "Sn", [50, "Tin", 118.71])
    check_element(periodic_table_dict, "Sr", [38, "Strontium", 87.62])
    check_element(periodic_table_dict, "Ta", [73, "Tantalum", 180.94788])
    check_element(periodic_table_dict, "Tb", [65, "Terbium", 158.92535])
    check_element(periodic_table_dict, "Tc", [43, "Technetium", 98])
    check_element(periodic_table_dict, "Te", [52, "Tellurium", 127.6])
    check_element(periodic_table_dict, "Th", [90, "Thorium", 232.03806])
    check_element(periodic_table_dict, "Ti", [22, "Titanium", 47.867])
    check_element(periodic_table_dict, "Tl", [81, "Thallium", 204.3833])
    check_element(periodic_table_dict, "Tm", [69, "Thulium", 168.93421])
    check_element(periodic_table_dict, "U", [92, "Uranium", 238.02891])
    check_element(periodic_table_dict, "V", [23, "Vanadium", 50.9415])
    check_element(periodic_table_dict, "W", [74, "Tungsten", 183.84])
    check_element(periodic_table_dict, "Xe", [54, "Xenon", 131.293])
    check_element(periodic_table_dict, "Y", [39, "Yttrium", 88.90585])
    check_element(periodic_table_dict, "Yb", [70, "Ytterbium", 173.054])
    check_element(periodic_table_dict, "Zn", [30, "Zinc", 65.38])
    check_element(periodic_table_dict, "Zr", [40, "Zirconium", 91.224])


def check_element(periodic_table_dict, symbol, expected):
    """Verify that the actual element that came from the
    periodic_table_dict contains the same values as the
    expected element.

    Parameters
        symbol: a symbol for a chemical element
        expected: a list that contains the expected values for symbol
    Return: nothing
    """
    # Verify that symbol is in the periodic table dictionary.
    assert symbol in periodic_table_dict, \
        f'"{symbol}" is missing from the periodic table dictionary.'
    actual = periodic_table_dict[symbol]

    # Verify that the element's atomic number is correct.
    act_number = actual[ATOMIC_NUMBER_INDEX]
    exp_number = expected[ATOMIC_NUMBER_INDEX]
    assert act_number == exp_number, \
        f'wrong atomic number for "{symbol}": ' \
        f'expected {exp_number} but found {act_number}'

    # Verify that the element's name is correct.
    act_name = actual[NAME_INDEX]
    exp_name = expected[NAME_INDEX]
    assert act_name == exp_name, \
            f'wrong name for "{symbol}": ' \
            f'expected {exp_name} but found {act_name}'

    # Verify that the element's atomic mass is correct.
    act_mass = actual[ATOMIC_MASS_INDEX]
    exp_mass = expected[ATOMIC_MASS_INDEX]
    assert act_mass == approx(exp_mass), \
            f"wrong atomic mass for {exp_name}: " \
            f"expected {exp_mass} but found {act_mass}"


def test_parse_formula():
    """Verify that the parse_formula function works correctly.

    Parameters: none
    Return: nothing
    """
    # Call the make_periodic_table function
    # and verify that it returns a dictionary.
    periodic_table_dict = make_periodic_table()
    assert isinstance(periodic_table_dict, dict), \
        "make_periodic_table function must return a dictionary: " \
        f" expected a dictionary but found a {type(periodic_table_dict)}"

    # Call the parse_formula function and
    # verify that it returns a list.
    sym_quant_list = parse_formula("H2O", periodic_table_dict)
    assert isinstance(sym_quant_list, list), \
        "parse_formula function must return a list: " \
        f" expected a list but found a {type(sym_quant_list)}"

    # Call the compute_molar_mass function four times and
    # verify that it returns the correct number each time.
    assert parse_formula("H2O", periodic_table_dict) \
            == [("H",2), ("O",1)]
    assert parse_formula("C6H6", periodic_table_dict) \
            == [("C",6), ("H",6)]
    assert parse_formula("(C2(NaCl)4H2)2C4Na", periodic_table_dict) \
            == [("C",8), ("Na",9), ("Cl",8), ("H",4)]

    # Call the parse_formula function six times, each time
    # with a different invalid chemical formula. Verify that
    # parse_formula function raises an exception each time.
    with pytest.raises(FormulaError):
        parse_formula("L", periodic_table_dict)
    with pytest.raises(FormulaError):
        parse_formula("4H", periodic_table_dict)
    with pytest.raises(FormulaError):
        parse_formula("H2L4", periodic_table_dict)
    with pytest.raises(FormulaError):
        parse_formula("-H", periodic_table_dict)
    with pytest.raises(FormulaError):
        parse_formula("(H2O", periodic_table_dict)
    with pytest.raises(FormulaError):
        parse_formula("H2)O3", periodic_table_dict)


def test_compute_molar_mass():
    """Verify that the compute_molar_mass function works correctly.

    Parameters: none
    Return: nothing
    """
    # Call the make_periodic_table function
    # and verify that it returns a dictionary.
    periodic_table_dict = make_periodic_table()
    assert isinstance(periodic_table_dict, dict), \
        "make_periodic_table function must return a dictionary: " \
        f" expected a dictionary but found a {type(periodic_table_dict)}"

    # Call the compute_molar_mass function
    # and verify that it returns a number.
    molar_mass = compute_molar_mass([["O",2]], periodic_table_dict)
    assert isinstance(molar_mass, int) or isinstance(molar_mass, float), \
        "compute_molar_mass function must return a number: " \
        f" expected a number but found a {type(molar_mass)}"

    # Call the compute_molar_mass function four times and
    # verify that it returns the correct number each time.
    assert compute_molar_mass([], periodic_table_dict) == 0
    assert compute_molar_mass([["O",2]], periodic_table_dict) \
            == approx(31.9988)
    assert compute_molar_mass([["C",6],["H",6]], periodic_table_dict) \
            == approx(78.11184)
    assert compute_molar_mass([["C",13],["H",16],["N",2],["O",2]],
            periodic_table_dict) == approx(232.27834)


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
