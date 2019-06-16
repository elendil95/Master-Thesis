After looking at this paper again, my opinion of it has changed: While i think their thesis is solid, in that the presence of grammatical structure does reduce the search space and thus the security of user-generated pass phrases, 
their testing is not sufficient to prove it in my opinion. their testing sample is very samll as i mentioned, and i struggle to see how it could provide useful generalizations. This is further compounded by the fact that they mention the existanc of the Amazon PayPhrase dataset (which is larger and it had bradly the same characteristics from what i understand), so i do wonder why they limited themselves in such manner.
While simple, i think that their use of POS tagging and the Brown corpus is the right way to go; but i think they failed in their experiemnts. On the other hand however, i recognize that it is harder ro do research with passphrases as they are not as widely used ass passwords, thus there is less data available to work with.

SMALL EDIT TO THE POINT ABOVE: The choiche of dictionaries itself is solid, but the data they are traying to crack is still quite small. Also they are testing with JTR and HashCat which we have established are not made for this.
EDIT 2: The amazon Payphrase wasn't actually a passphrase corpus.


- Don't tey reference a whole lot of their own work?  

- Don't they dismiss JtR and Hascat rather easily? (No they do not, they just were not made for this sorta thing. however their example is kinda weird).

I think this might be a nice avenue of research for my thesis, as neural networks' performance in naturla language processing seem well-suited to tackilng passphrases and this potential issue in particular. 
In this regard i find it interesting to compare this paper with the second one, because it too dealt wirh natural language: In that paper the authors though that increasing natural language disctionaries in the training data would increase the gueessing effeectiveness of their system, but they were ultimately proven wrong: To over-simplify things, one might say that the inclusion of natural language sets ended up generating more noise as far as the network was concerned.
I beleive hoewer that in the caase of passphrases things might turn out differntly, if we assume that passphrases are much more subject to the patterns of natural language by nature as opposed to normal passowrds.
