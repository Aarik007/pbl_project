import hashlib

def hash_file(file_path):
    h = hashlib.new("sha256")
    with open(file_path,"rb") as file:
        while True:
            chunk=file.read(1024)
            if chunk == b"":
                break
            h.update(chunk)
    return h.hexdigest()

def verify_integrity(file1,file2):
    hash1 =hash_file(file1)
    hash2 =hash_file(file2)
    print("\nchecking integrity between ",file1,"and",file2)
    if hash1==hash2:
        return "file is intact no modification"
    return "file is modified possible unsafe"

if __name__  =="__main__":
    print("sha hash of file is:",hash_file(r"venv/sample_files/sample.txt"))
    print(verify_integrity(r"venv/sample_files/Screenshot 2026-02-15 at 1.56.03 PM.png",r"venv/sample_files/Screenshot 2026-02-15 at 1.57.24 PM.png"))
