from hashlib import sha256
import csv


def hash_password_hack(input_file_name,output_file_name):

    hash_password_to_password = dict()
    hack = dict()
    
    for password in range(1,10000):
        hashing_number = sha256(b'%i'% password).hexdigest()
        hash_password_to_password[hashing_number] = password
    with open(input_file_name) as f:
        psswords_singer = csv.reader(f)
        for row in psswords_singer:
            name_users = row[0]
            for key in row[1:]:
                hack.update({name_users : hash_password_to_password[key]})

                with open(output_file_name, 'w') as out:
                    for key in hack.keys():
                            out.write("%s,%s\n"%(key,hack[key]))
                            
