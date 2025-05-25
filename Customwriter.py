import Buddy, random, textwrap

fonts=["LettersFont\Lettersv1-Regular (8).ttf","LettersFont\Lettersv2-Regular (2).ttf"]



slate=Buddy.Handwriting()

text11=''' A translator program 
called a compiler or interpreter, translates the source program into the object program. This is the compilation or interpretation phase. All the testing of the source program as regards the correct format of instructions is performed at this stage and the errors, if any, are printed. If there is no error, the source program is transformed into the machine language program called Object Program. The Object Program is executed to perform calculations. This stage is the execution phase. Data, if required by the 
program, are supplied now and the results are obtained on the output device. The complete process is shown in fig 1.1 below:'''

# Text corpus division
text12='''1.6 C PROGRAMMINGLANGUAGE 
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
C is a general purpose, structured programming language. Among the two 
types of programming languages discussed earlier, C lies in between these two 
categories. That’s why it is often called a middle level language. It means that 
it combines the elements of high level languages with the functionality of'''



slate.write(text=text12,fontsize=72,font_path=fonts)
