# Aimpoint Digital Ad Optimization Hackathon

Suppose we have different versions of an ad that we want to gauge public response to. How do we select what is the best version of the ad to show to people?

To tackle this question, this hackathon has provided an API that takes as input one of 5 different ads and returns the response to that ad ("click" or "no click"). We assume that the probability of click for each of the 5 ads is fixed and does not vary over time. The goal then of this hackathon is to devise some scheme to query this API that maximizes the total number of clicks over 1000 queries. 