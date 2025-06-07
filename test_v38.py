#!/usr/bin/env python3

import json
from solution import calculate_reimbursement

def test_key_cases():
    """Test Algorithm V38 against key breakthrough cases"""
    
    # Test cases from your discoveries
    test_cases = [
        # Low receipt cases (the V38 breakthrough)
        {"days": 3, "miles": 93, "receipts": 1.42, "expected_note": "Low receipt case - should use (base + receipts) * 1.1"},
        {"days": 1, "miles": 50, "receipts": 25, "expected_note": "Low receipt case"},
        {"days": 2, "miles": 100, "receipts": 75, "expected_note": "Low receipt case"},
        
        # Vacation penalty cases  
        {"days": 2, "miles": 69, "receipts": 2116, "expected_note": "Vacation penalty case"},
        {"days": 3, "miles": 87, "receipts": 2178, "expected_note": "Vacation penalty case"},
        {"days": 1, "miles": 45, "receipts": 2452, "expected_note": "Vacation penalty case"},
        
        # 5-day trips
        {"days": 5, "miles": 400, "receipts": 600, "expected_note": "5-day trip - high receipts"},
        {"days": 5, "miles": 250, "receipts": 100, "expected_note": "5-day trip - low receipts"},
        
        # Long trips that were problematic
        {"days": 8, "miles": 400, "receipts": 1200, "expected_note": "8-day trip"},
        {"days": 11, "miles": 550, "receipts": 800, "expected_note": "11-day trip"},
        {"days": 13, "miles": 650, "receipts": 1000, "expected_note": "13-day trip"},
        {"days": 14, "miles": 300, "receipts": 500, "expected_note": "14-day trip - low miles"},
        {"days": 14, "miles": 1200, "receipts": 800, "expected_note": "14-day trip - high miles"},
        
        # High-ratio cases
        {"days": 3, "miles": 200, "receipts": 800, "expected_note": "High-ratio case"},
        {"days": 4, "miles": 300, "receipts": 1200, "expected_note": "High-ratio case"},
    ]
    
    print("ALGORITHM V38 TEST RESULTS")
    print("=" * 50)
    print(f"{'Days':<4} {'Miles':<6} {'Receipts':<9} {'Result':<8} {'Note'}")
    print("-" * 50)
    
    for case in test_cases:
        result = calculate_reimbursement(case["days"], case["miles"], case["receipts"])
        base = 98 * case["days"] + 0.50 * case["miles"]
        
        print(f"{case['days']:<4} {case['miles']:<6} ${case['receipts']:<8.2f} ${result:<7.2f} {case['expected_note']}")
        
        # Show ratio for context
        if case["receipts"] < 100:
            expected_low = (base + case["receipts"]) * 1.1
            print(f"     -> Low receipt formula: ${expected_low:.2f}")
        
    print("\n" + "=" * 50)
    print("V38 BREAKTHROUGH: Low receipt cases use (base + receipts) * 1.1")
    print("This should dramatically improve performance on ~13 critical cases")

def test_sample_from_dataset():
    """Test a few cases from the actual dataset"""
    try:
        with open('public_cases.json', 'r') as f:
            data = json.load(f)
            cases = data['cases'][:10]  # Test first 10 cases
            
        print("\nSAMPLE DATASET TEST (First 10 cases)")
        print("=" * 50)
        
        total_error = 0
        for i, case in enumerate(cases):
            result = calculate_reimbursement(
                case['trip_duration_days'],
                case['miles_traveled'], 
                case['total_receipts_amount']
            )
            expected = case['expected_reimbursement_amount']
            error = abs(result - expected)
            total_error += error
            
            print(f"Case {i+1}: Expected ${expected:.2f}, Got ${result:.2f}, Error ${error:.2f}")
        
        avg_error = total_error / len(cases)
        print(f"\nAverage Error on 10 cases: ${avg_error:.2f}")
        
        if avg_error < 50:
            print("🎯 TARGET ACHIEVED! Ready for submission!")
        else:
            print(f"Gap to target: ${avg_error - 50:.2f}")
            
    except FileNotFoundError:
        print("public_cases.json not found - run locally to test full dataset")

if __name__ == "__main__":
    test_key_cases()
    test_sample_from_dataset()
