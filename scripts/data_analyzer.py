#!/usr/bin/env python3
"""
Project 168 Data Analyzer
Core data analysis functions for esoteric research patterns

Author: Project 168 Research Team
Created: 2025-08-17
"""

import pandas as pd
import numpy as np
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Project168Analyzer:
    """Main analysis class for Project 168 datasets"""
    
    def __init__(self, data_path="../data"):
        self.data_path = Path(data_path)
        self.core_data = None
        self.esoteric_data = None
        self.hypercards_data = None
        
    def load_datasets(self):
        """Load all CSV datasets from the data directories"""
        try:
            # Load core datasets
            core_path = self.data_path / "core" / "core_datasets.csv"
            if core_path.exists():
                self.core_data = pd.read_csv(core_path)
                logger.info(f"Loaded {len(self.core_data)} core datasets")
            
            # Load esoteric datasets
            esoteric_path = self.data_path / "esoteric" / "esoteric_datasets.csv"
            if esoteric_path.exists():
                self.esoteric_data = pd.read_csv(esoteric_path)
                logger.info(f"Loaded {len(self.esoteric_data)} esoteric datasets")
            
            # Load hypercards datasets
            hypercards_path = self.data_path / "hypercards" / "hypercards_datasets.csv"
            if hypercards_path.exists():
                self.hypercards_data = pd.read_csv(hypercards_path)
                logger.info(f"Loaded {len(self.hypercards_data)} hypercards datasets")
                
        except Exception as e:
            logger.error(f"Error loading datasets: {e}")
    
    def analyze_patterns(self):
        """Analyze cross-dataset patterns and correlations"""
        results = {}
        
        if self.core_data is not None:
            results['core_analysis'] = {
                'total_datasets': len(self.core_data),
                'data_types': self.core_data['type'].value_counts().to_dict(),
                'sources': self.core_data['source'].value_counts().to_dict()
            }
        
        if self.esoteric_data is not None:
            results['esoteric_analysis'] = {
                'total_datasets': len(self.esoteric_data),
                'data_types': self.esoteric_data['type'].value_counts().to_dict(),
                'sources': self.esoteric_data['source'].value_counts().to_dict()
            }
            
        if self.hypercards_data is not None:
            results['hypercards_analysis'] = {
                'total_datasets': len(self.hypercards_data),
                'data_types': self.hypercards_data['type'].value_counts().to_dict(),
                'sources': self.hypercards_data['source'].value_counts().to_dict()
            }
        
        return results
    
    def generate_report(self):
        """Generate comprehensive analysis report"""
        self.load_datasets()
        patterns = self.analyze_patterns()
        
        print("=== Project 168 Data Analysis Report ===")
        print(f"Analysis Date: {pd.Timestamp.now()}\n")
        
        for category, analysis in patterns.items():
            print(f"--- {category.upper()} ---")
            print(f"Total Datasets: {analysis['total_datasets']}")
            print(f"Data Types: {analysis['data_types']}")
            print(f"Sources: {analysis['sources']}")
            print()

if __name__ == "__main__":
    analyzer = Project168Analyzer()
    analyzer.generate_report()
