import hashlib

target_hash = input("please enter the hash value")

def brute_force_six_digit_hash(target_hash):
    for number in range(1000000):  
        password = f"{number:06d}" # so that 0 is represented as 000000 and so on
        
        hash_object = hashlib.sha256(password.encode())
        hashed_password = hash_object.hexdigest()
        
        # Compare the hash with the target hash
        if hashed_password == target_hash:
            print(f"Password found: {password}")
            return password

    print("Password not found.")
    return None

brute_force_six_digit_hash(target_hash)
