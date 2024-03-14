
(sec:uncertainty)=
# Parameter uncertainty 

<hr style="height:4px; background-color:black; border:none;">

<br>

We treat parameter uncertainty probabilistically by starting with a
baseline subjective prior over the parameters. We form this baseline
"prior" conditioned on available data. Rather than assuming a full
commitment to this baseline distribution, we allow for some skepticism
in by exploring sensitivity to distributional changes. We limit the
scope of the sensitivity analysis by penalizing deviations from the
baseline prior using a relative entropy or Kullback-Leibler measure of
divergence. This divergence is well known to have convenient
mathematical and conceptual implications. We implement this sensitivity
analysis by converting our one-person maximization problem into a
two-player game where the sensitivity analysis is conducted via
minimization. This delivers a form of ambiguity aversion consistent with
two alternative representations of ambiguity aversion: smooth ambiguity
and variational preferences.[^2]

Our model is dynamic and Markovian. As such, it could be formulated from
the vantage point of an initial period or recursively. Even in the
absence of parameter uncertainty, we find it convenient computationally
to solve it from the perspective of an initial date. This makes it a
"static problem." We adopt this same static perspective to explore the
consequences of uncertainty. In contrast to the single-agent decision
theory, this has conceptual implications beyond just computational
considerations as the minimization is performed as well at the initial
date. In effect, we treat the two-player formulation as a static max-min
game where, as we noted, the minimizing player is used as a formal
device to explore the sensitivity to changes in the distribution over
parameters used in optimization.

We implement a static formulation of robustness to parameter uncertainty
as follows. For each site, we consider the parameter pair
$(\gamma^i, \theta^i)$ for $i=1,2,...,I.$ Let $\varphi$ denote full
parameter vector including all sites and hence of dimension
$2 \times I.$ We use a regression approach to construct baseline
estimates of the site-specific productivities given site attributes.
Each site may intersect multiple municipalities, and we write $M^i$ for
the set of municipalities that overlap site $i$. We construct
site-specific productivities using 

$$
 \begin{bmatrix} \gamma^i \cr \theta^i \end{bmatrix}
 = \begin{bmatrix} \sum_{m \in M^i} w_m^i \exp\left(  \beta_\gamma \cdot R_\gamma^m \right) \cr  \frac 1 {P^A_{2017}}\sum_{m \in M^i} w_m^i \exp\left( \beta_\theta \cdot R_\theta^m \right) \end{bmatrix}.$$ (productivity_construct)

In this regression, $R_\gamma^m$ is a vector of geographical variables
used to construct baseline estimates for the carbon-absorption
productivity for municipality, $m$. Similarly, $R_\theta^m$ is a vector
of such variables used to construct baseline estimates for the value of
agricultural output per hectare for the same municipality. $w_m^i$ is an
area-based weight of the importance of municipality $m$ in site $i,$ and
$P^A_{2017}$ is the price of cattle in 2017.

Uncertainty in the composite regression parameter vector,
$\beta' \mathrel{\overset{\mathrm{def}}{=}}({\beta_\gamma}', {\beta_\theta}'),$
induces uncertainty in the site-specific productivities,
$(\gamma^i, \theta^i)$ for $i = 1,2,...,I.$ The underlying dimension of
the uncertainty is given by the number of the unknown regression
parameters, which is substantially less than $2 \times I.$ This
reduction turns out to be important for implementation. We use a
regression method because we do not have direct evidence for each of the
site-specific productivities. Our productivity data are available at
different resolutions than the sites within our model. For these
reasons, we use attributes as right-hand side variables in the
regression and feed in site-specific attributes. Moreover, we use the
regression approach to fill in missing observations. Since the dependent
variables in the regressions are expressed in terms of logarithms, we
exponentiate the predictions implied by regressions.

We use historical evidence on land-use productivity to estimate the two
regression equations as functions of attributes. We impose a familiar
and convenient conjugate prior to produce a Bayesian posterior $\pi$,
for the $\beta'$s. See, for instance, {cite:t}`RS1961`. The unknown regression
coefficients are presumed to be normally distributed conditioned on the
regression-error variances and the regression-error variance are posited
to have an inverse gamma distribution. We use quasi-analytical formulas
to deduce posterior distributions for the regression predictions that we
use as baseline probability distributions for the site-specific
productivities.[^3] While the baseline distributions $\pi$ constructed
in this matter are "posterior" from the perspective of our regression
analysis, they play the role of a "prior" for the social planner acting
conditioned on data used in the regression analysis.[^4]

Our measure of divergence used to explore sensitivity restricts the
alternative probabilities to be absolutely continuous with respect to
the baseline distribution. With this restriction, it suffices to focus
on alternative distributions to the baseline specification for the
regression coefficients. This simplifies substantially the numerical
computations.


**Remark 1**. *An interesting extension could include a probabilistic
specification of heterogeneity in the productivity parameters not
captured by the regression formulation. This would add to the
computational burden as the sensitivity analysis would be over a
substantially larger space and would require a plausible probability
specification of the unobserved heterogeneity.*


Given the vector of regression parameters, $\beta,$ in a set,
${\mathcal B},$ we write $f(d, \beta)$ for the discounted utility
obtained from a sequence of decisions $d$ with implied productivity
parameters given by formula
{eq}`productivity_construct`. We abstract from uncertainty in
this calculation, but this could also be incorporated into the analysis.
We use a familiar relative entropy (or Kullback-Leibler) divergence
measure to capture ambiguity about the parameter distribution given by

$$\int_{\mathcal B} \log g(\beta) g(\beta) d \pi( \beta) \ge 0,$$ 

