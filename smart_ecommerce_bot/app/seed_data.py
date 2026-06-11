from sqlmodel import Session

from app.models import Product


def seed_products(session: Session):

    products = [
        Product(
            name="Lenovo IdeaPad Slim 3",
            brand="Lenovo",
            category="laptop",
            price=45000,
            specs="AMD Ryzen 5, 16GB RAM, 512GB SSD"
        ),
        Product(
            name="ASUS Vivobook 15",
            brand="ASUS",
            category="laptop",
            price=48500,
            specs="Intel i5, 8GB RAM, 512GB SSD"
        ),
        Product(
            name="MacBook Air M2",
            brand="Apple",
            category="laptop",
            price=89000,
            specs="M2 Chip, 8GB RAM"
        ),
    ]

    session.add_all(products)
    session.commit()
