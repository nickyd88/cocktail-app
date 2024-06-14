
// Creating favorite button - reverse fill of icon and make call to update the DB
function fav(recipeID) {
  const favCount = document.getElementById(`favs-count-${recipeID}`);
  const favButton = document.getElementById(`fav-button-${recipeID}`);

  if (favButton.className === "far fa-heart") {
    favButton.className = "fas fa-heart";
  } else {
    favButton.className = "far fa-heart";
  }

  // The database update will take a few seconds -- the favorite count will update when this call finishes
  fetch(`/fav/${recipeID}`, { method: "POST" })
    .then((res) => res.json())
    .then((data) => {
      favCount.innerHTML = data["favs"];
    })
    .catch((e) => alert("Could not fav recipe."));
}

// Create a filter for recipe stock

function filterSelection(c) {
  var x, i;
  x = document.getElementsByClassName("recipe-card");
  if (c == "all") c = "";
  for (i = 0; i < x.length; i++) {
    w3AddClass(x[i], "recipe-hide");
    if (x[i].className.indexOf(c) > -1) w3RemoveClass(x[i], "recipe-hide");
  }
}

function w3AddClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) == -1) {element.className += " " + arr2[i];}
  }
}

function w3RemoveClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      arr1.splice(arr1.indexOf(arr2[i]), 1);     
    }
  }
  element.className = arr1.join(" ");
}

function hideButton() {
  var form = document.getElementById("generate-form");
  form.style.display="none";
}