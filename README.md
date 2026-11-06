# Dasturlash texnologiyalari — 1-topshiriq (M1 + A1)

**Talaba:** Xamroyeva Gulruh  
**Guruh:** 1-1DIM-24  
**Fan:** Dasturlash texnologiyalari (DIM-2024, 5-semestr)

## Loyiha haqida

Ushbu repozitoriy 1-topshiriqning amaliy qismi (A1) uchun yaratilgan: zamonaviy IDE muhitini sozlash va Git/GitHub yordamida loyiha strukturasini shakllantirish.

- **Platforma:** Python 3
- **IDE:** Visual Studio Code (Python kengaytmasi bilan)
- **Versiyalarni boshqarish:** Git + GitHub

## Loyiha strukturasi

```
dasturlash-texnologiyalari/
├── src/        # dastur manba kodi
├── tests/      # unit testlar
├── docs/       # hujjatlar
├── .gitignore
├── LICENSE
└── README.md
```

## Ishga tushirish

```bash
git clone https://github.com/Gulcha777/dasturlash-texnologiyalari.git
cd dasturlash-texnologiyalari
python -m venv .venv
python src/main.py
python -m unittest discover tests
```

## Branch strategiyasi

- `main` — barqaror versiya
- `develop` — ishlab chiqish branch'i
- `feature/*` — har bir yangi ish uchun alohida branch, `develop`'ga Pull Request orqali qo'shiladi

Commit xabarlari [Conventional Commits](https://www.conventionalcommits.org/) formatida yoziladi.
