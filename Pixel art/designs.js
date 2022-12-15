// Select color input
const color = document.querySelector("#colorPicker");
var selectedColor = hexToRGB(color.value);
// Aware of color change by the user and convert to rgb format
color.addEventListener("input", function(evt){
    selectedColor = hexToRGB(color.value);
});

// Select size input
const heightInput = document.querySelector("#inputHeight");
const widthInput = document.querySelector("#inputWidth");

// Select table
const table = document.querySelector("#pixelCanvas");
// Create body of table for easy replacement
body = document.createElement("tbody");
body.setAttribute("id", "tbBody");
table.appendChild(body)
const form = document.querySelector("#sizePicker");
// When size is submitted by the user, call makeGrid()
form.addEventListener("submit", makeGrid);

/**
* @description Make grid when user submits height and width
* @param {Event} evt
*/
function makeGrid(evt) {
    evt.preventDefault();
    // Replace old canvas with empty canvas
    let newBody = document.createElement('tbody');
    table.replaceChild(
        newBody,
        document.getElementById("tbBody")
    );
    newBody.setAttribute("id", "tbBody");
    // Create canvas with inputed height and width
    let height = parseInt(heightInput.value, 10);
    let width = parseInt(widthInput.value, 10);
    for(let i = 0; i < height; i++){
        let row = document.createElement("tr");
        for(let j = 0; j < width; j++){
            let pixel = document.createElement("td");
            pixel.addEventListener("click", changeColor);
            row.appendChild(pixel);
        }
        newBody.appendChild(row);
    }
}

/**
* @description Change color when user select color for canvas
* @param {Event} evt
*/
function changeColor(evt){
    // Change color of pixel in canvas if its current color differs from selected color
    pixel = evt.target;
    if (pixel.style.backgroundColor != selectedColor){
        pixel.style.backgroundColor = selectedColor;
    }
    // else make default to white
    else{
        pixel.style.backgroundColor = "rgb(255, 255, 255)";
    }
}

/**
* @description Adds two numbers
* @param {string} hexColor
* @returns {string} rgb format of hexColor
*/
function hexToRGB(hexColor){
    // Split hex color to single r,g,b value
    let hexValues = hexColor.slice(1, ).match(/.{1,2}/g);
    // Convert and return rgb value in format rgb(x, y, z)
    let rgbValues = [
        parseInt(hexValues[0], 16),
        parseInt(hexValues[1], 16),
        parseInt(hexValues[2], 16),
    ];
    return "rgb(" + rgbValues[0] + ", " + rgbValues[1] + ", " + rgbValues[2] + ")";
}