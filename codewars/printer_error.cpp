#include <iostream>

std::string printerError(const std::string &s)
{
	std::string res;

	int cnt_wrongs = 0;

	for (uint32_t i = 0; i < s.size(); i++)
	{
		if (int(s[i]) > int('m'))
			cnt_wrongs++;
	}

	res = std::to_string(cnt_wrongs) + "/" + std::to_string(s.size());

	return res;
}

int main()
{
	std::string s = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz";
	s = printerError(s);
	std::cout << s << std::endl; // "3/56"

	s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz";
	s = printerError(s); 
	std::cout << s << std::endl; // "6/60"

	s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu";
	s = printerError(s);
	std::cout << s << std::endl; // "11/65"

	return 0;
}