import fastf1

def main():
    session = fastf1.get_session(2023, 'Monaco', 'Q')
    session.load()
    print(session.results.iloc[0:10].loc[:, ['BroadcastName/', 'Q3']])


if __name__ == "__main__":
    main()
