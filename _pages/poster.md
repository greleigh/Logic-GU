---
layout: page
title: Master in Logic in Gothenburg
permalink: MiL/poster
redirect_from: poster
---
{% assign mil = site.data.links['MiL'].url %}

[![Master in Logic poster](/assets/poster.png){: width="40%" style="float: right; border: 15px solid #fff;"}](/assets/poster.pdf)
If you are intrigued by logic and have a bachelor's degree in
Mathematics, Theoretical Philosophy, Computer Science or Linguistics consider
applying to the [Master in Logic at University of Gothenburg]({{mil}}).


## You should study logic iff this sentence is true.



Observe that "iff" is a short-hand for "if and only if". Let's name the
sentence $$A$$&nbsp;:

* $$A$$: "You should study logic iff this sentence is true."

Now, "this sentence" refers to the statement $$A$$ so we may rewrite $$A$$ as:

* $$A$$: "You should study logic iff $$A$$ is true."

If $$A$$ is true then "$$A$$ is true" is true and therefore "you should study
logic" is true. But even if $$A$$ is false "you should study logic" has to be
true. Let's see if we can make sense of this.

## Using propositional logic


We can divide $$A$$ into two less complex statements combined with the
operator $$\leftrightarrow$$:

* $$A$$: "You should study logic" $$\leftrightarrow$$ "$$A$$ is true."

Since $$A$$ and "$$A$$ is true" has the same truth conditions we can simplify
and rewrite it as

* $$A$$: $$B \leftrightarrow A$$

where $$B$$ is "You should study logic." As $$A$$ is the statement $$B
\leftrightarrow A$$ the proposition

*  <span>$$A \leftrightarrow (B \leftrightarrow A)$$</span>

is true (even without knowing if $$A$$ or $$B$$ are true or false.)

Propositional logic is the basic logic used to analyse complex statements in
terms of atomic statements. In this case the atomic statements are $$A$$ and
$$B$$ and these can be either true (T) or false (F):

<table>
<style>
td {
  text-align: center;
}
</style>
<thead>
<tr class="header">
<th>$$A$$</th>
<th>$$B$$</th>
<th> $$B \leftrightarrow A$$ </th>
<th>$$A \leftrightarrow (B \leftrightarrow A)$$</th>
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

The only two cases in which $$A \leftrightarrow (B \leftrightarrow A)$$ is
true is the first and third row. In both of these situations $$B$$ is true
(note that $$A$$ can be both true and false).

Therefore, in all circumstances $$B$$ is true and we have proved (without any
assumptions) that **you should study logic**.