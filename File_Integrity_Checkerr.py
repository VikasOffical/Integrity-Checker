import hashlib
import os

def create_test_files():
    """
    Create test files and directories for demonstration purposes.
    """
    os.makedirs('test_directory', exist_ok=True)
    
    with open('test_directory/original_file.txt', 'w') as f:
        f.write('This is the original file.')
    
    with open('test_directory/comparison_file.txt', 'w') as f:
        f.write('This is the original file.')  # Identical content for comparison
    
    with open('test_directory/different_file.txt', 'w') as f:
        f.write('This is a different file.')  # Different content for comparison

def calculate_file_hash(file_path, hash_algorithm='sha256'):
    """
    Calculate the hash of a file using the specified hash algorithm.
    
    :param file_path: The path to the file.
    :param hash_algorithm: The hash algorithm to use (default is sha256).
    :return: The hexadecimal hash value of the file.
    """
    hash_func = hashlib.new(hash_algorithm)
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def check_file_integrity(original_file_path, comparison_file_path, hash_algorithm='sha256'):
    """
    Check the integrity of a file by comparing its hash with another file's hash.
    
    :param original_file_path: The path to the original file.
    :param comparison_file_path: The path to the comparison file.
    :param hash_algorithm: The hash algorithm to use (default is sha256).
    :return: True if the files are identical, False otherwise.
    """
    original_file_hash = calculate_file_hash(original_file_path, hash_algorithm)
    comparison_file_hash = calculate_file_hash(comparison_file_path, hash_algorithm)
    
    if original_file_hash is None or comparison_file_hash is None:
        return False
    
    return original_file_hash == comparison_file_hash

def monitor_directory(directory_path, hash_algorithm='sha256'):
    """
    Monitor a directory for changes by calculating and comparing file hashes.
    
    :param directory_path: The path to the directory to monitor.
    :param hash_algorithm: The hash algorithm to use (default is sha256).
    :return: A dictionary with file paths as keys and their hash values as values.
    """
    file_hashes = {}
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_file_hash(file_path, hash_algorithm)
            if file_hash:
                file_hashes[file_path] = file_hash
    return file_hashes

def main():
    """
    Main function to demonstrate the usage of file integrity checker functions.
    """
    # Create test files and directory
    create_test_files()

    # Example paths to files and directory
    original_file = 'test_directory/original_file.txt'
    comparison_file = 'test_directory/comparison_file.txt'
    different_file = 'test_directory/different_file.txt'
    directory_to_monitor = 'test_directory'

    # Check file integrity
    if check_file_integrity(original_file, comparison_file):
        print(f"The files '{original_file}' and '{comparison_file}' are identical.")
    else:
        print(f"The files '{original_file}' and '{comparison_file}' are different.")

    if check_file_integrity(original_file, different_file):
        print(f"The files '{original_file}' and '{different_file}' are identical.")
    else:
        print(f"The files '{original_file}' and '{different_file}' are different.")

    # Monitor directory for changes
    file_hashes = monitor_directory(directory_to_monitor)
    for file_path, file_hash in file_hashes.items():
        print(f"File: {file_path}, Hash: {file_hash}")

if __name__ == '__main__':
    main()
