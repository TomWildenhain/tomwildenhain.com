import shutil
import os
import sys
from os import path
import django

def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personal_website.settings")
    django.setup()
    from django.conf import settings

    def clear_folder(path):
        try:
            shutil.rmtree(path)
        except FileNotFoundError:
            pass
        os.mkdir(path)

    compiled_path = path.join(settings.BASE_DIR, "compiled")
    static_path = path.join(compiled_path, "static")
    media_path = path.join(compiled_path, "media")
    static_source = settings.STATICFILES_DIRS[0]
    media_source = settings.MEDIA_ROOT
    clear_folder(compiled_path)
    shutil.copytree(static_source, static_path)
    shutil.copytree(media_source, media_path)

    from django.test import Client
    client = Client()

    def copy_file(url):
        response = client.get("/" + url)
        my_path = path.join(compiled_path, url)
        with open(my_path, "wb") as file:
            file.write(response.content)

    copy_file("index.html")
    copy_file("resume.html")
    copy_file("projects.html")

if __name__ == "__main__":
    main()