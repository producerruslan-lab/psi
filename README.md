# PSI Toolkit

Мини-пакет с CLI: калькулятор, текстовые утилиты (в т.ч. простой slugify с транслитерацией RU→EN).

## Быстрый старт (локально в Codex)
```bash
pip install -e .
psi --help

# Примеры
psi greet --name "Руслан"
psi calc add 2 5
psi text slugify "Привет, Мир!"
