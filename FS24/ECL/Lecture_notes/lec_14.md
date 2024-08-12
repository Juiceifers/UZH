#Lecture 14:
##Information Retrieval
- stopwords
  - can be removed, dont have to be
  - functionwords
- precision and recall work against each other
  - one can be increased by sacrificing the other
- average ranked position:
  - metric for measrueing how highly ranked the relevant documents are
  - the higher the better
- relevance: TF * IDF
  - term frequency * inverse document freuqnecy
  - TF: how often some term occurs in a given document
    - often counting lemmas
  - document frequency: in how many documents of our collection does the term occur => number of documents!
  - inverse document freuqnecy: 1 / docuent freq
    - the higher the doc freq the lower the inverse
  - a term that is frquent in my document but also occurs a lot in other document => not that special


##Trustyness of AI
- cyc = short form of encyclopedia 
  - had stated its sources
  - chatgpt does not state - cannot traceback

##Summary
1) Tokenization
   1) splitting all text
   2) recognizing (sentence) boundries
   3) numbers, hyphens, aphostrophes, special chars, diff languages
2) Lematisation & morphologhy analysis
   1) for "am": an der/ an das/ an die => not a single correct answer, need to define how to do this
   2) words can have different lemmas (example 3)
   3) ..schreiben...zu => 
   4) elicpical constructions: Blümslisalm...
   5) female forms: is it f r m? => matter of definition (nowadays male and female are seperate forms)
3) Part of Speech Tagging
   1) Problems:
      1) what happens with ROman numbers? EVerything starting with capital and unkown words -> proper nouns (has to be defined)
      2) d.h. => adverb (adverbial function)
      3) foreign language material => adj/foreign word? 
      4) noun or proper noun? => diff is proper noun refers to something specific and unique
         1) in this example: in this combo proper name
   2) accuracy: approx 96/97%
      1) if its 96% correct: every 25th word is worng and every sentence per avg has 25 words then every sentence has at least one error!!!
4) Parsing
   1) Treebanks
   2) Dependency structures
   3) Synatxt Trees, Constituents trees
5) Processing Spoken Language
   1) for exam: no complicated questions

6) Propername Recognition and Semantic Analysis
   1) Word semantics
   2) shallow semantics
   3) Formal semantics (not covered much here, idea of psyche)
   4) Normalization = 
7) Word Embeddings
   1) Vector representation
   2) at least one question abt this in the exam
      1) also byte pairing encodung
         1) splitting a word into its pieces on statistical ground
            1) unkown words will be split into its most similar sequence 
      2) usually 5-10/ sometimes 12 many hidden layers are used (can have much many more nodes per layer, like 300 or more)
      3) between each layer all the wheights need to be computed/adjused => A LOT OF COMPUTATION
8) Language MOdels 
   1) context based word prediction models
      1) chatting, bias, hate detection, spelling, translating
      2) base of neural machine translation systems
         1) to produce something fluent
9) Machine Translation
   1)  Rule based
   2)  statistical
       1)  from around mid 90s
       2)  pll corpora = same text in multiple languages
       3)  need to do sentence alignment
       4)  5 evaluation measures:
           1)  bleu = precision based method, does not model recall => gravity panelty
10) Neural Machine Translation
11) LLM-based MT
    1)  sideeffect of multilingual corpora
    2)  can be fine tuned
12) Evaluation of LLM
    1)  (last week)
13) Formal Languages
14) Search Systems


###Exam Prep:
- how good do we need to know super glue
  - give 3/5 good examples of what its testing + explain why to prove understanding
- we can use the sheet for PoS tagging etc
- exam lenght: 1hr 45min, 90 points
- no technical devices
- 
