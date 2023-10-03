/*=============== SHOW MENU ===============*/
const showMenu = (toggleId, navId) =>{
    const toggle = document.getElementById(toggleId),
          nav = document.getElementById(navId)
 
    toggle.addEventListener('click', () =>{
        // Add show-menu class to nav menu
        nav.classList.toggle('show-menu')
 
        // Add show-icon to show and hide the menu icon
        toggle.classList.toggle('show-icon')
    })
 }
 
 showMenu('nav-toggle','nav-menu')


// =================== HOME PAGE ================

const programItems = document.querySelectorAll(".program-items")
const indicators = document.querySelectorAll(".indicator .dot")

function eventHandler(index) {
    programItems.forEach((item, i) => {
        item.classList.remove("active")
        indicators[i].classList.remove('active')

    })
}
programItems.forEach((item, i) => {
    item.addEventListener('click', () => eventHandler(i))
    indicators[i].addEventListener("click", () => eventHandler(i))
})