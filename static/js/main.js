// Fetch the plant data from the server

import fetch from "node-fetch";
function reqData() {
  fetch("/get_data")
    .then((response) => response.json())
    .then((data) => {
      // Get the predicted plant class from the server
      const predictedClass = "{{ result.class_name }}";

      // Find the corresponding plant in the JSON data
      const plant = data.find((p) => p.name === predictedClass);
      console.log(data);
      // Display the plant information in the HTML page
      const plantInfoDiv = document.getElementById("plant-info");
      plantInfoDiv.innerHTML = `
              <h2>${plant.name}</h2>
              <p>${plant.activity}</p>
              <p>${plant.locations}</p>
              <p>${plant.poisonLevel}</p>
              <p>${plant.consumptionInfo}</p>
          `;
    })
    .catch((error) => console.error(error));
}
