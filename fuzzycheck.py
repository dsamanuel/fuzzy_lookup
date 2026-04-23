from nltk.metrics.distance import edit_distance

string1 = "apple"
string2 = "apples"
distance = edit_distance(string1, string2)
print(distance)