where
$g$ satisfies $\int g(\beta)  d\pi(\beta )= 1.$ Notice that the
non-negative (relative) density, $g,$ implies an alternative probability
distribution given by $g(\beta) d\pi(\beta).$ Preferences over
alternative decision sequences are given by:

$$\min_{g \ge 0, \int  g d\pi = 1} \int_{\mathcal B} \left[ f(d, \beta)  + \xi \log g(\beta)\right] g(\beta) d\pi(\beta),$$

for a penalty parameter $\xi > 0.$ For $\xi$ arbitrarily large, these
preferences are well approximated by expected utility preferences using
the baseline distribution $\pi.$

These preferences are recognizable as a special case of what are called
variational preferences for a static decision problem. The minimization
problem has a well-known quasi-analytical solution: 

$$
g^*(\beta) = \frac { \exp\left[ - \frac 1 \xi  f(d, \beta) \right]} {
\int_{\mathcal B} \exp\left[ - \frac 1 \xi  f(d, \beta) \right] d \pi(\beta)}$$ (minimizer)

with a minimized objective: 

$$
-\xi  \log \int_{\mathcal B} \exp\left[ - \frac 1 \xi  f(d, \beta) \right] d \pi(\beta).$$ (minimized_objective)

The minimizing $g$ given in
{eq}`minimized_objective` induces an "exponential tilt" of the
probabilities towards lower discounted utilities. The magnitude of $\xi$
determines the strength of this tilt. We shall refer to limiting
$\xi=\infty$ case as *ambiguity neutrality*. For this limit, the
decision problem uses the familiar expected utility objective:

$$\max_{\boldsymbol{d}}  \int_{\mathcal B} f({ d},  {\beta} )   g({\beta}) d\pi(\beta).$$


**Remark 2**. *The minimized objective given by
{eq}`minimized_objective` is a special case of a smooth ambiguity
objective, first suggested by {cite:t}`KlibanoffMarinacciMukerji:2005`. They
deduced a rationale for an ambiguity adjustment represented using a
concave function distinct from the one used for expressing risk
aversion. While they take such a concave adjustment to be a starting
point, we deduce a logarithmic-exponential representation from a
starting point motivated by robustness. Thus their axiomatic motivation
is different from the distributional robustness that interests us.*



**Remark 3**. *As posed, the minimization is over the marginal posterior
for the regression coefficients. With relative entropy divergence, we
may equivalently solve the minimization problem using the relative
entropy divergence over the conditional posterior distribution for the
regression coefficients and the marginal posterior for the
regression-error variances. We use this observation in our actual
calculations to simplify our algorithmic implementation.*


Given the parameter ambiguity adjustment, the implied decision problem
is a two-player zero-sum game. If we constraint the decision process $d$
to a convex set ${\mathcal D}.$

(prob:primal)=
**Problem 4**.

$$\max_{d \in {\mathcal D}} \min_{g \ge 0, \int g d\pi = 1}   \int_{\mathcal B} f({ d},  { \beta} )   g(\beta) d\pi(\beta) 
+ \xi \int_{\mathcal B} \log g(\beta ) g({\beta}) d\pi(\beta) .$$


For conceptual reasons, we switch order of maximization and
minimization.

(prob:reverse)=
**Problem 5**.

$$\min_{g \ge 0 , \int g d\pi = 1} \max_{ d \in {\mathcal D}}  \int_{\mathcal B} f({ d},  { \beta} )   g({\beta }) d\pi(\beta ) 
+ \xi \int \log g(\beta ) g({ \beta }) d\pi( \beta ) .$$


Under quite general conditions we may invoke the Max-min Theorem and
claim that the objective for Problems
[4](#prob:primal) and
[5](#prob:reverse) will
be same and the minimizing $g$ evaluated at the maximized $d$ for the
Problem [4](#prob:primal)
will agree with the minimizing $g$ from Problem
[5](#prob:reverse).
Similarly, the optimized decision processes will agree.

Consider the inner maximization for Problem
[5](#prob:reverse):

$$\max_{\boldsymbol{d}}  \int_{\mathcal B} f({ d},  {\beta} )   g({\beta}) d\pi(\beta)$$

where we are free to drop the relative entropy penalty as it does not
depend on the decision process ${ d}$. Provided that this inner problem
has a solution for the outer $g$ minimization, the planner is maximizing
against this particular (penalized) "worst-case probability." This
computation is of interest as a way to interpret the consequences of any
given choice of the penalty parameter $\xi$. Following a common practice
for robust Bayesian methods, we find it revealing to explore alternative
choices of $\xi$ and deduce their implications for the implied
worst-case probabilities.

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

[^2]: See {cite:t}`KlibanoffMarinacciMukerji:2005` for an initial axiomatic
    foundation for smooth ambiguity and
    {cite:t}`MaccheroniMarinacciRustichini:2006` for an axiomatic foundation
    for variational preferences. {cite:t}`MaccheroniMarinacciRustichini:2006`
    used {cite:t}`Hansen2001`'s application of relative entropy divergence as
    motivation for their work. See {cite:t}`HansenSargent:2023` for a recent
    analysis relating both preference formulations to statistical
    decision theory and robust control theory by embracing a different
    axiomatic perspective.

[^3]: See Appendix
    [\[appen:baseline\]](#appen:baseline){reference-type="ref"
    reference="appen:baseline"} for details

[^4]: Our static formulation of the two-player decision problem does not
    allow for the possibility of dynamic learning going forward. We
    abstract from this for computational tractability.
