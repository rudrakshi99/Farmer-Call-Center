from localization.translator import translate_text_to_language


def get_disease_recommendation(index, lang):
    return {
        "disease_name": translate_text_to_language(main_dic[index]["disease_name"], lang, "en"),
       "causes":{
       "1": translate_text_to_language(main_dic[index]["causes"]["1"], lang, "en"),
         "2": translate_text_to_language(main_dic[index]["causes"]["2"], lang, "en"), 
       },
         "prevent":{
         "1": translate_text_to_language(main_dic[index]["prevent"]["1"], lang, "en"),
            "2": translate_text_to_language(main_dic[index]["prevent"]["2"], lang, "en"),
            "3": translate_text_to_language(main_dic[index]["prevent"]["3"], lang, "en"),
            },
    }
    

main_dic = {
    "Apple___Apple_scab":{
          "disease_name":"Apple Scab",
          "causes":{
            "1":" Apple scab overwinters primarily in fallen leaves and in the soil. Disease development is favored by wet, cool weather that generally occurs in spring and early summer"
          ,"2": "Fungal spores are carried by wind, rain or splashing water from the ground to flowers, leaves or fruit. During damp or rainy periods, newly opening apple leaves are extremely susceptible to infection. The longer the leaves remain wet, the more severe the infection will be. Apple scab spreads rapidly between 55-75 degrees Fahrenheit.",
          },
          "prevent":{
          "1":"Choose resistant varieties when possible",
          "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",
          "3": "Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",
          }
    },
    "Apple___Black_rot":{
            "disease_name":"Apple Black Rot",
            "causes":{
                "1":"Black rot is caused by the fungus Botryosphaeria obtusa. The fungus overwinters in infected fruit and in the soil. The fungus is spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",
                "2":"The fungus infects blossoms, leaves, and fruit. The fungus enters the plant through wounds, such as those caused by insects or hail. The fungus can also enter through the stomata (pores) on the underside of the leaves. The fungus grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",
            },
            "prevent":{
                "1":"Choose resistant varieties when possible",
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",
            }
    },
    "Apple___Cedar_apple_rust":{
            "disease_name":"Apple Cedar Apple Rust",
            "causes":{
                "1":"Cedar apple rust is caused by the fungus Gymnosporangium juniperi-virginianae. The fungus overwinters in infected leaves and in the soil. The fungus is spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",
                "2":"The fungus infects blossoms, leaves, and fruit. The fungus enters the plant through wounds, such as those caused by insects or hail. The fungus can also enter through the stomata (pores) on the underside of the leaves. The fungus grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",
            },
            "prevent":{
                
                "1":"Choose resistant varieties when possible",
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",
            },
    },
    "Apple___healthy":{
            "disease_name":"Apple Healthy",
            "causes":{
                "1":"Heathy",
                "2":"",
            },
            "prevent":{
                "1":"Heathy",
                "2":"",
                "3":"",
            },
    },
    "Blueberry___healthy":{
            "disease_name":"Blueberry Healthy",
            "causes":{
                
                "1":"Heathy",
                "2":"", 
            },
            "prevent":{
                "1":"Heathy",
                "2":"",
                "3":"",
            },
    },
    "Cherry_(including_sour)___Powdery_mildew":{
            "disease_name":"Cherry Powdery Mildew",
            "causes":{
                "1":"Powdery mildew is caused by the fungus Podosphaera leucotricha. The fungus overwinters in infected leaves and in the soil. The fungus is spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",
                "2":"The fungus infects blossoms, leaves, and fruit. The fungus enters the plant through wounds, such as those caused by insects or hail. The fungus can also enter through the stomata (pores) on the underside of the leaves. The fungus grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",   
            },
            "prevent":{ 
                "1":"Choose resistant varieties when possible",
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",   
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",
            },
    },
    "Cherry_(including_sour)___healthy":{
            "disease_name":"Cherry Healthy",
            "causes":{
                "1":"Heathy",
                "2":"",
            },
            "prevent":{
                "1":"Heathy",
                "2":"", 
                "3":"", 
            },
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot":{
            "disease_name":"Corn Gray Leaf Spot",
            "causes":{
                "1":"Gray leaf spot is caused by the fungus Cercospora zeae-maydis. The fungus overwinters in infected leaves and in the soil. The fungus is spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",
                "2":"The fungus infects blossoms, leaves, and fruit. The fungus enters the plant through wounds, such as those caused by insects or hail. The fungus can also enter through the stomata (pores) on the underside of the leaves. The fungus grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",
            },
            "prevent":{
                "1":"Choose resistant varieties when possible",
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",
            },
    },
    "Corn_(maize)___Common_rust_":{
            "disease_name":"Corn Common Rust",
            "causes":{
                "1":"Common rust is caused by the fungus Puccinia sorghi. The fungus overwinters in infected leaves and in the soil. The fungus is spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",
                "2":"The fungus infects blossoms, leaves, and fruit. The fungus enters the plant through wounds, such as those caused by insects or hail. The fungus can also enter through the stomata (pores) on the underside of the leaves. The fungus grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",   
            },
            "prevent":{
                "1":"Choose resistant varieties when possible",
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",
            },
    },
    "Corn_(maize)___Northern_Leaf_Blight":{
            "disease_name":"Corn Northern Leaf Blight",
            "causes":{
                "1":"Northern leaf blight is caused by the fungus Exserohilum turcicum. The fungus overwinters in infected leaves and in the soil. The fungus is spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",
                "2":"The fungus infects blossoms, leaves, and fruit. The fungus enters the plant through wounds, such as those caused by insects or hail. The fungus can also enter through the stomata (pores) on the underside of the leaves. The fungus grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",   
            },
            "prevent":{
                "1":"Choose resistant varieties when possible",
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",   
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",   
            },
    },
    "Corn_(maize)___healthy":{
            "disease_name":"Corn Healthy",
            "causes":{
                "1":"Heathy",
                "2":"",
            },
            "prevent":{
                "1":"Heathy",
                "2":"", 
                "3":"",
            },
    },
    "Grape___Black_rot":{
            "disease_name":"Grape Black Rot",
            "causes":{  
                "1":"Black rot is caused by the fungus Guignardia bidwellii. The fungus overwinters in infected leaves and in the soil. The fungus is spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",
                "2":"The fungus infects blossoms, leaves, and fruit. The fungus enters the plant through wounds, such as those caused by insects or hail. The fungus can also enter through the stomata (pores) on the underside of the leaves. The fungus grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",   
            },
            "prevent":{
                
                "1":"Choose resistant varieties when possible",
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",
            },
    },

    "Grape___Esca_(Black_Measles)":{
            "disease_name":"Grape Esca",
            "causes":{  
                "1":"Esca is caused by the fungus Phaeoacremonium aleophilum. The fungus overwinters in infected leaves and in the soil. The fungus is spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",   
                "2":"The fungus infects blossoms, leaves, and fruit. The fungus enters the plant through wounds, such as those caused by insects or hail. The fungus can also enter through the stomata (pores) on the underside of the leaves. The fungus grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",       
            },
            "prevent":{
                "1":"Choose resistant varieties when possible",
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",   
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",   
            },
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)":{
            "disease_name":"Grape Leaf Blight",
            "causes":{  
                "1":"Leaf blight is caused by the fungus Isariopsis leaf spot. The fungus overwinters in infected leaves and in the soil. The fungus is spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",  
                "2":"The fungus infects blossoms, leaves, and fruit. The fungus enters the plant through wounds, such as those caused by insects or hail. The fungus can also enter through the stomata (pores) on the underside of the leaves. The fungus grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",   
            },
            "prevent":{ 
                "1":"Choose resistant varieties when possible",
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",   
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",   
            },  
    },  
    "Grape___healthy":{ 
            "disease_name":"Grape Healthy",
            "causes":{
                "1":"Heathy",
                "2":"", 
            },      
            "prevent":{
                "1":"Heathy",
                "2":"", 
                "3":"",
            },
    },
    "Orange___Haunglongbing_(Citrus_greening)":{

            "disease_name":"Orange Greening",   
            "causes":{  
                "1":"Citrus greening is caused by the bacterium Candidatus Liberibacter asiaticus. The bacterium overwinters in infected leaves and in the soil. The bacterium is spread by splashing water, rain, insects, birds, and wind. The bacterium can survive in the soil for several years.", 
                "2":"The bacterium infects blossoms, leaves, and fruit. The bacterium enters the plant through wounds, such as those caused by insects or hail. The bacterium can also enter through the stomata (pores) on the underside of the leaves. The bacterium grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The bacterium can survive in the soil for several years.",    
            },
            "prevent":{ 
                "1":"Choose resistant varieties when possible", 
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",   
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",   
            },  
    },  
    "Peach___Bacterial_spot":{  
            "disease_name":"Peach Bacterial Spot",
            "causes":{  
                "1":"Bacterial spot is caused by the bacterium Xanthomonas campestris pv. pruni. The bacterium overwinters in infected leaves and in the soil. The bacterium is spread by splashing water, rain, insects, birds, and wind. The bacterium can survive in the soil for several years.",   
                "2":"The bacterium infects blossoms, leaves, and fruit. The bacterium enters the plant through wounds, such as those caused by insects or hail. The bacterium can also enter through the stomata (pores) on the underside of the leaves. The bacterium grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The bacterium can survive in the soil for several years.",    
            },
            "prevent":{
                "1":"Choose resistant varieties when possible",
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",   
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",   
            },  
    },  
    "Peach___healthy":{ 
            "disease_name":"Peach Healthy", 
            "causes":{  
                "1":"Heathy",   
                "2":"", 
            },                  

            "prevent":{
                "1":"Heathy",
                "2":"",
                "3":"",
            },
    },
    "Pepper,_bell___Bacterial_spot":{   
            "disease_name":"Pepper Bacterial Spot", 
            "causes":{  
                "1":"Bacterial spot is caused by the bacterium Xanthomonas campestris pv. vesicatoria. The bacterium overwinters in infected leaves and in the soil. The bacterium is spread by splashing water, rain, insects, birds, and wind. The bacterium can survive in the soil for several years.", 
                "2":"The bacterium infects blossoms, leaves, and fruit. The bacterium enters the plant through wounds, such as those caused by insects or hail. The bacterium can also enter through the stomata (pores) on the underside of the leaves. The bacterium grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The bacterium can survive in the soil for several years.",    
            },
            "prevent":{ 
                "1":"Choose resistant varieties when possible", 
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",       
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",   
            },
    },
    "Pepper,_bell___healthy":{  
            "disease_name":"Pepper Healthy",
            "causes":{
                "1":"Heathy",
                "2":"", 
            },  
            "prevent":{ 
                "1":"Heathy",
                "2":"", 
                "3":"", 
            },  
    },  
    "Potato___Early_blight":{   
            "disease_name":"Potato Early Blight",
            "causes":{  
                "1":"Early blight is caused by the fungus Alternaria solani. The fungus overwinters in infected leaves and in the soil. The fungus is spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",    
                "2":"The fungus infects blossoms, leaves, and fruit. The fungus enters the plant through wounds, such as those caused by insects or hail. The fungus can also enter through the stomata (pores) on the underside of the leaves. The fungus grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",   
            },
            "prevent":{ 
                "1":"Choose resistant varieties when possible",
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",   
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",   
            },      
    },
    "Potato___Late_blight":{
            "disease_name":"Potato Late Blight",
            "causes":{
                "1":"Late blight is caused by the fungus Phytophthora infestans. The fungus overwinters in infected leaves and in the soil. The fungus is spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",    
                "2":"The fungus infects blossoms, leaves, and fruit. The fungus enters the plant through wounds, such as those caused by insects or hail. The fungus can also enter through the stomata (pores) on the underside of the leaves. The fungus grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",   
            },
            "prevent":{
                "1":"Choose resistant varieties when possible",
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",   
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",   
            },
    },
    "Potato___healthy":{    
            "disease_name":"Potato Healthy",
            "causes":{  
                "1":"Heathy",
                "2":"", 
            },  
            "prevent":{ 
                "1":"Heathy",
                "2":"",
                "3":"",
            },
    },
    "Raspberry___healthy":{
        
            "disease_name":"Raspberry Healthy",
            "causes":{  
                "1":"Heathy",
                "2":"", 
            },  
            "prevent":{ 
                "1":"Heathy",
                "2":"", 
                "3":"", 
            },
    },
    "Soybean___healthy":{
            "disease_name":"Soybean Healthy",
            "causes":{  
                "1":"Heathy",   
                "2":"", 
            },  
            "prevent":{ 
                "1":"Heathy",
                "2":"", 
                "3":"", 
            },  
    },  
    "Squash___Powdery_mildew":{ 
            "disease_name":"Squash Powdery Mildew",
            "causes":{  
                "1":"Powdery mildew is caused by the fungus Podosphaera xanthii. The fungus overwinters in infected leaves and in the soil. The fungus is spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",
                "2":"The fungus infects blossoms, leaves, and fruit. The fungus enters the plant through wounds, such as those caused by insects or hail. The fungus can also enter through the stomata (pores) on the underside of the leaves. The fungus grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",
            },
            "prevent":{ 
                "1":"Choose resistant varieties when possible",
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",   
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",   
            },
    },
    "Strawberry___Leaf_scorch":{
            "disease_name":"Strawberry Leaf Scorch",
            "causes":{
                "1":"Leaf scorch is caused by the fungus Colletotrichum acutatum. The fungus overwinters in infected leaves and in the soil. The fungus is spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",
                "2":"The fungus infects blossoms, leaves, and fruit. The fungus enters the plant through wounds, such as those caused by insects or hail. The fungus can also enter through the stomata (pores) on the underside of the leaves. The fungus grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",   
            },
            "prevent":{
                "1":"Choose resistant varieties when possible", 
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",   
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",   
            },
    },
    "Strawberry___healthy":{
            "disease_name":"Strawberry Healthy",
            "causes":{
                "1":"Heathy",
                "2":"",
            },
            "prevent":{
                "1":"Heathy",
                "2":"",
                "3":"",
            },
    },
    "Tomato___Bacterial_spot":{
            "disease_name":"Tomato Bacterial Spot",
            "causes":{
                "1":"Bacterial spot is caused by the bacterium Xanthomonas campestris pv. vesicatoria. The bacterium overwinters in infected leaves and in the soil. The bacterium is spread by splashing water, rain, insects, birds, and wind. The bacterium can survive in the soil for several years.",
                "2":"The bacterium infects blossoms, leaves, and fruit. The bacterium enters the plant through wounds, such as those caused by insects or hail. The bacterium can also enter through the stomata (pores) on the underside of the leaves. The bacterium grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The bacterium can survive in the soil for several years.",
            },
            "prevent":{
                "1":"Choose resistant varieties when possible",
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",   
            },
    },
    "Tomato___Early_blight":{
            "disease_name":"Tomato Early Blight",
            "causes":{
                "1":"Early blight is caused by the fungus Alternaria solani. The fungus overwinters in infected leaves and in the soil. The fungus is spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",
                "2":"The fungus infects blossoms, leaves, and fruit. The fungus enters the plant through wounds, such as those caused by insects or hail. The fungus can also enter through the stomata (pores) on the underside of the leaves. The fungus grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",
            },
            "prevent":{
                "1":"Choose resistant varieties when possible",
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",
            },
    },
    "Tomato___Late_blight":{

            "disease_name":"Tomato Late Blight",
            "causes":{  
                "1":"Late blight is caused by the fungus Phytophthora infestans. The fungus overwinters in infected leaves and in the soil. The fungus is spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",
                "2":"The fungus infects blossoms, leaves, and fruit. The fungus enters the plant through wounds, such as those caused by insects or hail. The fungus can also enter through the stomata (pores) on the underside of the leaves. The fungus grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",
            },
            "prevent":{
                "1":"Choose resistant varieties when possible",
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",   
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",   
            },
    },
    "Tomato___Leaf_Mold":{
            "disease_name":"Tomato Leaf Mold",
            "causes":{
                "1":"Leaf mold is caused by the fungus Sclerotinia sclerotiorum. The fungus overwinters in infected leaves and in the soil. The fungus is spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",
                "2":"The fungus infects blossoms, leaves, and fruit. The fungus enters the plant through wounds, such as those caused by insects or hail. The fungus can also enter through the stomata (pores) on the underside of the leaves. The fungus grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",
            },
            "prevent":{
                "1":"Choose resistant varieties when possible",
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",
            },
    },

    "Tomato___Septoria_leaf_spot":{
            "disease_name":"Tomato Septoria Leaf Spot",
            "causes":{  
                "1":"Septoria leaf spot is caused by the fungus Septoria lycopersici. The fungus overwinters in infected leaves and in the soil. The fungus is spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",   
                "2":"The fungus infects blossoms, leaves, and fruit. The fungus enters the plant through wounds, such as those caused by insects or hail. The fungus can also enter through the stomata (pores) on the underside of the leaves. The fungus grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",
            },
            "prevent":{
                "1":"Choose resistant varieties when possible",
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",
            },
    },
    "Tomato___Spider_mites Two-spotted_spider_mite":{
            "disease_name":"Tomato Spider Mites Two-spotted Spider Mite",
            "causes":{
            },

            "prevent":{ 
                "1":"Choose resistant varieties when possible",
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",
            },
    },
    "Tomato___Target_Spot":{
            "disease_name":"Tomato Target Spot",
            "causes":{
                "1":"Target spot is caused by the fungus Cercospora lycopersici. The fungus overwinters in infected leaves and in the soil. The fungus is spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",    
                "2":"The fungus infects blossoms, leaves, and fruit. The fungus enters the plant through wounds, such as those caused by insects or hail. The fungus can also enter through the stomata (pores) on the underside of the leaves. The fungus grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The fungus can survive in the soil for several years.",
            },
            "prevent":{
                "1":"Choose resistant varieties when possible",
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",
            },
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus":{
            "disease_name":"Tomato Yellow Leaf Curl Virus",
            "causes":{
                "1":"Tomato yellow leaf curl virus is caused by the virus Begomovirus. The virus overwinters in infected leaves and in the soil. The virus is spread by splashing water, rain, insects, birds, and wind. The virus can survive in the soil for several years.",
                "2":"The virus infects blossoms, leaves, and fruit. The virus enters the plant through wounds, such as those caused by insects or hail. The virus can also enter through the stomata (pores) on the underside of the leaves. The virus grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The virus can survive in the soil for several years.",
            },
            "prevent":{
                "1":"Choose resistant varieties when possible",
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",
            },
    },
    "Tomato___Tomato_mosaic_virus":{
            "disease_name":"Tomato Mosaic Virus",
            "causes":{
                "1":"Tomato mosaic virus is caused by the virus Tobamovirus. The virus overwinters in infected leaves and in the soil. The virus is spread by splashing water, rain, insects, birds, and wind. The virus can survive in the soil for several years.",
                "2":"The virus infects blossoms, leaves, and fruit. The virus enters the plant through wounds, such as those caused by insects or hail. The virus can also enter through the stomata (pores) on the underside of the leaves. The virus grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The virus can survive in the soil for several years.",
            },
            "prevent":{
                "1":"Choose resistant varieties when possible",
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",   
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",
            },
    },
    "Tomato___healthy":{
            "disease_name":"Tomato Healthy",
            "causes":{
                "1":"Tomato mosaic virus is caused by the virus Tobamovirus. The virus overwinters in infected leaves and in the soil. The virus is spread by splashing water, rain, insects, birds, and wind. The virus can survive in the soil for several years.",
                "2":"The virus infects blossoms, leaves, and fruit. The virus enters the plant through wounds, such as those caused by insects or hail. The virus can also enter through the stomata (pores) on the underside of the leaves. The virus grows on the plant and produces spores that are spread by splashing water, rain, insects, birds, and wind. The virus can survive in the soil for several years.",    
            },
            "prevent":{
                "1":"Choose resistant varieties when possible",
                "2":"Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring",
                "3":"Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",
            },
    },      
            

}
