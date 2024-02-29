# University Scores - Weighted Mean
# calculate your university average score with py

'''
className,score,CFU
classA,20,12
classB,30,6
'''

def weighted_avg_uni(score, cfu):
    numerator = sum([score[i]*cfu[i] for i in range(len(score))])
    denominator = sum(cfu)
    return round(numerator/denominator,2)

#weighted_avg_uni(score, cfu)
weighted_avg_uni(score=df_uni['score'], cfu=df_uni['CFU'])