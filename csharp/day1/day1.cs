using System;
using System.Collections.Generic;
using System.Linq;

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
            int last_number = Int32.Parse(data[0]);
            int count_increase = 0;
            int number = last_number;
            for (int i = 1; i < data.Length; i++)
            {
                number = Int32.Parse(data[i]);
                if (number > last_number)
                {
                    count_increase += 1;
                }
                last_number = number;
            }
            return count_increase;
        }

        public static int part2(string[] data)
        {
            int count_increase = -1;
            int last_sum = 0;
            int sum = last_sum;
            for (int i = 0; i < data.Length-2; i++) 
            {
                int number1 = Int32.Parse(data[i]);
                int number2 = Int32.Parse(data[i+1]);
                int number3 = Int32.Parse(data[i+2]);
                sum = number1 + number2 + number3;
                if (sum > last_sum)
                {
                    count_increase += 1;
                }
                last_sum = sum;
            }
            return count_increase;
        }

    }
}
