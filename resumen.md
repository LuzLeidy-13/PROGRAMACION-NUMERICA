### COMPARING THE MOORE-PENROSE PSEUDOINVERSE AND GRADIENT DESCENT FOR SOLVING LINEAR REGRESSION PROBLEMS: A PERFORMANCE ANALYSIS



##### This work compares two main methods for solving linear regression problems: the Moore-Penrose pseudoinverse (a direct or analytical mathematical solution) and gradient descent (an iterative method).

##### 

##### Linear regression models the relationship between a dependent variable and one or more independent variables, seeking the parameters that minimize the squared error (OLS). It can be solved using the Moore-Penrose pseudoinverse, which provides an exact solution, or by gradient descent, which iteratively adjusts the parameters. Its simplicity and efficiency make it fundamental in numerous scientific fields.

##### 

##### The depth of the analysis is reflected in the examination of the mathematical foundations of each method.For the pseudoinverse, the author highlights its practical implementation through Singular Value Decomposition (SVD), which avoids the numerical issues associated with directly computing. This approach ensures numericalstability but has a computational complexity dominated by the cubic term , limiting its applicability to high-dimensional problems

##### 

##### Gradient descent, on the other hand, is analyzed from the perspective of iterative optimization, where convergence toward the minimum depends on the learning rate and the spectral properties of the design matrix. The author theoretically explores how the condition number of X critically influences the algorithm's behavior. For well-conditioned matrices, convergence is monotonic, whereas in ill-conditioned problems, numerical instability and extremely slow convergence emerge.

##### 

##### The conclusions point toward a more nuanced understanding of the trade-off between analytical and iterative methods, suggesting that the optimal choice is determined by the interaction between dimensionality, numerical conditioning, and available computational resources. The work lays the theoretical foundation for the development of hybrid approaches that combine the advantages of both paradigms, particularly in the context of regularization and adaptive optimization.



