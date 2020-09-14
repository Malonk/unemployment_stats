import os

old = "old"
base = os.path.abspath(os.path.join(os.path.dirname(__file__), old))
dirs = [x for x in os.listdir(base)
        if os.path.isdir(os.path.join(base, x))]

new = os.path.join(base, "data")
if not os.path.exists(new):
    os.mkdir(new)

for folder in dirs:
    if folder != "scratches":
        continue
    for filename in os.listdir(os.path.join(base, folder)):
        a = os.path.join(base, folder, filename)
        b = os.path.join(base, "data", filename)
        os.rename(a,
                  b)
        print(f"Moved {a} to {b}")


