from src import mkapp

app = mkapp()

if __name__ == "__main__":
    app.run(host="127.0.0.1", exclude_paths = ["data", "src/models.py"])
