import hashlib
from hashlib import hash_file
import difflib
from difflib import SequenceMatcher
def fileEquals(file1, file2):
    hash1 = hash_file('sha256', file1)
    hash2 = hash_file('')