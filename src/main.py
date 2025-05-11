from src.read_json import load_categories_from_json
from config import FAIL_PACH
from src.create_class import Category

def main():
    # Загрузка данных
    categories = load_categories_from_json(FAIL_PACH)

    # Вывод результатов
    print("=" * 50)
    print("Загруженные категории:")
    for category in categories:
        print(f"\n{category}:")
        for product in category.products:
            print(f"  - {product}")

    print("\n" + "=" * 50)
    print(f"Всего категорий: {Category.counting_categories}")
    print(f"Всего уникальных товаров: {Category.total_unique_products}")


if __name__ == "__main__":
    main()
