// GrayCCC
using System;
namespace GrayCCC
{
	class GCCC
	{
		public static void Main()
		{
			// Console.Write("Input the key: ");
			// uint num;
			// if (!uint.TryParse(Console.ReadLine().Trim(), out num))
			// {
			// 	Console.WriteLine("Invalid key");
			// 	return;
			// }
			string text = "";
			string text2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ{} ";
			int num2 = 0;
			uint num = 1510650850;
			byte[] array = new byte[]
			{
				164,25, 4, 130, 126, 158, 91, 199, 173, 252, 239, 143, 150, 
				251, 126, 39, 104, 104, 146, 208, 249, 9, 219, 208, 101, 
				182, 62, 92, 6, 27, 5, 46
			};
			
			byte b = 0;
			while (num != 0u)
			{
				char c = (char)(array[num2] ^ (byte)num ^ b);
				if (!text2.Contains(new string(c, 1)))
				{
					Console.WriteLine("Invalid key");
					return;
				}
				text += c;
				b ^= array[num2++];
				num >>= 1;
				Console.WriteLine(text);
			}
			if (text.Substring(0, 5) != "FLAG{" || text.Substring(31, 1) != "}")
			{
				Console.WriteLine("Invalid key");
				return;
			}
			Console.WriteLine("Your flag is: " + text);
		}
	}
}
