#include <stdio.h>
#include <math.h>

int cols[16] = { 0 };

bool promising(int level)
{
	for (int i = 1; i < level; i++) {
		if (cols[i] == cols[level])
			return false;
		else if (level - i == abs(cols[level] - cols[i]))
			return false;
	}
	return true;
}

int back_queens(int level, int size)
{
	int cnt = 0;

	if (!promising(level))
		return 0;
	else if (level == size) {
		return 1;
	}
	for (int i = 1; i <= size; i++) {
		cols[level + 1] = i;
		cnt += back_queens(level + 1, size);
	}
	return cnt;
}

int main(){
    int N;
    scanf(" %d",&N);
    printf("%d", back_queens(0, N));
	return 0;
}