def f(p, q):
    # Edge Case: If both have 0 probability, no one ever wins.
    if p == 0 and q == 0:
        return None
    
    # Calculate the probability of a "Safe Round" (both miss)
    # common_ratio = (1-p) * (1-q)
    common_ratio = (1 - p) * (1 - q)
    
    # Scenario 1: A shoots first
    # Sum of geometric series: a / (1 - r)
    prob_a_starts = p / (1 - common_ratio)
    
    # Scenario 2: B shoots first
    # B must miss first (1-q), then it's exactly the same as A starting.
    prob_b_starts = (1 - q) * prob_a_starts
    
    return (prob_a_starts, prob_b_starts)