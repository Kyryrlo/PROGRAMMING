import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Функция для создания базы данных и таблиц
def create_database():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Authors (
            author_id INTEGER PRIMARY KEY AUTOINCREMENT,
            author_name TEXT NOT NULL,
            birth_date TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Genres (
            genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
            genre_name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            release_date TEXT,
            author_id INTEGER,
            genre_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES Authors (author_id),
            FOREIGN KEY (genre_id) REFERENCES Genres (genre_id)
        )
    ''')

    conn.commit()
    conn.close()

# Функция для вставки начальных данных
def insert_initial_data():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    authors = [
        ('Leo Tolstoy', '1828-09-09'),
        ('Fyodor Dostoevsky', '1821-11-11'),
        ('Jane Austen', '1775-12-16')
    ]

    genres = [
        ('Novel',),
        ('Science Fiction',),
        ('Romance',)
    ]

    books = [
        ('War and Peace', '1869-01-01', 1, 1),
        ('Crime and Punishment', '1866-01-01', 2, 1),
        ('Pride and Prejudice', '1813-01-28', 3, 3)
    ]

    cursor.executemany('INSERT INTO Authors (author_name, birth_date) VALUES (?, ?)', authors)
    cursor.executemany('INSERT INTO Genres (genre_name) VALUES (?)', genres)
    cursor.executemany('INSERT INTO Books (title, release_date, author_id, genre_id) VALUES (?, ?, ?, ?)', books)

    conn.commit()
    conn.close()

# Функция для получения списка книг из базы данных
def get_books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    query = '''
        SELECT Books.book_id, Books.title, Books.release_date, Authors.author_name, Genres.genre_name
        FROM Books
        JOIN Authors ON Books.author_id = Authors.author_id
        JOIN Genres ON Books.genre_id = Genres.genre_id
    '''
    
    cursor.execute(query)
    books = cursor.fetchall()
    conn.close()
    
    return books

# Функция для добавления автора в базу данных
def add_author(author_name, birth_date):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Authors (author_name, birth_date) VALUES (?, ?)', (author_name, birth_date))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Author added successfully")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Функция для добавления жанра в базу данных
def add_genre(genre_name):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Genres (genre_name) VALUES (?)', (genre_name,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Genre added successfully")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Функция для добавления книги в базу данных
def add_book(title, release_date, author_id, genre_id):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Books (title, release_date, author_id, genre_id) VALUES (?, ?, ?, ?)', (title, release_date, author_id, genre_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Book added successfully")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Функция для обновления данных автора в базе данных
def update_author(author_id, author_name, birth_date):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE Authors SET author_name = ?, birth_date = ? WHERE author_id = ?', (author_name, birth_date, author_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Author updated successfully")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Функция для обновления данных жанра в базе данных
def update_genre(genre_id, genre_name):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE Genres SET genre_name = ? WHERE genre_id = ?', (genre_name, genre_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Genre updated successfully")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Функция для обновления данных книги в базе данных
def update_book(book_id, title, release_date, author_id, genre_id):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE Books SET title = ?, release_date = ?, author_id = ?, genre_id = ? WHERE book_id = ?', (title, release_date, author_id, genre_id, book_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Book updated successfully")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Функция для удаления книг автора из базы данных
def delete_books_by_author(author_id):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Books WHERE author_id = ?', (author_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Books by author deleted successfully")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Функция для удаления книг по жанру из базы данных
def delete_books_by_genre(genre_id):
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Books WHERE genre_id = ?', (genre_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Books by genre deleted successfully")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Функция для удаления всех таблиц из базы данных
def drop_tables():
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS Books')
        cursor.execute('DROP TABLE IF EXISTS Authors')
        cursor.execute('DROP TABLE IF EXISTS Genres')
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Tables dropped successfully")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Функция для пересоздания таблиц базы данных
def recreate_tables():
    try:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Authors (
                author_id INTEGER PRIMARY KEY AUTOINCREMENT,
                author_name TEXT NOT NULL,
                birth_date TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Genres (
                genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
                genre_name TEXT NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Books (
                book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                release_date TEXT,
                author_id INTEGER,
                genre_id INTEGER,
                FOREIGN KEY (author_id) REFERENCES Authors (author_id),
                FOREIGN KEY (genre_id) REFERENCES Genres (genre_id)
            )
        ''')

        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Tables recreated successfully")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Функция для отображения графического интерфейса
