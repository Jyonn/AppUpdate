def main():
    import sys
    import os

    os.environ['DB_INIT_SCRIPT'] = 'True'

    if os.path.dirname(__file__) != '':
        os.chdir(os.path.dirname(__file__) + os.sep + os.path.pardir)
    else:
        os.chdir(os.path.pardir)

    cwd = os.getcwd()
    sys.path.insert(0, cwd)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppUpdate.settings")

    import django
    django.setup()

    from Developer.models import Developer
    # from Tag.models import Tag

    Developer.objects.all().delete()

    Developer.create("lqj679ssn", "123456")

if __name__ == "__main__":
    main()
