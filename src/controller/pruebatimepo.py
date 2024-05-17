import time
from ControladorUsuarios import UserData

def main():
    UserData.create_table()
    
    start_time = time.time()
    UserData.insert_user(123, 'John Doe', 5551234, 'john@example.com', 'comprimir', 'texto original', 'texto procesado')
    print(f"insert_user took {time.time() - start_time:.2f} seconds")

    start_time = time.time()
    UserData.query_user(123)
    print(f"query_user took {time.time() - start_time:.2f} seconds")

    start_time = time.time()
    UserData.update_user(123, 'Nombre', 'Jane Doe')
    print(f"update_user took {time.time() - start_time:.2f} seconds")

    start_time = time.time()
    UserData.delete_user(123)
    print(f"delete_user took {time.time() - start_time:.2f} seconds")

    UserData.drop_table()

if __name__ == "__main__":
    main()
