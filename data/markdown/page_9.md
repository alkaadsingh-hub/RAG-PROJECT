IEEE TRANSACTIONS ON VISUALIZATION AND COMPUTER GRAPHICS, VOL. XX, NO. XX, XX 2018
10
a learning-to-rank problem that learns to rank visualizations from
crowdsourced data. Retrieve-then-Adapt [1] extends the learning-to-
rank model that simultaneously outputs paired scores. VizDeck [54]
learns a linear scoring function from users’ up- and downvotes.
VizNet [43] demonstrates the feasibility of training a machine-
learning model to predict the effectiveness of visual encodings.
Nevertheless, those machine-learning approaches face two
major challenges, including poor generalisability and explainability.
First, the aforementioned models are trained over statistical or
visual encoding properties, assuming the underlying dataset and
speciﬁcation is available. More importantly, they only support a
limited number of chart types. To that end, Fu et al. [61] propose
a more general approach to assess the quality of visualization
images that generalizes to different visualization type and does
not require additional information except the visualization images.
Second, machine-learning models lack explainability that might
decrease trust. Moreover, they often exclude knowledge derived
from empirical studies. To address these limitations, Draco [49]
takes a hybrid perspective by encoding design knowledge as
constraints and learning a weighting function to trade off those
constraints, whereby outputting a ﬁnal score.
6.2.2
Discussion and Open Questions
Existing approaches predominately focus on objective qualities
that can be measured via user studies (e.g., task performance and
competition time). However, subjective metrics such as aesthetics
are relatively underexplored, despite that they are considered as
important features of good visualizations [116]. This is challenging
since it is difﬁcult to harvest crowdsourced data of subjective
quality of visualizations, since crowdsourced judgments can be
inconsistent and inaccurate. This underscores research needs
to propose methods for generating large-scale training datasets
for visualization research in a reliable and sustainable manner.
One promising way is to incorporate expert knowledge and
crowdsourcing experiments in dataset generation.
Going forward, we envision machine-learning approaches
that not only assess the visualization but also provide insightful
explanations. In this way, the approaches embrace explainability
by translating ML models into human-readable explanations and
even useful design guidelines.
6.3
Comparison
Characterizing the similarity or other metrics between two visual-
izations is helpful when dealing with a visualization collection.
Comparison
Visualization
Visualization
Numercial Value
Fig. 8. Input-output model of comparison.
Relations to goals and other tasks. Comparison is found to
assist in visualization generation and analysis. The comparison
metrics can be used as cost-functions in 1) recommendation to
perform anchor-based visualization generation (e.g., [81]), as well
as 2) querying to perform “query-by-example” (e.g., [8]). Besides,
the assessment metrics can be used to compute the difference.
Relations to visualization data. Comparison is studied on
both visualization programs and graphics, as shown in Table 3.
TABLE 3
Comparison is classiﬁed by the method (row) and the input (column)
Program
Text
Data
Graphics
Distance
[9], [52],
[79]
[8], [93]
[3], [56]
[9], [29], [52], [79],
[81], [117], [118]
Difference
[50], [56],
[119]
6.3.1
Challenges and Methods
Perhaps the most straightforward approach for comparing two
visualizations is to calculate the difference. GraphScape [119] is a
directed graph model where each link represents an edit operation
(e.g., add ﬁeld) and nodes denote the resulting visualizations.
Subsequently, each edit operation is registered with a cost, which
is learned from human judgments. Dziban [50] further translates
the graph model into a set of constraints and weights, similar
to Draco [49]. In this way, both approaches explicitly model the
difference between two charts as an operation associated with
a numerical cost. Nevertheless, this difference-based approach
becomes sophisticated when there exist multiple, often under-
speciﬁed, operations between two charts, where graph traversal is
essential for searching and weighting all possible paths. This is
further complicated by the limitation that GraphScape only includes
operations regarding data transformation and visual encodings.
Although it is methodologically feasible to extend GraphScape to
support other operations such as recoloring, such extensions are
labor-intensive, without a guarantee for exhaustiveness.
Partly due to the above challenges of difference-based methods,
most research adopts distance-based measurements [3], [8], [9],
[29], [52], [56], [79], [81], [93], [117], [118]. The key idea is to
convert a visualization into a feature vector, and compute the dis-
tance between two feature vectors according to distance functions.
Thus, the technical challenges of distance-based measurements are
two-fold: the choice of features and the distance function.
The features of visualizations vary among the underlying
sources, as discussed in subsubsection 4.2.2. In the context of
comparison, we identify four primary sources including graphics,
text, data, and speciﬁcations. For instance, Saleh et al. [93] extract
low-level visual features from graphics to learn style similarity,
and Chen et al. [8] model the conﬁguration pattern of multiple-
view visualization systems as a 1×126 vector measuring the layout.
Regarding text features, VizCommender [3] uses both hand-crafted
features (e.g., TF-IDF) and learned features (e.g., Doc2Vec). More
work uses hand-crafted features for the data [29], [81], [117], [118].
Finally, ChartSeer [9] uses deep learning approaches to convert
Vega-Lite speciﬁcations into embeddings.
The derived features are subsequently fed into a distance
function to derive the distance. Examples of common distance
functions include mutual information [8], [117], Earth Mover’s
Distance [29], [81], Bhattacharyya coefﬁcient [118], and Jaccard
coefﬁcient [79]. Nevertheless, the process of selecting distance
functions is hardly detailed in the literature, leaving rationales and
insights unexplored. This is worsened by the potential downside of
distance-based measurements that the feature representation is less
interpretable than the operations in difference-based measurements.
Thus, it is often difﬁcult to interpret the results, and the user study
suggests that the similarity measurement “does not fully understand
their (users’) intent” [9].
An important question that then arises is how to measure
the overall similarity when combining multiple sources. Naive
feature concatenation is a natural way to combine features from
