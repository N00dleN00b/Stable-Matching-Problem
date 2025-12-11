# Stable Matching Algorithm Variants

A Python implementation of extended Gale-Shapley algorithms for solving variations of the classic Stable Matching Problem, including support for forbidden pairs and preference indifference.

## Overview

This project implements two variations of the Gale-Shapley stable matching algorithm, addressing real-world scenarios where classical stable matching assumptions don't hold. The implementations handle forbidden matches (e.g., due to conflicts of interest) and tied preferences (where participants may be indifferent between multiple options).

## Features

- **Forbidden Matches Support**: Prevents specified pairs from being matched together
- **Preference Indifference Handling**: Accommodates tied preferences in ranking lists
- **GitHub Classroom Integration**: Automated testing and feedback system
- **Extensible Architecture**: Reuses core Gale-Shapley logic for efficient implementation

## Problem Variants

### Task A: Forbidden Matches

Implements stable matching with constraints on which pairs are allowed to match.

**Use Cases:**
- Academic advisor-student assignments with conflict of interest restrictions
- Residency matching programs with institutional prohibitions
- Collaborative project assignments with prior relationship constraints

**Function Signature:**

def gs_block(men, women, pref, blocked):
    """
    Computes stable matching while respecting forbidden pair constraints.
    
    Parameters:
    -----------
    men : list
        List of men to be matched
    women : list
        List of women to be matched
    pref : dict
        Dictionary mapping each person to their preference list
    blocked : set
        Set of tuples representing forbidden pairs
        Example: {('xavier','clare'), ('zeus','clare'), ('zeus','amy')}
    
    Returns:
    --------
    dict : Stable matching respecting blocked pairs
    """


**Theoretical Foundation:**

Based on the revised stable matching definition from Algorithm Design (p. 20), where a matching M is stable if:
1. No forbidden pair appears in M
2. There is no pair (m, w) ∉ M ∪ F where m and w prefer each other to their current partners

### Task B: Preference Indifference

Implements stable matching where participants can express indifference among multiple candidates.

**Use Cases:**
- Job matching where employers are equally satisfied with multiple qualified candidates
- College admissions where applicants rank schools in tiers
- Resource allocation with equivalent utility options

**Function Signature:**
python
def gs_tie(men, women, preftie):
    """
    Computes stable matching with tied preferences.
    
    Parameters:
    -----------
    men : list
        List of men to be matched
    women : list
        List of women to be matched
    preftie : dict
        Dictionary mapping each person to a list of sets representing preference tiers
        Example: {'xavier': [{'bertha'}, {'amy'}, {'clare'}],
                  'yancey': [{'amy','bertha'}, {'clare'}]}
    
    Returns:
    --------
    dict : Stable matching considering preference ties
    """


**Preference Format:**

Preferences are expressed as lists of sets, where:
- Elements in the same set indicate indifference
- Sets are ordered from most to least preferred
- Example: `[{'amy','bertha'}, {'clare'}]` means indifferent between Amy and Bertha, but both are preferred to Clare

**Example Preference Structure:**
```python
thepreftie = {
    'xavier': [{'bertha'}, {'amy'}, {'clare'}],           # Strict preferences
    'yancey': [{'amy','bertha'}, {'clare'}],              # Indifferent between Amy & Bertha
    'zeus': [{'amy'}, {'bertha','clare'}],                # Indifferent between Bertha & Clare
    'amy': [{'zeus','xavier','yancey'}],                  # Indifferent among all three
    'bertha': [{'zeus'}, {'xavier'}, {'yancey'}],         # Strict preferences
    'clare': [{'xavier','yancey'}, {'zeus'}]              # Indifferent between Xavier & Yancey
}
```

## Installation

```bash
# Clone the repository (via GitHub Classroom)
git clone <your-classroom-repository-url>
cd stable-matching-variants

# No external dependencies required (uses Python standard library)
```

## Usage

