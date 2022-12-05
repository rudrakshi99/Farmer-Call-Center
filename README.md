# Krashak.AI
> Problem Statement (AGRI12)


AI-based voice-assisted Contact Center for assisting Farmers for their problems. Farmers can log their problems with the contact center thru phone calls / SMS / website and in return an automated voice response can be provided to the farmers with a most appropriate solution for their problems.

# UNESCO India - Africa Hackathon

<p align="center"><img src="https://user-images.githubusercontent.com/55245862/205508044-e43024b4-3c92-4ab9-9f6b-e3c6038205a6.jpg" height="200" width="300"></p>

## Features

1. Localization
2. Provides best solutions to the farmer's problem using NLP algorithm and knowledge base repository.
3. Crop Recommendation
4. Fertilizer Recommendation
5. Disease Prediction
6. Weather Forcasting
7. AI Voice Assistance
8. Voice SMS in local language



## DATA SOURCE 📊
- [Crop recommendation dataset ](https://www.kaggle.com/atharvaingle/crop-recommendation-dataset) (custom built dataset)
- [Fertilizer suggestion dataset](https://github.com/Gladiator07/Harvestify/blob/master/Data-processed/fertilizer.csv) (custom built dataset)
- [Disease detection dataset](https://www.kaggle.com/vipoooool/new-plant-diseases-dataset)

## Notebooks 📓
- [Crop Recommendation](https://www.kaggle.com/atharvaingle/what-crop-to-grow)
- [Disease Detection](https://www.kaggle.com/atharvaingle/plant-disease-classification-resnet-99-2)


## How to use 💻
- Crop Recommendation system ==> enter the corresponding nutrient values of your soil, state and city. Note that, the N-P-K (Nitrogen-Phosphorous-Pottasium) values to be entered should be the ratio between them. Refer [this website](https://www.gardeningknowhow.com/garden-how-to/soil-fertilizers/fertilizer-numbers-npk.htm) for more information.
Note: When you enter the city name, make sure to enter mostly common city names. Remote cities/towns may not be available in the [Weather API](https://openweathermap.org/) from where humidity, temperature data is fetched.

- Fertilizer suggestion system ==> Enter the nutrient contents of your soil and the crop you want to grow. The algorithm will tell which nutrient the soil has excess of or lacks. Accordingly, it will give suggestions for buying fertilizers.

- Disease Detection System ==> Upload an image of leaf of your plant. The algorithm will tell the crop type and whether it is diseased or healthy. If it is diseased, it will tell you the cause of the disease and suggest you how to prevent/cure the disease accordingly.
Note that, for now it only supports following crops

#### GitHub Repository Structure


| S.No. | Branch Name                                                                  | Purpose                       |
| ----- | ---------------------------------------------------------------------------- | ----------------------------- |
| 1.    | [master](https://github.com/rudrakshi99/Farmer-Call-Center/tree/master)      | contains all Frontend code    |
| 2.    | [backend](https://github.com/rudrakshi99/Farmer-Call-Center/tree/backend)    | contains all Backend code     |
| 3.    | [ml](https://github.com/rudrakshi99/Farmer-Call-Center/tree/ml)              | contains all ML code          |


## Team Members:

| S.No. | Name | Role | GitHub Username:octocat: |
| --------------- | --------------- | --------------- | --------------- |
| 1. | Rudrakshi (Team Leader) | Frontend Development| [@rudrakshi99](https://github.com/rudrakshi99)  |
| 2. | Frank Makeba | Frontend Development | [@CutCoders](https://github.com/CutCoders) |
| 3. | Tony Onkgopotse Richard | Backend Development | [@Onkgopotse007](https://github.com/Onkgopotse007) |
| 4. | Pedro Anda Ondo Nchama | Backend Development| [@paondonchama](https://github.com/paondonchama)  |
| 5. | Faremi Saheed | ML Enhgineer | [@faremi](https://github.com/faremi)  |
| 6. | Ayushi Saxena | Product Designer | [@ayushisaxena19](https://github.com/ayushisaxena19)  |

## Maintainers✨

<table>
  <tbody><tr>
    <td align="center"><a href="https://github.com/rudrakshi99"><img alt="" src="https://avatars.githubusercontent.com/rudrakshi99" width="100px;"><br><sub><b>Rudrakshi</b></sub></a><br><a href="https://github.com/rudrakshi99/Farmer-Call-Center/commits/master?author=rudrakshi99" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/faremi"><img alt="" src="https://avatars.githubusercontent.com/faremi" width="100px;"><br><sub><b>Faremi Saheed </b></sub></a><br><a href="https://github.com/rudrakshi99/Farmer-Call-Center/commits/backend?author=faremi" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/paondonchama"><img alt="" src="https://avatars.githubusercontent.com/paondonchama" width="100px;"><br><sub><b>Pedro Anda Ondo Nchama </b></sub></a><br><a href="https://github.com/rudrakshi99/Farmer-Call-Center/commits/backend?author=paondonchama" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Onkgopotse007"><img alt="" src="https://avatars.githubusercontent.com/Onkgopotse007" width="100px;"><br><sub><b>Tony Onkgopotse Richard </b></sub></a><br><a href="https://github.com/rudrakshi99/Farmer-Call-Center/commits/call_api?author=Onkgopotse007" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/ayushisaxena19"><img alt="" src="https://avatars.githubusercontent.com/ayushisaxena19" width="100px;"><br><sub><b>Ayushi Saxena  </b></sub></a><br><a href="https://github.com/rudrakshi99/Farmer-Call-Center" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/CutCoders"><img alt="" src="https://avatars.githubusercontent.com/CutCoders" width="100px;"><br><sub><b>Frank Makeba </b></sub></a><br><a href="https://github.com/rudrakshi99/Farmer-Call-Center/commits/master?author=CutCoders" title="Code">💻</a></td>
  </tr>
</tbody></table>


# License :memo:

This project follows the [MIT License](https://choosealicense.com/licenses/mit/).

[![Uses Git](https://forthebadge.com/images/badges/uses-git.svg)](https://github.com/rudrakshi99/Jan-Dhan-Darshak) 
[![forthebadge](https://forthebadge.com/images/badges/made-with-javascript.svg)](https://github.com/rudrakshi99/Jan-Dhan-Darshak)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://github.com/rudrakshi99/Jan-Dhan-Darshak)
[![Built with love](https://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/rudrakshi99/Jan-Dhan-Darshak.git) [![Built By Developers](https://forthebadge.com/images/badges/built-by-developers.svg)](https://github.com/rudrakshi99/Jan-Dhan-Darshak) 
