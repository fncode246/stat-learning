`page 120`

# Chapter 3

### Exercise 1
The null hypothesis is that either of the predictors (TV, sales, or radio) has no effect on sales while the remaining predictors are held constant. By looking at $p$-values, we can reject $H-0$ for `TV` and `radio`.

### Exercise 2
KNN classifier: uses nearest neighbor methods to classify a given new point as a group of its nearest neighbors, giving us a qualitative output (discrete).
KNN regression: uses same methods but outputs a quantitative response (continuous).

### Exercise 3
1. Can simply test this on a Spreadsheet. At lower `GPA`, females have higher salary than male. As `GPA` increases, male salary overtakes female salary.  => iii   
The interaction term `GPA x Gender` has a *given* negative coefficient: At smaller values of `GPA` with `Gender = 1` for female, this has negligble effect. But as `GPA` increases, This negative value becomes larger and larger. Think of it as a line with smaller slope that is being overtaken by another slope which is `Gender = 0` (does not have negative coeff).

2. $$ salary = 50 + 20 \times 4 + 0.07 \times 110 + 35 \times 1 + (0.01 \times 4 \times 110) + (-10 \times 4 \times 1) = 137.1$$

2. False, The interaction term works in pair with the base values. Particularly, the $p$-values of the interaction term must be examined to check for statistical significance. We can also test by adding and removing the interaction term to observe changes in accuracy metrics, e.g. MSE.

### Exercise 4
1. Training RSS will be lower with cubic regression even when true relationship is linear because the cubic regression is more flexible, thereby fits the data better (i.e. overfits the data).
2. Test RSS will be higher with cubic regression because this, after overfitting the data, now fails to generalize with unseen test data. Linear regression will give lower test RSS.
2. Cubic regression would still give lower training RSS because regardless of whether true relationship is linear or non-linear, the more flexible method will fit the data better.
2. Not enough information for the test case. If true relationship is linear, linear regression will have lower test RSS. But if non-linear, cubic regression will perform better.