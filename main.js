(function () {
  var msnShoppingGamePane = document
    .querySelector("shopping-page-base")
    ?.shadowRoot.querySelector("shopping-homepage")
    ?.shadowRoot.querySelector("msft-feed-layout")
    ?.shadowRoot.querySelector("msn-shopping-game-pane");
  if (msnShoppingGamePane != null) {
    msnShoppingGamePane.scrollIntoView();
    msnShoppingGamePane.style.setProperty("grid-area", "slot1");
    msnShoppingGamePane.setAttribute("gamestate", "active");
    msnShoppingGamePane.cardsPerGame = 1;
    msnShoppingGamePane.resetGame();
  } else alert("Unable to locate the shopping game!");
})();

document.getElementsByTagName("shopping-page-base")[0].shadowRoot.children[0]
  .children[2].children[0].shadowRoot.children[0].children[1].shadowRoot
  .children[14].shadowRoot.children[1].children;

// selects product
document
  .querySelector("shopping-page-base")
  ?.shadowRoot.querySelector("shopping-homepage")
  ?.shadowRoot.querySelector("msft-feed-layout")
  ?.shadowRoot.querySelector("msn-shopping-game-pane")
  ?.shadowRoot.querySelector(".shopping-select-overlay-button")
  .click();

let item = document
  .querySelector("shopping-page-base")
  ?.shadowRoot.querySelector("shopping-homepage")
  ?.shadowRoot.querySelector("msft-feed-layout")
  ?.shadowRoot.querySelector("msn-shopping-game-pane")
  ?.shadowRoot.querySelectorAll(".shopping-game-card-outline");

let products = [];
item.forEach((it) => {
  products.push(
    it
      .querySelector(".shopping-game-card")
      .children[0].shadowRoot.children[0].children[0].children[1].querySelector(
        "a"
      )
      .getAttribute("title")
  );
});
return products;

document
  .querySelector("shopping-page-base")
  ?.shadowRoot.querySelector("shopping-homepage")
  ?.shadowRoot.querySelector("msft-feed-layout")
  ?.shadowRoot.querySelector("msn-shopping-game-pane")
  ?.shadowRoot.querySelectorAll(".shopping-game-card-outline")[0]
  ?.querySelector(".shopping-game-card")
  ?.children[0].shadowRoot.children[0].children[0].children[1].querySelector(
    "a"
  )
  .getAttribute("title");

price = document
  .querySelector("shopping-page-base")
  ?.shadowRoot.querySelector("shopping-homepage")
  ?.shadowRoot.querySelector("msft-feed-layout")
  ?.shadowRoot.querySelector("msn-shopping-game-pane")
  .shadowRoot.querySelectorAll(".shopping-game-card-outline")[0]
  .children[0].children[0].shadowRoot.querySelector(
    ".shopping-price-span-text"
  ).textContent;

console.log(price);
