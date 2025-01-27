#  ARITHMETICS

##	On the distribution of ϕ(σ(n))



###	Mathematical side of the functions used in this program :

_*Euler totient function :*_ _**ϕ(n)**_ 

The explicit formula of the **Euler** totient formula is given by :

$$
\phi(n) = n\prod_{p \vert n}(1 - \frac{1}{p})
$$


_*Sum of all positiv divisors of n :*_ _**σ(n)**_

There is two formula for calculating the sum of all positiv divisors of a natural number _**n**_ .

######	-	First, is using the direct sum of positiv divisors :

$$
\sigma(n) = \sum_{d \mid n} d
$$

######	-	Second, is using an explicit equation using prime divisors of _**n**_:

$$
\sigma(n) = \prod_{p^k \parallel n} ({\frac{1-p^{k+1}}{1-p}})
$$



In this program, we are using the second expression as we can find in  [sigma.py](src/functions/sigma.py) 

##	About the src/statement directory :

In this [src/statements](src/statements) you will find the main purpose of this program. In fact, you will find there some applications of those two arithmetical functions given just above.

For instance, the first statement in [upper_bounded.py](src/statements/upper_bounded.py) is the implementation of this statement right bellow :

$$
\forall\space c, x > 0,\space N = card(\lbrace n \leq x: \phi(\sigma(n)) \leq cn \rbrace)
$$

This implementation of this is :

```python
  totient.phi(sigma.sigma(n)) <= c*n :
```



