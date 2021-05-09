---
speaker: Rasmus Blanck
affil: FLoV
title: Interpretability and flexible formulas
date: 2020-12-18 10:15:00 +02:00
---

This talk is about two different generalisations of Gödel’s incompleteness theorems and the (natural?) idea of trying to merge the two into a stronger result.
The first generalisation I have in mind is Feferman’s theorem on the “interpretability of inconsistency”.
This result strengthens the second incompleteness theorem, by showing that the sentence expressing that PA is inconsistent is not only consistent with PA, but even that PA + “PA is inconsistent” is interpretable in PA.
The second generalisation is due to Kripke, who showed that there is a flexible formula: a formula “whose extension as a set is left undetermined” by PA.
<!--more-->
In particular, he constructed a Σ-1 formula γ(x), such that for every Σ-1 formula σ(x), the theory PA + “γ = σ” is consistent.
This result generalises the first incompleteness theorem, since any instance of such a γ must be independent of PA.
Unfortunately, the straightforward combination of Feferman’s and Kripke’s theorems — the “interpretability of flexibility” — is a false claim.
Indeed, it is easy to show that there can be no Σ-1 formula γ such that for all Σ-1 formulae σ, the theory PA + “γ = σ” is interpretable in PA.

There are, however, several weaker results available, due to Enayat, Hamkins, Shavrukov, Woodin, and me.
These results either (1) relax the restriction on γ, (2) further restrict the allowed choices of σ’s, (3) strengthen the interpreting theory beyond PA, or (4) use equality modulo finite differences.
I will present these four intermediate results, along with the remaining question that they all fail to answer.
Finally, I will discuss why the known proof method does not seem to lend itself to giving a positive answer to this remaining question, as well as explain how any counterexample would have to look.
