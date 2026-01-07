import re

def get_valid_coupons(code, businessLine, isActive):
    # 1. Define the required order for business lines
    order = {
        "electronics": 0,
        "grocery": 1,
        "pharmacy": 2,
        "restaurant": 3
    }
    
    # 2. Regular expression for alphanumeric characters + underscores
    # ^[a-zA-Z0-9_]+$ ensures it is non-empty and contains only allowed chars
    valid_code_pattern = re.compile(r'^[a-zA-Z0-9_]+$')
    
    valid_coupons = []
    
    # 3. Iterate through coupons and apply filtering logic
    for i in range(len(code)):
        c_code = code[i]
        c_line = businessLine[i]
        c_active = isActive[i]
        
        # Check all three conditions:
        # - isActive is true
        # - businessLine is in our allowed categories
        # - code is non-empty and matches the alphanumeric/underscore pattern
        if c_active and (c_line in order) and valid_code_pattern.match(c_code):
            valid_coupons.append((c_line, c_code))
            
    # 4. Sort the filtered list
    # Primary key: businessLine order index
    # Secondary key: code (lexicographical)
    valid_coupons.sort(key=lambda x: (order[x[0]], x[1]))
    
    # 5. Extract only the codes for the final result
    return [coupon[1] for coupon in valid_coupons]

# Example usage:
# codes = ["ELEC1", "groc_1", "Invalid!", "pharm123", "ELEC0"]
# lines = ["electronics", "grocery", "pharmacy", "pharmacy", "electronics"]
# active = [True, True, True, True, True]
# Result: ["ELEC0", "ELEC1", "groc_1", "pharm123"]