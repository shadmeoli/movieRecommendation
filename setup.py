from App.main import app_runner


if __name__ == '__main__':
    try:
        entry_point = app_runner()
        entry_point
    except:
        print("error")