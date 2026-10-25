IEEE TRANSACTIONS ON VISUALIZATION AND COMPUTER GRAPHICS, VOL. XX, NO. XX, XX 2018
5
instance, existing corpora mainly include graphics (e.g., [40]–
[42]) or tabular datasets (e.g., [43]) instead of programs, although
programs are also found to be common in our corpus (42/98). This
suggests the need for more recognition of balancing the machine-
and human-friendliness of visualization formats.
Visualization data often appears as byproducts in different
mediums such as PDF documents [23], computational sheets, and
notebooks [44]. In order for AI to access them, it needs to be able
to recognize and extract visualization data, which brings challenges
for interpreting the medium’s structure, developing conventional
standards, and proposing object detection algorithms. To that end,
recent research in parsing and analyzing visualization notebooks
seems a promising direction [3].
4.2
Representation
Now that we have considered different content formats of raw
visualization data, the next challenge is its representation. Firstly,
raw visualization data in the format of images or programs
might not explicitly represent the semantic information needed
(e.g., chart type). Thus, it is usually helpful to store and operate
visualization data in the internal representation formats to facilitate
the process. Secondly, raw data need to be converted into feature
representation to enable machine-learning techniques. Thus, we
discuss feature engineering and feature learning approaches used
to extract visualization features.
4.2.1
Internal Representation
Visualization programs tend to contain extraneous details (e.g.,
visual style) or miss semantics (e.g., chart type) that might
not meet particular needs of research. Thus, systems usually
express and operate on visualizations in simpler or more structured
formats by removing unwanted or unnecessary speciﬁcations and
Fig. 4. Internal representations of visualizations: A logic programming
maps speciﬁcations into logic facts for computation [49]; B relational
programming expresses visualizations in query language for relational op-
erations such as selection [53]; C set-theoretic programming facilitates
set operations [75].
adding customized information, which we refer to as internal
representations. However, we only ﬁnd 13 papers that explicitly
propose formal internal representation formats that are designed
towards the high-level goal of facilitating computation (Figure 4).
Draco [49] (Figure 4 A ) uses Answer Set Programming to
express visualization speciﬁcations as logical facts. This falls into
logic programming [76], which expresses problem domains as
facts or rules and beneﬁts logical computation. For instance, logical
facts are used to check whether the speciﬁcations satisfy compound
rules regarding the design knowledge.
Literature from data mining and databases [29], [52], [53], [55],
[77]–[82] usually uses relational programming to form visual-
izations as queries into database (Figure 4 B ). Those relational
queries facilitate operations on collections of visualizations such as
composing, ﬁltering, and sorting. This paradigm is also adopted by
the CompassQL language in Voyager [83]–[85].
Finally, Wang et al. [75] proposed a set-theoretic program-
ming representation that describes charts as a set of visual elements
(Figure 4 C ), which facilitates set computation, e.g., to determine
whether a visualization is a super-set of another.
4.2.2
Feature Representation
In this section, we discuss the features of visualizations, which are
the measurable properties serving as the input to machine learning
models. Features are extracted by feature engineering or feature
learning [86]. Feature engineering is the process of using domain
knowledge to extract features from raw data, while feature learning
replaces this manual process by developing automated approaches
that automatically discover useful representations. The features of
visualization data are multimodal, including graphics, program,
text, and underlying data (Table 1). Some papers use multiple
features for different tasks [31], [46] or use hybrids by feature
fusion for improving performances [32], [45], [51], [56]. In the
following text, we describe each category in detail.
Graphical features are the most common features of visu-
alizations. The overarching goal is for predictive tasks, e.g.,
to predict the chart type, or detection tasks. Early work uses
general image descriptors such as bag-of-keypoints [45] or patch
descriptors [32]. These descriptors are designed for general visual
content, containing only low-level information such as shapes
and regions. To raise the level of abstraction, researchers have
proposed special domain descriptors for visualization-speciﬁc
information, and in many cases outperform general descriptors
(e.g., [31]). Examples include regions of text elements (e.g., titles
and labels) [32], positions of text and mark elements [31], [40],
[46], relative positions between text and marks [47], and visual
styles of elements [40]. Despite promising results, such feature
engineering process remains labor-intensive and requires expertise.
Besides, it remains unclear whether human-crafted features are
informative and discriminating for accomplishing machine learning
tasks. Therefore, recent work has adopted feature learning more
than feature engineering (e.g., 12 versus 7 in 2020). Particularly,
convolutional neural networks (CNNs) have been widely used
to automatically learn spatial hierarchies of image features and
shown to outperform early approaches [12], [13], [31], [46], [51],
[57]–[60], [62]–[72]. VisCode [6] recently uses an autoencoder
to learn an effective representation that could conceal additional
information. Fu et al. [61] used the latent vectors of the autoencoder
model for prediction tasks. However, these models currently face
the same challenge as early general image descriptors in that
they might not capture visualization-speciﬁc information. This
