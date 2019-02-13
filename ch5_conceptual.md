`page 197`

# Chapter 5

### Exercise 2
1. Probability that the first bootstrap observation is the $j$th observation from the original sample = $\dfrac{1}{n}$. So probaility that it isn't = $1 - \dfrac{1}{n}$
2. Because bootstrap sampling assumes independent and identically distributed samples, probability that second observation isn't $j$th observation is same as above.
2. Because of the i.i.d. assumption, all observations have equal change of *not* being selected. Therefore, by the product rule or $n$ observations, we have = $\left(1 - \dfrac{1}{n}\right)^n$
2. $P(\text{in the sample}) = 1 - P(\text{not in sample}) = 1 - (1 - 1/5)^5 = 67.2\%$
2. $P(\text{in the sample}) = 1 - P(\text{not in sample}) = 1 - (1 - 1/100)^{100} = 63.4\%$
2. $P(\text{in the sample}) = 1 - P(\text{not in sample}) = 1 - (1 - 1/10000)^{10000} = 63.2\%$

### Exercise 3
1. Data is split into non-overlapping $K$ parts. The model is trained on the $1 - K$ parts of the data validatd on the $k$th part. This is done $K$ times.
2. Validation set approach: Advantage of $k$-fold CV over this approach is that the entire dataset is utilized for training and testing, thereby giving error estimates that are closer to true error rates.
2. LOOCV: Advantage of $k$-fold CV over this approach is that LOOCV is computationaly intensive. Also $k$-fold CV has less variance but higher bias than LOOCV (although both are sort of in the middle ground).

### Exercise 4
Bootstrap can be used to achieve this. Data is repeatedly sampled $Z$ times with replacement. Model is fit to each sample and errors rates are output for each $Z$.
