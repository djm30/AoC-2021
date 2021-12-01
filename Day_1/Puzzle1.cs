using System;
using System.IO;

var path = "./sonar.txt";


List<int> fileReader()
{
    List<int> returnList = new List<int>();
    foreach (string line in System.IO.File.ReadLines(path))
    {
        returnList.Add(Int16.Parse(line));
    }
    return returnList;
}

int tester()
{
    return 1;
}


int increasedCounter(List<int> list)
{
    int counter = 0;
    for (int i = 0; i < list.Count - 1; i++)
    {
        if (list[i + 1] > list[i])
        {
            counter++;
        }
    }
    return counter;
}

void partOne(List<int> sonar)
{
    Console.WriteLine("Part One:" + increasedCounter(sonar).ToString());
}

void partTwo(List<int> sonar)
{
    List<int> folds = new List<int>();
    for (int i = 0; i < sonar.Count - 2; i++)
    {
        folds.Add(sonar[i] + sonar[i + 1] + sonar[i + 2]);
    }
    Console.WriteLine("Part One:" + increasedCounter(folds).ToString());
}

void main()
{
    List<int> sonar = fileReader();
    partOne(sonar);
    partTwo(sonar);

}

main();


