# src/data_loader.py - Updated for sheet structure
import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

def load_financial_inclusion_data(excel_path='data/raw/ethiopia_fi_unified_data.xlsx'):
    """
    Load financial inclusion data from Excel with sheet structure
    
    Parameters:
    -----------
    excel_path : str
        Path to the Excel file
        
    Returns:
    --------
    tuple : (main_data, impact_links, reference_codes)
        DataFrames containing main data, impact links, and reference codes
    """
    try:
        # Load Excel file
        print(f"Loading data from: {excel_path}")
        
        # Read sheet names
        excel_file = pd.ExcelFile(excel_path)
        sheet_names = excel_file.sheet_names
        print(f"Available sheets: {sheet_names}")
        
        # Load main data (sheet 1)
        if len(sheet_names) >= 1:
            main_data = pd.read_excel(excel_path, sheet_name=sheet_names[0])
            print(f"Loaded main data from '{sheet_names[0]}': {main_data.shape}")
        else:
            main_data = pd.DataFrame()
            print("No main data sheet found")
        
        # Load impact links (sheet 2)
        if len(sheet_names) >= 2:
            impact_links = pd.read_excel(excel_path, sheet_name=sheet_names[1])
            print(f"Loaded impact links from '{sheet_names[1]}': {impact_links.shape}")
        else:
            impact_links = pd.DataFrame()
            print("No impact links sheet found")
        
        # Load additional sheets if present
        additional_data = {}
        if len(sheet_names) > 2:
            for sheet in sheet_names[2:]:
                additional_data[sheet] = pd.read_excel(excel_path, sheet_name=sheet)
                print(f"Loaded additional sheet '{sheet}': {additional_data[sheet].shape}")
        
        return main_data, impact_links, additional_data
        
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        
        # Fallback to CSV files if they exist
        try:
            main_data = pd.read_csv('data/raw/ethiopia_fi_unified_data.csv')
            impact_links = pd.read_csv('data/raw/impact_links.csv')
            return main_data, impact_links, {}
        except:
            print("Could not load CSV files either")
            return pd.DataFrame(), pd.DataFrame(), {}

def load_reference_codes(csv_path='data/raw/reference_codes.csv'):
    """
    Load reference codes for data validation
    """
    try:
        reference_codes = pd.read_csv(csv_path)
        print(f"Loaded reference codes: {reference_codes.shape}")
        return reference_codes
    except Exception as e:
        print(f"Error loading reference codes: {e}")
        return pd.DataFrame()

def separate_record_types(main_data):
    """
    Separate main data into observations, events, and targets
    
    Parameters:
    -----------
    main_data : DataFrame
        Combined main data
        
    Returns:
    --------
    tuple : (observations, events, targets)
        Separated DataFrames
    """
    if main_data.empty or 'record_type' not in main_data.columns:
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    
    observations = main_data[main_data['record_type'] == 'observation'].copy()
    events = main_data[main_data['record_type'] == 'event'].copy()
    targets = main_data[main_data['record_type'] == 'target'].copy()
    
    print(f"Separated: {len(observations)} observations, {len(events)} events, {len(targets)} targets")
    return observations, events, targets

def clean_and_prepare_data(observations, events, targets, impact_links):
    """
    Clean and prepare data for analysis
    
    Parameters:
    -----------
    observations, events, targets, impact_links : DataFrames
    
    Returns:
    --------
    tuple : Cleaned DataFrames
    """
    # Clean observations
    if not observations.empty:
        # Convert dates
        date_cols = ['observation_date', 'start_date', 'end_date']
        for col in date_cols:
            if col in observations.columns:
                observations[col] = pd.to_datetime(observations[col], errors='coerce')
        
        # Ensure numeric values
        if 'value_numeric' in observations.columns:
            observations['value_numeric'] = pd.to_numeric(observations['value_numeric'], errors='coerce')
    
    # Clean events
    if not events.empty:
        if 'event_date' in events.columns:
            events['event_date'] = pd.to_datetime(events['event_date'], errors='coerce')
    
    # Clean targets
    if not targets.empty:
        date_cols = ['target_date', 'start_date', 'end_date']
        for col in date_cols:
            if col in targets.columns:
                targets[col] = pd.to_datetime(targets[col], errors='coerce')
    
    # Clean impact links
    if not impact_links.empty:
        # Convert numeric columns
        numeric_cols = ['impact_magnitude', 'lag_months']
        for col in numeric_cols:
            if col in impact_links.columns:
                impact_links[col] = pd.to_numeric(impact_links[col], errors='coerce')
    
    return observations, events, targets, impact_links

def get_data_summary(observations, events, targets, impact_links):
    """
    Generate summary statistics for the datasets
    """
    summary = {
        'observations': {
            'count': len(observations),
            'date_range': None,
            'indicators': 0,
            'pillars': 0
        },
        'events': {
            'count': len(events),
            'date_range': None,
            'categories': 0
        },
        'targets': {
            'count': len(targets)
        },
        'impact_links': {
            'count': len(impact_links),
            'connected_events': 0
        }
    }
    
    # Observations summary
    if not observations.empty:
        if 'observation_date' in observations.columns:
            valid_dates = observations['observation_date'].dropna()
            if len(valid_dates) > 0:
                summary['observations']['date_range'] = (
                    valid_dates.min(), valid_dates.max()
                )
        
        if 'indicator_code' in observations.columns:
            summary['observations']['indicators'] = observations['indicator_code'].nunique()
        
        if 'pillar' in observations.columns:
            summary['observations']['pillars'] = observations['pillar'].nunique()
    
    # Events summary
    if not events.empty:
        if 'event_date' in events.columns:
            valid_dates = events['event_date'].dropna()
            if len(valid_dates) > 0:
                summary['events']['date_range'] = (
                    valid_dates.min(), valid_dates.max()
                )
        
        if 'category' in events.columns:
            summary['events']['categories'] = events['category'].nunique()
    
    # Impact links summary
    if not impact_links.empty and not events.empty:
        if 'parent_id' in impact_links.columns and 'id' in events.columns:
            connected = impact_links['parent_id'].isin(events['id']).sum()
            summary['impact_links']['connected_events'] = connected
    
    return summary