

## Results with stochastic variation in agricultural prices

<hr style="height:4px; background-color:black; border:none;">

<br>

For our final set of results, we explore implications allowing for an
explicit randomness in the agricultural price process. We generate these
results using the MPC method described previously. To keep things
tractable, we have the social planner assume a two state Markov process
for the price process. We obtained the inputs into this specification by
estimating a hidden-state Markov process with Gaussian noise as we
describe in Appendix
[A.8](#appendixA). Of course, this is a rather substantial
reduction in the price stochastic structure of agricultural prices, but
it allows to engage in an initial explore of price randomness in a
tractable way. Under the two-state Markov chain, there are two price
realizations: $p^a = \$35.7, \$44.3.$ The implied annual transition
probabilities for staying put in each state are: .71 for the low state
and .83 for the high state.[^2] From Table
{ref}`tab:shadow_price` we see only a small, and not necessarily
very meaningful, drop in the business-as-usual price (\$6.9 instead of
\$7.1) once we introduce fluctuations in agricultural prices.[^3]

Table
{ref}`tab:valueObjectiveDecomposition_78sites_mpc` presents our
results for present values decompositions. In addition to reporting
three quantiles, for comparison we include results imposing constant
agricultural prices equal to the mean under the implied stationary
distribution. The notable outcomes are as follows. First, the variation
while evident for the business-as-usual case ($b = \$0$) is much less
consequential when $b = \$15$ and $b = \$25$ for the overall planner
value. It is proportionately similar for the agricultural contribution
to the value for all three choices of $b$. Second, imposing the mean as
a constant price gives quite an accurate approximation to the median
response. In this sense, the stochastic specification for agricultural
prices only has modest impact on our results. Finally, Table
{ref}`tab:valueObjectiveDecomposition_78sites_mpc` in Appendix
[A.8](#appendixA) exhibits the transfer costs and again these
show only a modest impact of the presence uncertainty.



```{table}   Present-value decomposition with stochastic agricultural prices
:name: tab:valueObjectiveDecomposition_78sites_mpc
|                    | agricultural output value | net Transfers | forest Services | adjustment Costs | planner Value |
|--------------------|---------------------------|---------------|-----------------|------------------|---------------|
| $p^a$ =  |            stochastic               |               |                 |                  |
| b = \$0            |                           |               |                 |                  |
| 10\%               | 3.19                      | 0.00          | -1.07           | 0.06             | 2.10          |
| 50\%               | 3.30                      | 0.00          | -1.05           | 0.06             | 2.19          |
| 90\%               | 3.39                      | 0.00          | -1.03           | 0.06             | 2.27          |
| b = \$15           |                           |               |                 |                  |
| 10\%               | 0.24                      | 1.99          | 0.92            | 0.19             | 2.97          |
| 50\%               | 0.26                      | 2.00          | 0.92            | 0.19             | 2.99          |
| 90\%               | 0.27                      | 2.00          | 0.92            | 0.19             | 3.00          |
| b = \$25           |                           |               |                 |                  |
| 10\%               | 0.16                      | 3.48          | 0.96            | 0.27             | 4.33          |
| 50\%               | 0.18                      | 3.48          | 0.96            | 0.28             | 4.34          |
| 90\%               | 0.19                      | 3.48          | 0.96            | 0.28             | 4.35          |
| $p^a$ =     |           \$41.1                 |               |                 |                  |
| b = 0              | 3.31                      | 0.00          | -1.10           | 0.06             | 2.14          |
| b = 15             | 0.26                      | 2.02          | 0.95            | 0.17             | 3.06          |
| b = 25             | 0.17                      | 3.54          | 1.00            | 0.26             | 4.45          |
```

<br>

<br>

**Remark 1**. *One possible way to amplify the models impact of making
agricultural prices stochastic is to introduce specification uncertainty
into the analysis. {cite:t}`Anderson2003` propose a recursive way to make this
adjustment by using a relative entropy divergence to form penalties that
limit the potential misspecifications that are explored by the planner.
Thus the MPC approach could potentially be extended to incorporate this
extension, opening the door to greater adjustments for uncertainty.*


<br>
<hr style="height:4px; background-color:black; border:none;">



[^2]: Appendix [A.8](#appendixA) gives results for a second estimation of
    the hidden-state Markov process in which Gaussian shock variances
    are constrained to be the same. In this case, both realized states
    are lower and most of the time is spent in the higher of the two
    states.

[^3]: To construct the business-as-usual price for emissions when the
    agricultural prices are stochastic, we used the smoothed
    probabilities reported in left panel of Figure
    [15] in Appendix
    [A.8](#appendixA) to assign the discrete states in our
    computations. While we used a probability .5 threshold for this
    assignment, many of the probabilities are actually close to zero or
    one.
