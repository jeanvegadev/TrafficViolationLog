import secrets
from .models import AccessToken


def generate_access_token(user):
    # Check if the user already has an access token
    try:
        existing_token = AccessToken.objects.get(oficial=user)
        # Generate a new token
        new_token = secrets.token_urlsafe(32)
        # Update the existing token with the new token
        existing_token.token = new_token
        existing_token.save()
        # Return the new token
        return new_token
    except AccessToken.DoesNotExist:
        # If no token exists, generate a new one
        token = secrets.token_urlsafe(32)
        # Create a new AccessToken instance
        access_token = AccessToken.objects.create(oficial=user, token=token)
        # Return the generated token
        return token
