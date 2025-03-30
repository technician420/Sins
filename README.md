# Sins
I confess all the guilty stuff I did in my past.

First, create a .kdbx database using KeepassXC.
Second, set the KDF to obnoxiously high so it takes 60 seconds for your CPU to mount.
Encryption algorithm: Twofish 256-bit
KDF: Argon2d
Transform rounds: 38
Memory Usage: 8192 MiB
Parallelism: 8 threads

For password, I use 3 sources... random.org, GRC passwords, and KeepassXC built in password generator.
For the 1st source, I use the 32 char password
For the 2nd source, I use the 63 random printable ASCII set
For the 3rd source, I use between 64 and 128 characters (picked with TRNG) in the KeepassXC built in PW generator with everything enabled, even the extended ASCII set.
PW char length = 159 to 223 characters
Type your confession in the Password field if it's a sentence, otherwise in the Notes section. I typed mine in the Password field.
My size on disk is 4096 bytes, so I open Veracrypt and generate a keyfile called KF4096.
Veracrypt uses Bytes as a base unit so create a keyfile that is sized 4096. I like to use the Whirlpool hash function.
Now we XOR SinConfession.kdbx with KF4096 using my written fileXOR.py code.

(Check fileXOR.py source code.)

File1) SinConfession.kdbx
File2) KF4096
File3) SinsEncryptedOTP (Sins encrypted One Time Pad)

After this I use the shred command on KF4096 and SinConfession.kdbx.
shred KF4096
shred SinConfession.kdbx

Finally, SinsEncryptedOTP is ready to be uploaded online, for the world wide web to see!!
