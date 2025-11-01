def main():
    print("Hello from spatial!")
    q = polars.scan_csv("/home/isaac/Downloads/systems.csv")

    df = q.collect()
    plot(df)


if __name__ == "__main__":
    main()
