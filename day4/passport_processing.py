from typing import List, Tuple

REQUIRED_COLOR_SET = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"}

POSSIBLE_EYE_COLOR = {
    "amb", "blu","brn","gry","grn","hzl", "oth"
}

def process_passports(passports, required_fields={"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}):
    res = 0
    for passport in passports:
        res += required_fields.issubset(set(passport.keys()))
    return res


def process_passports_value(passports, required_fields={"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}):
    res = 0
    for passport in passports:
        if required_fields.issubset(set(passport.keys())):
            valid = True
            for field in required_fields:
                value = passport[field]
                if not check_field(value, field):
                    valid = False
            res += valid
    return res

def check_field(value, field):
    try:
        if field =='byr':
            return len(value) == 4 and int(value) >= 1920 and int(value) <= 2002
        if field == "iyr":
            return len(value) == 4 and int(value) >= 2010 and int(value) <= 2020
        if field == "eyr":
            return len(value) == 4 and int(value) >= 2020 and int(value) <= 2030
        if field == "hgt":
            unit = value[-2:]
            if unit == "cm":
                value = int(value[:-2])
                return value >= 150 and value <= 193
            if unit == "in":
                value = int(value[:-2])
                return value >= 59 and value <= 76
        if field == "hcl":
            return value[0] == "#" and len(value) == 7 and set(value[1:]).issubset(REQUIRED_COLOR_SET)
        if field == "ecl":
            return value in POSSIBLE_EYE_COLOR
        if field == "pid":
            return len(value) == 9 and int(value)
    except:
        return False



def parse_passports(lines):
    passports = []
    passport = {}
    for line in lines:
        if not line:
            passports.append(passport)
            passport = {}
        else:
            field_dict = parse_line(line)
            passport.update(field_dict)
    return passports

def parse_line(line):
    field_dict = {}
    fields = line.split(" ")
    for field in fields:
        f, value = field.split(":")
        field_dict[f] = value
    return field_dict



if __name__ == "__main__":
    input_file = input("Enter your Input File path: ")
    with open(input_file) as f:
        passports = parse_passports(list(f.read().splitlines()))

    print("Part 1: ", process_passports(passports))
    print("Part 2: ", process_passports_value(passports))