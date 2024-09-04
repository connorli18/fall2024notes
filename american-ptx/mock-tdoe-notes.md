# Mock Notes

----

### Conditional Probability

#### Q1

**Question:** You are given 1000 coins. Among them, 1 coin has head on both sides. The other 999 are fair coins. You randomly choose a coin and toss it 10 times. Each time, the coin turns up heads. What’s the probability that you choose is the double headed one?

**Answer:** Baye's Law
$$
\frac{\frac{1}{1000} \cdot 1}{\frac{1}{1000} \cdot 1 + \frac{999}{1000}\cdot \left(\frac{1}{2}\right)^{10}}
$$

#### Q2

**Question:** You are taking candies out of a jar that has 10 red candies, 20 blue candies and 30 green candies. What’s the probability that there are at least 1 blue candy and 1 green candy left in the jar after you’ve take out all the red candies?

**Answer:** 
$$
\begin{align*}
P(\text{1 Blue 1 Green At Least}) &= P(\text{Green Last}) \cdot P(\text{Blue Last}) + P(\text{Blue Last}) \cdot P(\text{Green Last}) \\
&= \frac{30}{60} \cdot \frac{20}{30} + \frac{20}{60} \cdot \frac{30}{40}\\
&= \frac{7}{12}
\end{align*}
$$

---

### Brainteasers

#### Q1

**Question:** A clock falls and breaks into 3 pieces, each piece adds up to the same amount…how does the clock break?

**Answer:** 3 pieces (it doesn't split into consecutive numbers)

- Piece 1: $11, 12, 1, 2$
- Piece 2: $9, 10, 3, 4$
- Piece 3: $5, 6, 7, 8$

#### Q2

**Question:** Each stick burns for one hour exactly. But they burn unevenly throughout, how do you measure 15 minutes?

**Answer:** Burn both ends of one stick to find $30$ minutes. At the same time, burn one end of the other stick. Once the 30 minutes runs out, burn the other end of stick 2 and you should be able to measure out 15 minutes.

----

### Expected Value

#### Q1

**Question:** How many flips do you need to get 4 heads in a row?

**Answer:** $e = $ number of flips until you get 4 heads
$$
\begin{align*}
e &= \underbrace{\frac{1}{2}(e+1)}_{T} + \underbrace{\frac{1}{4}(e+2)}_{HT} + \underbrace{\frac{1}{8}(e+3)}_{HHT} + \underbrace{\frac{1}{16}(e+4)}_{HHHT} + \frac{1}{16}(4)\\
e &= \dots
\end{align*}
$$

#### Q2

**Question:** You play a game where you get to keep the face value on the dice that you roll. Imagine that in this game, if you don't like the result of your first roll - you can reroll and take the value on the second roll as your "face value". How much is a fair amount to play the game?

**Answer:** 
$$
e = \underbrace{\frac{1}{2}(5)}_{4,5,6} + \underbrace{\frac{1}{2}(3.5)}_{1,2,3 \text{ reroll}} = 4.25
$$

----

### Behavioral Questions

- Why do you want to work @ Jane Street? Why do you specifically want to work the TDO Role?
- Talk about a time that you were working in a team and had a disagreement with a teammate. What happened and how did you resolve it? What did you learn about it?

----

### Other Questions (Too Lazy to Organize)

#### Q1

**Question:** If 1.5 chickens produce 1.5 eggs in 1.5 days, how many eggs will 9 chickens produce in 9 days?

**Answer:** 
$$
\text{rate} * \text{time} = \text{eggs} \quad \quad \text{rate} = \text{chickens} * \text{rate per chicken}
$$

$$
\begin{align*}
	1.5 * 1.5 * v = 1.5 \implies v = \frac{2}{3} \implies 9 * 9 * \frac{2}{3} = 54
\end{align*}
$$

#### Q2

**Question:** Four people need to cross a rickety bridge at night. Unfortunately, they have one torch and the bridge is too dangerous to cross without a torch. The bridge can support only two people at a time. All the people don’t take the same time to cross the bridge. Time for each person: 1 min, 2 mins, 7 mins, and 10 mins. What is the shortest time needed for all four of them to cross the bridge?

**Answer:** 17 minutes, explanation $\href{https://www.geeksforgeeks.org/four-people-rickety-bridge/}{\text{here}}$. 

#### Q3

**Question:** You have two ropes, each of which takes 1 hour to burn. But either rope has different densities at different points, so there's no guarantee of consistency in the time it takes different sections within the rope to burn. How do you use these two ropes ot measure 45 minutes?

**Answer:** Burn 3 ends, then once the first stick burns out, burn the only other end left!

#### Q4

**Question:** You have 12 identical balls. One of the balls is heavier than the rest (you don't know which). Using just a balance that can only show you which side of the tray is heavier, what is the least number of measurements you need to determine which balls is heavier than the rest?

**Answer:** (3) Weigh 4v4 $\rightarrow$ Weigh 2v2 $\rightarrow$ Weigh 1v1

#### Q5

**Question:** How many trailing zeros are there in $100!$ (factorial of 100)?

**Answer:** Count the number of $2 \times 5$ that exists, the hint is that $5$ is the limiting factor. But make sure you are also not undercounting since $25 = 5 \times 5$, so there are two factors of $5$. 

#### Q6

**Question:** A clock (numbered 1- 12 clockwise) fell off the wall and broke into three pieces. You find that the sums of the numbers on each piece are equal. What are the numbers on each piece?

**Answer:** (11, 12, 1, 2) and (5,6,7,8) and last piece

#### Q7

Check it [here](https://medium.com/@rishidarkdevil/the-drunk-passenger-problem-554ebb7bd151).

#### Q8

Check it [here](https://math.stackexchange.com/questions/1417274/connecting-noodles-probability-question).