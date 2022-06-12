import pandas as pd

json_data = pd.read_json(r'.\data.json')
categories = pd.read_csv(r'.\categories.csv')

class BMICalculator:
    def __init__(self):
        self.data:pd.DataFrame = json_data
        self.categories:pd.DataFrame = categories

        # Calculate the BMI
        self.data["BMI"] = self.data.apply(lambda row: self.calculate_bmi(row["WeightKg"],row["HeightCm"]), axis=1)
        # BMI Category and Health risk
        self.data[["BMICategory", "Healthrisk"]] = self.data.apply(lambda row: self._get_categories(row["BMI"]), axis=1)
    
    def calculate_bmi(self, mass, height):
        try:
            return(mass / ((height/100)*(height/100)))
        except:
            raise ValueError("Invalid parameters")

    def _get_categories(self, bmi):
        results = self.categories.loc[(bmi>=self.categories['BMIFrom']) & (bmi<self.categories['BMITo']),['BMICategory','Healthrisk']]
        bmi_category = results.iloc[0]["BMICategory"]
        health_risk = results.iloc[0]["Healthrisk"]
        return pd.Series([bmi_category, health_risk])

    def get_total_number_of_people_by_category(self, category):
        return len(self.data.query(f"BMICategory=='{category}'"))