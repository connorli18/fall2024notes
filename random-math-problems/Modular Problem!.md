# [Modular Problem] AMC 10A (22)

#### Problem

Define $L_n$ as the least common multiple of all the integers from $1$ to $n$ inclusive. There is a unique integer $h$ such that
$$
\frac{1}{1} + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{16} + \frac{1}{17} = \frac{h}{L_{17}}
$$
What is the remainder when $h$ is divided by $17$ ?

#### Solution

Let's evaluate the larger expression (without completely bashing it out).
$$
\begin{align*}
\frac{1}{1} + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{16} + \frac{1}{17} &= \frac{\left(\frac{17!}{1} + \frac{17!}{2} +  \frac{17!}{3} + \cdots + \frac{17!}{16} + \frac{17!}{17} \right)}{17!}
\end{align*}
$$
Essentially, we are searching for the 