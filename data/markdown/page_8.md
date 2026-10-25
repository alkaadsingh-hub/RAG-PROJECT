IEEE TRANSACTIONS ON VISUALIZATION AND COMPUTER GRAPHICS, VOL. XX, NO. XX, XX 2018
9
TABLE 2
The assessment task is classiﬁed by the output (row) and the method (column)
Rule-based
Machine Learning
Hybrid
Rankings
effectiveness rankings [87]
learning-to-rank [52], [53], [55], [58]
Scores
convert rankings to scores [49], [84], [85]
hand-crafted metrics [2], [5], [6], [77], [78], [90], [106]–[108]
learning-to-rank with scores [1]
predictive regression [43], [54], [61]
learning-to-weight
hand-crafted metrics [49]
instance, Poco and Heer [31] trained a classiﬁer to detect area, bar,
line, and plotting shapes, and consequently grouped shapes by types.
To support customized visualizations, several approaches [2], [34],
[89], [94], [100] use the node hierarchy information to group shape
nodes under the same ancestor. Nevertheless, those approaches
are only applicable to vector graphics. Finally, the shape clusters
are associated with the text clusters to identify axes, legends, and
label-mark relationships.
Composing. After the visualization graphic has been de-
composed into semantic groups (e.g., guides and marks), the
composing phase (Figure 6 B ) aims to extract the visual encoding
and/or the underlying data from this semantic information. Different
from the decomposing phase that uses computer vision and machine
learning tasks, this composing phase mainly uses heuristics by
leveraging domain knowledge about visualizations. We ﬁnd two
common methodological themes of those heuristics, depending on
whether the chart type has been extracted from the previous phase.
The ﬁrst class of heuristics uses information about the chart
type and guides to determine the scale and the encoding, which
is dominant in our corpus [32], [45]–[47], [60], [62], [91], [109]–
[111], [113]. For instance, given a scatterplot with axes and legends,
it is straightforward to derive the visual encodings, i.e., the x/y
positions maps to numerical values and the color encodes the
categorical data, and to calculate the scale. Consequently, the
underlying data could be computed via applying the reserve scale
computations over the marks. However, those heuristics are often
limited to a small set of chart types.
Another class [34], [89], [94] studies the more challenging
problem of decoding bespoke visualizations where the chart type is
unknown. However, they focus on D3 charts where the underlying
data is available by crawling the SVG node on the web. In this way,
they develop heuristics to determine the scale from guides and data,
and to derive the encoding from data and marks.
6.1.2
Discussion and Open Questions
In conclusion, it remains an open challenge to derive both the
visual encoding and the underlying data from bespoke visualization
graphics, whose chart types are not limited to common ones.
An important future research direction would be to improve the
current heuristics for determining visual encodings from bespoke
visualizations, i.e., by machine-learning approaches.
Another primary challenge of reverse engineering lies in
robustness and accuracy. The pipeline of reverse engineering
usually consists of multiple sequentially dependent tasks that are
prone to single points of failure; that is, the failure of one task
would spread to the whole system. For instance, common failure
cases such as text detection would impede the extraction of guides
and consequently the visual encoding [31], [91].
This motivates the use of semi-automatic approaches that
address imperfect algorithms with human intervention [92], [114],
[115]. Nevertheless, those frameworks of incorporating automatic
algorithms with human intervention are speciﬁc to chart types
and therefore not readily applicable to more general situations. A
related research direction is to investigate a general framework for
deconstructing bespoke visualizations.
6.2
Assessment
There is a long history of research on teaching machines to assess
and rank the quality of data visualizations. As shown in Table 2,
assessment outputs a numerical score of the visualization quality
or measures the relative quality in terms of ranking.
Assessment
Visualization
Scores/Ranking
Fig. 7. Input-output model of assessment.
Relations to goals and other tasks. The key motivation of
assessment is to improve visualization design, e.g., to derive scoring
metrics that can be used as cost functions for automatic generation.
That said, assessment is often combined with recommendation.
Relations to visualization data. Most surveyed techniques
take visualization programs as input, focusing on the visual
encoding and data quality. Nevertheless, Fu et al. [61] propose an
approach for assessing visualization images.
6.2.1
Challenges and Methods
Assessment is challenging due to the human-centered nature of
visualizations that requires large-scale empirical experiments to
understand what makes a visualization “good”. However, the
knowledge derived from large-scale empirical experiments is often
represented as design guidelines instead of quantiﬁable rules. As
such, much research aims to quantify knowledge about “good”
visualizations. In 1986, Mackinlay [87] developed the APT system
that ranked the effectiveness according to the accuracy rankings of
quantitative perceptual tasks for different visual encoding channels.
However, this ranking-based approach only reﬂects the relative
quality of visualizations. Scoring-based approaches are often more
desirable since scores measure the absolute quality and therefore
beneﬁt down-streaming tasks, e.g., scores can be used as the cost
function for optimization. To that end, Voyager [84], [85] and
Draco [49] map different single-criteria rankings to numerical
scores. Besides, researchers often leverage domain knowledge
to design hand-crafted, rule-based metrics that measures the
visualization quality such as informativeness [90], interesting-
ness [77], [78], [106], accuracy [77], [78], signiﬁcance [107],
saliency [108], visual importance [6], complexity [5], and mobile-
friendliness [2]. However, designing hand-crafted metrics usually
requires considerable effort. More critically, the design process
is often unsystematic and lacks a strong methodological base.
For example, Wu et al. [2] demonstrated that even seemingly
reasonable metrics do not always survive experimental scrutiny.
Besides, questions arise about how to weigh scores to reﬂect the
overall, multi-criteria quality. Several systems [5], [77], [78], [84],
[85], [90] determine the weights for each score through manual
reﬁnements that could become unsystematic.
As such, another line of research seeks to propose more
systematical machine learning approaches that learn to rank
and/or score visualizations from data collected from empirical
studies. VizByWiki [58] and DeepEye [52], [53], [55] formulate
