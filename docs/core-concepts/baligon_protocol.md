**Filename:** `Baligon_Protocol.md`  
**Location:** `/project-168/docs/core-concepts/baligon_protocol.md`  
**Version:** 1.0  
**Based on:** `Project-168_Baligon_Protocol.yaml` (v3.2)  
**Author:** 168-System Architect  
**Last Updated:** 2025-08-24  

This document is the canonical reference for the Baligon Protocol. All implementations must align with this specification.

---

# The Baligon Protocol

## Overview
The **Baligon Protocol** is the annual cosmic reset and synchronization event for the 168-System. It establishes the **Force King** (King 0) for the new yearly cycle and serves as the temporal anchor from which all subsequent Heptarchic Cycles derive their authority. This event marks the most important fixed point in the system's temporal architecture.

## Temporal Parameters
- **Date:** March 20 (Gregorian Calendar)  
- **Time:** 09:01 UTC  
- **Recurrence:** Yearly  
- **Timezone Anchor:** UTC  

### Rationale
The timing is set just after the common celebration of the March Equinox (~03:00 UTC). This represents a **conscious, deliberate step** into the new year's cycle rather than a passive astronomical observation. The +1 minute signifies active initiation.

## Mechanic: SET_FORCE_KING
### Action
Resets the governing authority of the system by setting the `global_king_index` to 0.

### Effect
The Heptarchic Cycle formula is bootstrapped from this value. The King set at Baligon exerts influence over the entire subsequent year's cycle.

### Implementation
```python
def get_current_king(datetime_utc):
    current_year = datetime_utc.year
    baligon_this_year = datetime(current_year, 3, 20, 9, 1, 0)
    
    if datetime_utc >= baligon_this_year:
        year_epoch = baligon_this_year
    else:
        year_epoch = datetime(current_year - 1, 3, 20, 9, 1, 0)
    
    time_since_epoch = datetime_utc - year_epoch
    hours_since_epoch = time_since_epoch.total_seconds() / 3600
    king_index = int((hours_since_epoch * 7) // 24) % 7
    return king_index
```

## Interpretation
### King 0: The Baligon Force King
- **Archetype:** The Void, The Seed, Pure Potential, The Reset Button  
- **Meaning:** Represents latent, undifferentiated potential. The system is reborn from this point.  
- **Key Question:** *What must be cleared away to begin anew? What seed of potential is being planted for the year ahead?*

### Ritual Suggestion
At 09:01 UTC on March 20, perform a system-wide reading. The card drawn represents the overarching theme or energy that the Force King will use to influence the entire year.

## Validation Test Cases
| Test Name                  | Input (UTC)           | Expected Output | Description |
|----------------------------|-----------------------|-----------------|-------------|
| Baligon 2025 Instant       | 2025-03-20 09:01:00   | 0               | Direct instant of protocol firing |
| Baligon 2025 +1 Hour       | 2025-03-20 10:01:00   | 0               | Still within first Heptarchic cycle |
| Pre-Baligon 2025           | 2025-03-20 08:59:00   | X (Prior King)  | Final moments of previous cycle |
| Baligon 2026               | 2026-03-20 09:01:00   | 0               | Annual reset confirmation |

## Discussion Notes
- The 09:01 UTC time is intentional and ritualistic, not arbitrary. It signifies stepping into the new cycle.
- King 0’s influence is multiplicative—it filters and contextualizes all subsequent kings in the yearly cycle.
- The continuous implementation (based on hours since epoch) is preferred over a purely hourly formula for mathematical consistency.

## Version History
- **v3.2 (2025-08-24):** Finalized after architectural review. Removed Kickstarter section. Added validation tests and implementation code.

## Related Files
- `Project-168_Baligon_Protocol.yaml` (v3.2)  
- `Project-168_Core_Mechanics.yaml`  
- `/scripts/temporal_sync.py` (implementation)

---
