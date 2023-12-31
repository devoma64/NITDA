const express = require("express");
const path = require("path");

const app = express();

// using some middleware to set the setting dir

app.use("/static", express.static(path.resolve(__dirname, "frontend", "static")));

app.get("/*", (req, res) => {

    res.sendFile(path.resolve(__dirname, "frontend", "index.html"));

})

app.listen(process.env.PORT || 5080, () => console.log("Server running....")); 