def main():
    create_database()  # Создание базы данных и таблиц при первом запуске
    insert_initial_data()  # Вставка начальных данных

    # Создание главного окна Tkinter
    root = tk.Tk()
    root.title("Library Management System")

    # Создание и настройка меню
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=file_menu)

    # Функция для обновления списка книг
    def refresh_books():
        books = get_books()
        tree.delete(*tree.get_children())
        for book in books:
            tree.insert('', 'end', values=book)

    # Создание и настройка интерфейса для добавления авторов
    def add_author_dialog():
        author_dialog = tk.Toplevel(root)
        author_dialog.title("Add Author")

        tk.Label(author_dialog, text="Author Name:").grid(row=0, column=0, padx=10, pady=5)
        author_name_entry = tk.Entry(author_dialog)
        author_name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(author_dialog, text="Birth Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5)
        birth_date_entry = tk.Entry(author_dialog)
        birth_date_entry.grid(row=1, column=1, padx=10, pady=5)

        def add_author_to_db():
            author_name = author_name_entry.get()
            birth_date = birth_date_entry.get()
            if author_name.strip() and birth_date.strip():
                add_author(author_name, birth_date)
                refresh_books()
                author_dialog.destroy()
            else:
                messagebox.showerror("Error", "Please fill in all fields")

        tk.Button(author_dialog, text="Add Author", command=add_author_to_db).grid(row=2, columnspan=2, padx=10, pady=10)

    # Создание и настройка интерфейса для добавления жанров
    def add_genre_dialog():
        genre_dialog = tk.Toplevel(root)
        genre_dialog.title("Add Genre")

        tk.Label(genre_dialog, text="Genre Name:").grid(row=0, column=0, padx=10, pady=5)
        genre_name_entry = tk.Entry(genre_dialog)
        genre_name_entry.grid(row=0, column=1, padx=10, pady=5)

        def add_genre_to_db():
            genre_name = genre_name_entry.get()
            if genre_name.strip():
                add_genre(genre_name)
                refresh_books()
                genre_dialog.destroy()
            else:
                messagebox.showerror("Error", "Please enter a genre name")

        tk.Button(genre_dialog, text="Add Genre", command=add_genre_to_db).grid(row=1, columnspan=2, padx=10, pady=10)

    # Создание и настройка интерфейса для добавления книг
    def add_book_dialog():
        book_dialog = tk.Toplevel(root)
        book_dialog.title("Add Book")

        tk.Label(book_dialog, text="Title:").grid(row=0, column=0, padx=10, pady=5)
        title_entry = tk.Entry(book_dialog)
        title_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(book_dialog, text="Release Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5)
        release_date_entry = tk.Entry(book_dialog)
        release_date_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(book_dialog, text="Author ID:").grid(row=2, column=0, padx=10, pady=5)
        author_id_entry = tk.Entry(book_dialog)
        author_id_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(book_dialog, text="Genre ID:").grid(row=3, column=0, padx=10, pady=5)
        genre_id_entry = tk.Entry(book_dialog)
        genre_id_entry.grid(row=3, column=1, padx=10, pady=5)

        def add_book_to_db():
            title = title_entry.get()
            release_date = release_date_entry.get()
            author_id = author_id_entry.get()
            genre_id = genre_id_entry.get()
            if title.strip() and release_date.strip() and author_id.strip() and genre_id.strip():
                add_book(title, release_date, author_id, genre_id)
                refresh_books()
                book_dialog.destroy()
            else:
                messagebox.showerror("Error", "Please fill in all fields")

        tk.Button(book_dialog, text="Add Book", command=add_book_to_db).grid(row=4, columnspan=2, padx=10, pady=10)

    # Создание и настройка интерфейса для обновления книг
    def update_book_dialog():
        selected_item = tree.focus()
        if selected_item:
            book_dialog = tk.Toplevel(root)
            book_dialog.title("Update Book")

            selected_book = tree.item(selected_item)['values']

            tk.Label(book_dialog, text="Title:").grid(row=0, column=0, padx=10, pady=5)
            title_entry = tk.Entry(book_dialog)
            title_entry.insert(0, selected_book[1])
            title_entry.grid(row=0, column=1, padx=10, pady=5)

            tk.Label(book_dialog, text="Release Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5)
            release_date_entry = tk.Entry(book_dialog)
            release_date_entry.insert(0, selected_book[2])
            release_date_entry.grid(row=1, column=1, padx=10, pady=5)

            tk.Label(book_dialog, text="Author ID:").grid(row=2, column=0, padx=10, pady=5)
            author_id_entry = tk.Entry(book_dialog)
            author_id_entry.insert(0, selected_book[3])
            author_id_entry.grid(row=2, column=1, padx=10, pady=5)

            tk.Label(book_dialog, text="Genre ID:").grid(row=3, column=0, padx=10, pady=5)
            genre_id_entry = tk.Entry(book_dialog)
            genre_id_entry.insert(0, selected_book[4])
            genre_id_entry.grid(row=3, column=1, padx=10, pady=5)

            def update_book_in_db():
                book_id = selected_book[0]
                title = title_entry.get()
                release_date = release_date_entry.get()
                author_id = author_id_entry.get()
                genre_id = genre_id_entry.get()
                if title.strip() and release_date.strip() and author_id.strip() and genre_id.strip():
                    update_book(book_id, title, release_date, author_id, genre_id)
                    refresh_books()
                    book_dialog.destroy()
                else:
                    messagebox.showerror("Error", "Please fill in all fields")

            tk.Button(book_dialog, text="Update Book", command=update_book_in_db).grid(row=4, columnspan=2, padx=10, pady=10)
        else:
            messagebox.showerror("Error", "Please select a book to update")

    # Создание и настройка интерфейса для удаления книг
    def delete_book_dialog():
        selected_item = tree.focus()
        if selected_item:
            result = messagebox.askyesno("Delete Book", "Are you sure you want to delete this book?")
            if result:
                book_id = tree.item(selected_item)['values'][0]
                delete_books_by_author(book_id)
                refresh_books()
        else:
            messagebox.showerror("Error", "Please select a book to delete")

    # Создание и настройка интерфейса для удаления всех данных
    def delete_all_data():
        result = messagebox.askyesno("Delete All Data", "Are you sure you want to delete all data?")
        if result:
            drop_tables()
            recreate_tables()
            refresh_books()

    # Создание и настройка интерфейса
    main_frame = ttk.Frame(root, padding="3")
    main_frame.grid(row=0, column=0, sticky="nsew")

    tree = ttk.Treeview(main_frame, columns=("ID", "Title", "Release Date", "Author", "Genre"), show="headings", selectmode="browse")
    tree.heading("ID", text="ID")
    tree.heading("Title", text="Title")
    tree.heading("Release Date", text="Release Date")
    tree.heading("Author", text="Author")
    tree.heading("Genre", text="Genre")
    tree.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=tree.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    tree.configure(yscrollcommand=scrollbar.set)

    refresh_books()

    # Создание кнопок для добавления, обновления и удаления книг, а также удаления всех данных
    button_frame = ttk.Frame(root)
    button_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    add_author_button = ttk.Button(button_frame, text="Add Author", command=add_author_dialog)
    add_author_button.grid(row=0, column=0, padx=5, pady=5)

    add_genre_button = ttk.Button(button_frame, text="Add Genre", command=add_genre_dialog)
    add_genre_button.grid(row=0, column=1, padx=5, pady=5)

    add_book_button = ttk.Button(button_frame, text    = "Add Book", command=add_book_dialog)
    add_book_button.grid(row=0, column=2, padx=5, pady=5)

    update_book_button = ttk.Button(button_frame, text="Update Book", command=update_book_dialog)
    update_book_button.grid(row=0, column=3, padx=5, pady=5)

    delete_book_button = ttk.Button(button_frame, text="Delete Book", command=delete_book_dialog)
    delete_book_button.grid(row=0, column=4, padx=5, pady=5)

    delete_all_button = ttk.Button(button_frame, text="Delete All Data", command=delete_all_data)
    delete_all_button.grid(row=0, column=5, padx=5, pady=5)

    # Настройка расширяемости интерфейса
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_columnconfigure(0, weight=1)

    # Запуск главного цикла Tkinter
    root.mainloop()

if __name__ == "__main__":
    main()

