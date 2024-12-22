if __name__ == '__main__':
    from app import app
    print("Starting the Platinium application...")
    app.run(host='0.0.0.0', port=5000)