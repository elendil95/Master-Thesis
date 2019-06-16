# Generate MD5 hashes
> cat passwords.txt |while read line; do echo -n "$line"|md5sum | tr -d " -" >> shell.hash; done

# Inital cracking results

## Hashcat report -- rockyou+best64**
Session..........: hashcat                       
Status...........: Exhausted
Hash.Type........: MD5
Hash.Target......: shell.hash
Time.Started.....: Tue Apr  2 11:39:28 2019 (1 min, 40 secs)
Time.Estimated...: Tue Apr  2 11:41:08 2019 (0 secs)
Guess.Base.......: File (rockyou.txt)
Guess.Mod........: Rules (/usr/share/hashcat/rules/best64.rule)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........: 11180.9 kH/s (13.00ms) @ Accel:256 Loops:77 Thr:1 Vec:8
Recovered........: 140478/418492 (33.57%) Digests, 0/1 (0.00%) Salts
Recovered/Time...: CUR:21413,N/A,N/A AVG:83471,5008289,120198938 (Min,Hour,Day)
Progress.........: 1104517645/1104517645 (100.00%)
Rejected.........: 0/1104517645 (0.00%)
Restore.Point....: 14344385/14344385 (100.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-77 Iteration:0-77
Candidates.#1....: $HEX[206b72697374656e616e6e65] -> $HEX[04a156616d6f]
Started: Tue Apr  2 11:39:26 2019
Stopped: Tue Apr  2 11:41:09 2019

**Found: ~140.000 (33.57%)**
**same result with just dictionary??!**

## Hascat report -- Just Rockyou

Session..........: hashcat                       
Status...........: Exhausted
Hash.Type........: MD5
Hash.Target......: shell.hash
Time.Started.....: Tue Apr  2 11:47:48 2019 (2 secs)
Time.Estimated...: Tue Apr  2 11:47:50 2019 (0 secs)
Guess.Base.......: File (rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  5882.3 kH/s (0.52ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 140478/418492 (33.57%) Digests, 0/1 (0.00%) Salts
Recovered/Time...: CUR:N/A,N/A,N/A AVG:0,0,0 (Min,Hour,Day)
Progress.........: 14344385/14344385 (100.00%)
Rejected.........: 0/14344385 (0.00%)
Restore.Point....: 14344385/14344385 (100.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: $HEX[206b72697374656e616e6e65] -> $HEX[042a0337c2a156616d6f732103]
Started: Tue Apr  2 11:47:46 2019
Stopped: Tue Apr  2 11:47:52 2019


##Hashcat report -- using  GAN

Session..........: hashcat                       
Status...........: Exhausted
Hash.Type........: MD5
Hash.Target......: shell.hash
Time.Started.....: Tue Apr  2 11:52:45 2019 (6 secs)
Time.Estimated...: Tue Apr  2 11:52:51 2019 (0 secs)
Guess.Base.......: File (it_gen_passwds.txt)
Guess.Mod........: Rules (/usr/share/hashcat/rules/best64.rule)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........: 13215.7 kH/s (10.73ms) @ Accel:256 Loops:77 Thr:1 Vec:8
Recovered........: 146352/418492 (34.97%) Digests, 0/1 (0.00%) Salts
Recovered/Time...: CUR:N/A,N/A,N/A AVG:60452,3627128,87051075 (Min,Hour,Day)
Progress.........: 77000000/77000000 (100.00%)
Rejected.........: 0/77000000 (0.00%)
Restore.Point....: 1000000/1000000 (100.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-77 Iteration:0-77
Candidates.#1....: sem4201801 -> eaxnea
Started: Tue Apr  2 11:52:43 2019
Stopped: Tue Apr  2 11:52:51 2019


**Found: ~146.000 (34.97%)** heyy that 1.4% more!**

