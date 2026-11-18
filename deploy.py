cd ~/php2shell-security-kit

cat << 'EOF' > deploy.py
import os
import shutil
import subprocess

project_dir = os.path.expanduser("~/php2shell-security-kit")
images_dir = os.path.join(project_dir, "images")
pictures_dir = "/sdcard/Pictures"

os.makedirs(images_dir, exist_ok=True)
print("[+] Images directory checked/created.")

copied_count = 0
for i in range(1, 15):
    img_name = f"pic{i}.png"
    src_path = os.path.join(pictures_dir, img_name)
    
    if not os.path.exists(src_path):
        src_path_jpg = os.path.join(pictures_dir, f"pic{i}.jpg")
        if os.path.exists(src_path_jpg):
            src_path = src_path_jpg
            img_name = f"pic{i}.jpg"

    dst_path = os.path.join(images_dir, img_name)
    
    if os.path.exists(src_path):
        shutil.copy(src_path, dst_path)
        print(f"[+] Copied {img_name}")
        copied_count += 1
    else:
        print(f"[-] {img_name} not found in Pictures folder.")

print(f"[+] Total {copied_count} images copied.")

images_markdown = ""
for i in range(1, 15):
    if os.path.exists(os.path.join(images_dir, f"pic{i}.png")):
        images_markdown += f'<p align="center"><img src="images/pic{i}.png" alt="pic{i}" width="80%"></p>\n'
    elif os.path.exists(os.path.join(images_dir, f"pic{i}.jpg")):
        images_markdown += f'<p align="center"><img src="images/pic{i}.jpg" alt="pic{i}" width="80%"></p>\n'

readme_content = f"""# php2shell Security Kit

<p align="center">
  <img src="images/banner.png" alt="Banner" width="100%">
</p>

## 📸 تصاویر و مستندات پروژه (Screenshots)
{images_markdown}

---

## 🔍 درباره پروژه (Overview)
این پکیج یک ماژول امنیتی و آموزشی برای بررسی، شناسایی و ایمن‌سازی آسیب‌پذیری‌های نوع **RCE (Remote Code Execution)** و تبدیل ناخواسته فایل به شل در زبان PHP (`php2shell`) است.

---

## 📂 ساختار مخزن (Repository Structure)
* **`/images`** ⬅️ اسکرین‌شات‌ها و مستندات تصویری (`pic1` تا `pic14`)
* **`/src`** ⬅️ کدهای سورس اصلی
  * `vulnerable.php` ⬅️ نسخه آسیب‌پذیر (برای تست و تحلیل)
  * `secure_patched.php` ⬅️ نسخه ایمن‌سازی شده (پچ شده)

---

## 💻 نحوه استفاده
جهت بررسی کدهای آسیب‌پذیر و پچ‌شده به پوشه `src` مراجعه کنید.
"""

with open(os.path.join(project_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_content)
print("[+] README.md updated successfully.")

subprocess.run(["git", "add", "."], cwd=project_dir)
subprocess.run(["git", "commit", "-m", "Add pic1 to pic14 screenshots and update README layout"], cwd=project_dir)
result = subprocess.run(["git", "push", "origin", "main"], cwd=project_dir)

if result.returncode == 0:
    print("[+] Successfully pushed everything to GitHub!")
else:
    print("[-] Git push failed.")
EOF

python3 deploy.py
