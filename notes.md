Multinomial Naive Bayes

| Size        | Accuracy      | Precision      | Recall      | F1          |
| ----------- | ----------- | -------------- | ------------- | ----------- |
| 100 samples |  0.15       | 0.012499999999 | 0.083333333 | 0.0217391304  |
| 1000 samples|  0.19       | 0.15807296876  | 0.281860916 | 0.1826662964  |
| 5000 samples|  0.087      | 0.057816323962 | 0.108122116 | 0.0564354801  |
| 10 000 samples | 0.07     | 0.034450303229 | 0.062482486 | 0.0245219907  |
| 40 000 samples | 0.042375 | 0.069259584147 | 0.049930227 | 0.0408452576  |


Support vector machine with linear kernel

| Size        | Accuracy    | Precision     | Recall        | F1           |
| ----------- | ----------- | ------------- | ------------- | ------------ |
| 100 samples | 0.15        | 0.01249999999 | 0.08333333333 | 0.0217391304 |
| 1000 samples| 0.235       | 0.19812596006 | 0.16629198966 | 0.1409799350 |
| 5000 samples | 0.192      | 0.01476923076 | 0.07692307692 | 0.0247805885 |

I had some troubles training the SVC model and therefore can't give more results with bigger sample sizes. Training with 1000 samples went very fast but 5000 samples took almost an hour. I tried finding ways to optimize the code to be able to get more samples but couldn't do better than this unfortunately. The NB learned quite fast up until 10k samples but having more samples than that took longer than expected.

As for the results it can be seen that the sample of 1000 samples had the best performance for both models. This is probably because the samples are generated randomly from the UN-english file and therefore the 1000 sample may have been a "better" sample than the others.

