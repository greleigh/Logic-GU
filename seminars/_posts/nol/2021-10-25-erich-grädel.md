---
speaker: Erich Grädel
affil: RWTH Aachen University
title: Semiring semantics for logical statements with applications to the strategy analysis of games
date: 2021-10-25 16:00:00 +02:00
---
Semiring semantics of logical formulae generalises the classical Boolean semantics by permitting multiple truth values from certain semirings. In the classical Boolean semantics, a model of a formula assigns to each (instantiated) literal a Boolean value.
K-interpretations, for a semiring K, generalize this by assigning to each such literal a value from K. We then interpret 0 as false and
all other semiring values as nuances of true, which provide additional information, depending on the semiring:
For example, the Boolean semiring over {0,1} corresponds classical semantics, the Viterbi-semiring can model confidence scores,
the tropical semiring is used for cost analysis, and min-max-semirings (A, max, min, a, b) for a totally ordered set
(A,<) can model different access levels. Most importantly, semirings of polynomials, such as N[X], allow us to track certain literals by mapping them
to different indeterminates. The overall value of the formula is then a polynomial that describes precisely what combinations of literals prove the truth of the formula.

This can also be used for strategy analysis in games.
Evaluating formulae that define winning regions in a given game in an appropriate
semiring of polynomials provides not only the Boolean information on who wins, but also tells us how they win and which strategies they might use. For this approach,
the case of Büchi games is of special interest, not only due to their practical importance, but also because it is the simplest case where
the logical definition of the winning region involves a genuine alternation of a greatest and a least fixed point.
We show that, in a precise sense, semiring semantics provide information about all absorption-dominant strategies -- strategies that win with minimal effort,
and we discuss how these relate to positional and the more general persistent strategies.
This information enables further applications such as game synthesis or determining minimal modifications to the game needed to change its outcome.
