#!/usr/bin/env python

from collections import Counter
from functools import cmp_to_key

pran = Counter('sagarprachi')


def matchfn(name):
    return sum((Counter(name) - (Counter('sagarprachi'))).values()) == 0 and (len(name) >= 4 and len(name) <= 6)

def sort_key(name):
  lowercase = name.lower()
  vowel_counts = {}
  for vowel in "aeiou":
      count = lowercase.count(vowel)
      vowel_counts[vowel] = count
  return (len(lowercase), sum(vowel_counts.values()))


with open('boynames.txt', 'r') as myfile:
    data = myfile.read().split("\n")

data = filter(lambda x: matchfn(x), data)
data = sorted(data, key=sort_key)

with open('boynamesranked.txt', 'w') as myfile:
    for name in data:
        myfile.write("{}\n".format(name))
