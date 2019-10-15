#include <iostream>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int imageArray[20][20];
int filteredArray[20][20];


int  main () {
	for(int i=0; i<10; i++){
		for(int j=0; j<10; j++){
			imageArray[i][j] = 0;
			//filteredArray[i][j]=
		}
        for (int j=10; j<20; j++) {
            imageArray[i][j] = 40;
        }
	}	

	for(int i=10; i<20; i++) {
		for(int j=0; j<10; j++) {
	        imageArray[i][j] = 40;
        }
		for(int j=10; j<20; j++) {
	        imageArray[i][j] = 0;
        }
	}

	for(int i=0; i<20; i++) {
		for(int j=0;j<20;j++) {
			//printf("%4.1f ", imageArray[i][j]);
			printf("%2d ", imageArray[i][j]);
		}
	printf("\n");
	}
	printf("\n\n");
    /*
	for(int i=0; i<8; i++) {
		for(int j=0;j<8;j++) {
			printf("%4.1f ", filteredArray[i][j]);
		}
	printf("\n");
	}
    */
}
