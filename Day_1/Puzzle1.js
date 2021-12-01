const fs = require('fs');
const readline = require('readline');

async function readInByLine(){
    const sonar = []
    const fileStream = fs.createReadStream("sonar.txt");

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    for await (const line of rl){
        sonar.push(parseInt(line))
    }
    return sonar;
}


const  main = async () =>{
    const sonar = await readInByLine();

    const increasedCounter = (list) => {
        let increasedCount = 0;
        for(let i = 0; i < list.length-1; i++){
            if(list[i+1] > list[i]){
                increasedCount+= 1;
            }
        }
        return increasedCount;
    }

    const partOne = () => {
        let increasedCount = increasedCounter(sonar)
        console.log("Part One: " + increasedCount.toString())
    }


    partOne()

    const partTwo = () =>{
        slidingWindows = []
        for(let i = 0; i < sonar.length-2; i++){
            slidingWindows.push(sonar[i] + sonar[i+1] + sonar[i+2])
        }
        let increasedCount = increasedCounter(slidingWindows)
        console.log("Part Two: " + increasedCount.toString())
    }
    partTwo()
}


main()