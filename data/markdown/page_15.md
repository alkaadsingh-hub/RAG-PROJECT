IEEE TRANSACTIONS ON VISUALIZATION AND COMPUTER GRAPHICS, VOL. XX, NO. XX, XX 2018
16
to incorporate that knowledge in ML models that is tailored to
visualization research, e.g., Draco [49].
7.3
A Big Data Perspective to Visualization Data
This survey highlights the theme of considering visualizations
as a data type. Moving forward, an evolving and promising
theme is big visualization data, which concerns processing and
analyzing visualization data at larger scales. This theme leads
to several new issues that deserve research efforts. Visualization
database systems should effectively store and manage visualizations
that are heterogeneous and often unstructured. Moreover, it is
unclear how to mine and analyze big visualization data, since
existing approaches mainly focus on small-scale visualization
collections and use simple statistics. These challenges demand a
holistic adaptation of data mining techniques to visualization data,
including but not limited to data cleaning, data transformation,
data reduction, feature extraction and analysis. For instance, when
collecting visualization datasets by web crawling, it is important to
clean the visualization collection by removing noise such as non-
visualization images. Therefore, there are still many open research
topics in terms of analyzing big visualization data.
7.4
Human-Visualization Ecosystem
Although this survey treats visualizations as data processed by AI,
we emphasize that visualizations are designed for and arguably
central to humans. Therefore, it is important to establish the
broader human-visualization ecosystem that AI could engage in
and contribute to. As discussed in section 4, there is a tradeoff
between human- and machine-friendliness of visualization data
formats that awaits better solutions. It is also helpful to identify
the limitations of AI approaches, which offers possibilities of
proposing mixed-initiative approaches (e.g., [115]). Besides, it is
promising to collect data regarding how humans perceive, assess
and use visualizations at scale, which empowers AI to learn new
insights and enable learning-based methods for visualization and
visual analytics [15]. Finally, as many AI approaches focus on
routine tasks (e.g., querying), a critical question arises of how AI
could engage humans in creative practices such as creating novel
visualizations (e.g., [143]).
8
DISCUSSION AND LIMITATION
In this section, we discuss the limitations in terms of mutual exclu-
siveness and collective exhaustiveness, as well as generalizability.
8.1
Exclusiveness and Exhaustiveness
In this survey, we use an inductive approach to organize the
literature and construct our taxonomy by observing existing work
and iteratively generalizing the classiﬁcation.
We note several dependencies among tasks. For instance,
assessment and comparison metrics are often used as optimization
functions for recommendation. However, those dependencies
should not be interpreted as violations of mutual exclusiveness.
Instead, dependencies suggest that tasks can be sequentially
combined into a system pipeline for solving complex problems.
Because we inductively collected the papers for this survey,
we do not claim that our taxonomy is exhaustive. There exist
many potential research questions that we have not observed yet.
It would be interesting to improve the taxonomy from a deductive
perspective by referring to task taxonomies in related ﬁelds such as
computer vision, artiﬁcial intelligence, and databases. For instance,
image compression and style transfer are well-studied tasks in
the computer vision community [28], which, however, remain
unexplored in the context of visualizations. That said, there exist
promising directions for future research of AI4VIS.
8.2
Generalization to Visualizations Beyond Charts
This survey makes simplifying assumptions by focusing on charts
and infographics, excluding scientiﬁc visualizations and work
tailored for a speciﬁc type of visualizations. An important concern
is how to generalize or extend the taxonomy to a wider spectrum
of visualization data. During our analysis process, we ﬁnd several
exceptions that warrant future improvement. In the following text,
we discuss notable extensions to our what-why-how taxonomy.
What. Our what taxonomy primarily focuses on visualization
data. However, visualizations are hardly considered as standalone
data in AI-empowered systems. Instead, it is often necessary to
provide ground-truth labels for visualizations as auxiliary data, e.g.,
chart types [31]. Another type of auxiliary data is user-generated,
i.e., interaction logs [144] and analysis provenance [15]. Future
research should study the taxonomy of auxiliary data to better
contextualize the opportunities for AI for visualization research.
Why. The why taxonomy is organized along two axes: single
or many visualizations versus inputting or outputting visualizations.
A missing perspective lies in work that neither inputs nor outputs
visualizations but instead exploits visualization data in the middle
stage. For instance, Lall´e et al. [145] collected eye-tracking data
when browsing visualizations and trained an ML model to predict
the learning curves of visualizations. Our survey does not cover
this kind of research due to our theme centered on considering
visualization as a data format, emphasizing how visualization data
are processed and produced. Another perspective for improving our
taxonomy is to expand the sub-categories by adding goals that are
currently conﬁned to a particular visualization. For instance, deep
learning methods for brushing point visualizations [144], [146] or
drawing graphs [147] fall under visualization enhancement and
generation category, respectively.
How. Echoing the above discussion about “what”, there exist
corresponding needs of identifying tasks for processing and
analyzing auxiliary data. This is crucial since our current task
taxonomy concerns visualization data. Moreover, we notice another
potential task for visualization data, namely visualization collection
summarization that aims to represent visualization collections in an
effective and compact manner. However, existing approaches are
limited and speciﬁc to visualization types, e.g., Scagnostics for scat-
terplots [140] and line charts [141]. In addition to those statistical
summarization approaches, more recent visual analytic approaches
use glyphs [9]. Future work could provide a systematical overview
of visualization summarization with increasing research efforts.
9
CONCLUSION
This survey probes the concept of considering visualizations as
an emerging data format and investigate the advance of applying
artiﬁcial intelligence to visualization data (AI4VIS). We present
a novel classiﬁcation that enables the readers to ﬁnd relevant
literature among a wide variety of research areas. Our classiﬁcation
can also help readers to understand current techniques and ﬁnd
areas for future research. We hope that our survey could help
stimulate new theories, problems, techniques, and applications.
