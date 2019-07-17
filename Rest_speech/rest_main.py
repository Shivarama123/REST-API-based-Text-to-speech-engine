import test_rest

if __name__ == '__main__':
    try:
        test_rest.start_rest_thread()
    except KeyboardInterrupt:
        pass

