def counter(filename):
    sum = 0
    with open(filename) as f:
        content = f.readlines()
        for line in content:  
            try:
                print(float(line))        
                sum += float(line)
            except: 
                print(f"cannot convert {line}")
    print(sum)



counter('number.txt')


"""
Practical task 1.
Write a script (""count_numbers"") to calculate and print out the sum of all numbers in the file named "numbers.txt", ignoring lines that are empty or start with '#' symbol.
====== number.txt=========
# 1000000 <-- do not count this
123.4
-34.21
56.71000444.45
-555.72
+234.2
false
False 2v

========================
Requirement 1. Create or use your GITHUB repo. Push code there and provide link to this repo as an answer;
Requirement 2. Your code runs without Exceptions;
Requirement 3. Lines that start with '#' symbol shall be ignored;
Requirement 4. Empty lines shall be ignored;
Requirement 5. Numbers can be positive and negative. e.g. "-1+2=1";
Requirement 6. Use your main language;
Requirement 7. Do the best you can. Do not spend more than 25 minutes. Push the code even if not all requirements are completed
"""
