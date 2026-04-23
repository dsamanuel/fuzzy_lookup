import Levenshtein as levenshtein

str1 = 'But I have promises to keep, and miles to go before I sleep.'
str2 = 'But I have many promises to keep, and miles to run before sleep.'

edit_distance = levenshtein.distance(str1, str2)
similarity_ratio = levenshtein.ratio(str1, str2)

print(f"Levenshtein Distance: {edit_distance}")
print(f"Similarity Ratio: {similarity_ratio:.2f}")  