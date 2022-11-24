from localization.translator import translate_text_to_language


def generate_fertilizer_report(index, lang):
    return {
        "info": translate_text_to_language(result[index]["info"], lang, "en"),
        "specifications": translate_text_to_language(result[index]["specifications"], lang, "en"),
        "application": {
            "1": translate_text_to_language(result[index]["application"]["1"], lang, "en"),
            "2": translate_text_to_language(result[index]["application"]["2"], lang, "en"),
        }
    }
    
result = {
    "10-26-26":{
        "info": "NPK is a DAP based composite fertiliser and is produced at IFFCOs Kandla unit, which apart from NPK 10:26:26 and also produces NPK 10-26-26. NPK 10-26-26 fixes the phosphorus and potassium content in the soil and is highly effective in soils with leaching condition.  The product is granular and comes in moisture resistant HDP bags allowing easy handling and storage.",
        "application":  {
            "1": "Used as a complex fertilizer for supply of all three major nutrient like Nitrogen, Phosphorus and Potash.",
            "2": "Used in basal application in crops like Wheat, Paddy, Maize, Pulses, Sugarcane, Vegetables etc."
            },
        "specifications":"Moisture : 1.5 percentage by wt. Max. Ammoniacal Nitrogen : 7.0 percentage by wt. Min. Water-soluble Phosphorus 22.5 percentage by wt. Min.Phosphorus 26.0 percentage by wt. Min. Water-soluble 26.0 by wt. Min. Particle-Size 90% passing through 4 mm. sieve"
    },
    "14-35-14":{
        "info":"GROMOR 14-35-14 is a complex fertilizer containing all major nutrients viz. Nitrogen, Phosphorous and Potassium. The only complex having highest total nutrient content among the NPK complex fertilisers. (Total nutrients are 63%).",
        "application":  {
            "1": "Contains Nitrogen, Phosphorous and Potassium",
            "2": "Highest total nutrient content among NPK fertilizers (63%)"
            },
        "specifications": "It is the highest Phosphate (35%) containing complex compared to any other NPK complexes. Entire Nitrogen is available in Ammonical form. 29% out of 35% Phosphate and entire Potash is available in water-soluble form and therefore, easily available to crops. The NPK ratio 1:2.5:1 is a scientific combination for basal application to all crops and all the nutrients are chemically combined and interaction is synergic. It does not contain any filler and it has 100% nutrient containing material having secondary and micro-nutrients such as Sulphur, Calcium, Magnesium and Iron.It is the highest Phosphate (35%) containing complex compared to any other NPK complexes. Entire Nitrogen is available in Ammonical form. 29% out of 35% Phosphate and entire Potash is available in water-soluble form and therefore, easily available to crops. The NPK ratio 1:2.5:1 is a scientific combination for basal application to all crops and all the nutrients are chemically combined and interaction is synergic. It does not contain any filler and it has 100% nutrient containing material having secondary and micro-nutrients such as Sulphur, Calcium, Magnesium and Iron."
    },
    "17-17-17":{
        "info": "Contains 17% Nitrogen, 17% P2O5 and 17 % K2O 17:17:17 contains most important primary nutrients Nitrogen, Phosphorous and Potash in equal proportion Single most important source of all major nutrients Granules are stronger, harder and of uniform size",
        "application":  {
            "1": "Due to high water solubility, has a greater mobility in the soil",
            "2": "It has good storage properties"
            },
        "specifications": "Moisture per cent by weight (maximum) - 1.5 Total Nitrogen per cent by weight (minimum) - 17.0 Ammoniacal nitrogen per cent by weight (minimum) - 5.0 Urea Nitrogen, per cent by weight (maximum) - 12.0 Neutral ammonium citrate soluble phosphates (as P2O5), per cent by weight (minimum) - 17.0 Water soluble phosphate (as P2O5), per cent by weight (minimum) - 14.5 Water soluble potash (as K2O) per cent by weight (minimum) - 17.0 Particle size- Not less than 90 per cent of the material shall pass through 4 mm IS sieve and be retained on 1 mm IS sieve. Not more than 5 per cent shall be below 1 mm IS sieve"
    },
    "20-20":{
        "info":'''
        The intended use of a triple 20 fertilizer is primarily to increase plant success and fertility in poor soil. But, it’s also effective for use on plants grown in hanging baskets to accommodate for the heavy leaching that occurs.  

When used appropriately, a 20-20-20 NPK encourages vibrant foliage to ensure optimum photosynthesis. While providing maximum support for flower and fruit formation.
        ''',
        "application":  {
            "1": "Depending on your application type, a 20-20-20 fertilizer can be applied as a liquid when watering or by working slow-release granules into the soil. In some cases, fertilizer spikes can also be very effective. ",
            "2": "When planting new trees in nutrient-deficient soil, a handful of triple 20 granules can be added to the hole prior to planting. This will help roots get established more quickly and encourage new growth."
            },
        "specifications": "The nutrient ratio in a 20-20-20 fertilizer is pretty straightforward. 20% nitrogen, 20% phosphorus and 20% potassium. Which is twice as much of each as in a standard, balanced NPK of 10-10-10. Making it the perfect choice to revitalize tired and infertile soil."
    },
    "28-28":{
        "info": "A complex fertiliser containing 2 major nutrients, Nitrogen at 28% and Phosphorus at 28%, provides instantaneous and prolonged greenness for crops.",
        "application":  {
            "1": "It is the most suitable fertiliser for crops like Paddy, Cotton, Chillies, Sugarcane, Vegetables etc. Kharif Paddy: 75-85 kg, Rabi paddy: 90-100 kg, Cotton: 175-200 kg, Chilly: 85-100 kg, Vegetables: 100-200 kg",
            },
        "specifications": "This is the highest Nitrogen containing complex fertiliser with 28%. Nitrogen in two different forms through longer period of time. 19% of Nitrogen is in Urea form and 9% is in Ammoniacal form. 25.2% out of 28% Phosphate is in water soluble form and easily available to plants. Ammonium Phosphate is coated over Urea prill, due to which the losses from Urea will be minimised."
    },
    "DAP":{
        "info": "Diammonium phosphate (DAP) NP 18:46 Most concentrated phosphate-based fertilizer. It is perfect for any agriculture crop to provide full phosphorus nutrition throughout crop growth and development, as well as a starter dose of nitrogen and low sulphur.It can be applied in autumn for tilling and in spring during sowing, as well as for pre-sowing cultivation. Dissolving in soil, it provides temporary alkalization of pH of the soil solution around the fertilizer granule, thus stimulating better uptake of phosphorus from the fertilizers on acid soils. Fertilizer’s sulphur also contributes to the better intake of nitrogen and phosphorus by plants.",
        "application":  {
            "1": "Period: Autumn, Spring",
            "2": "Method: Broadcasting, During planting (of tubers)",
            },
        "specifications":
        "Grade NP 18:46 pH 6.0–7.2 Granule strength MPa min. 6 Granule composition ≥95% Ø1–6 mm",
    },
    "Urea":{
        "info": "Urea is a source of Nitrogen, an essential nutrient crucial for crop growth and development. Urea is the most important nitrogenous fertilizer in the country because of its high N content (46%N).",
        "application":  {
            "1": "Used as a complex fertilizer for supply of all three major nutrient like Nitrogen, Phosphorus and Potash.",
            "2": "Used in basal application in crops like Wheat, Paddy, Maize, Pulses, Sugarcane, Vegetables etc."
            },
        "specifications": "Moisture 1.7 percentage by wt. Max. Ammoniacal Nitrogen : 2.0 percentage by wt. Min. Water-soluble Phosphorus : 10 percentage by wt. Min. Phosphorus : 26.0 percentage by wt. Min. Water-soluble : 26.0 by wt. Min. Particle-Size : 90% passing through 4 mm. sieve"
        
    }
}

