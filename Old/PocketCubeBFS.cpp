#include <iostream>
#include <queue>
int main()
{
	char cube[24] = {'r','r','r','r','w','w','w','w','b','b','b','b','y','y','y','y','g','g','g','g','o','o','o','o'};
	int R[24] = {0, 13, 2, 15, 4, 1, 6, 3, 10, 8, 11, 9, 12, 22, 14, 20, 16, 17, 18, 19, 7, 21, 5, 23};
	int Ri[24] = {0, 5, 2, 7, 4, 22, 6, 20, 9, 11, 8, 10, 12, 1, 14, 3, 16, 17, 18, 19, 15, 21, 13, 23};
	int R2[24] = {0, 22, 2, 20, 4, 13, 6, 15, 11, 10, 9, 8, 12, 5, 14, 7, 16, 17, 18, 19, 3, 21, 1, 23};

	int U[24] = {8, 9, 2, 3, 6, 4, 7, 5, 20, 21, 10, 11, 12, 13, 14, 15, 0, 1, 18, 19, 16, 17, 22, 23};
	int Ui[24] = {16, 17, 2, 3, 5, 7, 4, 6, 0, 1, 10, 11, 12, 13, 14, 15, 20, 21, 18, 19, 8, 9, 22, 23};
	int U2[24] = {20, 21, 2, 3, 7, 6, 5, 4, 16, 17, 10, 11, 12, 13, 14, 15, 8, 9, 18, 19, 0, 1, 22, 23};

	int F[24] = {2, 0, 3, 1, 4, 5, 19, 17, 6, 9, 7, 11, 10, 8, 14, 15, 16, 12, 18, 13, 20, 21, 22, 23};
	int Fi[24] = {1, 3, 0, 2, 4, 5, 8, 10, 13, 9, 12, 11, 17, 19, 14, 15, 16, 7, 18, 6, 20, 21, 22, 23};
	int F2[24] = {3, 2, 1, 0, 4, 5, 13, 12, 19, 9, 17, 11, 7, 6, 14, 15, 16, 10, 18, 8, 20, 21, 22, 23}
	
	
	
	
	return 0;
	
}