# PASSWORD NUMBERS

* total passwords in libero set: 667,714
    
    * Training set: 534,171 (80%)
        * of which 10 character strings: 461,442 (86.38%)
    
    * Testing set:133,542 (20%)
        * of which 10 character strings: 111,994 (83.86%)


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
Number of words in rockyou: 11,335,386
