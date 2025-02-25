from pq_black.formatter import format_power_query

def test_format_power_query():
    input_code = """let 
    Source = Table.FromRecords({[Name="Alice", Age=25], [Name="Bob", Age=30]}),
    Filtered = Table.SelectRows(Source, each [Age] > 26)
in
    Filtered"""
    
    expected_output = """let Source = Table.FromRecords({[Name="Alice",Age=25],[Name="Bob",Age=30]}),
Filtered = Table.SelectRows(Source, each [Age] > 26)
in Filtered"""
    
    assert format_power_query(input_code) == expected_output
