#Presentation

**Time:** 5 minutes

**Topic:**High level overview of the the thesis(abstract+findigs) , followed by critique and the new data from pre-trained PassGAN comparison


**You need to be clear about the findings and the conclusion, about what you actually accomplished with the thesis and what does it mean**
Hopefully the data from the new comparison will help solidify your argumen about why tuning for language difference is useful.

##Notes

Take it slow during the exam, keep calm and be clear.
Take notes when reading the papers and jut down any possible new insights


#Presentation Summary

##Overview of the thesis:

**INTRO**
The goal of the thesis was to explore the impact of language on GANs for password cracking: to thatend, we tested PassGAN with a set of Italian Passwords (the Libero dataset).
We also compared PassGAN with rule-based password crackers (HashCat):

Concerning the impact of language, our goal was three-fold:
* To see wheather GANs are capable of learning and using language-specific features in passwords, and compare them with rule-based tools (which have no such capability)
* To explore the impact of training with Natural Language data.
* To establish wheather PAssGAN or similar tools offer something new and unique, if they offer us things that could not be acheived with rule-based tools    

**FINDINGS**

* We found that rule-based tools are more effective than PassGAN when using the same number of password candidates, but also that PassGAN can match HashCat's performance if more password candidates can be used.
* We found that even when constrained to a low amount of password candidates, used in conjucntion with rule-based tools PassGAN can be an effective way to tackle longer passwords with language-specific characteristics.
* We found that natural language does not seem to have an impact of PassGAN's performance, suggesting that training should be limited to password data only. We would need to examine the topic more thorraly however in order to conclude that Natural Language is decremental.
* We found that mangling rules can be effective when used with PassGAN (in contrast to the original paper) as they improve performance with low numbers of Password candidates.
They might provide a compromise between the language-otpimizations provided by PassGAN.
* We found that PassGAN performs worse when cracking italian passwords, if the system has been trained on english-language passwords instead of italain ones (see next slides) 

Ultimately we concluded that PassGAN can be an effective tool for password cracking, and that it can be better suited to the task of cracking passwords from another langfuage than rule-based tools: we explained our preference by pointing out that PassGAN offers an attacker more flexibility when compared to rule-based tools: An attacker can either use it alongside rule-based crackers as a specialist tool, or invest the storage space, computing power and time necessary for it to out-perform rule-based tools.     


##New Data: Comparison with pre-trained model

One of the main criticisms we had in our discussion was that we did not perform a comparison between the pre-trained PassGAN model and our own.
This was something that we did not have the time for in our main thesis, so we proceeded to do it here: the results are shown below

|                   | - | best64 | gen2 |
|-------------------|---|--------|------|
| Pre-trained model | 5,212 (6.45%) | 14,005 (17.33%) | 41,222 (51.01%) |
| own model         | 12,096 (14.97%) | 23,352 (28.90%) | 50,318 (62.27%) |

As we can see there is a significant increase in the number of passwords found when PassGAN is trained on italian passwords: we take this result as further evidence that language differences do make an impact when cracking passwords, especially when using deep learning-based methods.

##Additional Criticisms

Most of the criticism we have about the thesis is laid out in our Discussion and Conclusion, but we would like to re-iterate on a particular point:

In our Conclusion we said that we did not give PassGAN a fair chance, as our early experiments in Section 4 were based off low guess number and thus we worried that our point of view was skiewed in favour of HashCat. In hindsight this is not such a big issue, but while reading Menlicher and Hitajwe realized that we made a mistake in how we laid our our testing section: we should have given more space to the strenght and weaknesses of each approach, and stressed that PassGAN is not designed to compete with HAshCat directly at low guess numbers. If we were given a second chanche, we would give more time to testing PAssGAN with huge wordlist, and only later attempt a comparison between PassGAN and HashCat with low guess numbers.
  
