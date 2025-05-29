import random,textwrap
text="1this is a file."
# def f1():
#     a=1
#     b=3
#     return a,b 
# a,b=f1()
# print(a,b)

# new_text=""
# for i in text:
#     if i=='1':
#         print("Yes")

text12='''_1.6 C PROGRAMMINGLANGUAGE 
Prior to writing C programs, it would be interesting to find out what really is C 
language, how it came into existence and where does it stand with respect to 
other computer languages. We will briefly outline these issues in the following 
section. 
1.6.1 History of  C  Programming Language 
C is a programming language developed at AT&T’s Bell Laboratory of USA 
in 1972. It was designed and written by Dennis Ritchie. As compared to other 
programming languages such as Pascal, C allows a precise control of input and 
output.  
Now let us see its historical development. The late 1960s were a turbulent era 
for computer systems research at Bell Telephone Laboratories. By 1960, many 
programming languages came into existence, almost each for a specific 
purpose. For example COBOL was being used for Commercial or Business 
Applications, FORTRAN for Scientific Applications and so on. So, people 
started thinking why could not there be a one general purpose language. 
Therefore, an International Committee was set up to develop such a language, 
which came out with the invention of ALGOL60. But this language never 
became popular because it was too abstract and too general. To improve this, a 
new language called Combined Programming Language (CPL) was developed 
at CambridgeUniversity. But this language was very complex in the sense that 
it had too many features and it was very difficult to learn. Martin Richards at 
CambridgeUniversity reduced the features of CPL and developed a new 
language called Basic Combined Programming Language (BCPL). But 
unfortunately it turned out to be much less powerful and too specific. Ken 
Thompson at AT & T’s Bell Labs, developed a language called B at the same 
time as a further simplification of CPL. But like BCPL this was also too 
specific. Ritchie inherited the features of B and BCPL and added some features 
on his own and developed a language called C. C proved to be quite compact 
and coherent. Ritchie first implemented C on a DEC PDP-11 that used the 
UNIX Operating System. 
Programming
 Fundamentals
 For many years the de facto standard for C was the version supplied with the 
UNIX version 5 operating system. The growing popularity of microcomputers 
led to the creation of large number of C implementations. At the source code 
level most of these implementations were highly compatible. However, since 
no standard existed there were discrepancies. To overcome this situation, 
ANSI established a committee in 1983 that defined an ANSI standard for the C 
language.  
1.6.2 Salient features of  C 
C is a general purpose%, structured programming language. Among the two 
types of programming languages discussed earlier, C lies in between these two 
categories. That’s why it is often called a middle level language. It means that 
it combines the elements of high level languages with the functionality of
 Design and develop an efficient algorithm to find the list of prime numbers in 
the range 501 to 2000. What is the complexity of this algorithm? 
b) Differentiate between Cubic-time and Factorial-time algorithms. Give example 
of one algorithm each for these two running times. 
c) Write an algorithm to multiply two square matrices of order n*n. Also explain 
the time complexity of this algorithm. 
d) What are asymptotic bounds for analysis of efficiency of algorithms? Why are 
asymptotic bounds used? What are their shortcomings? Explain the Big O and 
Big   notation with the help of a diagram. Find the Big O-notation and Θ
notation for the function: 
�
�(𝑛)= 100𝑛4 +1000𝑛3 +100000 
e) Write and explain the Left to Right binary exponentiation algorithm. 
Demonstrate the use of this algorithm to compute the value of 329 (Show the 
steps of computation). Explain the worst-case complexity of this algorithm. 
f) Write and explain the Bubble sort algorithm. Discuss its best and worst-case 
time complexity. 
g) What are the uses of recurrence relations? Solve the following recurrence 
relations using the Master’s method 
a. 𝑇(𝑛) = 4𝑇(𝑛
 4
 ) + 𝑛1 
b. 𝑇(𝑛) = 4𝑇(3𝑛
 4
 ) + 𝑛1 
a) What is an Optimisation Problem? Explain with the help of an example. When 
would you use a Greedy Approach to solve optimisation problem? Formulate the 
Task Scheduling Problem as an optimisation problem and write a greedy algorithm 
to solve this problem. Also, solve the following fractional Knapsack problem using 
greedy approach. Show all the steps. 
Suppose there is a knapsack of capacity 20 Kg and the following 6 items 
are to packed in it. The weight and profit of the items are as under: 
(p1, p2,…, p6) = (30,16,18,20,10, 7) 
(w1, w2,…, w6) = ( 5, 4, 6, 4, 5, 7) 
Select a subset of the items that maximises the profit while keeping the total 
weight below or equal to the given capaci'''

wo=textwrap.wrap(text12)
print(wo[3:])



       # if i < len(line) - 1:
                # # Width from start to next character
                #     substring = line[:i + 2]
                #     prev_substring = line[:i + 1]
                # Accurate width difference
                # x +=(fonts[rint].getbbox(substring))[2] - (fonts[rint].getbbox(prev_substring))[2]