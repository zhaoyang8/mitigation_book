(sec:pu)=
## Solution with parameter ambiguity aversion 

<hr style="height:4px; background-color:black; border:none;">

<br>

For solving the robustly optimal problem numerically, we take an
iterative approach, supported by the Min-max Theorem. Specifically, we
proceed as follows:

i)  Given a $g$, we solve the maximization problem for a candidate $d.$
    We ignore the relative entropy penalty term in this solution.

ii) For a given ${ d}$, we solve
    the minimization problem with the relative entropy penalization to
    obtain a new candidate for $g^*.$

iii) We repeat the steps until we achieve convergence.

Our computations in step ii) will exploit the quasi-analytical formula for
$g^*$ given in {eq}`minimizer`. We take as given a decision process, $d$, and
evaluate the discounted objective to obtain the numerator for
{eq}`minimizer`. The denominator, however, must be computed
numerically. Here we use a Monte Carlo method that was originally
developed for computing Bayesian posteriors. This method is based on
Hamiltonian dynamics and is often more computationally efficient for
high-dimensional problems than the familiar Metropolis-Hastings method.
See, for instance, {cite:t}`neal2011` and {cite:t}`carpenter2017`, with software
support given by {cite:t}`standev2018stancore`.[^2] See Appendix
[D](#sec:appendixD) for
more details.

<br>
<hr style="height:4px; background-color:black; border:none;">

[^2]: From a mathematical standpoint, this calculation is equivalent to
    computing a Bayesian posterior where $- \frac 1 \xi f(d, \beta)$
    plays the role of a log-likelihood function and $\pi$ plays the role
    of a prior. As noted in Remark
    [4.3](#conjugate), for programming simplicity, we worked
    with an augmented parameter space when computing the distribution of
    interest.