const wrapper = document.querySelector(".sliderWrapper");
const menuItems = document.querySelectorAll(".menuItem");

let products = [];

function fetchProducts() {
    fetch('https://didactic-chainsaw-699vr4qj46wj34vx5-8000.app.github.dev/api/products/')
        .then(response => response.json())
        .then(data => {
            products = data;
            // Initially set the first product as the chosen product
            if (products.length > 0) {
                choosenProduct = products[0];
                updateProductDisplay();
            }
            // Update the menu items with the fetched product data
            menuItems.forEach((item, index) => {
                if (products[index]) {
                    item.textContent = products[index].title;
                }
            });
        })
        .catch(error => console.error('Error fetching products:', error));
}

let choosenProduct = products.length > 0 ? products[0] : null;

const currentProductImg = document.querySelector(".productImg");
const currentProductTitle = document.querySelector(".productTitle");
const currentProductPrice = document.querySelector(".productPrice");
const currentProductColors = document.querySelectorAll(".color");
const currentProductSizes = document.querySelectorAll(".size");

function updateProductDisplay() {
    if (choosenProduct) {
        currentProductTitle.textContent = choosenProduct.title;
        currentProductPrice.textContent = "$" + choosenProduct.price;
        currentProductImg.src = choosenProduct.colors[0].img;

        currentProductColors.forEach((color, index) => {
            if (choosenProduct.colors[index]) {
                color.style.backgroundColor = choosenProduct.colors[index].code;
            }
        });
    }
}

menuItems.forEach((item, index) => {
  item.addEventListener("click", () => {
    if (products[index]) {
      // Change the current slide
      wrapper.style.transform = `translateX(${-100 * index}vw)`;

      // Change the chosen product
      choosenProduct = products[index];

      // Update texts of currentProduct
      updateProductDisplay();
    }
  });
});

currentProductColors.forEach((color, index) => {
  color.addEventListener("click", () => {
    if (choosenProduct.colors[index]) {
      currentProductImg.src = choosenProduct.colors[index].img;
    }
  });
});

currentProductSizes.forEach((size, index) => {
  size.addEventListener("click", () => {
    currentProductSizes.forEach((size) => {
      size.style.backgroundColor = "white";
      size.style.color = "black";
    });
    size.style.backgroundColor = "black";
    size.style.color = "white";
  });
});

const productButton = document.querySelector(".productButton");
const payment = document.querySelector(".payment");
const close = document.querySelector(".close");

productButton.addEventListener("click", () => {
  payment.style.display = "flex";
});

close.addEventListener("click", () => {
  payment.style.display = "none";
});

// Fetch products on page load
window.onload = fetchProducts;
