
(sec:model)=
# Model 

<hr style="height:4px; background-color:black; border:none;">

<br>

We pose the problem of a fictitious social planner who considers the
trade-off between using land for agriculture and nurturing or preserving
forests that function as carbon sinks. This planner internalizes the
externalities resulting from deforestation. The planner's problem is
dynamic with explicit heterogeneity across regions in the Amazon. Guided
by empirical measurements, the regions have two important sources of
heterogeneity: i) agricultural productivity and ii) ability to absorb
atmospheric carbon.

Let $i$ denote a site index for $i=1,2,...,I$ where $I$ is the total
number of sites and $t \in [0,T]$ is the point in time. We use
superscripts to denote sites and subscripts to denote dates. We adopt
the notational convention that uppercase letters depict the actual state
and lowercase letters the potential state realizations. At date $t,$
<br>

$\begin{array}{llll}
Z_t &  \mathrel{\overset{\mathrm{def}}{=}}& (Z_t^1, Z_t^2, ..., Z_t^I) & \textrm{ vector of area used for agriculture expressed in hectares} \cr
X_t & \mathrel{\overset{\mathrm{def}}{=}}& (X_t^1, X_t^2, ..., X_t^I) & \textrm{ vector of carbon captured expressed in Mg CO2e (CO2 equivalent)  } \cr
A_t & \mathrel{\overset{\mathrm{def}}{=}}& (A_t^1, A_t^2, ..., A_t^I) & \textrm{ vector of agricultural output} 
\end{array}$
<br>

We use the notation
$Z \mathrel{\overset{\mathrm{def}}{=}}\left\{Z_t: 0 \le t \le T\right\}$
to denote the corresponding process that evolves over time, and
similarly for other states and controls. In our base model, the single
aggregate state variable is $P^a_t,$ an index of cattle prices in Brazil
expressed in 2017 US dollars.[^2]

The state vector $Z_t$ is subject to an instant-by-instant and
coordinate-by-coordinate constraint: 

$\begin{gather*}
0 \le Z_t^i \le {\bar z}^i
\end{gather*}$

where ${\bar z}^i$ is the amount of land in the Amazon biome available
for agriculture at site $i$.[^3] Let ${\dot Z}_t$ be the time derivative
of $Z$ at date $t$.

The evolution of $X^i$ introduces an important asymmetry into our
problem. We write a "linear" version of this problem by introducing two
site-specific, scalar, non-negative control variables for our fictitious
planner, $U_t^i$ and $V_t^i$, that distinguish positive from negative
movements in the derivative of $Z_t^i:$ 

$$
\dot Z_t^i = U_t^i - V_t^i $$ (eq:z)

The site-specific state variable process
$X^i$ evolves as: 

$$
{\dot X}_t^i  = - \gamma^i U^i_t - \alpha \left[ X_t^i - \gamma^i  \left( {{\bar z}^i - Z_t^i }  \right) \right] $$ (eq:x)

