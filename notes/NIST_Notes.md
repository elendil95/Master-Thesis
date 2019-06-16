# Section 5

## 5.1.1.1
User-chosen passwords should be at least 8 characters in lenght.
System chosen passwords can be numeric or alphanumeric, and must be at least 6 characters long.

If the password chosen is rejected, the user must be prompted for another one.

*No* password policy of any kind should be imposed on the users.

## 5.1.1.2

Passwords should be between 8 and 64 caracters => ASCII + space, but UNICODE should be supported as well.

Again, system generated PINs should be at least 6 characters.

*no hints or security questions are allowed*

When signing up or resetting passwords, the system should compare hte perspective password against a database: content of this DB include dictionary words, previously leaked passwords and common key sequences.

System should provvide password strenght meters.

The system must not impose composition rules or force periodic passwords changes, but only force changes in the event of a breach.

"Verifiers SHALL store memorized secrets in a form that is resistant to offline attacks. Memorized secrets SHALL be salted and hashed using a suitable one-way key derivation function. Key derivation functions take a password, a salt, and a cost factor as inputs then generate a password hash. "

"Examples of suitable key derivation functions include Password-based Key Derivation Function 2 (PBKDF2) and Balloon. A memory-hard function SHOULD be used because it increases the cost of an attack. The key derivation function SHALL use an approved one-way function such as Keyed Hash Message Authentication Code (HMAC), any approved hash function in SP 800-107, Secure Hash Algorithm 3 (SHA-3), CMAC or Keccak Message Authentication Code (KMAC), Customizable SHAKE (cSHAKE), or ParallelHash. The chosen output length of the key derivation function SHOULD be the same as the length of the underlying one-way function output."

"The salt SHALL be at least 32 bits in length and be chosen arbitrarily so as to minimize salt value collisions among stored hashes. Both the salt value and the resulting hash SHALL be stored for each subscriber using a memorized secret authenticator.

In addition the system should perform an additional round of the key derivation funtion using a separate, secret salt of at least 112 bits. The secret salt should be stored separately from the regular salt and the password (ideally on separate hardware).

*afaik this extra roun should be performed after password creating and before the main encryption round, thus rendering dictionary attacks even with the salts useless.*
