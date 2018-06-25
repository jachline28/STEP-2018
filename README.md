# STEP 2018 

### Summer Trainee Engineering Program Intern (STEP)
There are eight classes per week (from 5/25 ~ 7/13) with different topics, including:  
1. [Intro](#week-1-i-can-haz-wordz)  
2. [Data Structures](#week-2-matrix-multiplication)  
3. [Code Modulity](#week-3-code-modulity)  
4. [Graph BFS & DFS](#week-4-graph-bfs-&-dfs)  
5. [TSP Challenges](#week-5-tsp-challenges)  
6. Distributed Computing and AppEngine  
7. Game Tree Challenge  
8. Caching and Optimizing  

************************************
#### Week 1: [I Can Haz Wordz](https://icanhazwordz.appspot.com/") 
The Goal is to get the highest score ([see help](https://icanhazwordz.appspot.com/help)) by creating long words, and the alphabets used are limited to the ones shown on the 4x4 grid.  

Some Points:  
1. In the provided [dictionary](https://icanhazwordz.appspot.com/dictionary.words), Q are always inmediately followed by U. So character replacement is used when cleaning the strings.  
2. I was stucked in finding substring, where I (Python Newbee) thought that `` if substring in string:   `` finds the longest non-continuous, but it doesn't, I have to do it manually, pairing one by one.
3. [Automated test](https://github.com/jachline28/STEP-2018/blob/master/week1/auto.py): Selenium Webdriver on Chrome. [Chrome Driver](http://chromedriver.chromium.org/) 
> useful functions in Selenium :
> > driver.find\_element\_by\_xpath()  
> > driver.find\_element\_by\_id()  
> > driver.get()   

[sample code by teachers](https://github.com/step2018/idohazwordz)
************************************
#### Week 2: Matrix Multiplication
Write code to calculate C = A * B, where A, B and C are matrices of size N * N. Measure the execution time of your code for various Ns, and plot the relationship between N and the execution time.


1. [Naive Solution](https://github.com/jachline28/STEP-2018/blob/master/week2/matrix.py): `O(n^3)` 
2. [Strassen Algorithm](https://github.com/jachline28/STEP-2018/blob/master/week2/Strassen.py): Using the concept of divide-and-conquer to fasten to `O(n^2.807)`. Efficient than Naive solution for large N.  
	Referncing: [Strassen 演算法講解 by ccjou](https://ccjou.wordpress.com/2013/06/04/%E5%88%86%E6%B2%BB%E7%9F%A9%E9%99%A3%E4%B9%98%E6%B3%95%E2%94%80%E2%94%80strassen-%E6%BC%94%E7%AE%97%E6%B3%95/)   
3. Encountered Problem (Python): The difference between normal list and numpy list, referencing [@aira002](https://qiita.com/aira002/items/50f0b58f57eba1ca2183) (有沒有逗點差別很大)  

##### Homework Question:    
1. Large-scale database systems used in a real world tend to prefer a tree O(log N) to a hash table O(1). Why?    
Ans: two reasons.  
(1) the size of hash table usually is larger than the actual size of data since "n bucket for n item" is too ideal and larger space can avoid frequent collisions.  
(2) Additionally, regarding searching in a large database, the searching criteria normally will not be finding a specific object, but rather covers a range of data.   

2. Design a cache that achieves the following operations with O(1). (1) Find if the given pair is contained in the cache or not. (2) If the pair is not contained, insert the pair into the cache after evicting the least recently accessed pair.   
Ans: [Hash Table with Linked-list](https://github.com/jachline28/STEP-2018/blob/master/week2/Q3.jpg)  

************************************
#### Week 3: Code Modulity  
Create a simple calculator with "Code Modulity" and "Rule of Debugging" in mind. (1) Add additional multiplication and division functions to  [Haraken Sensei's Code](https://github.com/xharaken/step2015/blob/master/calculator_modularize_2.py). (2) Add test cases that can evaluate all forms of possible inputs. (3) Add parenthesis   
*Some points for my code:*      
1. Implemented a easy CLI version supporting  Arithmetic Operators, Power, Modulo Calculation, Parenthesis Usage and Decimal to Binary, octal, hexadecimal systems.   
2. Test cases included striping all weird whitespaces, multi-use of symbol of multiplication `*` and `x`, detection of demominator as zero, parenthesis faliure   
3. Try to complete the Go version, but only finish (1) and (2) ... Go is hard QQ    
4. Things have **NOT** done:    
- no test case for binary, octal, hex formula   
- some code looks redundent, might have better data structures to reduce repetitive codes (think)   

*Some points from teacher's code:*   
1. The thought of giving labels to differencing between number and symbols    
2. Orders are still in consideration by implementing list   
3. The flow from tokenizing (labeling symbols, calculating numbers char by char, labeling numbers) to evaluating (formula calculation)    

************************************
#### Week 4: Graph BFS & DFS
This week's challenge is to find **interesting things** from links of wikipedia, where the data of links and page name can be downloaded from [here](https://drive.google.com/file/d/1HT6OiQgG0wfeC0xulLfuWqq7y4KT4xHW/view).   
I tried to find duplex connected clique in this dataset and my description is over [here](https://docs.google.com/document/d/16pQmg6Riw1BNAM6ijPzmBL7mH6uyTS4PaXDhCw4AmLs/edit).   
One of the big challenge is to deal with large dataset, so I did not traverse through the whole dataset to find the longest string.  

************************************
#### Week 5: TSP Challenges  

The detail of this week's homework is over [here](https://github.com/rika77/google-step-tsp), where I worked with [Rika-san](https://github.com/rika77) and [Saki-san](https://github.com/h54k3y).