where the parameters satisfy: $\gamma^i > 0, \alpha >0,$ for
$i=1,2,..., I.$ The first term on the right side of
{eq}`eq:x` connects
deforestation to a loss in captured carbon. The site-specific parameter
$\gamma^i> 0$ denotes the density of CO2e that is present in a primary
forest in site $i$.[^4] The next term expresses the growth in captured
CO2e, when the size of the forest in site $i$ is held constant. The
mean-reversion coefficient $\alpha$ guarantees that if one lets the
forest grow undisturbed in a deforested area, it would reach
$100 [1 - \exp(-\alpha100 )]\%$ of the maximal captured CO2e in 100
years as in {cite:t}`heinrich2021large`. In our case, we choose $\alpha$ such
that $100[1 - \exp(-\alpha100)]= 99\%$. Notice that, holding constant
the deforested area, the amount of carbon in a site converges to
$\gamma^i$ per hectare of remaining forest. In Remark
[3](#rem:cs), we argue that at
the optimum, one of the controls is always zero, which introduces
additional binding constraints into the analysis. We write this
constraint as: $U^i_tV^i_t=0$.

We model cattle output as proportional to the land allocated to cattle
farming, 

$$A_t^i = \theta^i Z_t^i $$ (eq:vofag)

where $\theta^i$
is a site-specific productivity parameter.

All of the locations contribute to emissions via the capture of carbon
and emissions that result because of agricultural activity with a net
impact given by

$$\kappa \sum_{i=1}^I Z^i_t -  \sum_{i=1}^I \dot X_t^i, $$ (eq:e)

where parameter $\kappa$ captures the emissions that result because of
cattle farming.[^5] We include a cost of adjustment to changes in the
use of land with contributions from each site. It is measured by

$$\frac \zeta 2 \left [\sum_{i=1}^I \left(U_t^i + V_t^i \right)\right]^2.$$

Importantly, the adjustment cost depends on the aggregate change in land
use.

The price process $P^a$ for the agricultural output evolves exogenously
as an $n$-state Markov chain in continuous time with time-invariant
transitions. This process has an infinitesimal generator represented as
an intensity matrix ${\mathbb M}$ with non-negative entries off-diagonal
entries ${\sf m}_{\ell\ell'} \ge 0$ for $\ell' \ne \ell$ and diagonal
entries

$${\sf m}_{\ell \ell} = - \sum_{\ell' = 1, \ell' \ne \ell}^n {\sf m}_{\ell \ell'} .$$

The implied transition probability matrix over an interval of time
$\tau$ is $\exp\left( \tau {\mathbb M} \right)$ computed using a matrix
counterpart to a power series.

Since many carbon trading schemes are based on emissions, we assume that
the planner takes as given a price for carbon emissions $P^e,$ the
initial price for agriculture and the Markov process that describes the
future evolution of the price $P^a_t$ for cattle and maximizes

$$
     \mathbb E\left\{ \int_0^\infty \exp(-\delta t) \left[-P^e  \left (\kappa\sum_{i=1}^I Z^i_{t}- \sum_{i=1}^I \dot X^i_t \right)+  P^a_t  \sum_{i=1}^I \theta^i Z^i_{t}-\frac \zeta 2 \left (\sum_{i=1}^I (U_t^i + V_t^i) \right)^2 \right ] dt\right\}$$ (eq:POGo)

subject to equations {eq}`eq:z`-{eq}`eq:x`, and the control restrictions:

$$U_t^i \ge 0, \hspace{1cm} V_t^i \ge 0 \hspace{1cm} t \ge 0.$$ 
where
$\delta$ is the subjective discount rate. The exogenously specified
emissions price, $P^e,$ is an input into the analysis that allows us to
explore how costly it will be to make important changes in deforestation
outcomes in Brazil. Its magnitude reflects the sum of the marginal value
attributed by the planner to emission and any monetary transfers
obtained from others, such as sales in carbon emission markets. In the
computations that follow, we take this price to be fixed over time, but
in future work we intend $P^e$ to fluctuate over time.

````{prf:remark} 

The objective function
{eq}`eq:POGo` values
agricultural output by the value of sales, thus assuming that inputs to
production have no alternative use. This choice is dictated by a lack of
data on the cost of attracting or redeploying agricultural inputs, but
it biases the results in favor of agricultural use.
````


````{prf:remark}
The only explicit interaction across sites in objective
function {eq}`eq:POGo`
occurs through the adjustment costs. This interaction is intended to be
the result of a less than perfectly elastic supply of resources needed
for changing land use at the level of the whole Amazon. Additionally,
sites are spatially related by their similarity in productivities for
alternative ways to use the land. A more complex model would introduce
interactions across sites via non-linearities in the valuation of
agricultural output and/or emissions, an extension worthy of exploration
in future work.
````

(rem:cs)=
````{prf:remark}
To show that the controls $U^i_t$ and $V^i_t$ satisfy the
complementary slackness condition $U^i_tV^i_t=0$ for each pair $(i,t),$
it is easier to consider a discrete-time model. The proof for the
analogous result for the continuous-time case goes through by taking
limits. Suppose you take a point where the optimal trajectory involves
$\min\{U^i_t, V^i_t\}>\Delta>0.$ If the planner lowers both controls by
$\Delta,$ then at time $t$, one obtains an increase of $\Delta$ in
$X^i_t$ and lower emissions $\gamma^i \Delta$. Equation
{eq}`eq:x` implies that
$X^i_t$ would have a lower drift and converge over time to the
stationary solution. This in turn implies that the *sum* of future
emissions would increase by $\gamma^i \Delta.$ However since the rate of
discount is positive, the value of the problem would increase. Thus, an
optimal solution cannot involve simultaneously positive values for
$U^i_t$ and $V^i_t.$
````


````{prf:remark}
Optimization problem
{eq}`eq:POGo` does not
involve the stocks of (extended) carbon in the atmosphere generated by
activities in the Amazon biome. However, given emission trajectories
from the optimal solution, one could use geo-science inputs to inform
the mapping of emissions from the Brazilian Amazon and elsewhere into
carbon in the atmosphere to compute the impact on the evolution of
carbon stocks. This would require a much more comprehensive model that
is beyond the scope of this particular exercise.
````


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

[^2]: We choose cattle prices because, in recent years, more than 85% of
    deforested land is dedicated to cattle grazing - soybean, the
    largest crop in the region, accounts for about 8% of the farming
    land (Mapbiomas - www.mapbiomas.org).

[^3]: For calibration of this and the other parameters see Section
    [calibration](#sec:cal)

[^4]: For simplicity, equation [\[eq:x\]](#eq:x) assumes that all deforestation occurs in primary
    forest, what is not far from what has been observed in the Brazilian
    Amazon.

[^5]: About 75 percent of emissions from agricultural activity in the
    Amazon is the result of the natural digestive process of cattle.
    Another approximately 21 percent is from soil management. Thus for
    simplicity we assume that cattle herd per hectare does not vary and
    that productivity variations come mostly from transportation costs
    and carcass weights.
