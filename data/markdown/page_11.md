IEEE TRANSACTIONS ON VISUALIZATION AND COMPUTER GRAPHICS, VOL. XX, NO. XX, XX 2018
12
6.4.2
Discussion and Open Questions
Research on indexing visualizations has been relatively limited in
the past decade, leaving room to boost technical development. Due
to the diversity of visualizations, even state-of-the-art methods are
often restricted to certain types of visualizations, e.g., proportion-
related infographics [1] or basic D3 visualizations [94]. How
to generalize those approaches to more types of visualizations
is a non-trivial issue that requires a deeper understanding of
how visualizations should be indexed. For instance, Hoque and
Agrawala’s approach [94] indexes D3 visualizations in Vega-Lite
syntax, which is insufﬁcient in expressing user queries such as
“sunburst diagrams”. Indexing becomes more challenging when
applying to raster graphics (bitmap images) that deserve research
efforts, e.g., reverse engineering.
The intention gap is another challenge for querying visual-
izations. From a theoretical perspective, there are not enough
empirical studies to understand the user needs in searching for
visualizations. Such studies are formative approaches to motivate
the design space of the indexes of visualizations. In a related venue,
Oppermann et al. [3] recently found that information seeking is
a core task when browsing visualization repositories, and that
users were more interested in content rather than styles. Similar
studies are needed to survey users and inform the design of future
search engines for visualization. From a practical perspective, it
is crucial to design convenient query interfaces that assist users
in specifying their intent. For instance, it is easy for users to
specify the region of interest on an example visualization and
interactively browse the results. Hoque and Agrawala’s query-by-
example feature seems a promising start. We also notice a large
body of research that studies query-by-pattern or query-by-sketch
in time-series visualizations, e.g., [125], [126]. Future work could
generalize those query paradigms to all visualization types.
6.5
Reasoning
Reasoning challenges machines to “read charts made for hu-
mans” [16]. Reasoning requires interpreting visualizations to
derive high-level information such as insights beyond extracting
visual encoding and data via reverse engineering. Reasoning is
distinct from assessment since reasoning usually outputs semantic
information (e.g., insights, text summaries) rather than a numerical
score. As shown in Table 5, we ﬁnd three common classes
depending on the targeted output of the reasoning process: visual
perceptual learning, chart summarization, and visual question
answering. We ﬁrst describe each class separately, followed by an
organized discussion of existing methods and research gaps.
Reasoning
Visualization
Semantic Information (insights, text 
summary, answers etc)
Fig. 10. Input-output model of reasoning.
Relations to goals and other tasks. Reasoning is mainly
for visualization enhancement (e.g., summarize natural language
descriptions [73]). It sometimes relies on reverse engineering to
improve the algorithm performance (e.g., [96]).
Relations to visualization data. Reasoning is studied on both
visualization images and programs.
6.5.1
Challenges and Methods
Visual perceptual learning aims to solve visual tasks by analyzing
visual information. For instance, Temporal Summary Images [106]
TABLE 5
Reasoning is classiﬁed by the class (row) and the method (column)
Rule-based
Learning-based
Visual Perceptual Learning
[106]
[57], [66]
Chart Summarization
[45], [48], [55],
[127]–[129]
[13], [68], [73],
[130]
Visual Question Answering
[47], [96]
[12], [67], [69]–[71]
automatically extracts points of interest in charts according to
predeﬁned heuristics. Recently, deep learning methods, trained on
labeled datasets, have been applied to improve machine perception
of visualization images. Bylinskii et al. [57] presented neural
network models to predict human-perceived visual importance of
visualization images. Similarly, Haehn et al. [66] evaluated the
performances of CNNs on Cleveland and McGill’s 1984 perception
experiments [131] and concluded that off-the-shelf CNNs were
not currently a good model for human graphical perception. Their
initial results underscore the importance of continued research to
improve the performance.
Chart summarization becomes increasingly important with
the rapid popularization of visualizations. Most existing approaches
generate text summaries such as natural language description
or captions [45], [48], [55], [73], [127]–[130]. The simplest
approach is to provide a short description of how to interpret
the chart [55], [127], e.g., “This chart shows the trend of average
departure delay in January”. More advanced approaches focus on
explaining and communicating high-level insights conveyed by
charts. Those approaches extract the data patterns and subsequently
convert patterns to natural language according to pre-deﬁned
templates [45], [48], [128], [129], e.g., “X was the most/least
frequent sub-category in A”. Liu et al. [130] offered an alternative
perspective that learns most noteworthy insights with deep learning
approaches. A common limitation of the above work is that natural
language summaries are generated via pre-deﬁned templates and
therefore conﬁned to few variations and generality. Thus, recent
research proposes several end-to-end deep-learning solutions for
generating chart captions [13], [68] or text summarization [73].
However, summarization still remains highly under-explored since
the algorithm performances have much space for improvements.
Visual question answering is another emerging research area
that aims to answer a natural language question given a visualiza-
tion image. Traditional methods [47] ﬁrst decode visualizations
into data tables and then parse template-based questions into
queries over the data table to generate answers. Kim et al. [96]
recently improved a natural language parser to support free-from,
crowdsourced questions. Another line of research studies end-
to-end deep learning approaches [12], [67], [69]–[71]. The key
challenge is that answering questions for visualizations requires
high-level reasoning of which existing visual question answering
models are not capable [12], [69]. Besides, visualization images are
sensitive to small local changes, i.e., shufﬂing the color in legends
greatly alters the charts’ information. Therefore, the major problem
is how to learn the features from visualization images and fuse them
with features from natural language questions. DVQA [12] learns
and fuses features via a sophisticated model containing multiple
sub-networks, each responsible for different components such as
spatial attention. Later work expands this work with improvements
to the models, e.g., PlotQA [70] and LEAF-QA [67] explicitly
apply reverse engineering to retrieve visual elements and feed the
extracted information into sub-networks. However, there still lacks
real-world datasets, good models, and evaluation metrics.
