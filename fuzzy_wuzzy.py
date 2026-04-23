from fuzzywuzzy import fuzz

str1 = 'But I have promises to keep, and miles to go before I sleep.'
str2 = 'But I have many promises to keep, and miles to run before sleep.'

str3 = 'California, USA'
str4 = 'California'


ratio1 = fuzz.ratio(str1, str2)



ratio2 = fuzz.ratio(str3, str4)
partial_ratio2 = fuzz.partial_ratio(str3, str4)


token_set_ratio = fuzz.token_set_ratio(str3, str4)

print(f"Similarity Ratio: {ratio1:.2f}")

print(f"Similarity Ratio: {ratio2:.2f}")
print(f"Partial Similarity Ratio: {partial_ratio2:.2f}")
print(f"Token Set Similarity Ratio: {token_set_ratio:.2f}")