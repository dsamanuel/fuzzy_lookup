### Fuzzy Lookup matching

- Fuzzy search is the process of finding strings that approximately match a given string.

- Let's check the main two fuzzy string matching algorithms in Python to compute similarity between pairs of strings.

##### Fuzzywuzzy
 - Fuzzywuzzy is a more feature-rich library for computing string similarity and performing fuzzy string matching in Python.
 - fuzzywuzzy has function for doing closest matching strings of a given string 
 - simple, simple partial, token-set, token-sort, partial-token-set, Process Extract and ExtractOne ratios

##### Levenshtein distance
- The Levenshtein distance between two strings is the number of deletions, insertions and substitutions needed to transform one string into another.
- Levenshtein Ratio and Distance
  
#### SequenceMatcher from difflib
- SequenceMatcher is available as part of the Python standard library. It uses the Ratcliff/Obershelp string matching algorithm which calculates the similarity metric between two strings as:
- Twice the number of matching (overlapping) characters between the two strings divided by the total number of characters in the two strings.
