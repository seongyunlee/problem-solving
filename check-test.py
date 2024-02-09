import subprocess
import random

def run_test(script_path, input_text):
    # Run the Python script and capture its standard output
    process = subprocess.Popen(['python', script_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input_text)
    return stdout.strip(), stderr.strip()

def run_check(script2_path, input_text, ans):
    # Run the first Python script
    process = subprocess.Popen(['python', script2_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate('\n'.join([input_text, ans]))

    return stdout.strip(), stderr.strip()

def test_case_generator():
    length = random.randint(10,11)

    #alphabet = "abcdefghijklmnopqrstuvwxyz".capitalize()

    return str(length)+'\n'+' '.join([str(random.randint(1,100)) for _ in range(length)])


if __name__ == "__main__":
    # Replace 'script1.py' and 'script2.py' with your file names
    script1_path = 'b14003.py'
    script2_path = 'b14003-2.py'

    # Provide input text (you can modify this according to your test case)



    rep = 1000

    for i in range(rep):
        # Compare the outputs
        test_case = test_case_generator()

        # Run the first Python script
        output1, error1 = run_test(script1_path, test_case)

        # Run the second Python script
        output2, error2 = run_check(script2_path, test_case, output1)
        
        if error2:
            print("Error in script2.py:", error2, test_case)
            exit()
        elif output2!="1":
            print("Outputs are different.")
            print(output2)
            exit()
