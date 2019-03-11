# t-test

The t-test, also called Student's T Test) compares two means and tells you if there is a significant difference between them, if the results are repeatable for an entire population and letting you know the probability of those results happening by chance. 

For example, you want to test the efficiency of a drug. You give the drug to a group of patient (patient group) and a placebo to another group (control group). You want to compare the average life expectancy between the two groups. 

1. What is a t-score ?

The t-score is the ratio between the difference between two groups and the difference whithin the groups. A large t-score tells you that the groups are different. A small t-score tells you that the groups are similar. When you run a t test, the bigger the t-value, the more likely it is that the results are repeatable.

2. What are T-Values and P-values ?

Every t-value has a p-value to go with it. A p-value is the probability that the results from your sample data occurred by chance. P-values are from 0% to 100%. For example, a p-value of .05 means there is only a 5% probability that the results from an experiment happened by chance. 

3. Type of t-tests ?

There are three main types of t-test:
- An Independent Samples t-test compares the means for two groups.
- A Paired sample t-test compares means from the same group at different times.
- A One sample t-test tests the mean of a single group against a known mean.

4. Calculate the t-statistic 

![alt text](https://github.com/xaviervasques/t-test/blob/master/Images/formula.png)

where M is the mean of each group, n the number of scores per group, S is the standard deviation. 

We also have to choose alpha, typically 0.05. This means that there is 95% confidence that the conclusion of the test will be valid. The degree of freedom can be calculated by the the following formula: df = nx + ny -2 

We therefore use a table to calculate the critical t-value:

![alt text](https://github.com/xaviervasques/t-test/blob/master/Images/table.png)

5. Compare the critical t-values with the calculated t statistic

If the calculated t-statistic is greater than the critical t-value, the test concludes that there is a statistically significant difference between the two populations. Therefore, you reject the null hypothesis that there is no statistically significant difference between the two populations.

In the t-test comparing the means of two independent samples, the following assumptions should be met:

Mean of the two populations being compared should follow a normal distribution. This can be tested using a normality test, such as the Shapiro–Wilk or Kolmogorov–Smirnov test, or it can be assessed graphically using a normal quantile plot.

The two populations being compared should have the same variance (testable using F-test, Levene's test, Bartlett's test, or the Brown–Forsythe test; or assessable graphically using a Q–Q plot). If the sample sizes in the two groups being compared are equal, Student's original t-test is highly robust to the presence of unequal variances. Welch's t-test is insensitive to equality of the variances regardless of whether the sample sizes are similar.

6. How to use it

Install numpy and scipy

pip install numpy

pip install scipy
    
Fill the data of your groups in a and b variables

Use ttest.py or ttest_scipy.py to use sciPy package 

python ttest.py

Source

https://towardsdatascience.com/inferential-statistics-series-t-test-using-numpy-2718f8f9bf2f

https://en.wikipedia.org/wiki/Student%27s_t-test

