from typing import List
import time

test_data = "Day_8/testinput.txt"
real_data = "Day_8/input.txt"

file = real_data

def get_num(letters : str) -> int:
    letters = "".join(sorted(letters))
    if letters == "abcefg": return "0"
    if letters == "cf" : return "1"
    if letters == "acdeg" : return "2"
    if letters == "acdfg" : return "3"
    if letters == "bcdf" : return "4"
    if letters == "abdfg" : return "5"
    if letters == "abdefg" : return "6"
    if letters == "acf" : return "7"
    if letters == "abcdefg" : return "8"
    if letters == "abcdfg" : return "9"


def map_letters(input : List[str]) -> None:
    input = list(map(set, input))
    a, b, c, d, e, f, g = [''] * 7
    one, four, seven, eight = '', '', '', ''
    for num in input:
        if len(num) == 2:
            one = num
        if len(num) == 4:
            four = num
        if len(num) == 3:
            seven = num
        if len(num) == 7:
            eight = num
    a = list(seven.difference(one))[0]
    cf = one
    bd = four.difference(one)
    eg = eight.difference(four | {a})
    for s in input:
        if s.issuperset(eg | bd | {a}) and len(s) ==6:
            f = list(s.difference(eg | bd | {a}))[0]
            c = list(one.difference(f))[0]
    for s in input:
        if s.issuperset(eg | {c} |{a}) and len(s)  == 5:
            d = list(s.difference(eg | {c} |{a}))[0]
            b = list(bd.difference(d))[0]
    for s in input:
        if s.issuperset(set([a,b,d,f])) and len(s) == 5:
            g = list(s.difference(set([a,b,d,f])))[0]
            e = list(eg.difference(g))[0]
    return {
        a : "a",
        b : "b",
        c : "c",
        d : "d",
        f : "f",
        e : "e",
        g : "g"
    }



def part_one():
    counter = 0 
    with open(file, "r") as f:
        for line in f.readlines():
            input, output = tuple(line.replace("\n", "").split("|"))
            output = output.split(" ")[1:]
            for w in output:
                if len(w) in [2,3,4,7]:
                    counter+=1

    print(f"Part One {counter}")


def part_two():
    sum = 0
    with open(file, "r") as f:
        for line in f.readlines():
            input, output = tuple(line.replace("\n", "").split("|"))
            input = input.split(" ")[: -1]
            output = output.split(" ")[1: ]
            mapping = map_letters(input)
            num = ""
            for seq in output:
                new_seq = ""
                for char in seq:
                    new_seq += mapping[char]
                num += get_num(new_seq)
            sum += int(num)
    print(f"Part Two {sum}")

part_one()
part_two()