# Pip and Virtual Environment Practice

## Activating Virtual Environment and Checking Packages

```bash
$ source _practice_pip_and_virtualenv/bin/activate
(_practice_pip_and_virtualenv) $ pip list
```

**Output:**
```
Package    Version
---------- -------
pip        24.0
```

---

## Deactivating Virtual Environment

```bash
$ deactivate
```
Exited the virtual env

---

## Comparing Global vs Virtual Environment Packages

```bash
$ pip3 list
```

**Output:**
```
Package                  Version
----------------------   ---------------
absl-py                  2.1.0
argcomplete              3.1.4
astunparse               1.6.3
...
```

**Key Insight:** The results are not the same! Each environment has its own libraries.

---

## Activating Virtual Environment Again

```bash
$ source _practice_pip_and_virtualenv/bin/activate
```

---

## Installing Django

```bash
$ pip install Django==2.2.4
```

**What information do you see returned in terminal after this command?**

```
Downloading Django-2.2.4-py3-none-any.whl (7.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.5/7.5 MB 92.5 kB/s eta 0:00:00
Downloading pytz-2026.1.post1-py2.py3-none-any.whl (510 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 510.5/510.5 kB 50.0 kB/s eta 0:00:00
Downloading sqlparse-0.5.5-py3-none-any.whl (46 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 46.1/46.1 kB 25.6 kB/s eta 0:00:00
Installing collected packages: pytz, sqlparse, Django
Successfully installed Django-2.2.4 pytz-2026.1.post1 sqlparse-0.5.5
```

---

## Using `pip freeze` vs `pip list`

### Command: `pip freeze`

```bash
$ pip freeze
```

**Output:**
```
Django==2.2.4
pytz==2026.1.post1
sqlparse==0.5.5
```

### Command: `pip list`

```bash
$ pip list
```

**Output:**
```
Package    Version
---------- -----------
Django     2.2.4
pip        24.0
pytz       2026.1.post1
sqlparse   0.5.5
```

### **What's the difference between freeze and list?**

**`pip freeze`** prints packages in a `name==version` format suitable for a `requirements.txt` file. It is meant for capturing an exact environment state so you can recreate it later. That's why `pip freeze` is often used together with output redirection like `pip freeze > requirements.txt`.

**`pip list`** is more for human inspection. By default it displays packages in a table with columns like Package and Version. It is easier to read when you just want to check what is installed.

---

## Creating a `requirements.txt` File

```bash
$ cd ~/Desktop
$ pip freeze > requirements.txt
$ ls
```

**Files in Desktop:**
```
Gift declaration.pdf
products.sql
requirements.txt
rgs_plan_ar_semester.pdf
```

**Contents of requirements.txt:**
```bash
$ cat requirements.txt
```

**Output:**
```
Django==2.2.4
pytz==2026.1.post1
sqlparse==0.5.5
```

---

## Uninstalling Django

```bash
$ pip uninstall Django
```

**Output:**
```
Found existing installation: Django 2.2.4
Uninstalling Django-2.2.4:
  Would remove:
    /media/...
    /media/...
    ....
Proceed (Y/n)? y
  Successfully uninstalled Django-2.2.4
```

---

## Checking for Uninstalled Package

```bash
$ pip show Django
```

**Output:**
```
WARNING: Package(s) not found: Django
```
