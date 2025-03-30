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
