## ACE
The average causal effect is calculated by taking the difference between the average potential outcomes under the treatment and control conditions.
Mathematically, it can be expressed as E[Y(1) - Y(0)], where Y(1) is the potential outcome under treatment and Y(0) is the potential outcome under control. 

In this case I will be calculating the ACE for a diagram looking like this. Where I will be calculating the effect of Smoking on Cancer. The variables are binary.

<img width="191" height="299" alt="smok-tar-can" src="https://github.com/user-attachments/assets/b8a8ecdf-ee7b-43b1-bd93-b3963653269c" />

The formula to be used in this case is this one.

ACE = P(Y=1|do(X=1)) - P(Y=1|do(X=0))

Where Y = cancer, X = Smoking, and Tar = F

left part of ACE formula:

$$P(Y=1|do(X=1))=\sum_{F}P(F|X'=1).\sum_{X'}P(Y=1|F,X'=1).P(X'=1)$$

$$P(Y=1|do(X=1))=(P(F=1|X=1).\sum_{X'}P(Y=1|F=1,X').P(X'))$$
$$+ (P(F=0|X=1).\sum_{X'}P(Y=1|F=0,X).P(X'))$$

$$P(Y|do(X=1))= P(F=1|X=1).[P(Y=1|X=0,F=1).P(X=0)+P(Y=1|X=1,F=1).P(X=1)]$$
              $$+P(F=0|X=1).[P(Y=1|X=0,F=0).P(X=0)+P(Y=1|X=1,F=0).P(X=1)]$$

right part of the formula:

$$P(Y=1|do(X=0))=\sum_{F}P(F|X=0).\sum_{X'}P(Y=1|F,X').P(X')$$

$$P(Y=1|do(X=0))=(P(F=1|X=0).\sum_{X'}P(Y=1|F=1,X').P(X'))$$
                $$+(P(F=0|X=0).\sum_{X'}P(Y=1|F=0,X').P(X'))$$
                
$$P(Y|do(X=0))= P(F=1|X=0).[P(Y=1|X=0,F=1).P(X=0)+P(Y=1|X=1,F=1).P(X=1)]$$
              $$+P(F=0|X=0).[P(Y=1|X=0,F=0).P(X=0)+P(Y=1|X=1,F=0).P(X=1)]$$


### Probabilities

The probabibilities can be fetched from the image below.

<img width="296" height="422" alt="probabilities" src="https://github.com/user-attachments/assets/36a33502-1e0c-4f8f-ab8b-88e83d09f315" />

### Result

P\_Y\_doX\_1=(0.65\*((0.35\*0.5)+(0.85\*0.5)) + 0.35\*((0.15\*0.5)+(0.10\*0.5)))

P\_Y\_doX\_0=(0.55\*((0.35\*0.5)+(0.85\*0.5)) + 0.45\*((0.15\*0.5)+(0.10\*0.5)))





