"""Dasturlash texnologiyalari - 1-topshiriq uchun asosiy modul."""


def salomlash(ism: str) -> str:
    """Berilgan ism uchun salomlashuv matnini qaytaradi.

    Bo'sh yoki faqat probeldan iborat ism berilsa, ValueError ko'tariladi.
    """
    ism = ism.strip()
    if not ism:
        raise ValueError("Ism bo'sh bo'lishi mumkin emas")
    return f"Assalomu alaykum, {ism}!"


def main() -> None:
    print(salomlash("Dasturlash texnologiyalari"))


if __name__ == "__main__":
    main()
