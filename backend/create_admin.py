# backend/create_admin.py
import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

# Create admin if doesn't exist
try:
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'Admin123!')
        print("✅ Admin created: admin / Admin123!")
    else:
        print("✅ Admin already exists")
except Exception as e:
    print(f"❌ Error: {e}")