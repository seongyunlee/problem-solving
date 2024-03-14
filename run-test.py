from itertools import combinations
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

    item = 2000

    return str(item)+"\n"+'\n'.join(' '.join([str(random.randint(0,10)) for _ in range(4)]) for _ in range(item))
    TC = []
    
    for i in range(1,11):
        for k in combinations(range(0,10),i):
           TC.append(str(i)+"\n"+' '.join(map(str,k))) 

    return TC
    '''
    T = 1

    test_case = []

    for _ in range(T):
        a,b = random.randint(1,100), random.randint(1,100)
        if a<b: a,b = b,a
        test_case.append(str(a)+' '+str(b))
    #alphabet = "abcdefghijklmnopqrstuvwxyz".capitalize()
    return str(T)+'\n'+'\n'.join(test_case)
    '''
def run_one():

    rep = 1

    script1_path = 'b2162.py'
    test_cases = test_case_generator()
    print(test_cases)

    for test_case in test_cases:
        # Compare the outputs

        # Run the first Python script
        output1, error1 = run_python_script(script1_path, test_case)

        print(output1)
        break

        R = output1.split('\n')
        if len(R)==1:
            print("0->\n",test_case)
        else:
            print(test_case)
            print(R)
def compare_two():

    rep = 3000

    script1_path = 'b14003.py'
    script2_path = 'b14003-2.py'

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

if __name__ == "__main__":
    # Replace 'script1.py' and 'script2.py' with your file names


    # Provide input text (you can modify this according to your test case)
    input_text = "Your input text goes here."
    run_one()
