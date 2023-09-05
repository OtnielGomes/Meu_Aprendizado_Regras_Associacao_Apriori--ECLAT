import pandas as pd
from apyori import apriori

# Panda option to see all columns
pd.options.display.max_columns = None

# Pre-processing

marketplace_data = pd.read_csv('mercado2.csv', header=None)
transactions = []
for i in range(len(marketplace_data)):
    transactions.append([str(marketplace_data.values[i, j])
                         for j in range(marketplace_data.shape[1])])
# print(transactions)
# Definition of the rules:
# min_support >> Products that are sold 4 x per day
# 4 * 7 = 28 >>> 28/ 7501 = 0.003
rules = apriori(transactions,
                min_support=0.003,
                min_confidence=0.2,
                min_lift=3)
results = list(rules)
# print(results)
# print(len(results))
# print(results[2])
# print(results)
# print(results[2][0])
# print(results[2][1])
# print(results[2][2], '\n')

r = results[2][2]
A = []
B = []
support = []
confidence = []
lift = []

for result in results:
    s = result[1]
    result_rules = result[2]
    for result_rule in result_rules:
        a = list(result_rule[0])
        b = list(result_rule[1])
        c = result_rule[2]
        l = result_rule[3]
        print(f'If >> {a} Then >> {b} >> Confidence {c} >> Lift {l}')
        A.append(a)
        B.append(b)
        support.append(s)
        confidence.append(c)
        lift.append(l)

rules_df = pd.DataFrame({'A': A,
                         'B': B,
                         'Support': support,
                         'Confidence': confidence,
                         'Lift': lift})
rules_df = rules_df.sort_values(by='Lift', ascending=False)
rules_df.to_csv('Results_M2_data.csv')

# visualization
print('\n\n\n')
rules_data = pd.read_csv('Results_M2_data.csv', header=None)
print(rules_data)
