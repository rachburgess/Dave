import re
import os

third_party_packages = set()

# Common Python built-ins that should be excluded
python_builtins = {
    'datetime', 'random', 'sys', 'math', 're', 'inspect', 'subprocess', 
    'importlib', 'codecs', 'pickle', 'os', 'time', 'json', 'hashlib', 
    'base64', 'statistics', 'fractions', 'platform', '__future__',
    '_threading_local', 'gc', 'itertools', 'functools', 'operator',
    'array', 'binascii', 'struct', 'string', 'token'
}

print("Scanning imports in /Users/rachelburgess/ directory...")

found_imports = []

# Walk only within /Users/rachelburgess/
for root, dirs, files in os.walk('/Users/rachelburgess'):
        if file.endswith('.py'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                continue
            
            # Find all 'import X' statements (X can be simple or dotted)
            imports = re.findall(r'^import (\w+)', content, re.MULTILINE)
            for pkg in imports:
                if pkg not in python_builtins and not pkg.startswith('_'):
                    found_imports.append(pkg)
            
            # Find all 'from X import Y' statements (X can be simple or dotted)
            from_imports = re.findall(r'^from (\w+) import', content, re.MULTILINE)
            for pkg in from_imports:
                if pkg not in python_builtins and not pkg.startswith('_'):
                    found_imports.append(pkg)

# Get unique third-party packages
third_party_packages.update(set(found_imports))

print(f"\nFound {len(third_party_packages)} third-party packages:\")
for pkg in sorted(third_party_packages):
    print(f"  - {pkg}")
