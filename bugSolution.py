def function_with_closed_file(filename):
    try:
        f = open(filename, 'w')
        f.write('some data')
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        f.close() # Ensure file is always closed

# Or better yet using a context manager:

def function_with_context_manager(filename):
    try:
        with open(filename, 'w') as f:
            f.write('some data')
    except Exception as e:
        print(f"An error occurred: {e}") 