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
import os

def xor_files(file1_path, file2_path, output_path):
    """XOR two files together and save the result to output_path."""
    with open(file1_path, 'rb') as f1, open(file2_path, 'rb') as f2:
        data1 = f1.read()
        data2 = f2.read()

    # Determine the smaller size
    min_size = min(len(data1), len(data2))
    
    # Truncate both files to the smaller size and XOR
    xor_data = bytes(a ^ b for a, b in zip(data1[:min_size], data2[:min_size]))
    
    # Save the result
    with open(output_path, 'wb') as out_file:
        out_file.write(xor_data)
    
    print(f"Successfully XOR'd files. Output saved to: {output_path}")

def main():
    print("File XOR Tool")
    file1 = input("Enter path to first file: ").strip('"')
    file2 = input("Enter path to second file: ").strip('"')
    output = input("Enter output file path: ").strip('"')

    if not os.path.exists(file1) or not os.path.exists(file2):
        print("Error: One or both input files do not exist!")
        return

    xor_files(file1, file2, output)

if __name__ == "__main__":
    main()
File1) SinConfession.kdbx
File2) KF4096
File3) SinsEncryptedOTP (Sins encrypted One Time Pad)

After this I use the shred command on KF4096 and SinConfession.kdbx.
shred KF4096
shred SinConfession.kdbx

Finally, SinsEncryptedOTP is ready to be uploaded online, for the world wide web to see!!
