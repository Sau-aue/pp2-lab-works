import re
import json


def parse_receipt(filename="raw.txt"):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    # 1) Extract prices
    # Finds numbers like 12.99 or 120.50
    prices = re.findall(r"\b\d+\.\d{2}\b", text)
    prices = [float(p) for p in prices]

    # 2) Find product names
    # Assumption:
    # A product line often looks like:
    # Milk 2.50
    # Bread 1.20
    # So we capture text before the final price
    product_names = []
    product_pattern = re.compile(r"^(.*?)(?:\s+)(\d+\.\d{2})$")

    for line in lines:
        match = product_pattern.match(line)
        if match:
            name = match.group(1).strip()

            # Skip lines that are probably totals/payment/date info
            if not re.search(r"(total|subtotal|tax|date|time|cash|card|visa|mastercard|payment)", name, re.IGNORECASE):
                if name:
                    product_names.append(name)

    # 3) Calculate total amount
    calculated_total = sum(prices)

    # 4) Extract date
    date_match = re.search(r"\b\d{2}[/-]\d{2}[/-]\d{4}\b", text)
    date = date_match.group() if date_match else None

    # 4) Extract time
    time_match = re.search(r"\b\d{2}:\d{2}(?::\d{2})?\b", text)
    time = time_match.group() if time_match else None

    # 5) Find payment method
    payment_match = re.search(
        r"\b(cash|card|visa|mastercard|debit|credit|paypal)\b",
        text,
        re.IGNORECASE
    )
    payment_method = payment_match.group() if payment_match else None

    # Try to find explicit total from receipt
    total_match = re.search(r"(?i)\btotal\b[:\s]*\$?(\d+\.\d{2})", text)
    total_from_receipt = float(total_match.group(1)) if total_match else None

    result = {
        "prices": prices,
        "product_names": product_names,
        "calculated_total": round(calculated_total, 2),
        "date": date,
        "time": time,
        "payment_method": payment_method,
        "receipt_total": total_from_receipt
    }

    return result


def main():
    result = parse_receipt("raw.txt")

    print("PARSED RECEIPT DATA")
    print("-" * 30)
    print("Prices:", result["prices"])
    print("Product names:", result["product_names"])
    print("Calculated total:", result["calculated_total"])
    print("Date:", result["date"])
    print("Time:", result["time"])
    print("Payment method:", result["payment_method"])
    print("Receipt total:", result["receipt_total"])

    print("\nJSON OUTPUT")
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()