
(sec:solution)=
# Solving the maximization problem 

<hr style="height:4px; background-color:black; border:none;">

<br>

To achieve the needed degree of economic and spatial richness, we use
numerical methods to obtain model solutions. Given the number of
locations that we use (1043 or 78), we necessarily have a large number
of state variables with state-constraints that bind at the optimal
solution. To confront the inequality restrictions that are central to
our problem, we use a so-called interior point method. This method
imposes penalties on logarithms of variables constrained to be
non-negative. While the interior point approximation pushes solutions
away from their zero boundaries, in practice the solutions will be close
enough to zero to identify the binding constraints.




