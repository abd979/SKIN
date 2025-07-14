prescription_data = {
    "Actinic keratosis": {
        "treatments": [
            {"type": "Cream", "form": "Topical", "name": "5-Fluorouracil (5-FU)", "instructions": "Apply once daily to affected area for 2-4 weeks."},
            {"type": "Cream", "form": "Topical", "name": "Imiquimod", "instructions": "Apply 3 times per week for up to 16 weeks."},
            {"type": "Surgery", "form": "Cryotherapy", "name": "Liquid nitrogen", "instructions": "Performed by dermatologist to freeze lesions."}
        ],
        "prevention": "Avoid direct sun exposure. Use SPF 30+ sunscreen daily. Wear wide-brim hats and protective clothing."
    },

    "Atopic Dermatitis": {
        "treatments": [
            {"type": "Cream", "form": "Topical", "name": "Hydrocortisone 1%", "instructions": "Apply thin layer twice daily to inflamed skin."},
            {"type": "Lotion", "form": "Moisturizer", "name": "CeraVe / Eucerin", "instructions": "Use generously after showering and before bed."},
            {"type": "Tablet", "form": "Oral", "name": "Cetirizine", "instructions": "Take 1 tablet daily to reduce itching."}
        ],
        "prevention": "Avoid harsh soaps, wear cotton clothes, moisturize regularly, avoid known allergens or triggers."
    },

    "Benign keratosis": {
        "treatments": [
            {"type": "Observation", "form": "None", "name": "No active treatment needed", "instructions": "Monitor for any changes or irritation."},
            {"type": "Surgery", "form": "Electrosurgery", "name": "Electrodesiccation", "instructions": "Used for cosmetic removal if needed."}
        ],
        "prevention": "Avoid trauma to skin, wear sun protection. Benign but see a doctor if it changes shape, color, or size."
    },

    "Dermatofibroma": {
        "treatments": [
            {"type": "Surgery", "form": "Excision", "name": "Minor surgical removal", "instructions": "Only if causing pain or cosmetic concern."},
            {"type": "Cream", "form": "Topical", "name": "Steroid cream", "instructions": "May reduce inflammation if irritated."}
        ],
        "prevention": "Usually not preventable. Avoid trauma or insect bites that can lead to formation."
    },

    "Melanocytic nevus": {
        "treatments": [
            {"type": "Observation", "form": "None", "name": "No treatment required", "instructions": "Monitor for changes in color, shape, or size."}
        ],
        "prevention": "Use sunscreen SPF 50+, avoid tanning beds, monitor with ABCDE rule (Asymmetry, Border, Color, Diameter, Evolving)."
    },

    "Melanoma": {
        "treatments": [
            {"type": "Surgery", "form": "Wide excision", "name": "Tumor removal with margins", "instructions": "Performed under local or general anesthesia."},
            {"type": "Cream", "form": "Topical", "name": "Imiquimod (early stages only)", "instructions": "Use only under oncologist guidance."},
            {"type": "Tablet", "form": "Oral", "name": "Dacarbazine", "instructions": "Chemotherapy under specialist supervision."}
        ],
        "prevention": "Early detection is critical. Avoid sunburns, use SPF 50+, get moles checked yearly by a dermatologist."
    },

    "Squamous cell carcinoma": {
        "treatments": [
            {"type": "Surgery", "form": "Mohs surgery", "name": "Layer-by-layer tumor removal", "instructions": "Highly effective, performed by dermatologist."},
            {"type": "Cream", "form": "Topical", "name": "5-Fluorouracil", "instructions": "Apply twice daily for 3-6 weeks (superficial cases)."}
        ],
        "prevention": "Avoid UV exposure, use sunscreen, treat actinic keratoses early to prevent progression."
    },

    "Tinea Ringworm Candidiasis": {
        "treatments": [
            {"type": "Cream", "form": "Topical", "name": "Clotrimazole 1%", "instructions": "Apply twice daily for 2–4 weeks."},
            {"type": "Tablet", "form": "Oral", "name": "Fluconazole 150mg", "instructions": "Take one tablet weekly for 2–4 weeks (if severe)."},
            {"type": "Powder", "form": "Topical", "name": "Antifungal powder", "instructions": "Apply to dry skin folds to prevent moisture build-up."}
        ],
        "prevention": "Keep skin dry, avoid sharing towels, wear breathable fabrics, disinfect gym equipment and footwear."
    },

    "Vascular lesion": {
        "treatments": [
            {"type": "Laser", "form": "Pulsed dye laser", "name": "Laser therapy", "instructions": "Performed in sessions by dermatologist."},
            {"type": "Observation", "form": "None", "name": "No treatment needed", "instructions": "Benign unless growing or bleeding."}
        ],
        "prevention": "Usually congenital or age-related. Avoid trauma to lesion area. Monitor for unexpected growth."
    }
}
