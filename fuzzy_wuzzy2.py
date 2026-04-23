from fuzzywuzzy import fuzz
import Levenshtein as levenshtein
from fuzzywuzzy import process

str_list = ['Joseph Biden', 'Joe Biden','Joseph R Biden']

str1 = 'But I have promises to keep, and miles to go before I sleep.'
str2 = 'But I have many promises to keep, and miles to run before sleep.'

#Simple Ratio
simple_ratio = fuzz.ratio("fuzzy was a bear", "fuzzy fuzzy was a bear")

#Simple Partial Ratio
partial_similarity_ratio = fuzz.partial_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear")

#Token Set Ratio
fuzz_token_set_ratio = fuzz.token_set_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear")

#Token Sort Ratio
fuzz_token_sort_ratio = fuzz.token_sort_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear")

#Partial Token Sort Ratio
partial_token_sort_ratio = fuzz.partial_token_sort_ratio("fuzzy was a bear", "wuzzy duzzy was a bear")

#partial Token Set Ratio
partial_token_set_ratio = fuzz.partial_token_set_ratio("fuzzy was a bear", "wuzzy duzzy was a bear")

#Levenshtein Ratio and Distance
levenshtein_similarity_ratio = levenshtein.ratio(str1, str2)
levenshtein_edit_distance = levenshtein.distance(str1, str2)

#Process Extract and ExtractOne ratios
match_ratios = process.extract('joe r biden', str_list, scorer=fuzz.token_sort_ratio)
best_match = process.extractOne('joe r biden', str_list, scorer=fuzz.token_sort_ratio)

print(f"Simple Ratio: {simple_ratio:.2f}")

print(f"Simple Partial Ratio: {partial_similarity_ratio:.2f}")

print(f"Token Set Ratio: {fuzz_token_set_ratio:.2f}")

print(f"Token Sort Ratio: {fuzz_token_sort_ratio:.2f}")

print(f"Partial Token Sort Ratio: {partial_token_sort_ratio:.2f}")
print(f"Partial Token Set Ratio: {partial_token_set_ratio:.2f}")

print(f"Levenshtein Similarity Ratio: {levenshtein_similarity_ratio:.2f}")
print(f"Levenshtein Edit Distance: {levenshtein_edit_distance}")

print(f"Match Ratios: {match_ratios}")
print(f"Best Match: {best_match}")