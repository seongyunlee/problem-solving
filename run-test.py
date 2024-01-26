import subprocess
import random

def run_python_script(script_path, input_text):
    # Run the Python script and capture its standard output
    process = subprocess.Popen(['python', script_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input_text)
    return stdout.strip(), stderr.strip()

def compare_outputs(output1, output2):
    # Compare the standard outputs
    return output1 == output2

def test_case_generator():
    length = 1000

    alphabet = "abcdefghijklmnopqrstuvwxyz".capitalize()
    
    return '\n'.join([''.join([alphabet[random.randint(0,25)] for _ in range(length)]) for _ in range(2)])


if __name__ == "__main__":
    # Replace 'script1.py' and 'script2.py' with your file names
    script1_path = 'script1.py'
    script2_path = 'script2.py'

    # Provide input text (you can modify this according to your test case)
    input_text = "Your input text goes here."



    rep = 1000

    for i in range(rep):
        # Compare the outputs
        test_case = test_case_generator()

        # Run the first Python script
        output1, error1 = run_python_script("./b9252.py", test_case)

        # Run the second Python script
        #output2, error2 = run_python_script("./b21311-1.py", test_case)

        print(output1)
        print(str(i+1)+"/"+str(rep))
        """ if compare_outputs(output1, output2):
            print("Outputs are the same.")
        else:
            print("Outputs are different.")
            print(test_case) """
