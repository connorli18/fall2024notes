# Introduction to Proofs

#### Why should we care?

This class is generally about <u>group theory</u>. You can think about groups as a collection of abstract items (like a bucket that contains a bunch of random math stuff and symbols). These are really useful because they help us generate proofs for more complex problems.

The reason why is because groups and sets have very interesting properties (which we can show/prove that they exist), and then we can use these properties to find some very nice results when we apply them to things that we are actually interested in. Hopefully, it's a way to turn hard problems into something more conceptually basic.

So, let's define some of these "basic concepts".

#### What is a Set?

Sets are just like a "collection" of unique items, and sets are determined by their elements. We use certain notations to talk about defining these sets.
$$
\begin{align*}

\forall \quad \quad &\text{for all} \\
\iff \quad \quad &\text{if and only if (iff)}\\
\in, \notin \quad \quad &\text{element is in, element is not in}\\
\varnothing \quad \quad &\text{empty set}

\end{align*}
$$
The empty set is a set with no elements in it, i.e. $\varnothing = \{\}$. 

We say that $2 \in X$ if it looks something like this, $X = \{2,3,4,5,6\}$. We can also say that $7 \notin X$. 

Now, imagine some set $X = \{1,2,3,4,5,6,7,8\}$. We can say that $\forall x \in X$, $x \neq 0$. This is the same thing as saying "for all elements $x$ in the set $X$, not a single one of those elements equals $0$". 

Since sets are defined by their elements, we can say that if $X = \{0,1,2,3\}$ and $Y = \{0,1,2,3\}$, then $X = Y$. Also, order doesn't matter so the set $\{0,1,2,3\} = \{3,1,2,0\}$. 

----

#### More Set Terminology

##### Subset

I'm not sure exactly what notation your teacher uses, but we define an important notion of a **subset**. Intuitively, we say that a set $X$ is a subset of a set $Y$ if all elements of $X$ are in $Y$. 

This means that set $X = \{1,2,3\}$ is a subset of $Y = \{1,2,3,4,5\}$. We write this as $X \subset Y$. There is somethings some thing where you can say $\subseteq$ and things, but I generally only use $X \subset Y$. 

Another interesting property if $X = Y$, then $X \subset Y$ and $Y \subset X$. This is also true as an iff statement.
$$
X = Y \iff X \subset Y \text{ and } Y \subset X
$$
We write the formal definition below.

<u>Definition</u>: A set $X$ is a subset of set $Y$ $\iff$ $\forall \;x\in X$, $x \in Y$.  

##### Finite Sets

We say that $X$ is a finite set if it has an integer number of elements. There are some fancy ways to write this; but if you can count it, then it's finite. You can also say that $X$ is finite if it's not infinite.

<u>Note</u>: This is different that a "countable" set, so be sure to be precise.

##### Sets of Numbers

- $\mathbb{N} = \{1,2,3,\dots\}$ is the set of natural numbers 
- $\mathbb{Z} = \{\dots,-2,-1,0,1,2\dots\}$ is the set of integers
- $\mathbb{Q} = \left\{\frac{a}{b}\;:\; a \in \mathbb{Z} \and b \in \mathbb{Z} \and b \neq 0\right\}$ is the set of rational numbers (this is to say that it is the set of fractional numbers defined $\frac{a}{b}$ where $a$ and $b$ are part of the integers and $b$ does not equal zero)
- $\mathbb{R}$ are the real numbers
- $\mathbb{C}$ are the complex numbers

We say that $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$. Each one of these is a subset of the others in this order :)

##### Defining New Sets from the Old

<u>Intersection</u>: Let's say we want to find the intersection of two sets. Intuitively, we know that this is the set of elements that are shared among the two sets. However, let's define it more formally with sets $X$ and $Y$. 
$$
X \cap Y = \{x :\; x \in X \and x \in Y\}
$$
We say that the intersection $X \cap Y$ is the set of elements $x$ where $x$ is in $X$ and $x$ is in $Y$. 

<u>Union</u>: The union of two sets is the unique combination of elements from both sets. For example, take $X = \{1,2,3,4\}$ and $Y = \{3,4,5,6\}$. Then we say $X \cup Y = \{1,2,3,4,5,6\}$. 

We can define this in a more specific manner.
$$
X \cup Y = \{x : x \in X \or x \in Y \}
$$

##### Cartesian Product

The Cartesian product is the total cross-product between two sets. It's like taking every element of set $X$ and taking every element from set $Y$ and creating pairs like $(x,y)$, more formally:
$$
X \times Y = \{(x,y) : \forall x \in X, \forall y \in Y\}
$$
We have that the collection of all points in some graphable area on Desmos is $\mathbb{R} \times \mathbb{R}$. 

##### Power Set

We say that $Y$ is the power set of all $X$ if $Y$ is the "set of all subsets of $X$". Keep in mind, a subset of $X$ is both $X$ itself and $\varnothing$. I'm not too sure about notation, but I'll give you an example. Take $X = \{1,2,3\}$. 
$$
\text{Power set of }X = \left\{\varnothing, \{1\}, \{2\}, \{3\}, \{1,2\}, \{2,3\}, \{3,1\}, \{1,2,3\}\right\}
$$
As you can see, it is a set that contains sets!

Another important note is that $1 \neq \{1\}$. The first is an element, the second is a set! 

-----

### Functions

Functions are confusing, but you can rely on the same notion from Calc III and Calc I in what a function is. If a function passes the VLT, then it is a function.

First, let me briefly explain what a function is, and then I'll explain why the above is important. 

**Definition:** A function $f: X \to Y$ is a mapping of elements of $X$ to elements of $Y$. For example, the function $f: \mathbb{R} \to \mathbb{R}$ where $f(x) = 2x$ takes some real number $x$ and maps it to $2x$. 
$$
1 \mapsto 2 \quad\quad \sqrt{2} \mapsto 2\sqrt{2} \quad \quad \frac{3}{2} \mapsto 3
$$
The reason why that's important is because the VLT is a fancy way of saying that "every input should only map to one output". We define a couple of important function definitions.

- Use this website to determine what is [surjective, injective, bijective](https://www.mathsisfun.com/sets/injective-surjective-bijective.html)

- Use this website to read about [inverses](https://sites.math.washington.edu/~arms/m300A17/InvFunc.pdf)