import re, math
from collections import Counter
WORD = re.compile(r'\w+')
def checkans(ans,oans):
     def get_cosine(vec1, vec2):
          intersection = set(vec1.keys()) & set(vec2.keys())
          numerator = sum([vec1[x] * vec2[x] for x in intersection])
          sum1 = sum([vec1[x]**2 for x in vec1.keys()])
          sum2 = sum([vec2[x]**2 for x in vec2.keys()])
          denominator = math.sqrt(sum1) * math.sqrt(sum2)
          if not denominator:
             return 0.0
          else:
             return float(numerator) / denominator
     def text_to_vector(text):
          words = WORD.findall(text)
          return Counter(words)
     text1 = ans
     text2 = oans
     vector1 = text_to_vector(text1)
     vector2 = text_to_vector(text2)
     cosine = get_cosine(vector1, vector2)
     print ('Cosine:', cosine)
     omark = cosine * 10
     return cosine



def calculate_similarity(text1, text2):
    distance = Levenshtein.distance(text1, text2)
    similarity_score = 1 - (distance / max(len(text1), len(text2)))
    return similarity_score