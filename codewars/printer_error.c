#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void int_to_str(char *str, int num)
{
	int t_num = num;

	int cnt_d = 0;
	while (t_num > 0)
	{
		t_num /= 10;
		cnt_d++;
	}

	char res[cnt_d + 1];
	res[cnt_d] = '\0';

	while (num > 0)
	{
		cnt_d--;
		int l_d = num % 10;
		res[cnt_d] = l_d + 48;
		num /= 10;
	}

	strcat(str, res);
}

int num_len(int num)
{

	int len = 0;

	while (num > 0)
	{
		num /= 10;
		len++;
	}

	return len;
}

char *printerError(char *s)
{

	int cnt_wrongs = 0, len_given_str = 0;

	int i = 0;
	while (s[i] != '\0')
	{

		if ((int)s[i] > (int)'m')
			cnt_wrongs++;

		len_given_str++;
		i++;
	}

	int len_of_res = num_len(cnt_wrongs) + num_len(len_given_str) + 2;
	char *res = calloc(len_of_res, sizeof(char));
	res[0] = '\0';

	int_to_str(res, cnt_wrongs);
	strcat(res, "/");
	int_to_str(res, len_given_str);

	return res;
}

int main()
{

	char *s = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz";
	s = printerError(s); 
	printf("%s\n", s); // "3/56"

	s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz";
	s = printerError(s); 
	printf("%s\n", s); // "6/60"

	s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu";
	s = printerError(s); 
	printf("%s\n", s); // "11/65"

	return 0;

}