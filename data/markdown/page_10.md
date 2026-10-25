IEEE TRANSACTIONS ON VISUALIZATION AND COMPUTER GRAPHICS, VOL. XX, NO. XX, XX 2018
11
different sources [29], [79]. For instance, Luo et al. [52] propose
a feature vector concatenated from ﬁve aspects, each represented
by a one-hot vector describing visualization types, x-axis, y-
axis, group/bin operations, and aggregation functions. Another
method is to compute the aggregated distance by weighting
hybrid distances, e.g., chart encoding distance, keyword tagging
distance, and dimensional interaction distance by Xu et al. [56].
Nevertheless, both feature concatenation and distance aggregation
assume a linear relationship among different vectors, which seems
far from capturing the real-world complexity and thus yield limited
performances when perceived by users.
6.3.2
Discussion and Open Questions
Comparison and assessment are closely related and share the
same goal of outputting a numerical score. Comparison has been
predominately rooted in feature engineering and hand-crafted
distance functions. The major downside is that it does not actually
learn from user feedback and thus usually fails to meet the users’
intent. Unlike assessment, few little machine learning approaches
have been applied to comparison. Several approaches (e.g., [56])
use pre-trained ML models to perform feature learning. However,
they do not ﬁne-tune the models on user feedback data. Thus,
proposing dataset and ML approaches for comparison is a clear
step to improve the performance.
Nevertheless, it is non-trivial to adapt ML approaches to
comparison, since comparison involves two visualizations while
standard ML models only take one entity as input. ScatterNet [120]
addresses this issue. It is a deep learning model for predicting
similarities between scatterplots by learning from crowdsourced
human feedback data. Nevertheless, it is unclear how to adapt this
approach to other statistical charts. A key challenge is that CNN
models used in ScatterNet are worse at capturing human perception
in other charts [61], [66].
6.4
Querying
Querying is the task of retrieving relevant visualizations that
satisfy the users’ needs from a visualization collection. It is a
crucial component of Information Retrieval (IR) systems, which
are also known as search engines, especially in the context of the
web [121]. Querying in this context is distinct from visualization
query language (Figure 4 B ). The latter speciﬁes visualizations as
a query into a database, while the former describes a query into a
visualization collection.
Querying
Input Query
Visualization Collection
Visualization
Fig. 9. Input-output model of querying.
Relations to goals and other tasks. Querying is mainly for
visualization retrieval (Table 4). It is often built upon other tasks
like transformation (e.g., [94]) and comparison (e.g., [8]).
Relations to visualization data. Querying directly in the
image space can be difﬁcult since semantic information is lost.
As such, it is often performed on visualization programs, where
semantic information such as titles and axis labels are available.
6.4.1
Challenges and Methods
There are two viewpoints that characterize querying: how to specify
users’ needs and how to match the needs.
TABLE 4
Querying is classiﬁed by the method (row) and the input (column)
Keywords
Natural
Language
Structural
Example
Exact
[8], [60], [94]
Best
[11], [122]
[123], [124]
[1], [10]
[93]
The simplest form of querying syntax is keywords. Key-
words are popular since they are intuitive and easy to express.
Choudhury and Giles [11] developed a search engine that allowed
users to search ﬁgures by keywords in the captions. Similarly,
Voder [122] supports keyword-based queries into data ﬁelds as
well as general words like ‘outlier’ from the data fact associated
with a visualization. Li et al. [123], [124] extends keywords to
natural language queries by extracting structural keywords from
queries and matching the extracted words with text in visualizations.
Nevertheless, keywords-based queries often fail to disambiguate
unstructured queries since words have multiple meanings.
Structural queries are a mechanism for resolving ambigu-
ity and improving the retrieval quality and have been used in
multiple systems [1], [8], [10], [60], [94]. They are built on
keywords with the addition of structural constraints. For instance,
DiagramFlyer [10] is a search engine where a query contains
eight key structural ﬁelds (e.g., type, x-label, legend) that can
uniquely describe a visualization. Those structural constraints make
it possible to search information more than text in visualizations.
For instance, Retrieve-then-Adapt [1] retrieves infographics based
on a query composed of graphical and textual elements. Notably,
visualization speciﬁcations are a functional candidate for structural
queries. Hoque and Agrawala [94]’s search engine indexes D3
visualizations as Vega-Lite speciﬁcations and supports queries in
the Vega-Lite syntax. Accordingly, it lets users ﬁnd visualizations
based on a wide range of constraints such as mark types, encodings,
and non-data-encoding attributes. In the best case where the input
query is a complete Vega-Lite speciﬁcation, their research engine
actually supports “query-by-example”.
This example-based query is another format that offers an
intuitive method for users to specify their intent. Saleh et al. [93]
implemented a search engine for stylistic search over infographic
corpora by returning stylistically similar images given a query
image. However, more sophisticated analysis methods are necessary
to capture characteristics beyond stylistic similarities.
Now that we have discussed the query syntax, the next challenge
is how to reason which visualizations are most relevant to the
user-input query, which can be classiﬁed into exact-match and
best-match methods. Exact-match techniques are used for ﬁltering
visualizations by strict conditions, e.g., to retrieve visual analytic
systems containing four views [8], bar charts [94], or charts
describing a dataset [60]. However, exact-matching is not always
possible especially when the input conditions are too strict. As
such, more systems use best-match approaches [1], [10], [11], [93],
[122]–[124] that rank visualizations according to metrics. Those
metrics measure the degree to which a visualization is relevant
to the input query. They use natural language models for text
components (e.g., synonyms [10], [122], text relevance [123], [124])
and similarity metrics [1], [8]. However, relevance or similarity
metrics are insufﬁcient for retrieving visualizations that are not
only relevant but also of high quality. In response, Retrieve-then-
Adapt [1] learns the distribution of visual elements in the corpus
in an attempt to empathize visualizations with common elements,
assuming that the more frequent an element is, the better it is.
