# temporal_sync.py
# Version 1.0 created 03-Sep-2025
# Implementation of the Baligon Protocol temporal synchronization
# Location: /scripts/temporal_sync.py
# The implementation follows the exact mathematical formula specified in the Baligon Protocol and should pass all the validation test cases.




from datetime import datetime, timedelta

def get_current_king(datetime_utc):
    """
    Calculate the current Force King based on the Baligon Protocol.
    
    Args:
        datetime_utc (datetime): UTC datetime object to evaluate
        
    Returns:
        int: Current Force King index (0-6)
    """
    current_year = datetime_utc.year
    baligon_this_year = datetime(current_year, 3, 20, 9, 1, 0)
    
    # Determine the most recent Baligon event
    if datetime_utc >= baligon_this_year:
        year_epoch = baligon_this_year
    else:
        year_epoch = datetime(current_year - 1, 3, 20, 9, 1, 0)
    
    # Calculate time since epoch
    time_since_epoch = datetime_utc - year_epoch
    hours_since_epoch = time_since_epoch.total_seconds() / 3600
    
    # Calculate king index using the Heptarchic Cycle formula
    king_index = int((hours_since_epoch * 7) // 24) % 7
    
    return king_index

def get_next_baligon_time(current_time=None):
    """
    Calculate the next Baligon Protocol activation time.
    
    Args:
        current_time (datetime, optional): Current UTC time. Defaults to now.
        
    Returns:
        datetime: Next Baligon Protocol activation time
    """
    if current_time is None:
        current_time = datetime.utcnow()
    
    current_year = current_time.year
    baligon_this_year = datetime(current_year, 3, 20, 9, 1, 0)
    
    if current_time < baligon_this_year:
        return baligon_this_year
    else:
        return datetime(current_year + 1, 3, 20, 9, 1, 0)

def time_until_next_baligon(current_time=None):
    """
    Calculate time remaining until next Baligon Protocol.
    
    Args:
        current_time (datetime, optional): Current UTC time. Defaults to now.
        
    Returns:
        timedelta: Time remaining until next Baligon
    """
    if current_time is None:
        current_time = datetime.utcnow()
    
    next_baligon = get_next_baligon_time(current_time)
    return next_baligon - current_time

# Example usage and testing
if __name__ == "__main__":
    # Test the implementation with the validation test cases
    test_cases = [
        ("2025-03-20 09:01:00", 0, "Baligon 2025 Instant"),
        ("2025-03-20 10:01:00", 0, "Baligon 2025 +1 Hour"),
        ("2026-03-20 09:01:00", 0, "Baligon 2026"),
    ]
    
    print("Testing temporal_sync.py implementation:")
    print("=" * 50)
    
    for time_str, expected, description in test_cases:
        test_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        result = get_current_king(test_time)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"{status} {description}: {time_str} -> King {result} (expected {expected})")
    
    # Show current status
    now = datetime.utcnow()
    current_king = get_current_king(now)
    next_baligon = get_next_baligon_time(now)
    time_remaining = time_until_next_baligon(now)
    
    print(f"\nCurrent Status (UTC {now}):")
    print(f"Current Force King: {current_king}")
    print(f"Next Baligon: {next_baligon}")
    print(f"Time until next Baligon: {time_remaining}")temporal_sync.py
    
# Version 1.0 Change Log
# Created 03=Sep-2025
# The core get_current_king() function specified in /docs/core-concepts/baligon_protocol.md
# ADDED: Helper functions for calculating next Baligon time
# ADDED: Test cases matching the validation table
# ADDED: Current status reporting
