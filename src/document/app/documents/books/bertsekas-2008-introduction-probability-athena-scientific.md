---
tags: [physical]
---

# Bertsekas, D., & Tsitsiklis, J. N. (2008). Introduction to probability. Athena Scientific.


```python

@book{bertsekas2008introduction,
  title={Introduction to probability},
  author={Bertsekas, Dimitri and Tsitsiklis, John N},
  year={2008},
  publisher={Athena Scientific}
}
```

## Notes

---

> Probability is common sense reduced to calculations. Laplace.
> 

## Index

## Sample Space and Probability

> La palabra "probabilidad" tiene sus raíces en el latín **"probabilitas"**,  reflejando la idea de algo que es probable o creíble. Con el tiempo, su  significado se enfocó en la posibilidad de que ocurran eventos,  convirtiéndose en un pilar fundamental de las matemáticas y la  estadística modernas.
> 

**Probability** can be **defined as**:

- **Frequentist**: This approach defines probability as the ratio of the number of favorable outcomes to the total number of equally possible outcomes.
- **Subjective**: This approach defines probability as a degree of belief or confidence that an individual has in the occurrence of an event, based on their knowledge and experience.

QA:

- What does probability means?
- …

Set:

- **Set**: A collection of objects.
- **Empty Set**: A set with not objects.
- Set Definition **Strategy**: Intension vs. Extension.
- **Subset**:  …
- **Universal Set**: …
- Set Operator:  Union, Intersection
- Set Properties: Disjuction,  Partition, Complement [This properties / can also be defined as operator; because they are properties of operations]
- Ordered Pair: …
- Venn Diagram: …
- Set Algebras: …

Probabilistic Model:

![image.png](documents/books/bertsekas-2008-introduction-probability-athena-scientific/image.png)

![Many tools can be used to represent this experiments like a **Sequential Tree Description**.](documents/books/bertsekas-2008-introduction-probability-athena-scientific/image-1.png)

Many tools can be used to represent this experiments like a **Sequential Tree Description**.

- A **probabilistic model** is a mathematical description of an uncertain situation.
- A **sequential probabilistic model** is a model defined a by experiments done in  sequence.
- A **discrete probability model** is a model where the **sample space** consists of outcomes that are finite or countable, with  each outcome assigned a probability between 0 and 1 such that the total  probability sums to 1.
- A **continuous probability models**: probabilistic models with **continuous sample spaces** differ from their discrete counterparts in that the probabilities of the single-element events may not be sufficient to characterize the probability law. ❓ Ho to define continuity?
- **Structure**: Sample Space, Probability Law.
- **Event**: Any subset of the sample space. Note that the outcomes of the experiment is the **materialization of the event**.
- There is no restriction on what constitutes an experiment.
- The sample space of an experiment may consist of a finite or an infinite
number of possible outcomes.
- **Rule**: Every experiment results should be map to one event; meaning that **events** must be **mutually exclusive**.
- Every experiment's outcome must map to exactly one event. If the sample space satisfies this property, it is said to be collectively exhaustive.
- Independent Events: …
- Independent Trials: …
- …

Probability Formalism:

- **Classical Probability**: Based on equally likely outcomes; probabilities assigned by symmetry.
- **Axiomatic Probability**:  Probability defined using a formal set of axioms (e.g., Kolmogorov’s axioms).
- **Subjective Probability**: Probability is a degree of belief or personal judgment about the likelihood of an event.
- **Bayesian Probability**: Combines prior beliefs with new evidence to update probabilities using Bayes' theorem.
- **Measure-Theoretic Probability**: A rigorous formalism defining probability as a measure on a σ-algebra.
- **Geometric Probability**: Assigns probabilities based on lengths, areas, or volumes in continuous spaces.
- **Quantum Probability**: Probabilities derived from quantum mechanics, using wavefunctions and operators.
- **Fuzzy Probability**: Deals with uncertainty when probabilities are imprecise or partially known.
- **Propensity Probability**: Probability as a physical tendency or disposition of a system to produce certain outcomes.

