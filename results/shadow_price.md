

## Shadow prices under business-as-usual

<hr style="height:4px; background-color:black; border:none;">

<br>

We infer a *shadow* value for the planner based on historical
experience. To obtain this value, we first choose an interval
$[\underline t,  \bar t]$ and then select a time invariant price for
emissions, denoted by $P^{ee},$ to match the aggregate deforestation
predicted by the model at a final observation period $\bar t.$ We let
$(X_{\underline t}^o, Z_{\underline t}^o)$ denote the initial observed
state vector. We also input the realized history of agricultural prices
$\{P^a_t: {\underline t}\le t \le {\bar t}\}.$ We then compute the
optimal trajectory for the state variables implied by our model for
alternative choices of $P^{ee}$ and find the choice of $P^{ee}$ that
matches the observed value of the aggregate deforestation at $\bar t$
:[^2] $\sum_{i=1}^I Z_{\bar t}^i.$

We use $\underline t=1995,$ the initial date for our price data and
$\bar t = 2008$ the announcement of the Amazon fund that would pay for
preservation projects in the Amazon, using money contributed mostly by
Norway.

The business-as-usual price, $P^{ee},$ depends on the model
specifications, as we document in Table
{ref}`tab:shadow_price`. For instance, since an increase in the
agricultural price makes cattle farming more productive, the
business-as-usual carbon price has to increase to achieve the same
deforestation outcome. Also, with more sites at a finer resolution, some
of the smaller sites will have agricultural productivities that are
relatively higher, increasing the incentive to deforest. As Table 
{ref}`tab:shadow_price` shows, the business-as-usual price is
larger when we have a finer partition of sites. Finally, uncertainty in
the productivity parameters leads to a smaller business-as-usual price
for reasons that will become clear in our subsequent discussion. In what
follows, we will consider solutions to the optimization problem starting
in 2017 and a discount rate of 2 percent.

We will explore implications when the planner uses $P^e=P^{ee}+b$ for
$b=0, 10,15, 20,$ and $25$ where $b$ represents transfers per ton of
*net* captured emissions to the planner. Specifically, when net
emissions total $E$ tons of CO$_2,$ the planner receives a transfer of
$bE$. Note that even $b=25$ corresponds to a social price that is low
when compared to the prevailing price of emissions in some regions of
the globe. The forces that lead to changes in shadow prices have a
direct and partially offsetting effect on deforestation. Consequently,
the implied optimal (or robustly optimal) trajectories for each choice
of $b$ will be less sensitive to the particular model specification.
Essentially, the same argument applies to changes in the subjective
discount rate.[^3]

```{table}  Business-as-usual prices
:name: tab:shadow_price

| number of sites | agricultural price | $\xi$    | carbon price ($P^{ee}$) |
|-----------------|--------------------|----------|-------------------------|
| 1043            | $p^a = 41.1$       | $\infty$ | 7.6                     |
| 78              | $p^a = 41.1$       | $\infty$ | 7.1                     |
| 78              | $p^a = 41.1$       | 1        | 5.3                     |
| 78              | stochastic         | $\infty$ | 6.9                     |
```



<br>
<hr style="height:4px; background-color:black; border:none;">

[^1]: We thank Pengyu Chen, Bin Cheng, Patricio Hernandez, João Pedro
    Vieira, Daniel (Samuel) Zhao for their expert research assistance
    and to Joanna Harris and Diana Petrova for their helpful comments
    and to Carmen Quinn for editorial assistance. Assunção's research
    was supported by the Climate-Policy Initiative-Brazil, Hansen's
    research was supported in part by the Griffin Applied Economics
    Incubator Project on Policy-making in an Uncertain World and by an
    EPIC/Argonne National Laboratory collaboration award, and
    Scheinkman's research was supported in part by the Columbia Climate
    School.

[^2]: We obtain a similar value if instead we minimize the norm of the
    vector
    $(\frac{X_{\bar t} - X^o_{\bar t}}{X^o_{\bar t}}, \frac{Z_{\bar t} - Z^o_{\bar t}}{Z^o_{\bar t}})$,

[^3]: Since emissions are a low duration asset relative to cattle, a
    larger discount rate implies less deforesting, thus lowering
    $P^{ee}$, approximating future trajectories for a given $b.$ In
    fact, our simulations show that future trajectories do not change
    much for each $b,$ when we move from 2 to 3 percent.
