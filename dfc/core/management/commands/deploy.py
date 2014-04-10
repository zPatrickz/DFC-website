from optparse import make_option
from django.core.management.base import BaseCommand
from dfc.settings import BASE_DIR
class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--new',
                    action='store_true',
                    dest = 'new',
                    default=False,
                    help='Delete all existing databases and deploy a new site.'),
    )

    help = ('Deploy the site.')
    usage_str = "Usage: sudo ./manage.py deploy [--new]"
    

    def handle(self, new=False, **options):
        #new = options.get('new', None)
        if new:
            import os
            db_file_path = os.path.join(BASE_DIR,'db.sqlite3')
            core_migrations_path = os.path.join(BASE_DIR,'core/migrations')
            photologue_migrations_path = os.path.join(BASE_DIR,'photologue/migrations')
            manage_file_path = os.path.join(BASE_DIR, 'manage.py')
            photo_file_path = os.path.join(BASE_DIR, 'mediaroot/photo')
            doc_file_path = os.path.join(BASE_DIR, 'mediaroot/filer_public')
            markdown_extension_file_path = os.path.join(BASE_DIR, 'simpleeditor/markdown_extension/simpleeditor.py')
            import site
            SITE_PACKAGE_DIR = [x for x in site.getsitepackages() if ('dist-packages' in x) or ('site-packages' in x)][0]
            markdown_extension_path = os.path.join(SITE_PACKAGE_DIR, 'markdown/extensions')
            import subprocess
            print 'removing existing databases...'
            p=subprocess.Popen(["rm -f "+db_file_path],stdin=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            (out,err) = p.communicate()
            if err != '':
                 print err
                 return
            print 'removing existing migrations...'
            p2=subprocess.Popen(["rm -r -f "+core_migrations_path],stdin=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            (out,err) = p2.communicate()
            if err != '':
                 print err
                 return
            p3=subprocess.Popen(["rm -r -f "+photologue_migrations_path],stdin=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            (out,err) = p3.communicate()
            if err != '':
                 print err
                 return
            print 'removing existing photo files...'
            
            p5=subprocess.Popen(["rm -r -f "+photo_file_path],stdin=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            (out,err) = p5.communicate()
            if err != '':
                 print err
                 return
            p6=subprocess.Popen(["git rm --ignore-unmatch -r -f "+photo_file_path],stdin=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            (out,err) = p6.communicate()
            if err != '':
                 print err
                 return
            print 'removing existing document files...'
            
            p5=subprocess.Popen(["rm -r -f "+doc_file_path],stdin=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            (out,err) = p5.communicate()
            if err != '':
                 print err
                 return
            p6=subprocess.Popen(["git rm --ignore-unmatch -r -f "+doc_file_path],stdin=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            (out,err) = p6.communicate()
            if err != '':
                 print err
                 return
            print 'syncing database...'
            p4=subprocess.Popen(["python "+manage_file_path+" syncdb"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            p4.stdin.write("yes\n")
            p4.stdin.flush()
            p4.stdin.write("dfc@dfc.com\n")
            p4.stdin.flush()
            print 'Email: dfc@dfc.com'
            (out,err) = p4.communicate()
            if err != '':
                 print err
                 return
            print 'setting up photologue...'
            print 'creating size \'admin_thumbnail\''
            p4=subprocess.Popen(["python "+manage_file_path+" plcreatesize admin_thumbnail"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            p4.stdin.write("100\n")#width
            p4.stdin.write("100\n")#height
            p4.stdin.write("yes\n")#crop to fit
            p4.stdin.write("yes\n")#pre cache
            p4.stdin.write("yes\n")#increment count
            print 'creating size \'activity_cover_small\''
            p4=subprocess.Popen(["python "+manage_file_path+" plcreatesize activity_cover_small"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            p4.stdin.write("100\n")#width
            p4.stdin.write("100\n")#height
            p4.stdin.write("yes\n")#crop to fit
            p4.stdin.write("yes\n")#pre cache
            p4.stdin.write("yes\n")#increment count
            print 'creating size \'activity_cover_medium\''
            p4=subprocess.Popen(["python "+manage_file_path+" plcreatesize activity_cover_medium"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            p4.stdin.write("180\n")#width
            p4.stdin.write("180\n")#height
            p4.stdin.write("no\n")#crop to fit
            p4.stdin.write("yes\n")#pre cache
            p4.stdin.write("yes\n")#increment count
            print 'creating size \'activity_cover_large\''
            p4=subprocess.Popen(["python "+manage_file_path+" plcreatesize activity_cover_large"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            p4.stdin.write("320\n")#width
            p4.stdin.write("320\n")#height
            p4.stdin.write("no\n")#crop to fit
            p4.stdin.write("yes\n")#pre cache
            p4.stdin.write("yes\n")#increment count
            print 'creating size \'photo_small\''
            p4=subprocess.Popen(["python "+manage_file_path+" plcreatesize photo_small"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            p4.stdin.write("100\n")#width
            p4.stdin.write("100\n")#height
            p4.stdin.write("yes\n")#crop to fit
            p4.stdin.write("yes\n")#pre cache
            p4.stdin.write("yes\n")#increment count
            print 'creating size \'photo_medium\''
            p4=subprocess.Popen(["python "+manage_file_path+" plcreatesize photo_medium"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            p4.stdin.write("300\n")#width
            p4.stdin.write("300\n")#height
            p4.stdin.write("no\n")#crop to fit
            p4.stdin.write("yes\n")#pre cache
            p4.stdin.write("yes\n")#increment count
            print 'creating size \'photo_large\''
            p4=subprocess.Popen(["python "+manage_file_path+" plcreatesize photo_large"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            p4.stdin.write("600\n")#width
            p4.stdin.write("600\n")#height
            p4.stdin.write("no\n")#crop to fit
            p4.stdin.write("yes\n")#pre cache
            p4.stdin.write("yes\n")#increment count
            print 'setting up markdown...'
            p4=subprocess.Popen(["cp -rf "+markdown_extension_file_path+" "+markdown_extension_path],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            (out,err) = p4.communicate()
            if err != '':
                 print err
                 return
            print 'setting up development environment...'
            print 'creating first organization (for development only)'
            from core.models import Organization
            org = Organization(username="org1",email="org1@hahahahah.com")
            org.set_password("123456")
            org.save()
            print 'creating first user (for development only)'
            from core.models import User
            usr = User(first_name="W",last_name="TF",email="usr1@hahahahah.com")
            usr.set_password("123456")
            usr.save()
            print "site successfully deployed!"
        else:
            print self.usage_str
