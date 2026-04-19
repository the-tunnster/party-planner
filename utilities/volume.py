from decimal import Decimal, InvalidOperation
import re


_VOLUME_PATTERN = re.compile(
    r"^\s*(?P<amount>\d+(?:\.\d+)?)\s*(?P<unit>ml|milliliter|milliliters|millilitre|millilitres|l|liter|liters|litre|litres)?\s*$",
    re.IGNORECASE,
)
_ML_UNITS = {"ml", "milliliter", "milliliters", "millilitre", "millilitres"}
_LITER_UNITS = {"l", "liter", "liters", "litre", "litres"}


def volume_to_ml(value: object) -> int:
    if isinstance(value, int):
        return value

    if isinstance(value, float):
        if value.is_integer():
            return int(value)
        raise ValueError(f"Unsupported numeric volume value: {value}")

    text = str(value).strip()
    if not text:
        raise ValueError("Volume value cannot be empty.")

    if text.isdigit():
        return int(text)

    match = _VOLUME_PATTERN.match(text)
    if not match:
        raise ValueError(f"Unsupported volume value: {value}")

    amount_text = match.group("amount")
    unit = (match.group("unit") or "").lower()

    try:
        amount = Decimal(amount_text)
    except InvalidOperation as exc:
        raise ValueError(f"Unsupported volume value: {value}") from exc

    if unit in _ML_UNITS:
        if amount != amount.to_integral_value():
            raise ValueError(f"Milliliter volume must be a whole number: {value}")
        return int(amount)

    if unit in _LITER_UNITS:
        volume_ml = amount * Decimal("1000")
        if volume_ml != volume_ml.to_integral_value():
            raise ValueError(f"Liter volume does not convert to whole milliliters: {value}")
        return int(volume_ml)

    raise ValueError(f"Volume value is missing a supported unit: {value}")


def format_volume_label(volume_ml: int) -> str:
    if volume_ml >= 1000:
        liters = Decimal(volume_ml) / Decimal("1000")
        return f"{liters.normalize():g} L"

    return f"{volume_ml} ml"