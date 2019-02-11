`page 168`

# Chapter 4

### Exercise 4
1. 10% on average.
2. 1% on average.
2. $0.10^{100} \times 100 = 10^{-98}\%$
2. As $p$ increases, observations that are geometrically near increase exponentially.
2. $p=N,l=0.10^{1/N}$

### Exercise 5
1. On training set, LDA and QDA will both perform well. On test set, LDA will outperform.
2. QDA will outperform in both.
2. As $n$ increases, QDA, being a more flexible method will better fit the test data. Variance is offest by larger sample size.
2. False. QDA for linear decision boundary will underperform as it won't be able to generalize on the test data after overfitting on the training data.

### Exercise 6
1. Using logistic function $p(X) = \dfrac{e^{\beta_0 + \beta_1X_1 + \beta_2X_2}}{1 + e^{\beta_0 + \beta_1X_1 + \beta_2X_2}}$ for $X = [40, \: 3.5]$, we get $p(X) = 37.8\%$ probability that this student will get an A.
2. Rearranging above function, we get **log odds** or **logit** transformation of $p(X)$: $\log\left(\dfrac{p(X)}{1-p(X)}\right) = \beta_0 + \beta_1X_1 + \beta_2X_2$. Plugging in the values, we get $X_2 = 50 \: \text{hours}$.

### Exercise 7
Bayes rule:  
$$p_k(X) = \dfrac{\pi_kf_k(x)}{\sum_{l=1}^{k}f_l(x)}$$.

Plugging in the density function for normal random variable (page 170), we get posterior probability $p_{\text{yes}}(4) = 75.2\%$ that observation $X = 4$ belongs to $K=\text{yes}$ class. See [here](https://blog.princehonest.com/stat-learning/ch4/7.html) for a working solution.

### Exercise 8

Odds caluclated with $\dfrac{p(X)}{1-p(X)}$. So **(a)** $27\%$ and **(b)** $0.19$.