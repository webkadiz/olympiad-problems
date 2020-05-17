#include <iostream>
#include <stack>

using namespace std;

string brainLuck(const string &code, const string &input)
{

	unsigned char data[30000] = {0};
	int data_ptr = 0;
	stack<int> stack_left_brackets;

	int after_last_instruction = code.length();
	int point_on_instruction = 0;
	int point_on_input = 0;
	string output = "";

	while (point_on_instruction < after_last_instruction)
	{
		char cur_instruction = code[point_on_instruction];

		if (cur_instruction == '>')
		{
			data_ptr++;
		}
		else if (cur_instruction == '<')
		{
			data_ptr--;
		}
		else if (cur_instruction == '+')
		{
			data[data_ptr]++;
		}
		else if (cur_instruction == '-')
		{
			data[data_ptr]--;
		}
		else if (cur_instruction == '.')
		{
			output += data[data_ptr];
		}
		else if (cur_instruction == ',')
		{
			data[data_ptr] = input[point_on_input];
			point_on_input++;
		}
		else if (cur_instruction == '[')
		{
			if (data[data_ptr] == 0)
			{
				int lvl = 1;

				while (lvl != 0)
				{
					point_on_instruction++;
					if (code[point_on_instruction] == '[')
					{
						lvl++;
					}
					if (code[point_on_instruction] == ']')
					{
						lvl--;
					}
				}
			}
			else
			{
				stack_left_brackets.push(point_on_instruction);
			}
		}
		else if (cur_instruction == ']')
		{
			if (data[data_ptr] == 0)
			{
				stack_left_brackets.pop();
			}
			else
			{
				point_on_instruction = stack_left_brackets.top();
			}
		}

		point_on_instruction++;
	}

	return output;
}

int main()
{
	string code, s;
	cin >> code >> s;

	string res = brainLuck(code, s);

	cout << res;

	return 0;
}