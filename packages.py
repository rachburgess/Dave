import re
import os

third_party_packages = set()
python_builtins = {
    'datetime', 'random', 'sys', 'math', 're', 'inspect', 'subprocess', 
    'importlib', 'codecs', 'pickle', 'os', 'time', 'json', 'hashlib', 
    'base64', 'statistics', 'fractions', 'platform', '__future__'
}

print("Scanning imports in Dave directory...")

for root, dirs, files in os.walk('Dave'):
    for file in files:
        if file.endswith('.py'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            
            # Find all import statements
            imports = re.findall(r'^import (\w+)', content, re.MULTILINE)
            for pkg in imports:
                if pkg not in python_builtins and not pkg.startswith('_'):
                    third_party_packages.add(pkg)
            
            from_imports = re.findall(r'^from (\w+) import', content, re.MULTILINE)
            for pkg in from_imports:
                if pkg not in python_builtins and not pkg.startswith('_'):
                    third_party_packages.add(pkg)

# Print what we're finding
all_imports = []
for root, dirs, files in os.walk('Dave'):
    for file in files:
        if file.endswith('.py'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            
            imports = re.findall(r'^import (\w+)', content, re.MULTILINE)
            from_imports = re.findall(r'^from (\w+) import', content, re.MULTILINE)
            all_imports.extend(imports + from_imports)

print(f"\nRaw imports found ({len(all_imports)}):")
for imp in list(set(all_imports))[:30]:
    print(f"  - {imp}")

print(f"\nFiltered third-party packages:")
# Check each import more carefully
for pkg in list(set(all_imports)):
    if pkg.lower() not in python_builtins and not pkg.startswith('_'):
        print(f"  - {pkg}")
