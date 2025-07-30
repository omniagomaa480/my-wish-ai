def calculate_calories(age, weight, height, activity, goal):
    bmr = 10 * weight + 6.25 * height - 5 * age + 5

    activity_factor = {
        "low": 1.2,
        "moderate": 1.55,
        "high": 1.9
    }
    calories = bmr * activity_factor.get(activity, 1.2)

    if goal == "lose":
        calories -= 300
    elif goal == "gain":
        calories += 300

    return int(calories)


def generate_meal_plan(calories):
    return {
        "breakfast": "شوفان بالحليب + موز",
        "lunch": "دجاج مشوي + رز بني + سلطة",
        "dinner": "زبادي + تونة + بطاطا مسلوقة",
        "snacks": "تفاح + مكسرات",
        "total_calories": calories
    }
