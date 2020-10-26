import pandas
import matplotlib.pyplot as plt
from numpy import percentile, sqrt
from statistics import *
from pandas import 


df = pandas.read_csv('CancerRisk.csv')
gender_calories = [[], []]

for i in range(len(df)):
    if df['Gender'][i] == 1:
        gender_calories[0].append(df['Calories'][i])
    else:
        gender_calories[1].append(df['Calories'][i])


def confidence_interval(data, confidence=0.95):
    dist = NormalDist.from_samples(data)
    z = NormalDist().inv_cdf((1 + confidence) / 2.)
    h = dist.stdev * z / ((len(data) - 1) ** .5)
    return dist.mean - h, dist.mean + h


def get_stats(lst, label):
    quartiles = percentile(lst, [25, 50, 75])
    print('Min', label, 'calories:', min(lst))
    print('1st quartile:', quartiles[0])
    print('Mean', label, 'calories:', mean(lst))
    print('Median', label, 'calories:', median(lst))
    print('3rd quartile:', quartiles[2])
    print('Max', label, 'calories:', max(lst))
    print('Standard deviation:', stdev(lst))
    print('IQR:', quartiles[2] - quartiles[0])
    print('95% confidence interval:', confidence_interval(lst, 0.95))
    print('Margin of error:', 1.96 * stdev(lst) / sqrt(len(lst)))
    print('Sample size:', len(lst))


fig, ax = plt.subplots()
ax.boxplot(gender_calories)
plt.title('calorie consumption of genders')
plt.xlabel('gender')
plt.ylabel('calories')
plt.show()


groups = ['male', 'female']
for i in range(len(gender_calories)):
    get_stats(gender_calories[i], groups[i])