Komolgorov Axioms:

![image.png](documents/books/bertsekas-2008-introduction-probability-athena-scientific/image-2.png)

Discrete Models:

- Discrete Probability Law: P(E) is Number of elements in E / n.

Continuous Models:

- Probabilistic models with continuous sample spaces differ from their discrete counterparts in that the probabilities of the single-element events may not be sufficient to characterize the probability law.

Properties of Probability Laws:

- If $A \subset B$, then $\mathbf{P}(A) \leq \mathbf{P}(B)$.
- $\mathbf{P}(A \cup B) = \mathbf{P}(A) + \mathbf{P}(B) - \mathbf{P}(A \cap B)$.
- $\mathbf{P}(A \cup B) \leq \mathbf{P}(A) + \mathbf{P}(B)$.
- $\mathbf{P}(A \cup B \cup C) = \mathbf{P}(A) + \mathbf{P}(A^{c} \cap B) + \mathbf{P}(A^{c} \cap B^{c} \cap C)$.

Conditional Probability:

- **Conditional Probability** provides us with a way to reason the outcome of an experiment, based on **partial information**.
- Given an experiment; we know that the outcomes lies in a given event A; what is the likelihood that the outcome also belongs to another event B.
- In an experiment involving two successive rolls of a die, you are told that the sum of the two rolls is 9. How likely is it that the first roll was a 6?
- How likely is it that a person has a disease given that a medical test was negative?
- A spot shows up on a radar screen. How likely is it that it corresponds to an aircraft?
- **Conditional Probability**: `$\mathbf{P}(A \mid B) = \frac{\mathbf{P}(A \cap B)}{\mathbf{P}(B)}$`.
- …

Properties of **Conditional Probability**:

![image.png](documents/books/bertsekas-2008-introduction-probability-athena-scientific/image-3.png)

Modelling with Probability:

- …

Multiplicative Rule:

- Assuming that all the conditioning events have positive probability, we have $\mathbf{P}\left(\bigcap_{i=1}^n A_i\right) = \mathbf{P}(A_1)\mathbf{P}(A_2 \mid A_1)\mathbf{P}(A_3 \mid A_1 \cap A_2) \cdots \mathbf{P}\left(A_n \mid \bigcap_{i=1}^{n-1} A_i\right)$.

**Total Probability Theorem:**

![image.png](documents/books/bertsekas-2008-introduction-probability-athena-scientific/image-4.png)

