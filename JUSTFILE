# Default recipe - list available commands
default SESSION_NAME="gfetch-cli":
    @just --list

# Run app
dev:
    uv run python manage.py tailwind dev 
# Run tests
test *args:
    uv run pytest {{ args }}
