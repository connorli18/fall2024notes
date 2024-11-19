# [Higher Math] Midterm Review

-----

### Relations

- Equivalence Relation (?)
- Types of relations
- Functions as relations

---

### Functions

#### General Notes

**Definition:** Take two sets, $X$ and $Y$. A function $f: X \to Y$ (a function from $X$ to $Y$) is a collection of ordered pairs $(x,y)$ such that $x \in X$ and $y \in Y$. 

- The condition for these ordered pairs to be considered a function is that they follow the Vertical Line Test (VLT). Anoterh way to put this is that each input only ever has one output!

More formally, we can say that $\forall x \in X$, the function $(x,y)$ only ever has one $y$. In these scenarios, we tend to use the "negative" definition, and say that if $(x_1, y_1) \in f$ and $(x_1, y_2) \in f$, then $y_1 = y_2$. 

----

Some important definitions are as follows:

- **Image (Range):** The image of $f: X \rightarrow Y$ is basically all the values in $Y$ that values $x \in X$ map to. In order words, it's the "range" of the function. 
  - However, we use the term image because this refers to the "range" of a specific set. You can imagine that you have a function $f(x) = x^2$ defined over all the real numbers. The range is $(0, \infty)$, but let's say that we only cared about the inputs $\{1,2,3\}$. Then, the image of this set of the function would be $\{1,4,9\}$. 
- **PreImage (Domain):** This is a fancy word for domain, but it's basically like all the elements $x \in X$ that map to values $y \in Y$. In the above example, take something like $\{1,4,9\}$ as output values for the function $f(x) = x^2$. Then, we can say the preimage of this set is $\{1,2,3\}$ because those are the values that map to those outputs.

----

There are three types of "mappings". Consider the function $f: A \to B$ where $a \in A$ and $b \in B$. 

- **Injective (one-to-one):** If $f(a) = f(b)$, then $a = b$. Another way to say this is that every input value only maps to one output value. You will never have a case where your function has something like $f(1) = f(3)$. 
- **Surjective (onto):** For all $b \in B$, there exists some $a \in A$ such that $f(a) = b$. This is basically saying that every possible output (in set $B$) guarentees to have some input from set $A$ that can map to it. 
- **Bijective:** Both surjective and injective! 
  - <u>NOTE</u>: If they ever ask about the inverse of a function, this is only possible with a bijective function! If you think about it, it makes sense why you can only have an inverse (that is a function) if the properties of injectivity and surjectivity are satisfied.

-----

#### Example Problems

**Problem 1 (HW 5):** Give the following definitions:

- a function $f: X \rightarrow Y$ 

A function $f: X \to Y$ (a function from $X$ to $Y$) is a collection of ordered pairs $(x,y)$ such that $x \in X$ and $y \in Y$, and $\forall x \in X$, the function $(x,y)$ only ever has one $y$. 

- for $A \subset X$, the set $f(A)$ 

$$
f(A) = \{f(a) \in Y\;:\; \forall a \in A\}
$$

- for $C \subset Y$, the set $f^{-1}(C)$ 

$$
f^{-1}(C) = \{a \in A\;:\;\forall c \in C, f(a) = c\}
$$

**Injective Proof:** By definitino of injectivity, we have that if $f(a) = f(b)$, then $a = b$. 

Take any element of $x \in A \cap B$. It should be obvious that $f(x) \in f(A)$ and $f(x) \in f(B)$. Now, take any element $y \in f(A) \cap f(B)$. Assume that $x_1 \in A \implies f(x_1) = y$ and $x_2 \in B \implies f(x_2 ) = y$ Then, $f(x_1) = f(x_2) = y$ and we know that $x_1 = x_2$ and so that $x_1 \in A \cap B$. This means that double inclusion so we good.

----

### Limits 

$$
(|a| - |b|)^2 = |a|^2 + |b|^2 - 2|a||b| \implies |a| + |b|
$$



**Example 4 HW 7**

$0 < |x| < \delta \implies 0 < |x - M| < \epsilon$. Assume that $\delta = \frac{1}{x}$ . this means that $x \sin (x)$ and around $x = 0$,  

Fix some $M$. Now, define $x = \frac{1}{\pi(M+1)}$ $\rightarrow f(x_0) = \pi(M+1) > M$. Thus, your bound fails.  

Limits:
$$
3x^2 - 3 < \epsilon \iff \delta = \sqrt{}
$$
