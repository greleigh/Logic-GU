---
layout: poster
title: You should study logic iff this sentence is true.
---
{% assign wiki = "https://en.wikipedia.org/wiki/Liar_paradox" %}
{% assign mil = "https://www.gu.se/en/study-gothenburg/logic-masters-programme-h2log" %}

Observe that "iff" is a short-hand for "if and only if".

## Understanding the statement

Let's name the statement $A$ to easier talk about it:

* $A$: "You should study logic iff this sentence is true."

Now, "this sentence" refers to the statement $A$ so we may rewrite $A$ as:

* $A$: "You should study logic iff $A$ is true."

We can now divide $A$ into two less complex statements combined with the
operator $\leftrightarrow$:

* $A$: "You should study logic" $\leftrightarrow$ "$A$ is true."

Since $A$ and "$A$ is true" has the same truth conditions we can simplify and
rewrite it as

* $A$: $B \leftrightarrow A$

where $B$ is "You should study logic." As $A$ is the statement $B
\leftrightarrow A$ the proposiiton

*   $A \leftrightarrow (B \leftrightarrow A)$ 

has to be true.

## Analyzing it using propositional logic

Propositional logic is the basic logic used to analyse complex statements in
term atomic statements. In this case the atomic statements are $A$ and $B$ and
these can be either true (T) or false (F):

<table>
<style>
td {
  text-align: center;
}
</style>
<thead>
<tr class="header">
<th>$A$</th>
<th>$B$</th>
<th> $B \leftrightarrow A$ </th>
<th>$A \leftrightarrow (B \leftrightarrow A)$</th>
</tr>
</thead>
<tbody>
<tr>
	<td>T</td><td>T</td><td>T</td><td markdown="span">**T**</td>
</tr>
<tr>
	<td>T</td><td>F</td><td>F</td><td>F</td>
</tr>
<tr>
	<td>F</td><td>T</td><td>F</td><td markdown="span">**T**</td>
</tr>
<tr>
	<td>F</td><td>F</td><td>T</td><td>F</td>
</tr>
</tbody>
</table>

The only two cases in which $A \leftrightarrow (B \leftrightarrow A)$ is the
first and third row, where $B$ is true as well.

Therefore, $B$ is true and **you should study logic**.

## Paradoxes

This statement is "self referential", but not paradoxical. However, it's easy
to come with a self refential paradoxical statement:

* L: "This sentence is false."

That statement is paradoxical in that we can prove that if it is true, then it
is false. And if it is false, then it is true. Thus, we can prove that it's
both true and false at the same time.

L is called the "Liar sentence", and you can read more about it and other
paradoxes at the [Wikipedia page]({{wiki}}).

## Study logic

If you intrigued by logic and paradoxes and have a bachelor's degree in
Mathematics, Theoretical Philosophy, Computer Science or Linguistics consider
applying to the [Master in Logic at University of Gothenburg]({{mil}}).
