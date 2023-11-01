
const navigateTo = url => {
    history.pushState(null, null, url);
        router();

}

const router = async () => {
    // creating an array of object containing paths

    const routes = [
        {
            path: "/", view: () => console.log("viewing dashboard")
        },
        {
            path: "/posts", view: () => console.log("viewing posts")
        },
        {
            path: "/settings", view: () => console.log("viewing settings")
        }
    ];

    // Test each path match
    const potentialMatch = routes.map(route => {
        return {
            route: route,
            isMatch: location.pathname === route.path
        };
    });

    let match = potentialMatch.find(potentialMatch => potentialMatch.isMatch);

    if (!match) {
        match = {
            route: routes[0],
            isMatch: true
        };
       
    }
    console.log(match.route.view())
};

document.addEventListener("DOMContentLoaded", () => {
   document.body.addEventListener("click", e => {
    if (e.target.match("[data-link]")){
        e.preventDefault();
        navigateTo(e.target.href);
    }
   })

    router(); 
});
    


