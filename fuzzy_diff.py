from difflib import SequenceMatcher as SM

str1 = "But I have promises to keep, and miles to go before I sleep."
str2 = "But I have many promises to keep, and miles to run before I sleep."

similarity_ratio = SM(isjunk=None, a=str1, b=str2).ratio() 
print(f"Similarity Ratio: {similarity_ratio:.2f}")
