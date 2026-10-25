IEEE TRANSACTIONS ON VISUALIZATION AND COMPUTER GRAPHICS, VOL. XX, NO. XX, XX 2018
1
AI4VIS: Survey on Artiﬁcial Intelligence
Approaches for Data Visualization
Aoyu Wu, Yun Wang, Xinhuan Shu, Dominik Moritz, Weiwei Cui, Haidong Zhang,
Dongmei Zhang, and Huamin Qu
Abstract—Visualizations themselves have become a data format. Akin to other data formats such as text and images, visualizations are
increasingly created, stored, shared, and (re-)used with artiﬁcial intelligence (AI) techniques. In this survey, we probe the underlying
vision of formalizing visualizations as an emerging data format and review the recent advance in applying AI techniques to visualization
data (AI4VIS). We deﬁne visualization data as the digital representations of visualizations in computers and focus on data visualization
(e.g., charts and infographics). We build our survey upon a corpus spanning ten different ﬁelds in computer science with an eye toward
identifying important common interests. Our resulting taxonomy is organized around WHAT is visualization data and its representation,
WHY and HOW to apply AI to visualization data. We highlight a set of common tasks that researchers apply to the visualization data and
present a detailed discussion of AI approaches developed to accomplish those tasks. Drawing upon our literature review, we discuss
several important research questions surrounding the management and exploitation of visualization data, as well as the role of AI in
support of those processes. We make the list of surveyed papers and related material available online at ai4vis.github.io.
Index Terms—Survey; Data Visualization; Artiﬁcial Intelligence; Data Format; Machine Learning
!
1
INTRODUCTION
D
ATA visualizations use visual representations of abstract
data to amplify human cognition. Researchers traditionally
investigate visualizations as artifacts created for people. This paper
revisits this traditional perspective in line with the growing research
interest in applying artiﬁcial intelligence (AI) to visualizations.
Similar to common data formats like text and images, visualizations
are increasingly created, shared, collected, and reused with the
power of AI. Thus, we see that visualizations are becoming
a new data format processed by AI. For instance, this trend
was evident at the 2020 IEEE Visualization Conference, where
multiple techniques were proposed for automating the creation
of visualizations [1]–[5], retargeting visualizations [6], [7], and
analyzing visualization ensembles [8], [9]. In light of this trend,
new concepts and research problems are emerging, raising the need
to organize existing literature and clarify the research landscape.
This survey describes the research vision of formalizing visual-
izations as an emerging data format and reviews recent advances
in developing AI approaches for visualization data (AI4VIS). We
deﬁne visualization data as the digital representations of visual-
izations in computers and focus on data visualization. Different
from common formats, visualization data contains multimodal
information such as visual encodings, encoded data, text, and
images. Those characteristics pose new challenges in developing
tailored AI approaches (e.g., how to represent visualization data).
•
A. Wu, X. Shu, and H. Qu are with the Hong Kong University of Science
and Technology. Email: {awuac, xinhuan.shu, huamin}@cse.ust.hk. This
work is done when A. Wu is an intern at MSRA.
•
Y. Wang, W. Cui, H. Zhang, and D. Zhang are with Microsoft Research Asia.
Email: {wangyun, weiwei.cui, haidong.zhang, dongmeiz}@microsoft.com.
•
D. Moritz is with Carnegie Mellon University and Apple. Email: do-
moritz@cmu.edu.
Manuscript received xx xxx. xxxx; revised xx xxx. xxxx; accepted xx xxx.
xxxx. Date of publication xx xxx. xxxx; date of current version x xxx. xxxx.
(Corresponding author: Yun Wang).
Recommended for minor revision
Digital Object Identiﬁer:
Nevertheless, AI is a broad notion that has been studied
in different areas. Those areas have different motivations and
research questions about applying AI to visualization data, the
proposed techniques, and the content format used to represent
visualizations. For instance, the Web and Information Retrieval
community advances the technology for searching visualizations
(e.g., [10], [11]), while research in Computer Vision recently studies
visual question answering in charts (e.g., [12], [13]). Therefore,
a comprehensive understanding of AI4VIS research requires a
foundation in rich literature from diverse disciplines.
We construct a literature corpus by a relation-search ap-
proach [14], i.e., graph traversal over the citation and reference
networks. This approach allows us to collect 98 publications from
10 research communities – publications from the visualization
community account for roughly one-third. While not being exhaus-
tive, our corpus provides sufﬁcient research instances to synthesize
relevant work that contributes to the understandings of important
common research questions and techniques. As shown in Figure 1,
we organize and categorize AI4VIS research following a well-
established what-why-how viewpoint [15]:
• What is visualization data. We formalize the concept of
visualization data by providing an overview of its content
formats as well as the representations (Figure 1 A ).
• Why apply AI to visualization data. We identify three common
goals for AI4VIS research, namely visualization generation,
enhancement, and analysis (Figure 1 B ). We classify those
goals into subcategories to provide a comprehensive response
to ongoing discussions like “why should we teach machines
to read charts made for humans” [16].
• How to apply AI to visualization data. Most importantly, we
contribute a task abstraction regarding how to apply AI to
visualization data (Figure 1 C ). The task abstraction is critical
since it allows for domain-agnostic and consistent descriptions
of research questions across different disciplines. Besides,
it facilitates an organized discussion reconciling distinct
arXiv:2102.01330v2  [cs.HC]  19 Jul 2021