### Basic Implementation

```python
from gs import gs_block, gs_tie

# Task A: Forbidden Matches
men = ['xavier', 'yancey', 'zeus']
women = ['amy', 'bertha', 'clare']
pref = {
    'xavier': ['bertha', 'amy', 'clare'],
    'yancey': ['amy', 'bertha', 'clare'],
    'zeus': ['amy', 'bertha', 'clare'],
    'amy': ['yancey', 'xavier', 'zeus'],
    'bertha': ['xavier', 'yancey', 'zeus'],
    'clare': ['xavier', 'yancey', 'zeus']
}
blocked = {('xavier', 'clare'), ('zeus', 'clare'), ('zeus', 'amy')}

matching = gs_block(men, women, pref, blocked)
print(matching)

# Task B: Preference Indifference
preftie = {
    'xavier': [{'bertha'}, {'amy'}, {'clare'}],
    'yancey': [{'amy', 'bertha'}, {'clare'}],
    'zeus': [{'amy'}, {'bertha', 'clare'}],
    'amy': [{'zeus', 'xavier', 'yancey'}],
    'bertha': [{'zeus'}, {'xavier'}, {'yancey'}],
    'clare': [{'xavier', 'yancey'}, {'zeus'}]
}

matching_tie = gs_tie(men, women, preftie)
print(matching_tie)
```

## Development Guidelines

### Code Requirements

1. **Author Attribution**: Include your name(s) as a comment in the first line of `gs.py`
   ```python
   # Author: Your Name
   ```

2. **Code Reuse**: Leverage the original `gs()` method implementation where appropriate to avoid duplication

3. **Testing**: Utilize GitHub Classroom's automated testing for immediate feedback

4. **Iteration**: Submit multiple times until tests pass - there's no penalty for resubmissions

### File Structure

```
.
├── gs.py                 # Main implementation file (your code goes here)
├── test_gs.py           # Automated test suite (do not modify)
├── README.md            # Project documentation
└── .github/
    └── workflows/       # CI/CD configuration for automated testing
```

## Testing & Validation

### Automated Testing

GitHub Classroom provides automated feedback on correctness:

1. Push your code to the repository
2. GitHub Actions runs test suite automatically
3. Check the "Actions" tab for test results
4. Review feedback and iterate as needed

### Manual Testing

```python
# Run local tests
python -m pytest test_gs.py -v

# Test specific functions
python -m pytest test_gs.py::test_gs_block -v
python -m pytest test_gs.py::test_gs_tie -v
```

## Implementation Strategy

### Recommended Approach

1. **Understand the Base Algorithm**: Review the standard Gale-Shapley implementation
2. **Identify Modifications**: Determine where constraints affect the algorithm flow
3. **Adapt Proposal Logic**: Modify the proposal mechanism to respect forbidden pairs or handle ties
4. **Validate Stability**: Ensure final matching satisfies stability conditions
5. **Test Incrementally**: Use automated tests to verify correctness at each step

### Key Considerations

- **Forbidden Matches**: Check blocked set before creating/accepting proposals
- **Preference Ties**: Handle sets within preference lists appropriately
- **Edge Cases**: Consider scenarios with no valid matching or multiple stable solutions
- **Efficiency**: Maintain O(n²) complexity where n is the number of participants

## Theoretical Background

### Stable Matching Definition

A matching M is **stable** if there exists no blocking pair (m, w) where:
- Both m and w prefer each other to their current partners in M
- The pair (m, w) is not forbidden (for Task A)

### Properties

- **Existence**: A stable matching always exists (even with constraints)
- **Proposer Optimality**: Proposing side receives their best stable partner
- **Receiver Pessimality**: Receiving side gets their worst stable partner

## References

- Algorithm Design by Kleinberg & Tardos (Chapter 1: Stable Matching)
- Gale-Shapley Algorithm (1962): "College Admissions and the Stability of Marriage"

