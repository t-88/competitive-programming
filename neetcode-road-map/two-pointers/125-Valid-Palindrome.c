#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isPalindrome1(char * s){
    int i = -1;
    int ls = 0;
    char* l = '\0';
    while(s[++i] != '\0') {
        if(isalpha(s[i])) {
            l = realloc(l,ls + 1);
            l[ls + 1] = tolower(s[i]);
            ls++;
        }
    }
    l = realloc(l,ls + 1);
    l[ls + 1] = '\0';
    l++;
    ls--;

    i = 0;
    while(l[i] == l[ls] && ls > i){
        i++;
        ls--;
    }
    if(l[i] != l[ls] && i != ls + 1) {
        return false;
    }
    return true;
}
bool isPalindrome(char * s){
    int m = 0;
    while(s[m++] != '\0') {}

    int i = 0;
    int k = 0;
    while (i < m) {
        k = i;
        while (!isalpha(s[i])) {
            i++;
        }
        while (!isalpha(s[m])) {
            m--;
        }
        if(m < i && m == k) {
            return true;
        }
        if(tolower(s[m]) != tolower(s[i])) {
            return false;
        }
        i++;
        m--;
    }
    

    return true; 
}
int main() {
    printf("%d\n",isPalindrome("race a car"));
    return 0;
}