def simple_interest(principal, rate, time):
    """Tính lãi đơn: I = P * R * T / 100"""
    return principal * rate * time / 100


def main():
    print("=== Simple Interest Calculator ===")
    principal = float(input("Nhap so tien goc (P): "))
    rate = float(input("Nhap lai suat moi nam (%): "))
    time = float(input("Nhap thoi gian (nam): "))

    interest = simple_interest(principal, rate, time)
    total = principal + interest

    print(f"Tien lai: {interest:,.2f}")
    print(f"Tong so tien nhan duoc: {total:,.2f}")


if __name__ == "__main__":
    main()