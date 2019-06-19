# PASSWORD NUMBERS

* total passwords in libero set: 667,714
    
    * Training set: 534,171 (80%)
        * of which 10 character strings: 461,442 (86.38%)
    
    * Testing set:133,542 (20%)
        * of which 10 character strings: 111,994 (83.86%)

**it_gen_passwords has 1 million entries not 100 thousands, you fucking cunt!**

# STANDALONE CRACKING PERFORMANCE ON SUBSET OF 10 CHARACTERS

## Training set

* Rockyou: 70,550 (25.36%) of passwords found
* Rockyou + best64 rules: 115,339 (41,47%) of passwords found
* Rockyou + generated2 rules: 202,624 (72.85%) of passowrds found

* PassGAN: 15,924 (5,72%) of passowrd found
* PassGAN + best64 rules: 40,659 (14.62%) of passowrds found
* PassGAN + generated2 rules:  134,114 (48.22%) of passwords found

## Testing set

* Rockyou: 19,215 (23.78%) of passwords found
* Rockyou + best64 rules: 30,170 (37.33%) of passwords found
* Rockyou + generated2: 59134 (73.18%) of passwords found

* PassGAN: 4,637 (5.74%) of passwords found
* PassGAN + best64 rules: 11,053 (13.68%) of passwords found
* PassGAN + generated2 rules: 34,896 (43.18%) of passowrds found


## Thougts

The performance of both PassGAN seems to be broadly consistent among the two datasets, with comparable  percentages of passowrds found across the two sets. Higher numbers can be acheived by using a potfile and applying them sequentially.

I am surprised to see just how much influence an extensive ruleset can have on performace, gen2 is the second biggest one in terms of raw entries.

That said, i am really concerned by the lack of performance of PassGAn, even with the gen2 rules it sits a large 20% behind. And this is with both target *and* PassGAN using 10 character strings, whcih should make things easier. This might be due to a number of factors however: The shortness of the PassGAN list might be a bottleneck to its effectiveness both with and without rules, as could be 
the fact that it lacks a NL training source...

Next steps should probably be to try again with more samples, and to check for patterns of unique passowrds that might have been caught by passgan but not Rockyou (this is probably best done by using potfiles).

Maybe i should generate the same number of samples with passGAN as there are words in rockyou.
Also compare the 2 lists for uniques: what passwords has PassGAN found that hashcat missed? or vice versa.
You can also try to train again with NLP and see what happens.

# DAY 2

created a bigger PassGAN sample file with the same number of entries as RockYou: from a quick check it seems that there are roughtly 408.250 entries common to both files. There is a significant overlap with the initial sample of PAssGAN passwords. It might also be nice to compare what passowrds have been found by just the new set and not the old set.

## CRACKING PERFORMANCE WITH NEW PassGAN set (14.3 million entries).

**Testing Set**

* PassGAN: 10.735 (13.28%) of passwords found.
* PassGAN+best64: 20.638 (25.54%) of passwords found.
* PassGAN+gen2: 48751 (60.33%) of passwords found. 

## Possible Passwords comparisons:

* Compare the passwords found by small passgan sample and big one to see is there are patterns to the passwords only the big one found (no rules). Given the significal overlap this is rather nlikely though
* Compare the passwords found by just rockyou and just big PassGAN and do the same.
* Compare the passowrds found in Rockyou+Gen2 and bigPassGAN+gen2

Try to crack the training set with big PassGAN and see if the results are significantly different than with small one: maybe the bigger size of the sample may lead to over-fitting when run on the training set?

**Comparisons might be the most useful when you run Rockyou+gen2>big_passgan+gen2: what passwords have beeen found by passgan and not rockyou? because the percentile increase is likely to be small, hopefully there should be a pattern or something like it in the results** 

## NL Testing

* Repubblica 50%: 51,232 (63.40%) passwords found.
* Repubblica 100%: 48,651 (60.20%) passwords found

* ItwaC 50%: 50,133 (62.04%) of passwords found.
* ItwaC 100%: 47,646 (58.96%) of passwords found.

##Random notes
PassGAN samples at a rough speed of 64000 samples written every 2 seconds

##Pre-trained model vs. OG PassGAN model (both 195000 iterations)
* just_pretrained: 5,212 (6.45%) of passwords found.
* pretrained+best64: 14,005 (17.33%) of passwords found.
* pretrained+gen2: 41,222 (51.01%) of passwords found.

* just_passgan: 12,096 (14.97%) of passwords found.
* passgan+best64: 23,352 (28.90%) of passwords found.
* passgan+gen2: 50,318 (62.27%) of passwords found.
