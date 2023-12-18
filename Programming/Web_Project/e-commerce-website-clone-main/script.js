const bar = document.querySelector("#bar");
const nav = document.querySelector("#navbar");
const close = document.querySelector(".close");


if(bar){
    bar.addEventListener("click", () => {
        nav.classList.toggle("active");
    });
}
if(close){
    close.addEventListener("click",()=>{
        nav.classList.remove("active");
    })
}

// Single Product's Image Slider

const mainImg = document.querySelector('.main-img');
const smallImgs = document.querySelectorAll('.small-img');

smallImgs.forEach((smallImg) => {
  smallImg.addEventListener('click', () => {
    // Remove the active class from all the small images
    smallImgs.forEach((img) => {
      img.classList.remove('active_img');
    });

    // Set the clicked small image as active
    smallImg.classList.add('active_img');

    // Set the clicked small image as the source of the main image
    mainImg.src = smallImg.src;
  });
});

// Single Product's Image Slider End

// Linking the product's image to the product page

const prods = document.querySelectorAll('.prods');

prods.forEach((prod) => {
    prod.addEventListener('click', () => {
        window.location.href = "sproduct.html";
    }
    );
});





