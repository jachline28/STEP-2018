# STEP 2018 

### Summer Trainee Engineering Program Intern (STEP)
There are eight classes per week (from 5/25 ~ 7/13) with different topics, including:  
1. Intro  
2. Data Structures  
3. Code Modulity  
4. More Data Structures and Algorithms  
5. TSP Challenges  
6. Distributed Computing and AppEngine  
7. Game Tree Challenge  
8. Caching and Optimizing  

************************************
#### Week 1: [I Can Haz Wordz](https://icanhazwordz.appspot.com/")
The Goal is to get the highest score ([see help](https://icanhazwordz.appspot.com/help)) by creating long words, and the alphabets used are limited to the ones shown on the 4x4 grid.  

Some Points:  
1. In the provided [dictionary](https://icanhazwordz.appspot.com/dictionary.words), Q are always inmediately followed by U. So character replacement is used when cleaning the strings.  
2. I was stucked in finding substring, where I (Python Newbee) thought that `` if substring in string:   `` finds the longest non-continuous, but it doesn't, I have to do it manually, pairing one by one.
3. Automated test: Selenium Webdriver on Chrome. [Chrome Driver](http://chromedriver.chromium.org/) 
> useful functions in Selenium :
> > driver.find\_element\_by\_xpath()  
> > driver.find\_element\_by\_id()  
> > driver.get()   

************************************
#### Week 2: Matrix Multiplication
Write code to calculate C = A * B, where A, B and C are matrices of size N * N. Measure the execution time of your code for various Ns, and plot the relationship between N and the execution time.


1. Naive Solution: `O(n^3)` 
2. Strassen Algorithm: Using the concept of divide-and-conquer to fasten to `O(n^2.807)`. Efficient than Naive solution for large N.  
	Referncing: [Strassen 演算法講解 by ccjou](https://ccjou.wordpress.com/2013/06/04/%E5%88%86%E6%B2%BB%E7%9F%A9%E9%99%A3%E4%B9%98%E6%B3%95%E2%94%80%E2%94%80strassen-%E6%BC%94%E7%AE%97%E6%B3%95/)   
3. Encountered Problem (Python): The difference between normal list and numpy list, referencing [@aira002](https://qiita.com/aira002/items/50f0b58f57eba1ca2183) (有沒有逗點差別很大)  

************************************
