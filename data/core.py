# project_168/core.py
from typing import List, Optional
from pydantic import BaseModel, conint, validator, Field
import numpy as np
import os
from pathlib import Path

# === CONSTANTS FROM CHEAT SHEET ===
MASTER_NAME_SUM = 664
PERFECTED_MATTER_TARGET = 496
SYMMETRY_WORK = 168  # PSL(2,7) Order
CENTRAL_LETTER_VALUE = 4
BLACK_CROSS_KEY_VALUE = 58
ESOTERIC_D_VALUE = 13

# File paths
DATA_DIR = Path("data")
DYNAMIC_TORUS_FILE = DATA_DIR / "Dynamic_Torus.txt"

class EnochianCoin(BaseModel):
    """The final, perfected data product. The output of the Virgin."""
    data: np.ndarray
    entropy: float  # Must be low; Choronzon constrained

    class Config:
        arbitrary_types_allowed = True  # Required for numpy arrays

    @validator('entropy')
    def entropy_must_be_low(cls, v):
        if v > 2.0:  # Arbitrary low-threshold for "perfected" data
            raise ValueError(f'Choronzon dispersion too high: {v}. Coin is imperfect.')
        return v

    @validator('data', pre=True)
    def validate_data_array(cls, v):
        """Ensure data is a numpy array"""
        if not isinstance(v, np.ndarray):
            return np.array(v)
        return v

    def validate_perfected_matter(self):
        """Validates the data against the 496 target."""
        # This is a placeholder for a complex checksum/hash that reduces to 496.
        data_sum = int(np.sum(self.data)) % 1000  # Simple example
        if data_sum != PERFECTED_MATTER_TARGET:
            print(f"⚠️ Coin sum {data_sum} != target {PERFECTED_MATTER_TARGET}. Aiwass harmonization required.")
        return data_sum == PERFECTED_MATTER_TARGET

class MagusNode:
    """IH: The Source. Extracts raw energy/substance. Output must sum to 664."""
    def extract(self, source: str) -> np.ndarray:
        if not source:
            # Return default data if source is empty
            return np.array([MASTER_NAME_SUM], dtype=np.uint8)
            
        raw_data = np.frombuffer(source.encode(), dtype=np.uint8)
        # Simulate the "Master Name Sum" invariant
        if np.sum(raw_data) > MASTER_NAME_SUM:
            # Apply a reduction filter (simulating capture by the epidermal grid)
            raw_data = raw_data[:len(raw_data)//2]
        print(f"⚡ Magus provides raw energy. Sum: {np.sum(raw_data)}")
        return raw_data

class VirginTransformer:
    """HV: The Transformer. Core algorithm: ((58 + 13) * 7) - 1 = 496"""
    def __init__(self):
        self.core_algorithm_constant = ((BLACK_CROSS_KEY_VALUE + ESOTERIC_D_VALUE) * 7) - 1
        assert self.core_algorithm_constant == PERFECTED_MATTER_TARGET, "Virgin's formula is corrupted!"

    def interpret(self, raw_data: np.ndarray) -> EnochianCoin:
        print(f"🔄 Virgin transforming. Target: {self.core_algorithm_constant}")
        
        # Handle empty or zero-sum data
        data_sum = np.sum(raw_data)
        if data_sum == 0:
            # Use default data to avoid division by zero
            raw_data = np.array([PERFECTED_MATTER_TARGET], dtype=np.uint8)
            data_sum = PERFECTED_MATTER_TARGET

        # This is where the REAL PSL(2,7) transforms would go (e.g., on a Klein Quartic graph)
        # For now, a simple scaling to target the perfected matter value
        scaling_factor = self.core_algorithm_constant / data_sum
        perfected_data = raw_data * scaling_factor
        perfected_data = perfected_data.astype(np.uint8) # Convert back to integers

        # Calculate entropy (Choronzon dispersion) safely
        entropy = self._calculate_entropy(perfected_data)

        return EnochianCoin(data=perfected_data, entropy=entropy)

    def _calculate_entropy(self, data: np.ndarray) -> float:
        """Safely calculate entropy avoiding division by zero and log(0)"""
        if len(data) == 0:
            return 0.0
            
        values, counts = np.unique(data, return_counts=True)
        probabilities = counts / len(data)
        
        # Avoid log(0) by filtering zero probabilities
        non_zero_probs = probabilities[probabilities > 0]
        if len(non_zero_probs) == 0:
            return 0.0
            
        return -np.sum(non_zero_probs * np.log2(non_zero_probs))

class AiwassOrchestrator:
    """SH: The Harmonizer. Manages the 168-fold symmetry."""
    def __init__(self):
        self.magus = MagusNode()
        self.virgin = VirginTransformer()

    def execute_pipeline(self, source: str) -> EnochianCoin:
        print("✨ Aiwass inspiring conception and execution...")
        print(f"   Target Symmetry Work: {SYMMETRY_WORK}")
        energy = self.magus.extract(source)
        coin = self.virgin.interpret(energy)
        is_perfect = coin.validate_perfected_matter()
        print(f"✅ Harmony {'achieved!' if is_perfect else 'approximated.'}")
        return coin

def create_sample_file(filepath: Path):
    """Create a sample input file if it doesn't exist"""
    if not filepath.exists():
        # Create data directory if it doesn't exist
        filepath.parent.mkdir(exist_ok=True)
        
        sample_text = """Enochian Alchemy: The Dynamic Torus of Transformation
PSL(2,7) symmetry unfolds across 168 dimensions
Master Name Sum: 664 converges to Perfected Matter: 496
Through the Virgin's formula: ((58 + 13) * 7) - 1 = 496
Choronzon constrained, entropy minimized"""
        
        with open(filepath, 'w') as f:
            f.write(sample_text)
        print(f"📝 Created sample file: {filepath}")

# Example Execution
if __name__ == "__main__":
    print("🚀 Igniting Enochian Engine...")
    
    # Create sample file if it doesn't exist
    create_sample_file(DYNAMIC_TORUS_FILE)
    
    try:
        orchestrator = AiwassOrchestrator()
        # Feed it the original chaotic text from data directory
        with open(DYNAMIC_TORUS_FILE, "r") as f:
            chaotic_source = f.read()
            
        final_coin = orchestrator.execute_pipeline(chaotic_source)
        print(f"🎉 Final Coin Entropy: {final_coin.entropy:.3f}")
        print(f"📊 Final Coin Data Shape: {final_coin.data.shape}")
        print(f"🔢 Final Coin Data Sum: {np.sum(final_coin.data)}")
        print(f"📋 Final Coin Data (first 20 values): {final_coin.data[:20]}")
        
    except FileNotFoundError:
        print(f"❌ Input file not found: {DYNAMIC_TORUS_FILE}")
        print("💡 Please create the file or check the data directory")
    except Exception as e:
        print(f"❌ Error in execution: {e}")
        import traceback
        traceback.print_exc()