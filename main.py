from database import create_tables, insert_sample_markers
from profiler import profile_text


def print_results(result):
    print("\nSociolinguistic Style Profile")
    print("-----------------------------")

    print(f"Overall style: {result['overall_style']}")
    print(f"Total sociolinguistic marker score: {result['total_score']}")

    print("\nCategory scores:")
    if result["scores"]:
        for category, score in result["scores"].items():
            print(f"- {category}: {score}")
    else:
        print("- No category scores found")

    print("\nDetected markers:")
    if result["detected"]:
        for item in result["detected"]:
            print(
                f"- {item['marker']} → {item['category']} "
                f"(weight: {item['weight']})"
            )
            print(f"  {item['description']}")
    else:
        print("- No markers detected")


def main():
    create_tables()
    insert_sample_markers()

    print("Sociolinguistic Style Profiler")
    print("------------------------------")
    print("Enter a text, and the program will analyze its sociolinguistic style.")
    print("Type 'exit' to stop.\n")

    while True:
        user_text = input("Enter text:\n> ")

        if user_text.lower() == "exit":
            print("Goodbye!")
            break

        result = profile_text(user_text)
        print_results(result)
        print("\n")


main()