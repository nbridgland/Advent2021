namespace MyApp // Note: actual namespace depends on the project name.
{
    public class Program
    {
        public static void Main(string[] args)
        {
            string file_contents = System.IO.File.ReadAllText("input.txt");
            string[] data = file_contents.Split('\n');
            int answer1 = part1(data);
            int answer2 = part2(data);
            Console.WriteLine($"The answer for part 1 is {answer1}");
            Console.WriteLine($"The answer for part 2 is {answer2}");
        }
        public static int part1(string[] data)
        {
            int depth = 0;
            int horizontal = 0;
            foreach (string entry in data)
            {
                string[] unpacked_data = entry.Split(' ');
                string direction = unpacked_data[0];
                string distanceString = unpacked_data[1];
                int distance = Int32.Parse(distanceString);
                if (direction == "forward")
                {
                    horizontal += distance;
                }
                if (direction == "down")
                {
                    depth += distance;
                }
                if (direction == "up")
                {
                    depth -= distance;
                }
            }
            return horizontal*depth;
            
        }

        public static int part2(string[] data)
        {
            int depth = 0;
            int horizontal = 0;
            int aim = 0;
            foreach (string entry in data)
            {
                string[] unpacked_data = entry.Split(' ');
                string direction = unpacked_data[0];
                string distanceString = unpacked_data[1];
                int distance = Int32.Parse(distanceString);
                if (direction == "forward")
                {
                    horizontal += distance;
                    depth += distance*aim;
                }
                if (direction == "down")
                {
                    aim += distance;
                }
                if (direction == "up")
                {
                    aim -= distance;
                }
            }
            return horizontal*depth;
        }

    }
}
