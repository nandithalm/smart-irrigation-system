class FuzzyController:
    """
    A simple rule-based fuzzy logic implementation.
    In a real system, you might use scikit-fuzzy, but this demonstrates the logic.
    """
    
    def __init__(self):
        # Soil moisture ranges (0-1024 typically for analog, but let's normalize 0-100%)
        # Here we assume the input is already normalized or mapped to a reasonable range.
        # Let's say 0 is completely dry and 1000 is soaking wet.
        pass

    def get_irrigation_need(self, moisture_level, rain_probability):
        """
        Determines if the pump should be turned ON based on simple fuzzy rules.
        moisture_level: 0 (dry) to 1024 (wet)
        rain_probability: 0.0 to 1.0
        """
        need_water = False
        reasoning = ""
        
        # Rule 1: Very Dry
        if moisture_level > 800:
            need_water = True
            reasoning = "Soil is extremely dry. Watering immediately."
            
        # Rule 2: Moderately Dry but it might rain
        elif moisture_level > 600:
            if rain_probability > 0.7:
                need_water = False
                reasoning = "Soil is dry, but high probability of rain. Holding off."
            else:
                need_water = True
                reasoning = "Soil is dry and no rain expected. Watering."
                
        # Rule 3: Wet
        else:
            need_water = False
            reasoning = "Soil moisture is optimal or wet. No watering needed."
            
        return need_water, reasoning