Let $A_{1},\ldots,A_{n}$ be disjoint events that form a partition of the sample space (each possible outcome is included in one and only one of the events $A_{1},\ldots,A_{n}$ and assume that $\mathbf{P}(A_{i})>0$, for all $i=1,\ldots,n$. Then, for any event $B$, we have

$\mathbf{P}(B) =\mathbf{P}(A_{1}\cap B)+\cdots+\mathbf{P}(A_{n}\cap B)$
           $=\mathbf{P}(A_{1})\mathbf{P}(B\,|\,A_{1})+\cdots+\mathbf{P}(A_{n}) \mathbf{P}(B\,|\,A_{n}).$

**Bayes' Rule:**

Let $A_{1},A_{2},\ldots,A_{n}$ be disjoint events that form a partition of the sample space, and assume that $\mathbf{P}(A_{i})>0$, for all $i$. Then, for any event $B$ such that $\mathbf{P}(B) > 0$, we have

- $\mathbf{P}(A_{i}\,|\,B) =\frac{\mathbf{P}(A_{i})\mathbf{P}(B\,|\,A_{i})}{\mathbf{P}(B)}$
- $=\frac{\mathbf{P}(A_{i})\mathbf{P}(B\,|\,A_{i})}{\mathbf{P}(A_{1}) \mathbf{P}(B\,|\,A_{1})+\cdots+\mathbf{P}(A_{n})\mathbf{P}(B\,|\,A_{n})}.$

**Independence:**

![image.png](documents/books/bertsekas-2008-introduction-probability-athena-scientific/image-5.png)

![image.png](documents/books/bertsekas-2008-introduction-probability-athena-scientific/image-6.png)

Counting:

![image.png](documents/books/bertsekas-2008-introduction-probability-athena-scientific/image-7.png)

![image.png](documents/books/bertsekas-2008-introduction-probability-athena-scientific/image-8.png)

![image.png](documents/books/bertsekas-2008-introduction-probability-athena-scientific/image-9.png)

- The counting principle is based on a divide-and-conquer approach, whereby the
counting is broken down into stages through the use of a tree.
- Permutation: …
- Combination: …
- Partition: …

### Set Practice

**Problem 1.** Consider rolling a six-sided die. Let $A$ be the set of outcomes where the roll is an even number. Let $B$ be the set of outcomes where the roll is greater than 3. 

Calculate and compare the sets on both sides of De Morgan's laws
$(A \cup B)^c = A^c \cap B^c, \quad (A \cap B)^c = A^c \cup B^c$.

**Problem 2.** Let $A$ and $B$ be two sets.

(a) Show that

- $A^{c}=(A^{c}\cap B)\cup(A^{c}\cap B^{c})$,
- $B^{c}=(A\cap B^{c})\cup(A^{c} \cap B^{c})$

(b) Show that  $(A\cap B)^{c}=(A^{c}\cap B)\cup(A^{c}\cap B^{c})\cup(A\cap B^{c})$.
(c) Consider rolling a six-sided die. Let $A$ be the set of outcomes where the roll is an odd number. Let $B$ be the set of outcomes where the roll is less than 4. Calculate the sets on both sides of the equality in part **(b)**, and verify that the equality holds.

**Problem 3.** Prove the identity $A \cup \left(\bigcap_{n=1}^{\infty} B_n\right) = \bigcap_{n=1}^{\infty} (A \cup B_n)$.

**Problem 4.** Cantor's diagonalization argument. Show that the unit interval $[0,1]$ is uncountable, i.e., its elements cannot be arranged in a sequence.

### Probabilistic Models Problem Set

> …
> 

**Problem 5.** Out of the students in a class, 60% are  geniuses, 70% love chocolate, and 40% fall into both categories.  Determine the probability that a randomly selected student is neither a 
genius nor a chocolate lover.

**Problem 6.** A six-sided die is loaded in a way that each even face is twice as likely as each odd face. All even faces are equally likely, as are all odd faces. Construct a probabilistic model for a single roll of this die and find the probability that the outcome is less than $4$.

**Problem 7.** A four-sided die is rolled repeatedly, until the first time (if ever) that an even number is obtained. What is the sample space for this experiment?

**Problem 8.*** **Bonferroni's inequality.**

(a) Prove that for any two events $A$ and $B$, we have ${\bf P}(A\cap B)\geq{\bf P}(A)+{\bf P}(B)-1$.

(b) Generalize to the case of $n$ events $A_{1},A_{2},\ldots,A_{n}$, by showing that  ${\bf P}(A_{1}\cap A_{2}\cap\cdots\cap A_{n})\geq{\bf P}(A_{1})+{\bf P}(A_{2})+\cdots +{\bf P}(A_{n})-(n-1)$.

**Problem 9.*** The inclusion-exclusion formula. Show the following generalizations of the formula $\mathbf{P}(A\cup B)=\mathbf{P}(A)+\mathbf{P}(B)-\mathbf{P}(A\cap B)$.

(a) Let $A$, $B$, and $C$ be events. Then, 

$\mathbf{P}(A\cup B\cup C)=\mathbf{P}(A)+\mathbf{P}(B)+\mathbf{P}(C)- \mathbf{P}(A\cap B)-\mathbf{P}(B\cap C)-\mathbf{P}(A\cap C)+\mathbf{P}(A\cap B \cap C)$.

(b) Let $A_{1},A_{2},\ldots,A_{n}$ be events. Let $S_{1}=\{i\mid 1\leq i\leq n\}, S_{2}=\{(i_{1},i_{2})\mid 1\leq i_{1}<i_{2}\leq n\}$, and more generally, let $S_{m}$ be the set of all $m$-tuples $(i_{1},\ldots,i_{m})$ of indices that satisfy $1\leq i_{1}<i_{2}<\cdots<i_{m}\leq n$. Then,

$\mathbf{P}\left(\cup_{k=1}^{n}A_{k}\right) =\sum_{i\in S_{1}}\mathbf{P}(A_{i})-\sum_{(i_{1},i_{2})\in S_{2}} \mathbf{P}(A_{i_{1}}\cap A_{i_{2}})$
+ $\sum_{(i_{1},i_{2},i_{3})\in S_{3}}\mathbf{P}(A_{i_{1}}\cap A_{i_{2}}\cap A_{i_{3}})-\cdots+(-1)^{n-1}\mathbf{P}\left(\cap_{k=1}^{n}A_{k}\right)$.

### Conditional Probability Problem Set

**Problem 11.** We roll two fair 6-sided dice. Each one of the 36 possible outcomes is assumed to be equally likely.

1. (a) Find the probability that doubles are rolled.
2. (b) Given that the roll results in a sum of 4 or less, find the conditional probability that doubles are rolled.
3. (c) Find the probability that at least one die roll is a 6.
4. (d) Given that the two dice land on different numbers, find the conditional probability that at least one die roll is a 6.

**Problem 12.** A coin is tossed twice. Alice claims that the event of two heads is at least as likely if we know that the first toss is a head than if we know that at least one of the tosses is a head. Is she right? Does it make a difference if the coin is fair or unfair? How can we generalize Alice's reasoning?

**Problem 13.** We are given three coins: one has heads in both faces, the second has tails in both faces, and the third has a head in one face and a tail in the other. We choose a coin at random, toss it, and it comes heads. What is the probability that the opposite face is tails?

**Problem 14.** A batch of one hundred items is inspected by testing four randomly selected items. If one of the four is defective, the batch is rejected. What is the probability that the batch is accepted if it contains five defectives?

**Problem 15.** Let $A$ and $B$ be events. Show that $\mathbf{P}(A\cap B\,|\,B)=\mathbf{P}(A\,|\,B)$, assuming that $\mathbf{P}(B)>0$.

### Bayes’ Rule Theorem

**Problem 19.** Alice searches for her term paper in her filing cabinet, which has several drawers. She knows that she left her term paper in drawer $j$ with probability $p_{j} > 0$. The drawers are so messy that even if she correctly guesses that the term paper is in drawer $i$, the probability that she finds it is only $d_{i}$. Alice searches in a particular drawer, say drawer $i$, but the search is unsuccessful. Conditioned on this event, show that the probability that her paper is in drawer $j$, is given by
$\frac{p_{j}}{1-p_{i}d_{i}},\qquad\text{if }j\neq i,\qquad\frac{p_{i}(1-d_{i})}{1 -p_{i}d_{i}},\qquad\text{if }j=i$.

**Problem 21.** Two players take turns removing a ball from a jar that initially contains $m$ white and $n$  black balls. The first player to remove a white ball wins. Develop a  recursive formula that allows the convenient computation of the  probability that the starting player wins.

**Problem 22.** Each of $k$ jars contains $m$ white and $n$ black balls. A ball is randomly chosen from jar 1 and transferred to jar 2, then a ball is randomly chosen from jar 2 and transferred to jar 3, etc. Finally, a ball is randomly chosen from jar $k$. Show that the probability that the last ball is white is the same as the probability that the first ball is white, i.e., it is $m/(m+n)$.

**Problem 23.** We have two jars, each initially containing  an equal number of balls. We perform four successive ball exchanges. In  each exchange, we pick simultaneously and at random a ball from each  jar and move it to the other jar. What is the probability that at the  end of the four exchanges all the balls will be in the jar where they  started?

**Problem 24. The prisoner's dilemma.** The release of two out of three prisoners has been announced, but their identity is kept secret. One of the prisoners considers asking a friendly guard to tell him who is the prisoner other than himself that will be released, but hesitates based on the following rationale: at the prisoner's present state of knowledge, the probability of being released is $2/3$, but after he knows the answer, the probability of being released will become $1/2$, since there will be two prisoners (including himself) whose fate is unknown and exactly one of the two will be released. What is wrong with this line of reasoning?

**Problem 25.** **A two-envelopes puzzle.** You are handed two envelopes, and you know that each contains a positive integer dollar amount and that the two amounts are different. The values of these two amounts are modeled as constants that are unknown. Without knowing what the amounts are, you select at random one of the two envelopes, and after looking at the amount inside, you may switch envelopes if you wish. A friend claims that the following strategy will increase above $1/2$ your probability of ending up with the envelope with the larger amount: toss a coin repeatedly, let $X$ be equal to $1/2$ plus the number of tosses required to obtain heads for the first time, and switch if the amount in the envelope you selected is less than the value of $X$. Is your friend correct?

**Problem 26. The paradox of induction.** Consider a statement whose truth is unknown. If we see many examples that are compatible with it, we are tempted to view the statement as more probable. Such reasoning is often referred to as *inductive inference* (in a philosophical, rather than mathematical sense). Consider now the statement that "all cows are white." An equivalent statement is that "everything that is not white is not a cow." We then observe several black crows. Our observations are clearly compatible with the statement, but do they make the hypothesis "all cows are white" more likely?

To analyze such a situation, we consider a probabilistic model. Let us assume that there are two possible states of the world, which we model as complementary events:

- $A:$ all cows are white,
- $A^{c}:$ 50% of all cows are white.

Let $p$ be the prior probability $\mathbf{P}(A)$ that all cows are white. We make an observation of a cow or a crow, with probability $q$ and $1-q$, respectively, independent of whether event $A$ occurs or not. Assume that $0<p<1$, $0<q<1$, and that all crows are black.

- (a) Given the event $B=\{\text{a black crow was observed}\}$, what is $\mathbf{P}(A\,|\,B)$?
- (b) Given the event $C=\{\text{a white cow was observed}\}$, what is $\mathbf{P}(A\,|\,C)$?

**Problem 27.** Alice and Bob have $2n+1$ coins, each coin with probability of heads equal to $1/2$. Bob tosses $n+1$ coins, while Alice tosses the remaining $n$ coins. Assuming independent coin tosses, show that the probability that after all coins have been tossed, Bob will have gotten more heads than Alice is $1/2$.

### Independence Problem Set

> …
> 

**Problem 30.** A hunter has two hunting dogs. One day, on the trail of some animal, the hunter comes to a place where the road diverges into two paths. He knows that each dog, independent of the other, will choose the correct path with probability$p$. The hunter decides to let each dog choose a path, and if they agree, take that one, and if they disagree, to randomly pick a path. Is his strategy better than just letting one of the two dogs decide on a path?

**Problem 32.** **The king's sibling.** The king has only one sibling. What is the probability that the sibling is male? Assume that every birth results in a boy with probability \(1/2\), independent of other births. Be careful to state any additional assumptions you have to make in order to arrive at an answer.

**Problem 33.** **Using a biased coin to make an unbiased decision.** Alice and Bob want to choose between the opera and the movies by tossing a fair coin. Unfortunately, the only available coin is biased (though the bias is not known exactly). How can they use the biased coin to make a decision so that either option (opera or the movies) is equally likely to be chosen?

**Problem 35. Reliability of a $k$-out-of-$n$ system.** A system consists of $n$ identical components, each of which is operational with probability $p$, independent of other components. The system is operational if at least $k$ out of the $n$ components are operational. What is the probability that the system is operational?

**Problem 37.** A cellular phone system services a population of $n_{1}$ "voice users" (those who occasionally need a voice connection) and $n_{2}$ "data users" (those who occasionally need a data connection). We estimate that at a given time, each user will need to be connected to the system with probability $p_{1}$ (for voice users) or $p_{2}$ (for data users), independent of other users. The data rate for a voice user is $r_{1}$ bits/sec and for a data user is $r_{2}$ bits/sec. The cellular system has a total capacity of $c$ bits/sec. What is the probability that more users want to use the system than the system can accommodate?

**Problem 39.** A particular class has had a history of low attendance. The annoyed professor  decides that she will not lecture unless at least $k$ of the $n$ students enrolled in the class are present. Each student will independently show up with probability $p_{g}$ if the weather is good, and with probability $p_{b}$ if the weather is bad. Given the probability of bad weather on a given day, obtain an expression for the probability that the professor will teach her class on that day.

**Problem 42.*** **Gambler's ruin.** A gambler makes a sequence of independent bets. In each bet, he wins $1 with probability $p$, and loses $1 with probability $1 - p$. Initially, the gambler has $k, and plays until he either accumulates $n or has no money left. What is the probability that the gambler will end up with $n?

**Problem 44.*** Let $A$, $B$, and $C$ be independent events, with $\mathbf{P}(C)>0$. Prove that $A$ and $B$ are conditionally independent given $C$.

**Problem 46.*** **Laplace's rule of succession.** Consider $m+1$ boxes with the $kth$ box containing $k$ red balls and $m-k$ white balls, where $k$ ranges from $0$ to $m$. We choose a box at random (all boxes are equally likely) and then choose a ball at random from that box, $n$ successive times (the ball drawn is replaced each time, and a new ball is selected independently). Suppose a red ball was drawn each of the $n$ times. What is the probability that if we draw a ball one more time it will be red? Estimate this probability for large $m$.

### Counting Problem Set

> …
> 

**Problem 49. De Mere's puzzle.** A six-sided die is rolled three times independently. Which is more likely: a sum of 11 or a sum of 12? (This question was posed by the French nobleman de Mere to his friend Pascal in the 17th century.)

**Problem 50. The birthday problem.** Consider $n$ people who are attending a party. We assume that every person has an equal probability of being born on any day during the year, independent of everyone else, and ignore the additional complication presented by leap years (i.e., assume that nobody is born on February 29). What is the probability that each person has a distinct birthday?

**Problem 51. An urn contains $m$ red and $n$ white balls.**

- (a) We draw two balls randomly and simultaneously. Describe the sample space and calculate the probability that the selected balls are of different color, by using two approaches: a counting approach based on the discrete uniform law, and a sequential approach based on the multiplication rule.
- (b) We roll a fair 3-sided die whose faces are labeled 1, 2, 3, and if $k$ comes up, we remove $k$ balls from the urn at random and put them aside. Describe the sample space and calculate the probability that all of the balls drawn are red, using a divide-and-conquer approach and the total probability theorem.

Problem 52. We deal from a well-shuffled 52-card deck. Calculate the probability that the 13th card is the first king to be dealt.

Problem 53. Ninety students, including Joe and Jane, are to be split into three classes of equal size, and this is to be done at random. What is the probability that Joe and Jane end up in the same class?

**Problem 53.** Ninety students, including Joe and Jane, are to be split into three classes of equal size, and this is to be done at random. What is the probability that Joe and Jane end up in the same class?

**Problem 54.** Twenty distinct cars park in the same parking lot every day. Ten of these cars are US-made, while the other ten are foreign-made. The parking lot has exactly twenty spaces, all in a row, so the cars park side by side. However, the drivers have varying schedules, so the position any car might take on a certain day is random.

1. (a) In how many different ways can the cars line up?
2. (b) What is the probability that on a given day, the cars will park in such a way that they alternate (no two US-made are adjacent and no two foreign-made are adjacent)?

**Problem 55.** Eight rooks are placed in distinct squares of an $8\times 8$ chessboard, with all possible placements being equally likely. Find the probability that all the rooks are safe from one another, i.e., that there is no row or column with more than one rook.

**Problem 56.** An academic department offers 8 lower level courses: $\{L_{1},L_{2},\ldots,L_{8}\}$ and 10 higher level courses: $\{H_{1},H_{2},\ldots,H_{10}\}$. A valid curriculum consists of 4 lower level courses, and 3 higher level courses.

1. (a) How many different curricula are possible?
2. (b) Suppose that $\{H_{1},\ldots,H_{5}\}$ have $L_{1}$ as a prerequisite, and $\{H_{6},\ldots H_{10}\}$ have $L_{2}$ and $L_{3}$ as prerequisites, i.e., any curricula which involve, say, one of $\{H_{1},\ldots,H_{5}\}$ must also include $L_{1}$. How many different curricula are there?

**Problem 57.** How many 6-word sentences can be made using each of the 26 letters of the alphabet exactly once? A word is defined as a nonempty (possibly jibberish) sequence of letters.

**Problem 58.** We draw the top 7 cards from a well-shuffled standard 52-card deck. Find the probability that:

1. (a) The 7 cards include exactly 3 aces.
2. (b) The 7 cards include exactly 2 kings.
3. (c) The probability that the 7 cards include exactly 3 aces, or exactly 2 kings, or both.

**Problem 62.** Correcting the number of permutations for indistinguishable objects. When permuting $n$ objects, some of which are indistinguishable, different permutations may lead to indistinguishable object sequences, so the number of distinguishable object sequences is less than $n!$. For example, there are six permutations of the letters A, B, and C:

ABC, ACB, BAC, BCA, CAB, CBA,

but only three distinguishable sequences that can be formed using the letters A, D, and D:

ADD, DAD, DDA.

1. (a) Suppose that $k$ out of the $n$ objects are indistinguishable. Show that the number of distinguishable object sequences is $n!/k!$.
2. (b) Suppose that we have $r$ types of indistinguishable objects, and for each $i$, $k_{i}$ objects of type $i$. Show that the number of distinguishable object sequences is $\frac{n!}{k_{1}!\:k_{2}!\cdots k_{r}!}.$

## Discrete Random Variables

> …
> 

## General Random Variables

> …
> 

## Further Topics on Random Variables

> …
> 

## Limit Theorems

> …
> 

## The Bernoulli and Poisson Processes

> …
> 

## Markov Chains

> …
> 

## Bayesian Statistical Inference

> …
> 

## Classical Statistical Inferences

> …
> 

## References

- [De Laplace, P. S. (1816). Essai philosophique sur les probabilités. Mme Ve Courcier.](De%20Laplace,%20P%20S%20(1816)%20Essai%20philosophique%20sur%20les%20184598edb790807c8a3bd6d238de4af3.md)
- [https://archive.org/details/introductiontopr0000bert/page/53/mode/1up?view=theater](https://archive.org/details/introductiontopr0000bert/page/53/mode/1up?view=theater)
- https://en.wikipedia.org/wiki/Collectively_exhaustive_events
- https://en.wikipedia.org/wiki/Event_(probability_theory)
- https://en.wikipedia.org/wiki/Dutch_book_theorems
- https://en.wikipedia.org/wiki/Probability_axioms
- https://en.wikipedia.org/wiki/Cox%27s_theorem
- https://en.wikipedia.org/wiki/Bayes%27_theorem
- https://en.wikipedia.org/wiki/Prior_probability
- https://en.wikipedia.org/wiki/Posterior_probability
- [‣](https://app.notion.com/p/fff598edb79081658776d93214bffa03?pvs=21)
- [‣](https://app.notion.com/p/fff598edb7908142a968e7231c59aa41?pvs=21)
- [‣](https://app.notion.com/p/fff598edb79081daa204f496b84ec42e?pvs=21)
- [‣](https://app.notion.com/p/fff598edb790814f8623d7223dc2f856?pvs=21)
- [‣](https://app.notion.com/p/fff598edb7908129b20efabd97b3a583?pvs=21)
- [‣](https://app.notion.com/p/fff598edb790819db08bc030a780cfc5?pvs=21)
- [‣](https://app.notion.com/p/fff598edb790814b9df6f90962e26b1b?pvs=21)
- [‣](https://app.notion.com/p/fff598edb790814d94c3d7c702e5b817?pvs=21)
