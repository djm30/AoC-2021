const fs = require('fs');
const readline = require('readline');



let readInByLine = async () =>{
    const directions = []
    const fileStream = fs.createReadStream("directions.txt");

    let re = /(forward|up|down)\s(\d*)/g;

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });
    let i = 0;
    for await (const line of rl){
        
        if(i==8){
            break;
        }
        let match = re.exec(line);

        console.log("Line: "  +  line)
        console.log(match)
        console.log("\n");

        if(match){
            directions.push(
                {
                    direction : match[1],
                    amount : match[2]
                }
            )
        }
        i++;
    }


    return directions;
}




let main = async () =>{
    directions = await readInByLine();
    console.log(directions);
}

main()