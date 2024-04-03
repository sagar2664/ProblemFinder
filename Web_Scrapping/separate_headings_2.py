import os

def read_until_time(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f_in:
        with open(output_file, 'a', encoding='utf-8') as f_out:  # 'a' for append mode
            text = f_in.read()
            found_time = False
            for word in text.split():
                if word.endswith("time"):
                    #found_time = True
                    f_out.write(word[:-4])
                    break
                f_out.write(word + " ")
                # if word.endswith("time"):
                #     found_time = True
                #     break
            f_out.write("\n")

input_folder = "qdata"
output_file = "output.txt"

with open(output_file, 'w', encoding='utf-8') as f_out:
    # Iterate over all .txt files in the input folder
    # for filename in os.listdir(input_folder):
    #     #if filename.endswith(".txt"):
    #     input_file = os.path.join(input_folder, filename)
    #     read_until_time(input_file, output_file)
    
    for idx in range(1, 5001):
        input_file = f"qdata//problem_statement_{idx}.txt"
        read_until_time(input_file,output_file)
