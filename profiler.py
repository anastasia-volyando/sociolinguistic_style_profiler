import re
from database import get_markers


def normalize_text(text):
    return text.lower()


def find_markers(text):
    normalized_text = normalize_text(text)
    markers = get_markers()

    detected = []
    scores = {}

    for marker, category, weight, description in markers:
        marker_lower = marker.lower()

        pattern = r"\b" + re.escape(marker_lower) + r"\b"

        if re.search(pattern, normalized_text):
            detected.append({
                "marker": marker,
                "category": category,
                "weight": weight,
                "description": description
            })

            if category not in scores:
                scores[category] = 0

            scores[category] += weight

    return detected, scores


def classify_style(scores):
    if not scores:
        return "No strong sociolinguistic style detected"

    strongest_category = max(scores, key=scores.get)

    labels = {
        "internet_slang": "Informal internet speech",
        "casual_speech": "Casual conversational speech",
        "gen_z_speech": "Gen Z / online youth style",
        "formal_register": "Formal register",
        "academic_register": "Academic register",
        "politeness": "Polite or professional style",
        "hedging": "Hedged / cautious style"
    }

    return labels.get(strongest_category, strongest_category)


def calculate_total_score(scores):
    return sum(scores.values())


def profile_text(text):
    detected, scores = find_markers(text)
    overall_style = classify_style(scores)
    total_score = calculate_total_score(scores)

    return {
        "detected": detected,
        "scores": scores,
        "overall_style": overall_style,
        "total_score": total_score
    }