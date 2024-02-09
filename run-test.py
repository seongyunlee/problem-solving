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
    length = random.randint(10,11)

    #alphabet = "abcdefghijklmnopqrstuvwxyz".capitalize()

    return str(length)+'\n'+' '.join([str(random.randint(1,100)) for _ in range(length)])


if __name__ == "__main__":
    # Replace 'script1.py' and 'script2.py' with your file names
    script1_path = 'b14003.py'
    script2_path = 'b14003-2.py'

    # Provide input text (you can modify this according to your test case)
    input_text = "Your input text goes here."



    rep = 1000

    for i in range(rep):
        # Compare the outputs
        test_case = test_case_generator()

        # Run the first Python script
        output1, error1 = run_python_script(script1_path, test_case)

        # Run the second Python script
        output2, error2 = run_python_script(script2_path, test_case)
        '''
        print(output1)
        print(str(i+1)+"/"+str(rep))
        if error1:
            print("Error in script1.py:", error1, test_case)
        '''
        if compare_outputs(output1, output2):
            print("Outputs are the same.")
        else:
            print("Outputs are different.")
            print(test_case, output1, output2)
            exit()