"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""
import getpass                                                                  
import os                                                                       
import sys                                                                      
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html     
                                                                                
# Print out the command line arguments in sys.argv, one per line:               
# YOUR CODE HERE                                                                   
print(sys.argv, "\n")                                                              
# Print out the OS platform you're using:                                          
# YOUR CODE HERE                                                                   
print(sys.platform)                                                                
print(sys.version.split('/'))                                                      
# Print out the OS platform you're using:                                          
# Print out the version of Python you're using:                                    
# YOUR CODE HERE                                                                
                                                                                
                                                                                
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html   
                                                                                
# Print the current process ID                                                  
# YOUR CODE HERE                                                                
pid = os.getpid()                                                               
print(pid)                                                                      
# Print the current working directory (cwd):                                    
# YOUR CODE HERE                                                                
cwd = os.getcwd()                                                               
print(cwd)                                                                      
                                                                                
# Print out your machine's login name                                           
# YOUR CODE HERE                                                                
user = getpass.getuser()                                                        
print(user)                  
