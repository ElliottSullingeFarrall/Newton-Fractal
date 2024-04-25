# Newton Fractal

## Newton-Raphson Method

Consider a polynomial $p(z) = \prod_{i=1}^n (z - \zeta_i)$ with $n$ distinct roots $\zeta_i \in \mathbb{C}$. If we pick a starting point $z_0 \in \mathbb{C}$, we can use the Newton-Raphson method to define a sequence $z_n$ that will either converge to one of the roots or diverge. The sequence is given by
$$z_{n+1} = z_n - \frac{p(z_n)}{p'(z_n)}$$
However, we don't know which starting values $z_0$ correspond to which root $\zeta_i$.

## Creating the Fractal

Start by picking a few distinct roots $\zeta_i \in \mathbb{C}$ and use them to construct the polynomial function $p$ and its derivative $p'$.

Next a function `newton_raphson` that takes an argument $z_0$ and returns the value that the Newton-Raphson method converges to. In practice this will require using two parameters that you can tweak as desired:
* A tolerance on how small the changes in $z_n$ can be before we decide that we have converged.
* A maximum number of iterations we do before we decide that the sequence will not converge.

Then, use `newton_raphson` to create a function `fractal` that takes an argument $z_0$ and returns the root $\zeta_i$ that the sequence is converging to.

Finally, use `imshow` from `matplotlib` to plot which roots correspond with which starting values in the complex plane. 

