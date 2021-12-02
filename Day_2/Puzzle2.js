const fs = require('fs');
const readline = require('readline');



let readInByLine = async () =>{
    const directions = []
    const fileStream = fs.createReadStream("directions.txt");

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    for await (const line of rl){
        
        directions.push(line)

    }
    return directions;
}

let applyRegex = (list) => {
        
    let re =  RegExp("(forward|up|down)\s(\d*)", "g")

    return list.map((x) =>{
        console.log(x)
        return
        match = re.exec(x)

        return {
            direction : match[1],
            value : match[2]
        };
    })
}




let main = async () =>{

    directions = await readInByLine();
    directions = applyRegex(directions);
    console.log(directions);
}

main()