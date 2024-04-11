

# Introduction

<hr style="height:4px; background-color:black; border:none;">

<br>

This paper investigates the potential social gains of designing prudent
policies that combat deforestation in the Brazilian Amazon through the
lens of a spatial and dynamic model. We build the model to capture the
trade-off between agricultural production[^2] and forest preservation or
regeneration.

The Amazon forest contains $123\pm31$ billion tons of captured carbon
that can be released into the atmosphere, equivalent to the historical
cumulative emissions of the United States
({cite:t}`malhi2006theregionalvariation`, {cite:t}`friedlingstein2022global`). The
Brazilian Amazon occupies $60\%$ of the 2.7 million square miles that
comprise the Amazon. From 1985 to 2021, the agricultural area in the
Brazilian Amazon increased from 68.6 to 240.5 thousand square miles. The
associated deforestation, comprising an area the size of Texas, has
resulted in high emissions, setting the Brazilian Amazon as a
substantial outlier in a plot of countries' emissions per-capita *vs.*
GDP per-capita. (see [Figure
1](#fig:k))

```{figure} ../aux_input/scatter_emission_gdp_log.png
---
name: fig:K
---
Each dot represents a country in 2018, except for the
European Union and the Brazilian Amazon. Highlighted letters stand for
(C)hina, (I)ndia, (E)uropean Union, and (U)nited States. Sources: World
Bank Data, downloaded on March 2021; Fatos da Amazônia 2021
(www.amazonia2030.org).
```

We use our model of the Brazilian Amazon to provide insights into
structuring policy improvements that realign economic incentives for
allocating land use. We make the model quantitative through the use of
detailed spatial information from multiple data sets. Our data document
large cross-sectional variability in cattle farming productivity and in
the potential absorption of carbon in the Brazilian Amazon. This
heterogeneity highlights the importance of incorporating a spatial
dimension in the model. To account for these locational differences, we
divide the Amazon region into various sub-regions or sites, each of
which has its own capacity to support agriculture and forestry. While
the model has considerable cross-sectional richness, it is nevertheless
highly stylized for reasons of tractability and transparency.

We pose the model in continuous time. The cross-sectional heterogeneity
in productivities and the natural state constraints on the land
allocation preclude standard recursive methods for solving the
associated Hamilton-Jacobi-Bellman (HJB) equations. Instead, we use and
extend methods from Modified Predictive Control (MPC) that were
originally developed in control theory and engineering to study
multi-plant production in real time. MPC methods approximate inequality
constraints on the states using what is called an interior point method.
They allow for uncertainty specified as a Markov process by
incorporating a shorter uncertainty horizon than the overall control
horizon as a means of approximation. We extend these methods to explore
subjective ambiguity from the standpoint of the social planner by making
a model-determined robustness adjustment to the subjective probabilities
for the unknown parameters. We are once again pushed to use a numerical
method, in this case a Markov chain Monte Carlo method based on
Hamiltonian dynamics. Such a method is particularly valuable for
high-dimensional problems and has substantial advantages over the
familiar Metropolis-Hastings approach. We use the Hamiltonian Markov
chain approach in a novel way to confront what is sometimes referred to
as "deep uncertainty" about productivity parameters. Alternatively, we
may interpret this treatment of subjective ambiguity as a robust
Bayesian formulation of the control problem of interest.

To set the stage for our analysis, we use the model to elicit an
estimate of the shadow price for emissions revealed by the deforestation
during 1995-2008. The year 1995 is the first date at which we have
reliable price data on cattle prices.[^3] The year 2008 marks the
beginning of the Amazon Fund, financed primarily by the Norwegian and
German governments.[^4] We use the inferred shadow price for simulations
designed to capture "business-as-usual." We also use this shadow price
to measure the value for Brazilians of the "forest services" provided by
preserved areas. These services include climate services as well as the
economic value of production that occurs without destroying the Amazon
forest.[^5]

We study the impact of adding outside payments for *net* capture of
CO$_2$ in the Amazon. We produce results in three steps. In step one, we
construct the finest grid by considering 1043 sites in the Amazon biome
with each measuring 67.5km$\times$ 67.5km. For this level of detail, we
produce results without accounting for uncertainty in the price of
agricultural output. Instead, we impose that the price corresponds to
the (stationary) average of the two-state Markov process we fit to the
observed agricultural prices. We also use these deterministic solutions
to ascertain whether and by how much Brazil would gain if the country
signed an agreement for a set of hypothetical dollar transfers per net
ton of CO$_2$ captured. Our model output shows the overall social gains
to reallocating production in the cross-section, including the option to
preserve or enhance the Brazilian rain forest.

In the second step, we consider 78 sites, each of which is
270km $\times$ 270km. For this level of aggregation, we
produce results that take into account stochastic changes in the price
of agricultural output as well as, for comparison, deterministic results
for this 78-site resolution. The results are quite close, showing that
our stochastic representation of externally determined agricultural
prices plays a minor role in the analysis.

Central to our analysis, we allow the productivities for carbon
absorption and agriculture to be site-specific. Estimates of these
crucial productivity parameters are subject to non-trivial uncertainty.
Moreover, while we have cross-sectional data that are informative, these
data do not give us direct measurements for the site-specific
productivities. Instead, we use regression methods to provide the inputs
needed for our analysis. Uncertainty in the regression coefficients
induces uncertainty in the implied site-specific productivity
parameters. The typical approach to uncertainty quantification explores
such parameter uncertainty from the perspective of an external analyst.
Instead, we incorporate this uncertainty explicitly into the decision
problem of our hypothetical social planner. While it is appealing to
address the parameter uncertainty probabilistically, there is ambiguity
as to what probabilities to impose.

In the third step, we explicitly consider parameter ambiguity from the
perspective of the social planner. We again use the less refined 78-site
partition of the Brazilian Amazon. We start with a baseline posterior
distribution over site-specific productivity parameters for carbon
sequestration and agricultural productivity implied by the regression
estimation. While convenient, this baseline construction is *ad hoc* and
uncertain. This leads us to engage in a sensitivity analysis that
explores distributional sensitivity subject to penalization. This
estimation is done prior to the decision-making of the social planner
and so acts as "prior" when exploring alternative courses of action.
Rather than fully embracing this distribution, the planner uses it as a
baseline in a sensitivity analysis subject to penalization to ascertain
which departures should be of most concern. The magnitude of a penalty
parameter limits how much sensitivity is entertained and serves as the
inverse of an ambiguity aversion parameter. For the computation of the
optimal solutions, in this case of parameter ambiguity, we use the
Markov chain Monte Carlo method based on Hamiltonian dynamics that we
alluded to earlier.

While we assume that the planner can directly control deforestation, we
view the solution to the planner's problem as providing a benchmark for
comparing the outcomes of alternative *ad hoc* policies, and suggesting
improvements over current policies.[^6]

<!-- The rest of the paper is organized as follows: In the next section,
Section [\[sec:literature\]](#sec:literature){reference-type="ref"
reference="sec:literature"}, we review some of the relevant literature.
This is followed in Section
[\[sec:model\]](#sec:model){reference-type="ref" reference="sec:model"}
with an exposition of our theoretical model. Section
[\[section:apu\]](#section:apu){reference-type="ref"
reference="section:apu"} shows how we confront parameter uncertainty.
Section [\[sec:cal\]](#sec:cal){reference-type="ref"
reference="sec:cal"} summarizes how we use a large collection of
relevant data sets to calibrate the model. Section
[\[sec:computation\]](#sec:computation){reference-type="ref"
reference="sec:computation"} discusses the numerical methods used to
compute solutions to the social planner's maximization problem. Our
results are presented in Section
[\[sec:res\]](#sec:res){reference-type="ref" reference="sec:res"}, which
is followed by our conclusions and suggestions for further work. -->

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

[^2]: Since close to $90\%$ of the deforested land in the Amazon biome
    is currently used for pasture, we identify agriculture with cattle
    farming in this paper, and use the two terms interchangeably.

[^3]: Until mid-94, Brazil went through a period of very high and
    volatile inflation.

[^4]: Their funding was a pay-for-performance scheme based on an
    emissions price of \$5 per ton of CO2e. It generated USD 1.2 billion
    in payments in 2008-2017 ({cite:t}`angelsen2017redd`, {cite:t}`correa2019amazon`)
    and provides an example of how deforestation may be influenced by
    outside payments.

[^5]: These include forest products like natural rubber, nuts, and açaí,
    alongside sustainable timber.

[^6]: Brazil has experience implementing effective policies to curb
    deforestation. The launch of satellite-based monitoring systems, the
    creation of protected areas, the enactment of conditioned-credit
    measures, and the creation of a priority list of municipalities,
    resulted in a reduction of more than 80% in the deforestation rates
    between 2004 and 2012 ({cite:t}`gandour2018forest`, {cite:t}`Assuncao2019`,
    {cite:t}`assunccao2020effect`, {cite:t}`assunccao2022deterring` and
    {cite:t}`assunccao2022optimal`).
