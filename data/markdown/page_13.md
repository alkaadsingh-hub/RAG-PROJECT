IEEE TRANSACTIONS ON VISUALIZATION AND COMPUTER GRAPHICS, VOL. XX, NO. XX, XX 2018
14
the increasing availability of datasets. Draco [49] and Dziban [50]
learn to assess visualizations by weighting design rules for visu-
alizations. Subsequently, they formulate a constraint optimization
problem to recommend the best or top-k visualizations. As
discussed, such approaches combining assessment and optimization
are commonly adopted for recommending insights. Other ML
approaches seek to directly learn the mappings between data
and visual encodings by training an end-to-end model, including
Data2Vis [74], VizML [38], and DataShot [88].
In addition to data encodings, other approaches study how to
recommend non-data-encoding attributes such as layouts and colors.
Most approaches formulate optimization problems with the primary
goal to deﬁne the optimization target, that is, the assessment metrics.
Several metrics are human-crafted cost functions [2], [5], [59],
[90], [106], while other metrics are data-driven, including machine
learning models trained on human assessment dataset [1] and
distances to common patterns mined from a corpus [95]. Several
systems contribute novel optimization algorithms to improve
efﬁciency, including reinforcement learning [2] and Markov chain
Monte Carlo methods [1]. Similar to recommending top-k insights,
both algorithms are progressive.
Hybrid Recommendation decides both data and encodings. A
straightforward approach for hybrid recommendation is to combine
data and encoding recommendation sequentially. This approach
is widely implemented in visualization recommenders including
DataVizard [135], DataSite [128], Proﬁler [117], Calliope [4],
Voder [138], and DataShot [88]. Other approaches take an end-
to-end perspective, formulating the recommendation tasks as an
optimization problem. Examples are Voyager [83], [85], DeepEye
and its extensions [52], [53], [55]. Thus, the core problem is
to provide an overall assessment score regarding both the data
and encodings. The ﬁrst step is to translate a visualization into a
formal representation, i.e., visualization query language (VQL).
Assessment metrics are then proposed to evaluate the quality of
a VQL representation. Finally, Voyager ranks the recommended
visualizations, while DeepEye proposes efﬁcient algorithms to
generate the top-k visualizations.
6.6.2
Discussion and Open Questions
An ongoing discussion in recommending visualizations is the
problem formulation including optimization and prediction. Op-
timization requires the careful design of optimization functions
which are often the assessment scores. Another important concern
is the efﬁcient algorithms for solving the complex, sometimes
multi-objective, optimization problem due to the huge design
space of visualizations. Generally speaking, optimization-based
approaches have the potential to be extended to the human-in-the-
loop approaches, since the predicted assessment scores help users
determine the visualization quality. Nevertheless, hand-crafted cost
functions for assessment are often insufﬁcient. On the other hand,
machine learning assessment requires massive training data that
labels human assessment and therefore is expensive. In contrast,
prediction-based approaches such as VizML [38] only demand
training data describing the dataset and visualizations without the
need for human labeling. This reduces the overhead of constructing
dataset and thus helps boost the performance. Thus, the above
discussion opens up many interesting general questions: How
to interpret the prediction-based ML models to understand the
reasoning process and potentially derive assessment scores? How
to reduce the costs for collecting training datasets?
There exist other research gaps with respect to recommendation.
For instance, few ML approaches have yet been applied to
recommend insights and non-data-encodings. Is it beneﬁcial to
collect training data for those tasks such as predicting important
data ﬁelds given a data table? Besides, many existing approaches
only recommend top-k, separated visualizations given a large data
table, while it is unlikely that “top-k visualizations ﬁt all”. Future
research should study how to recommend dashboards, and even
visual analytics systems for more comprehensive and intelligent
data analysis. Generating a coherent data story compromising of
multiple data facts is another interesting question. Finally, existing
systems are conﬁned to well-known charts. Recent research in
computer vision has proposed generative models for generating
synthetic images. An interesting question is to apply generative
models to recommend synthetic, novel visualizations.
6.7
Mining
Mining is an emerging task motivated by the rapid popularization
and accumulation of visualization data online (Table 7). Generally,
there are two kinds of mining tasks, i.e., mining design patterns
and mining data patterns, that are discussed in the following text.
Mining
Visualization Collection
Patterns
Fig. 12. Input-output model of mining.
Relations to goals and other tasks. The goal of mining is
visualization analysis, i.e., to discover useful information or patterns
from a visualization collection. Reverse-engineering is often a
prerequisite for mining to obtain semantic information.
Relations to visualization data. Reasoning is studied on both
visualization graphics and programs.
6.7.1
Challenges and Methods
Mining Design Patterns. The concept of design mining refers
to leveraging data mining techniques to derive design principles
from existing artifacts. Smart et al. [95] formally introduced design
mining in visualizations and proposed an unsupervised clustering
technique to derive common color ramps. However, design mining
has been implicitly practiced in several early systems but for
different goals. Choudhury and Giles [11] investigate the design
patterns (e.g., colored or not) of 300 line graphs sampled from
top computer science conferences. Viziometrics [42] computes the
average number of visualizations in academic papers from different
research domains. In the visualization community, Beagle [40]
automatically crawled SVG-based visualizations online to investi-
gate how popular, e.g., line and bar charts are on the web. Hoque
and Agrawala [94] performed a design demographics analysis
of 7,860 D3 visualizations to identify common patterns such as
how frequently circles are used. More recently, Chen et al. [8]
studied the composition and conﬁguration patterns in multiple-
view visualizations collected from visualization papers.
TABLE 7
Mining is classiﬁed by the class (row) and the method (column)
Statistics
Clustering
Visual Analysis
Design Pattern
[8], [11], [40],
[42], [94]
[95]
Data Pattern
[9], [56]
