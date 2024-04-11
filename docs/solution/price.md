
## Solution with price stochasticity under ambiguity neutrality

<hr style="height:4px; background-color:black; border:none;">

<br>

To account for stochastic prices in a tractable way, we construct an
approximate Markov chain with two states $P^a_\ell < P^a_h$ and
transitions that match the empirical transitions from monthly data.[^3]
When considering a stochastic evolution of prices, we find "Modified
Predictive Control" (MPC) methods (*e.g.* {cite:t}`ScokaertRawlings:1998`,
{cite:t}`Bemporadetal:2002`, {cite:t}`Thangaveletal:2018`) to be particularly suitable
for solving our planner's problem. Our MPC approximation is implemented
as follows.[^4] Given the current period, say date zero, we break the
future into two segments: a) an uncertainty horizon of say $\tau$ time
periods and b) the remaining $T- \tau$ time periods beyond this
uncertainty horizon for which we abstract from uncertainty. While the
cattle price distribution follows a Markov chain, to simplify our
computations, we set the prices in periods $\tau+1, \dots T$ equal to
the value that prevails at $\tau.$ Prior to date $\tau +1,$ we confront
randomness in this problem by imposing appropriate "measurability"
restrictions on the controls as functions of potentially realized
states. We then apply the interior point method to find the optimal
trajectory at zero given $P^a_0.$ We keep the optimal date $t=1$ states
computed at time $t=0$ and repeat. That is, we consider the problem
stating at $t=1$ with the new state vector and divide the future into
two segments: an uncertainty segment of length $\tau$ and a remaining
period of $T-\tau - 1.$ This step will determine an optimal state at
period 2. We continue this procedure to produce the optimal state at
periods 3, 4, \..., T supported by the corresponding optimal controls.

In practice, the dimensionality of the stochastic problem increases
geometrically as a function of the uncertainty horizon, $\tau.$
Consequently, this MPC method becomes tractable when the uncertainty
horizon can be relatively short and still obtain good approximations. We
determine an "adequate" uncertainty horizon $\tau^*$ by checking the
difference in the value of the problem $V(\tau)-V(\tau-1)$ for
$\tau = 0,1, \dots,\tau^*.$ In our coarse grid with 78 sites and price
randomness, we chose $\tau^*=5.$

Many of the results we will show entail projections into the future. We
report results based on two hundred simulated sequences of cattle
prices, $P^a_t,$ $t=1,\dots T,$ using the observed $P^a_0$ and the
calibrated Markov chain.

<br>
<hr style="height:4px; background-color:black; border:none;">


[^3]: See Appendix [A](#sec:appendixA) for details.

[^4]: Related computational approaches have been proposed by
    {cite:t}`CaiJuddSteinbacks:2017` and {cite:t}`CaiJudd:2023`.