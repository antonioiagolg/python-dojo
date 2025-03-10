import hashlib

def get_sha1_file(a_file):
    h = hashlib.sha1()
    with open(a_file, "rb") as file:
        chunk = 0
        while chunk != b"":
            chunk = file.read(1024)
            h.update(chunk)
    return h


def hash_file(file_name1, file_name2):
    h1 = get_sha1_file(file_name1)
    h2 = get_sha1_file(file_name2)

    return h1.hexdigest(), h2.hexdigest()


msg1, msg2 = hash_file("file1.pdf", "file1.pdf")

if msg1 != msg2:
    print("Not identical")
else:
    print("Identical")
