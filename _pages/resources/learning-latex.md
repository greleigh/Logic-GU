---
layout: page
title: Learning LaTeX
---
{% assign latex = "https://www.latex-project.org" %}
{% assign latex4logic = "https://www.logicmatters.net/latex-for-logicians" %}
{% assign latex-wb = "https://en.wikibooks.org/wiki/LaTeX" %}
{% assign ol = "https://www.overleaf.com" %}
{% assign ol-learn = "https://www.overleaf.com/learn/latex/" %}
{% assign tex-se = "https://tex.stackexchange.com" %}
{% assign ctan = "https://www.ctan.org" %}
{% assign ctan-pkg = "https://www.ctan.org/pkg/" %}
{% assign learn-beamer = "/beamer" | prepend: ol-learn %}

[LaTeX]({{ latex }}) is a document preparation system for creating technical and scientific documents. It is especially useful for typesetting logic with its plethora of special symbols. The Logical Theory textbook, as well as most of our lecture notes/slides are all produced using LaTeX.

Writing in LaTeX is much simpler than using a word processor like Word. A LaTeX file is just a plain text file containing the content of your document and a few special commands describing the structure of your document. If you are familiar with basic html or markdown (both used extensively in web design) you will be at home with LaTeX. Feeding this text file to LaTeX will produce a pdf of the document.

# Getting started

Nowadays you can write LaTeX documents on the web without needing to download and install anything. A popular online LaTeX tool is [Overleaf](https://www.overleaf.com/).

1. Start with the [*Learn LaTeX in 30 minutes*]({{ ol-learn }}Learn_LaTeX_in_30_minutes) guide.
2. Learn the interface provided by Overleaf by [creating a document in Overleaf](https://www.overleaf.com/learn/how-to/Creating_a_document_in_Overleaf).
3. The [LaTeX Wikibook]({{ latex-wb }}) is an excellant resource for learning about the more advanced features of LaTeX.


# Logic in LaTeX

LaTeX is an excellent tool for typesetting mathematical notation. The basics of this are covered in the *Learn LaTeX in 30 minutes* guide listed above. More functionality is provided through *packages* which is usually as simple as adding `\usepackage{package-name}` to the preamble of your document (i.e., somewhere above `\begin{document}`).

1. Read the [documentation on typesetting mathematics in LaTeX]({{ ol-learn }}/Mathematical_expressions) provided by Overleaf. This guide also introduces the mathematics package `amsmath` that introduces the most common mathematical symbols, provides better support for equations, and much more. See also the [list of further reading]({{ ol-learn }}/Mathematical_expressions#Further_reading) provided at the end of the guide and the [LaTeX wikibook on using `amsmath`]({{ latex-wb }}/Advanced_Mathematics).
2. Check out the logic related tips you can find at the [LaTeX for Logicians page]({{ latex4logic }}), ranging from logic-specific symbols to writing truth-tables and proof trees.
3. Visit the [TeX StackExchange]({{ tex-se }}) for answers to your LaTeX questions.
4. If you need to figure out how to display a particular symbol in LaTeX, [detexify](https://detexify.kirelabs.org/classify.html) is your tool: you just paste or draw the symbol you want and that site will tell you the command.
5. See the [LaTeX miscellany](#a-latex-miscellany) below our own recommendations.

# Beam your logic with Beamer

At some point you will want to present your labour to others. Beamer is a LaTeX class for creating presentations.

1. Learn how to [create a presentation]({{ learn-beamer }}) in Beamer.
1. Use a [beamer template](https://www.overleaf.com/latex/templates/beamer-presentation/jvmwtkmnqtpp) to create your own presentation.

# A LaTeX miscellany

There are thousands of LaTeX packages. These can be adding new symbols, new design templates, or new functionality. Here is a brief (and highly personal) recommendation. All of the following are included in the standard LaTeX setup and their documentation is available through the [Comprehensive TeX Archive Network (CTAN)]({{ ctan }}); simply search for the package name on that site.

## Logic specific

- **Alphabets** You can never have too many ‘x’s. The `amsmath` package implements the caligraphic and fraktur scripts. Use these sparingly: your work is to be read, not framed!
- **Proof trees** Whether its natural deduction, tableaux or sequent calculus, we all need to typeset a formal proof at somepoint in our lifetime. The LaTeX for Logicians page has a separate entry on [typesetting natural deduction proofs]({{ latex4logic }}/nd/) with links to different packages. I recommend `ebproof` and `bussproofs`. The latter package (and its extension `bussproofs-extra`) is used in the [Open Logic Text]({{ site.data.links['open-logic'].url }}). 
- **Automata** The TikZ package provides an extensive (and quite scary) toolkit for building figures and graphics within LaTeX. Search the [TeXample database](https://texample.net) for what you need and adapt from there.

## General packages

- Theorems, lemmas and proofs, oh my! The `amsthm` package is the classic. A modern alternative is provided by `thmtools`.
- Internal links. The `hyperref` package to the rescue. I recommend the overview in [the LaTeX wikibook]({{ latex-wb }}/Hyperlinks). To reduce the chance of another package conflictin with `hyperref` it is recommended to be the *last* package loaded.
