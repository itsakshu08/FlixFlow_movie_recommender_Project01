import os
import pandas as pd
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Migrate users from CSV to Django User model'

    def handle(self, *args, **kwargs):
        # Get the CSV file path
        csv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'user_data.csv')
        
        # Read the CSV file
        df = pd.read_csv(csv_path)
        
        # Migrate each user
        for _, row in df.iterrows():
            username = row['username']
            password = row['password']
            
            # Check if user already exists
            if not User.objects.filter(username=username).exists():
                # Create new user
                user = User.objects.create_user(
                    username=username,
                    password=password,  # Django will hash this automatically
                    email=f"{username}@example.com"  # Placeholder email
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully created user: {username}'))
            else:
                self.stdout.write(self.style.WARNING(f'User already exists: {username}'))
