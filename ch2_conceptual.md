`page 52`
# Chapter 2 

### Exercise 2
1. Inferential regression. Quantitative output of CEO salary based on firm's features. $n=500, p=3.$
2. Predictive classification. Binary prediction of `success` or `failure`. $n=20, p=13.$
2. Predictive regression. Percentage of exchange rate. $n=52, p=3.$



### Exercise 3
1. training error - decreaes monotonically as flexibility increases.
2. test error - U-shaped. First decreases as model is fitting data, then increases because susceptible to noise.
2. Bayes (irreducible) error rate - defined for classification problems. Measures errors for points that lie on the wrong side of decision boundary. No model can perfectly fit data because $\hat{f}$ is also a function of $Var(\epsilon)$ which is always greater than $0$. Training error lower than this means model is overfitting.
2. (squared) bias - decreases because flexible methods better capture real-world problems. 
2. variance - increases because flexible methods more susceptible to small changes in dataset.


### Exercise 5
A very flexible approach is better at capturing non-linear relationships in the data, and decreases bias.

The disadvantage of a very flexible approach is that it requries a large number of observations, and usually has high variance.

A more flexible approach is preferred when the interpretability of a model is not important and large data is available.

A less flexible approach is preferred for inference-based modeling.

### Exercise 6
Paramteric methods assume a specific form and reduce the task of estimating $f$ down to one of just estimating its set of parameters $\beta_p$ for $p$ predictor variables. This simplifies the task of finding $\hat{f}$. Non-paramteric methods do not make any such assumptions and instead try to fit the data as closely as possible without overfitting. Non-parametric methods, however, require a large number of $n$ observations.

Paramterics methods run the risk of *overfitting* because they require a greater number of parameters and, therefore, follow the noise too closely. Because they make assumptions on the form of $f$, it is possible that the estimate is very different from the true $f$.

### Exercise 7

Obs. | $X_1$ | $X_2$ | $X_3$ | $Distance(0, 0, 0)$ | $Y$
-----|-------|--------|------|---------------------|----
1    |  0    | 3      |   0  |   3                 | Red
2    |2    | 0      |   0  |   2                 | Red
3    |  0    | 1      |   3  |$\sqrt{10} \approx 3.2$| Red
4    |  0    | 1      |   2  |$\sqrt{5} \approx 2.2$| Green
5    |  -1   | 0    |   1  |$\sqrt{2} \approx 1.4$| Green
6    |  1    | 1      |   1  |$\sqrt{3} \approx 1.7$| Red

b. Green Observation #5 is closet to $K=1$  
c. Red. Observations #2, #5, and #6 are closest neighbors to $K=3$, two of which are red.
d. Small. Because smaller $K$ means decisions boundary is more flexible which can fit non-linearities closer.