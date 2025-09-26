import time

def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        

        with open('execution_log.txt', 'a') as file:
            file.write(f"Function {func.__name__} executed in {execution_time:.4f} seconds\n")
        
        return result
    return wrapper
