const fs = require('fs');
const readline = require('readline');


direction =  fs.readFileSync("./directions.txt").toString().split("\n").map((x) =>{
    return {direction : x.split(" ")[0], value : parseInt(x.split(" ")[1])}
})

let calc =  () => {

    let horizontal = 0, depth = 0, aim_depth = 0;

    direction.forEach((x) =>{
        const {direction, value} = x;
        switch(direction){
            case "up":
                depth -= value;
                break;
            case "down":
                depth += value;
                break;
            case "forward":
                horizontal += value;
                aim_depth += value * depth;
        }
    })

    return{
        part_one : horizontal * depth,
        part_two : horizontal * aim_depth
    }
}

console.log(calc())